"""Serialize RIS batch downloads across KLex processes (at most 0.5 requests/s)."""
from __future__ import annotations

from contextlib import contextmanager
import os
from pathlib import Path
import threading
import time
import urllib.request

_THREAD_LOCK = threading.Lock()
_LOCK_PATH = Path(os.environ.get('KLEX_RIS_HTTP_LOCK', str(Path(__file__).resolve().parent / '.cache' / 'ris-http.lock')))


@contextmanager
def request_slot():
    # Keep the lock until the response closes: slow requests cannot overlap either.
    _LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with _THREAD_LOCK, _LOCK_PATH.open('a+b') as lock:
        if os.name == 'posix':
            import fcntl
            fcntl.flock(lock, fcntl.LOCK_EX)
        else:
            import msvcrt
            if lock.tell() == 0:
                lock.write(b'0'); lock.flush()
            lock.seek(0)
            while True:
                try:
                    msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
                    break
                except OSError:
                    time.sleep(0.1)
        try:
            lock.seek(0)
            try:
                previous = float(lock.read().decode('ascii'))
            except ValueError:
                previous = 0
            time.sleep(max(0, min(2, previous + 2 - time.time())))
            try:
                yield
            finally:
                lock.seek(0); lock.truncate()
                lock.write(str(time.time()).encode('ascii')); lock.flush()
        finally:
            if os.name == 'posix':
                fcntl.flock(lock, fcntl.LOCK_UN)
            else:
                lock.seek(0)
                msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)


@contextmanager
def open_ris(request, timeout=60, guard=None):
    with request_slot():
        if guard:
            guard()
        with urllib.request.urlopen(request, timeout=timeout) as response:
            yield response
