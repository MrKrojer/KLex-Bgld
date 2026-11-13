# How this history was made, and how to make it again

This file records how the `austria/burgenland/acts` repository was built from the official RIS Open Government Data API v2.6 (`https://data.bka.gv.at/ris/api/v2.6/Landesrecht`).

## Short version

```sh
python3 -X utf8 tools/build.py --jurisdiction burgenland --repo . --today 2026-11-13 --offline
python3 -X utf8 tools/check_repo.py --jurisdiction burgenland --repo . --today 2026-11-13
python3 -X utf8 tools/test_repo.py --repo .
```

`data/fassungen.json` lists every RIS document (`NOR...` / `LBG...`) used, with the SHA-256 of its XML (sha256 of `data/fassungen.json`: `2e9748e0a9afed3f4af3e95fedd92db7e60a3cd9c0cfd6882b5411361c3efe13`).

## Coverage (1429 acts, 15328 provisions, 25257 versions in force)

| Act | Slug | Gesetzesnummer | RIS documents | Provisions | Versions in force | Data notes |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| ALSV | `alsv/` | 10000296 | 7 | 7 | 7 | 0 |
| Bgld. AWH-VO 2025 | `awh-vo-2025/` | 20001536 | 73 | 73 | 73 | 0 |
| Bgld. BauG | `baug/` | 10000504 | 153 | 47 | 153 | 1 |
| Bgld. BauVO 2008 | `bgld-bauvo-2008/` | 20000684 | 107 | 59 | 107 | 0 |
| BGLD-BH-UEV-ARBEITS-UND-SOZIALRECHTSDELIKTE | `bgld-bh-uev-arbeits-und-sozialrechtsdelikte/` | 20001554 | 3 | 3 | 3 | 0 |
| BGLD-BH-UEV-KRAFTFAHRDELIKTE | `bgld-bh-uev-kraftfahrdelikte/` | 20001545 | 3 | 3 | 3 | 0 |
| BGLD-BH-UEV-ROTATIONSSYSTEM-2026 | `bgld-bh-uev-rotationssystem-2026/` | 20001549 | 4 | 4 | 4 | 0 |
| BGLD-BH-UEV-STEINBRUCH-PILGERSDORF | `bgld-bh-uev-steinbruch-pilgersdorf/` | 20001592 | 3 | 3 | 3 | 0 |
| BGLD-BH-UEV-VERKEHRSDELIKTE-2026 | `bgld-bh-uev-verkehrsdelikte-2026/` | 20001591 | 4 | 4 | 4 | 0 |
| Bgld. BO 2002 | `bgld-bo-2002/` | 20000180 | 58 | 27 | 58 | 0 |
| Bgld. BVB-ÜVO | `bgld-bvb-uevo/` | 20001300 | 3 | 3 | 3 | 0 |
| Bgld. L-Bau-V 2010 | `bgld-l-bau-v-2010/` | 20000805 | 10 | 6 | 10 | 0 |
| BGLD-UMGEBUNGSLAERMSCHUTZVO | `bgld-umgebungslaermschutzvo/` | 20001212 | 16 | 10 | 16 | 0 |
| Bgld. UPV | `bgld-upv/` | 20000916 | 5 | 5 | 5 | 0 |
| Bgld. BH-GeO | `bh-geo/` | 20001472 | 12 | 9 | 12 | 0 |
| Bgld. EZVO PV/Solar | `ezvo-pv-solar/` | 20001332 | 51 | 26 | 51 | 0 |
| Bgld. G-DSVO | `g-dsvo/` | 10000258 | 19 | 19 | 19 | 0 |
| Bgld. GemO 2003 | `gemo/` | 20000221 | 269 | 118 | 269 | 0 |
| GeOL | `geol/` | 20001481 | 30 | 25 | 30 | 0 |
| GHO 2020 | `gho-2020/` | 20001252 | 72 | 61 | 72 | 1 |
| Bgld. GVVO | `gvvo/` | 20000629 | 13 | 12 | 13 | 0 |
| Bgld. HSkVO | `hskvo/` | 20001333 | 9 | 9 | 9 | 0 |
| Bgld. HTVO 2011 | `htvo-2011/` | 20000840 | 45 | 12 | 45 | 0 |
| Bgld. JagdG 2017 | `jagdg/` | 20001124 | 323 | 172 | 323 | 0 |
| Bgld. KBBG 2009 | `kbbg/` | 20000713 | 208 | 45 | 208 | 0 |
| Bgld. KBEV 2009 | `kbev-2009/` | 20000770 | 27 | 24 | 27 | 0 |
| Bgld. KJHEV | `kjhev/` | 20001232 | 36 | 23 | 36 | 0 |
| Bgld. L-DSVO | `l-dsvo/` | 20000276 | 2 | 2 | 2 | 0 |
| L-VG | `l-vg/` | 10000141 | 271 | 103 | 271 | 2 |
| Bgld. LBedG 2020 | `lbedg/` | 20001247 | 308 | 168 | 308 | 1 |
| LEP 2011 | `lep-2011/` | 20000863 | 6 | 6 | 6 | 0 |
| LKGV 1990 | `lkgv-1990/` | 10000239 | 24 | 8 | 24 | 0 |
| LVAV 2012 | `lvav-2012/` | 20000888 | 10 | 5 | 10 | 0 |
| Bgld. LVwGG | `lvwgg/` | 20000946 | 115 | 48 | 115 | 0 |
| NG 1990 | `ng/` | 10000254 | 446 | 137 | 444 | 5 |
| Bgld. PKVO | `pkvo/` | 20001595 | 28 | 28 | 28 | 0 |
| Bgld. RDSt-VO | `rdst-vo/` | 20001478 | 5 | 5 | 5 | 0 |
| Bgld. RPG 2019 | `rpg/` | 20001224 | 210 | 84 | 210 | 4 |
| Bgld. SHG 2024 | `shg/` | 20001460 | 59 | 52 | 59 | 0 |
| Bgld. VPG-VO | `vpg-vo/` | 20000620 | 13 | 4 | 13 | 0 |
| Bgld. VVAV | `vvav/` | 20000837 | 6 | 6 | 6 | 0 |
| 2. Bgld. LVwgBG | `2-bgld-lvwgbg/` | 20000998 | 8 | 8 | 8 | 0 |
| 3. GruVe-ÄVE | `3-gruve-aeve/` | 20001120 | 2 | 2 | 2 | 0 |
| AARHUS-BETEILIGUNGSGESETZ | `aarhus-beteiligungsgesetz/` | 20001241 | 4 | 4 | 4 | 0 |
| ABFALLWIRTSCHAFTSGESETZ-1993 | `abfallwirtschaftsgesetz-1993/` | 10000365 | 169 | 76 | 164 | 7 |
| ABGABENANPASSUNGSGESETZ-2009 | `abgabenanpassungsgesetz-2009/` | 20000766 | 8 | 8 | 8 | 0 |
| ABGELTUNG-STATIONAERER-MEDIZINISCHER-VERSORGUNGS | `abgeltung-stationaerer-medizinischer-versorgungs/` | 20000723 | 10 | 7 | 10 | 0 |
| ABGELTUNG-STATIONAERER-MEDIZINISCHER-VERSORGUNGS-1140 | `abgeltung-stationaerer-medizinischer-versorgungs-1140/` | 20001140 | 4 | 4 | 4 | 0 |
| Bgld. AbgG | `abgg/` | 20000768 | 14 | 10 | 14 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DEN | `aenderung-der-gemeindegrenze-zwischen-den/` | 20000873 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DEN-0881 | `aenderung-der-gemeindegrenze-zwischen-den-0881/` | 20000881 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DEN-0911 | `aenderung-der-gemeindegrenze-zwischen-den-0911/` | 20000911 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DEN-1086 | `aenderung-der-gemeindegrenze-zwischen-den-1086/` | 20001086 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DEN-1087 | `aenderung-der-gemeindegrenze-zwischen-den-1087/` | 20001087 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER | `aenderung-der-gemeindegrenze-zwischen-der/` | 20000931 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1088 | `aenderung-der-gemeindegrenze-zwischen-der-1088/` | 20001088 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1229 | `aenderung-der-gemeindegrenze-zwischen-der-1229/` | 20001229 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1230 | `aenderung-der-gemeindegrenze-zwischen-der-1230/` | 20001230 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1231 | `aenderung-der-gemeindegrenze-zwischen-der-1231/` | 20001231 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1255 | `aenderung-der-gemeindegrenze-zwischen-der-1255/` | 20001255 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1337 | `aenderung-der-gemeindegrenze-zwischen-der-1337/` | 20001337 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1338 | `aenderung-der-gemeindegrenze-zwischen-der-1338/` | 20001338 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1339 | `aenderung-der-gemeindegrenze-zwischen-der-1339/` | 20001339 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1512 | `aenderung-der-gemeindegrenze-zwischen-der-1512/` | 20001512 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1517 | `aenderung-der-gemeindegrenze-zwischen-der-1517/` | 20001517 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1518 | `aenderung-der-gemeindegrenze-zwischen-der-1518/` | 20001518 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1522 | `aenderung-der-gemeindegrenze-zwischen-der-1522/` | 20001522 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZE-ZWISCHEN-DER-1523 | `aenderung-der-gemeindegrenze-zwischen-der-1523/` | 20001523 | 5 | 5 | 5 | 0 |
| AENDERUNG-DER-GEMEINDEGRENZEN-ZWISCHEN-DER | `aenderung-der-gemeindegrenzen-zwischen-der/` | 20000480 | 3 | 3 | 3 | 0 |
| AENDERUNG-DER-GRENZE-ZWISCHEN-DEN | `aenderung-der-grenze-zwischen-den/` | 20000467 | 4 | 4 | 4 | 0 |
| AENDERUNG-DER-GRENZEN-ZWISCHEN-DEN | `aenderung-der-grenzen-zwischen-den/` | 20000482 | 2 | 2 | 2 | 0 |
| AENDERUNG-DER-LANDESGRENZE-ZWISCHEN-BURGENLAND | `aenderung-der-landesgrenze-zwischen-burgenland/` | 10000106 | 10 | 10 | 10 | 0 |
| AENDERUNG-DER-LANDESGRENZE-ZWISCHEN-DEM | `aenderung-der-landesgrenze-zwischen-dem/` | 10000123 | 7 | 7 | 7 | 0 |
| AENDERUNG-DER-SATZUNG-DES-GEMEINDEVERBANDES | `aenderung-der-satzung-des-gemeindeverbandes/` | 20000491 | 2 | 2 | 2 | 0 |
| AENDERUNG-DER-SPRENGEL-DER-POLITISCHEN | `aenderung-der-sprengel-der-politischen/` | 10000084 | 3 | 3 | 3 | 0 |
| AENDERUNG-DER-SPRENGEL-DES-POLITISCHEN | `aenderung-der-sprengel-des-politischen/` | 10000077 | 3 | 3 | 3 | 0 |
| AENDERUNG-DER-VEREINBARUNG-UEBER-DIE | `aenderung-der-vereinbarung-ueber-die/` | 20001594 | 3 | 3 | 3 | 0 |
| AENDERUNG-DES-GEMEINDENAMENS-DER-MARKTGEMEINDE | `aenderung-des-gemeindenamens-der-marktgemeinde/` | 20000767 | 2 | 2 | 2 | 0 |
| AENDERUNG-DES-GEMEINDENAMENS-FORCHTENAU-AUF | `aenderung-des-gemeindenamens-forchtenau-auf/` | 20000430 | 3 | 3 | 3 | 0 |
| AENDERUNG-DES-GEMEINDENAMENS-OGGAU-IN | `aenderung-des-gemeindenamens-oggau-in/` | 20000427 | 3 | 3 | 3 | 0 |
| AENDERUNG-DES-GEMEINDENAMENS-SANKT-ANDRAE | `aenderung-des-gemeindenamens-sankt-andrae/` | 20000429 | 3 | 3 | 3 | 0 |
| AENDERUNG-DES-GEMEINDENAMENS-SAUERBRUNN-IN | `aenderung-des-gemeindenamens-sauerbrunn-in/` | 20000428 | 3 | 3 | 3 | 0 |
| AENDERUNG-DES-GEMEINDEVERBANDES-BOCKSDORF | `aenderung-des-gemeindeverbandes-bocksdorf/` | 20000492 | 4 | 4 | 4 | 0 |
| AENDERUNG-DES-GEMEINDEVERBANDES-BOCKSDORF-HEUGRA | `aenderung-des-gemeindeverbandes-bocksdorf-heugra/` | 20000499 | 4 | 4 | 4 | 0 |
| AENDERUNG-DES-GEMEINDEVERBANDES-OLLERSDORF-IM | `aenderung-des-gemeindeverbandes-ollersdorf-im/` | 10000378 | 5 | 5 | 5 | 0 |
| AENDERUNG-DES-SITZES-DES-GEMEINDEVERBANDES | `aenderung-des-sitzes-des-gemeindeverbandes/` | 10000449 | 3 | 3 | 3 | 0 |
| AENDERUNG-DES-STANDESAMTSVERBANDES-BOCKSDORF-IN | `aenderung-des-standesamtsverbandes-bocksdorf-in/` | 20000500 | 4 | 4 | 4 | 0 |
| AENDERUNG-DES-STRASSENVERLAUFES-DER-B | `aenderung-des-strassenverlaufes-der-b/` | 20001036 | 3 | 3 | 3 | 0 |
| AENDERUNG-VON-STANDESAMTSBEZIRKEN | `aenderung-von-standesamtsbezirken/` | 10000089 | 9 | 9 | 9 | 0 |
| AENDERUNG-VON-STANDESAMTSBEZIRKEN-0093 | `aenderung-von-standesamtsbezirken-0093/` | 10000093 | 2 | 2 | 2 | 0 |
| AENDERUNG-VON-TEILSTRECKEN-DER-LANDESGRENZE | `aenderung-von-teilstrecken-der-landesgrenze/` | 10000076 | 6 | 6 | 6 | 0 |
| AENDERUNG-ZWISCHEN-DEM-LAND-BURGENLAND | `aenderung-zwischen-dem-land-burgenland/` | 10000197 | 7 | 7 | 7 | 0 |
| AENDERUNGSVEREINBARUNG-BETREFFEND-KLIMASCHUTZMAS | `aenderungsvereinbarung-betreffend-klimaschutzmas/` | 20001143 | 2 | 2 | 2 | 0 |
| ALLGEMEINE-NATURSCHUTZVERORDNUNG | `allgemeine-naturschutzverordnung/` | 10000309 | 9 | 9 | 9 | 0 |
| ALLGEMEINES-FAHRVERBOT-AUF-DER-GEMEINDESTRASSE | `allgemeines-fahrverbot-auf-der-gemeindestrasse/` | 20000178 | 2 | 2 | 2 | 0 |
| ANERKENNUNG-DES-QUALITAETSRAHMENS-FUER-DIE | `anerkennung-des-qualitaetsrahmens-fuer-die/` | 20000905 | 13 | 13 | 13 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE | `angelegenheiten-des-eigenen-wirkungsbereiches-de/` | 10000327 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0060 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0060/` | 20000060 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0148 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0148/` | 20000148 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0226 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0226/` | 20000226 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0231 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0231/` | 20000231 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0232 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0232/` | 20000232 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0233 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0233/` | 20000233 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0234 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0234/` | 20000234 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0359 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0359/` | 10000359 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0361 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0361/` | 10000361 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0362 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0362/` | 10000362 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0363 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0363/` | 10000363 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0498 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0498/` | 20000498 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0522 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0522/` | 20000522 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0580 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0580/` | 20000580 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0823 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0823/` | 20000823 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-0836 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-0836/` | 20000836 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-1099 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-1099/` | 20001099 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-1100 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-1100/` | 20001100 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-1101 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-1101/` | 20001101 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-1102 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-1102/` | 20001102 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-1103 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-1103/` | 20001103 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-1104 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-1104/` | 20001104 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-DE-1108 | `angelegenheiten-des-eigenen-wirkungsbereiches-de-1108/` | 20001108 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-EI | `angelegenheiten-des-eigenen-wirkungsbereiches-ei/` | 10000354 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-EI-0497 | `angelegenheiten-des-eigenen-wirkungsbereiches-ei-0497/` | 20000497 | 3 | 2 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-EI-0514 | `angelegenheiten-des-eigenen-wirkungsbereiches-ei-0514/` | 20000514 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-ME | `angelegenheiten-des-eigenen-wirkungsbereiches-me/` | 20000034 | 3 | 2 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-NA | `angelegenheiten-des-eigenen-wirkungsbereiches-na/` | 20000525 | 6 | 2 | 6 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-NA-0527 | `angelegenheiten-des-eigenen-wirkungsbereiches-na-0527/` | 20000527 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-VO | `angelegenheiten-des-eigenen-wirkungsbereiches-vo/` | 20000225 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-VO-0511 | `angelegenheiten-des-eigenen-wirkungsbereiches-vo-0511/` | 20000511 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHES-VO-1107 | `angelegenheiten-des-eigenen-wirkungsbereiches-vo-1107/` | 20001107 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHS-DER | `angelegenheiten-des-eigenen-wirkungsbereichs-der/` | 20000705 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHS-DER-0773 | `angelegenheiten-des-eigenen-wirkungsbereichs-der-0773/` | 20000773 | 2 | 2 | 2 | 0 |
| ANGELEGENHEITEN-DES-EIGENEN-WIRKUNGSBEREICHS-DER-0855 | `angelegenheiten-des-eigenen-wirkungsbereichs-der-0855/` | 20000855 | 3 | 3 | 3 | 0 |
| ANGELEGENHEITEN-DES-NIEDERLASSUNGS-UND-AUFENTHAL | `angelegenheiten-des-niederlassungs-und-aufenthal/` | 20000368 | 3 | 3 | 3 | 0 |
| ANORDNUNG-EINER-VOLKSABSTIMMUNG | `anordnung-einer-volksabstimmung/` | 10000200 | 4 | 4 | 4 | 0 |
| ANORDNUNG-EINER-VOLKSBEFRAGUNG | `anordnung-einer-volksbefragung/` | 20000099 | 5 | 5 | 5 | 0 |
| ANPASSUNG-DER-ORTSTAXE | `anpassung-der-ortstaxe/` | 20000100 | 3 | 3 | 3 | 0 |
| ANPASSUNGEN-DER-BURGENLAENDISCHEN-LANDESRECHTSOR | `anpassungen-der-burgenlaendischen-landesrechtsor/` | 20001272 | 37 | 37 | 37 | 0 |
| ANPASSUNGEN-DES-BURGENLAENDISCHEN-GEMEINDERECHTS | `anpassungen-des-burgenlaendischen-gemeinderechts/` | 20001277 | 4 | 4 | 4 | 0 |
| ANPASSUNGSFAKTOR-IN-RUHE-UND-VERSORGUNGSRECHTLIC | `anpassungsfaktor-in-ruhe-und-versorgungsrechtlic/` | 20001568 | 3 | 3 | 3 | 0 |
| ANSTELLUNGSERFORDERNISSE-FUER-ELEMENTARPAEDAGOGI | `anstellungserfordernisse-fuer-elementarpaedagogi/` | 10000506 | 44 | 11 | 43 | 2 |
| ANWENDUNG-DES-VERTRAGSBEDIENSTETENGESETZES | `anwendung-des-vertragsbedienstetengesetzes/` | 10000041 | 4 | 4 | 4 | 0 |
| ANZEIGEPFLICHT-BEI-ERKRANKUNGEN | `anzeigepflicht-bei-erkrankungen/` | 10000033 | 2 | 2 | 2 | 0 |
| ANZEIGEPFLICHT-BEI-ERKRANKUNGEN-IN-ANSTALTEN | `anzeigepflicht-bei-erkrankungen-in-anstalten/` | 10000034 | 2 | 2 | 2 | 0 |
| Bgld. AOG | `aog/` | 20001413 | 22 | 20 | 22 | 0 |
| ARBEITNEHMERFOERDERUNGSGESETZ | `arbeitnehmerfoerderungsgesetz/` | 10000201 | 17 | 11 | 17 | 0 |
| Bgld. ArchivG | `archivg/` | 20001298 | 28 | 22 | 28 | 0 |
| ART-UND-AUSMASS-DER-VERWENDUNG | `art-und-ausmass-der-verwendung/` | 20000610 | 4 | 4 | 4 | 0 |
| ARTENSCHUTZVERORDNUNG-2001 | `artenschutzverordnung-2001/` | 20000110 | 12 | 9 | 11 | 1 |
| ASP-PRAEVENTIONSVERORDNUNG-2026 | `asp-praeventionsverordnung-2026/` | 20001546 | 3 | 3 | 3 | 0 |
| AUFFORSTUNG-VON-NICHTWALDFLAECHEN | `aufforstung-von-nichtwaldflaechen/` | 10000220 | 7 | 6 | 7 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE | `aufhebung-der-verordnung-der-gemeinde/` | 20000236 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE-0245 | `aufhebung-der-verordnung-der-gemeinde-0245/` | 20000245 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE-0268 | `aufhebung-der-verordnung-der-gemeinde-0268/` | 20000268 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE-0357 | `aufhebung-der-verordnung-der-gemeinde-0357/` | 20000357 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE-0384 | `aufhebung-der-verordnung-der-gemeinde-0384/` | 20000384 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE-0588 | `aufhebung-der-verordnung-der-gemeinde-0588/` | 20000588 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE-0639 | `aufhebung-der-verordnung-der-gemeinde-0639/` | 20000639 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-GEMEINDE-0662 | `aufhebung-der-verordnung-der-gemeinde-0662/` | 20000662 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-MARKTGEMEINDE | `aufhebung-der-verordnung-der-marktgemeinde/` | 20000047 | 3 | 3 | 3 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-MARKTGEMEINDE-0070 | `aufhebung-der-verordnung-der-marktgemeinde-0070/` | 20000070 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-MARKTGEMEINDE-0174 | `aufhebung-der-verordnung-der-marktgemeinde-0174/` | 20000174 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DER-MARKTGEMEINDE-0175 | `aufhebung-der-verordnung-der-marktgemeinde-0175/` | 20000175 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DES-GEMEINDERATES | `aufhebung-der-verordnung-des-gemeinderates/` | 20000861 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-DES-GEMEINDERATES-0993 | `aufhebung-der-verordnung-des-gemeinderates-0993/` | 20000993 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DER-VERORDNUNG-UEBER-DIE | `aufhebung-der-verordnung-ueber-die/` | 20001041 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-DES-GETRAENKE-UND-SPEISEEISABGABEGESET | `aufhebung-des-getraenke-und-speiseeisabgabegeset/` | 20000106 | 3 | 3 | 3 | 0 |
| AUFHEBUNG-DES-SCHLACHTHAUSZWANGES | `aufhebung-des-schlachthauszwanges/` | 10000096 | 3 | 3 | 3 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-GEMEINDE | `aufhebung-einer-verordnung-der-gemeinde/` | 20000235 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-GEMEINDE-0613 | `aufhebung-einer-verordnung-der-gemeinde-0613/` | 20000613 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-GEMEINDE-0640 | `aufhebung-einer-verordnung-der-gemeinde-0640/` | 20000640 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-GEMEINDE-0642 | `aufhebung-einer-verordnung-der-gemeinde-0642/` | 20000642 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-GEMEINDE-0643 | `aufhebung-einer-verordnung-der-gemeinde-0643/` | 20000643 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-GEMEINDE-0741 | `aufhebung-einer-verordnung-der-gemeinde-0741/` | 20000741 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-GEMEINDE-0899 | `aufhebung-einer-verordnung-der-gemeinde-0899/` | 20000899 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-STADTGEMEINDE | `aufhebung-einer-verordnung-der-stadtgemeinde/` | 20000320 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DER-STADTGEMEINDE-0694 | `aufhebung-einer-verordnung-der-stadtgemeinde-0694/` | 20000694 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-BUERGERMEISTERS | `aufhebung-einer-verordnung-des-buergermeisters/` | 20001012 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-BUERGERMEISTERS-1323 | `aufhebung-einer-verordnung-des-buergermeisters-1323/` | 20001323 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-BUERGERMEISTERS-1324 | `aufhebung-einer-verordnung-des-buergermeisters-1324/` | 20001324 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-BUERGERMEISTERS-1325 | `aufhebung-einer-verordnung-des-buergermeisters-1325/` | 20001325 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-BUERGERMEISTERS-1326 | `aufhebung-einer-verordnung-des-buergermeisters-1326/` | 20001326 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-BUERGERMEISTERS-1329 | `aufhebung-einer-verordnung-des-buergermeisters-1329/` | 20001329 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES | `aufhebung-einer-verordnung-des-gemeinderates/` | 20000830 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1072 | `aufhebung-einer-verordnung-des-gemeinderates-1072/` | 20001072 | 3 | 3 | 3 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1196 | `aufhebung-einer-verordnung-des-gemeinderates-1196/` | 20001196 | 3 | 3 | 3 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1327 | `aufhebung-einer-verordnung-des-gemeinderates-1327/` | 20001327 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1344 | `aufhebung-einer-verordnung-des-gemeinderates-1344/` | 20001344 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1508 | `aufhebung-einer-verordnung-des-gemeinderates-1508/` | 20001508 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1509 | `aufhebung-einer-verordnung-des-gemeinderates-1509/` | 20001509 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1513 | `aufhebung-einer-verordnung-des-gemeinderates-1513/` | 20001513 | 3 | 3 | 3 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1519 | `aufhebung-einer-verordnung-des-gemeinderates-1519/` | 20001519 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1524 | `aufhebung-einer-verordnung-des-gemeinderates-1524/` | 20001524 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1525 | `aufhebung-einer-verordnung-des-gemeinderates-1525/` | 20001525 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1526 | `aufhebung-einer-verordnung-des-gemeinderates-1526/` | 20001526 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-GEMEINDERATES-1527 | `aufhebung-einer-verordnung-des-gemeinderates-1527/` | 20001527 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINER-VERORDNUNG-DES-MAGISTRATES | `aufhebung-einer-verordnung-des-magistrates/` | 20000229 | 3 | 3 | 3 | 0 |
| AUFHEBUNG-EINES-TEILES-DER-VERORDNUNG | `aufhebung-eines-teiles-der-verordnung/` | 20000309 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINES-TEILES-DER-VERORDNUNG-0311 | `aufhebung-eines-teiles-der-verordnung-0311/` | 20000311 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINES-TEILES-DER-VERORDNUNG-0820 | `aufhebung-eines-teiles-der-verordnung-0820/` | 20000820 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-EINR-VERORDNUNG-MIT-DER | `aufhebung-einr-verordnung-mit-der/` | 20000795 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-VON-TEILEN-EINER-VERORDNUNG | `aufhebung-von-teilen-einer-verordnung/` | 20000755 | 2 | 2 | 2 | 0 |
| AUFHEBUNG-VON-VERORDNUNGEN-DES-BUERGERMEISTERS | `aufhebung-von-verordnungen-des-buergermeisters/` | 20001040 | 3 | 3 | 3 | 0 |
| AUFLASSUNG-DER-EISENBAHNZUFAHRTSSTRASSE-IN-OBERW | `auflassung-der-eisenbahnzufahrtsstrasse-in-oberw/` | 20000532 | 2 | 2 | 2 | 0 |
| AUFLASSUNG-DER-EISENBAHNZUFAHRTSSTRASSE-IN-PAMHA | `auflassung-der-eisenbahnzufahrtsstrasse-in-pamha/` | 20000781 | 4 | 4 | 4 | 0 |
| AUFLASSUNG-DER-EISENBAHNZUFAHRTSSTRASSEN-IN-GOLS | `auflassung-der-eisenbahnzufahrtsstrassen-in-gols/` | 20000537 | 7 | 7 | 7 | 0 |
| AUFLASSUNG-DER-EISENBAHNZUFAHRTSSTRASSEN-IN-PARN | `auflassung-der-eisenbahnzufahrtsstrassen-in-parn/` | 20000535 | 4 | 4 | 4 | 0 |
| AUFLASSUNG-DER-EISENBAHNZUFAHRTSSTRASSEN-IN-WEID | `auflassung-der-eisenbahnzufahrtsstrassen-in-weid/` | 20000538 | 5 | 5 | 5 | 0 |
| AUFLASSUNG-DER-LANDWIRTSCHAFTLICHEN-FACHSCHULE-N | `auflassung-der-landwirtschaftlichen-fachschule-n/` | 20000893 | 2 | 2 | 2 | 0 |
| AUFLASSUNG-DER-LASCHOBERSTRASSE-IN-EISENSTADT | `auflassung-der-laschoberstrasse-in-eisenstadt/` | 20000534 | 2 | 2 | 2 | 0 |
| AUFLASSUNG-DES-BAHNWEGES-L-2431 | `auflassung-des-bahnweges-l-2431/` | 20000536 | 2 | 2 | 2 | 0 |
| AUFLASSUNG-EINER-EISENBAHNZUFAHRTSSTRASSE-IN-JEN | `auflassung-einer-eisenbahnzufahrtsstrasse-in-jen/` | 20000533 | 2 | 2 | 2 | 0 |
| AUFLASSUNG-VON-EISENBAHNZUFAHRTSSTRASSEN | `auflassung-von-eisenbahnzufahrtsstrassen/` | 20000531 | 2 | 2 | 2 | 0 |
| AUFLOESUNG-DER-OERTLICHEN-TOURISMUSVERBAENDE-LAC | `aufloesung-der-oertlichen-tourismusverbaende-lac/` | 20001160 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-BAUFONDS-BUNDESSTRASSEN-VORFINANZ | `aufloesung-des-baufonds-bundesstrassen-vorfinanz/` | 10000223 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-GEMEINDERATES-DER-MARKTGEMEINDE | `aufloesung-des-gemeinderates-der-marktgemeinde/` | 20000586 | 2 | 2 | 2 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-DRASSBURG | `aufloesung-des-gemeindeverbandes-drassburg/` | 10000482 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-GRAFENSCHACHEN | `aufloesung-des-gemeindeverbandes-grafenschachen/` | 20000195 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-LEITHAPRODERSDO | `aufloesung-des-gemeindeverbandes-leithaprodersdo/` | 20001343 | 5 | 5 | 5 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-NEUSTIFT-BEI | `aufloesung-des-gemeindeverbandes-neustift-bei/` | 20001181 | 5 | 5 | 5 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-OLLERSDORF | `aufloesung-des-gemeindeverbandes-ollersdorf/` | 10000452 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-PERSONENNAHVERK | `aufloesung-des-gemeindeverbandes-personennahverk/` | 20001543 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-PIRINGSDORF-UNT | `aufloesung-des-gemeindeverbandes-piringsdorf-unt/` | 10000380 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-POETTELSDORF-ZE | `aufloesung-des-gemeindeverbandes-poettelsdorf-ze/` | 20000118 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-RECHNITZ-MARKT | `aufloesung-des-gemeindeverbandes-rechnitz-markt/` | 10000379 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-STEINBRUNN-ZILL | `aufloesung-des-gemeindeverbandes-steinbrunn-zill/` | 10000315 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-GEMEINDEVERBANDES-STOOB | `aufloesung-des-gemeindeverbandes-stoob/` | 20000794 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-LANDESVERBANDES-BURGENLAND-TOURIS | `aufloesung-des-landesverbandes-burgenland-touris/` | 20001424 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-LANDTAGES | `aufloesung-des-landtages/` | 10000253 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-LANDTAGES-0429 | `aufloesung-des-landtages-0429/` | 10000429 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-LANDTAGES-0769 | `aufloesung-des-landtages-0769/` | 20000769 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-OERTLICHEN-TOURISMUSVERBANDES-DER | `aufloesung-des-oertlichen-tourismusverbandes-der/` | 20000067 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-OERTLICHEN-TOURISMUSVERBANDES-DER-0094 | `aufloesung-des-oertlichen-tourismusverbandes-der-0094/` | 20000094 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-OERTLICHEN-TOURISMUSVERBANDS-HORI | `aufloesung-des-oertlichen-tourismusverbands-hori/` | 20001184 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-OERTLICHEN-TOURISMUSVERBANDS-NIKI | `aufloesung-des-oertlichen-tourismusverbands-niki/` | 20001198 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-OERTLICHEN-TOURISMUSVERBANDS-RITZ | `aufloesung-des-oertlichen-tourismusverbands-ritz/` | 20001176 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-REGIONALVERBANDES-KIRSCHBLUETENRE | `aufloesung-des-regionalverbandes-kirschbluetenre/` | 20000159 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-BOCKSDORF | `aufloesung-des-standesamtsverbandes-bocksdorf/` | 20001096 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-EBERAU | `aufloesung-des-standesamtsverbandes-eberau/` | 20000013 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-ELTENDORF | `aufloesung-des-standesamtsverbandes-eltendorf/` | 10000433 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-GRAFENSCHACH | `aufloesung-des-standesamtsverbandes-grafenschach/` | 10000358 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-KAISERSDORF | `aufloesung-des-standesamtsverbandes-kaisersdorf/` | 10000374 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-KEMETEN | `aufloesung-des-standesamtsverbandes-kemeten/` | 10000311 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-KOHFIDISCH | `aufloesung-des-standesamtsverbandes-kohfidisch/` | 20000261 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-LEITHAPRODER | `aufloesung-des-standesamtsverbandes-leithaproder/` | 20001154 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-MANNERSDORF | `aufloesung-des-standesamtsverbandes-mannersdorf/` | 20000973 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-MARZ | `aufloesung-des-standesamtsverbandes-marz/` | 10000246 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-MOGERSDORF | `aufloesung-des-standesamtsverbandes-mogersdorf/` | 20000494 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-NEUHAUS-AM | `aufloesung-des-standesamtsverbandes-neuhaus-am/` | 20000194 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-PIRINGSDORF | `aufloesung-des-standesamtsverbandes-piringsdorf/` | 10000376 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-POETTELSDORF | `aufloesung-des-standesamtsverbandes-poettelsdorf/` | 20000113 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-RECHNITZ | `aufloesung-des-standesamtsverbandes-rechnitz/` | 10000375 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-SCHACHENDORF | `aufloesung-des-standesamtsverbandes-schachendorf/` | 20000813 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-SCHATTENDORF | `aufloesung-des-standesamtsverbandes-schattendorf/` | 10000276 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-SIGLESS | `aufloesung-des-standesamtsverbandes-sigless/` | 20000074 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-STEINBRUNN | `aufloesung-des-standesamtsverbandes-steinbrunn/` | 20001155 | 3 | 3 | 3 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-STOOB | `aufloesung-des-standesamtsverbandes-stoob/` | 20000814 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-STREM | `aufloesung-des-standesamtsverbandes-strem/` | 10000446 | 4 | 4 | 4 | 0 |
| AUFLOESUNG-DES-STANDESAMTSVERBANDES-UNTERWART | `aufloesung-des-standesamtsverbandes-unterwart/` | 10000312 | 4 | 4 | 4 | 0 |
| AUFTEILUNG-DES-DER-BURGENLAND-TOURISMUS | `aufteilung-des-der-burgenland-tourismus/` | 20001558 | 3 | 3 | 3 | 0 |
| AUFTEILUNG-UND-VERWENDUNG-NACH-DEM | `aufteilung-und-verwendung-nach-dem/` | 10000212 | 13 | 13 | 13 | 0 |
| AUFWANDSENTSCHAEDIGUNG-DER-GEMEINDEMANDATARE | `aufwandsentschaedigung-der-gemeindemandatare/` | 10000329 | 6 | 6 | 6 | 0 |
| AUFWANDSENTSCHAEDIGUNG-DER-GEMEINDEMANDATARE-DER | `aufwandsentschaedigung-der-gemeindemandatare-der/` | 10000341 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-HOECHSTBEITRAGSGRUNDLAGE-UND | `aufwertungsfaktoren-hoechstbeitragsgrundlage-und/` | 20000264 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-HOECHSTBEITRAGSGRUNDLAGE-UND-0718 | `aufwertungsfaktoren-hoechstbeitragsgrundlage-und-0718/` | 20000718 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-HOECHSTBEITRAGSGRUNDLAGE-UND-0777 | `aufwertungsfaktoren-hoechstbeitragsgrundlage-und-0777/` | 20000777 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-HOECHSTBEITRAGSGRUNDLAGE-UND-0832 | `aufwertungsfaktoren-hoechstbeitragsgrundlage-und-0832/` | 20000832 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-HOECHSTBEITRAGSGRUNDLAGE-UND-0871 | `aufwertungsfaktoren-hoechstbeitragsgrundlage-und-0871/` | 20000871 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-HOECHSTBEITRAGSGRUNDLAGE-UND-0925 | `aufwertungsfaktoren-hoechstbeitragsgrundlage-und-0925/` | 20000925 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-HOECHSTBEITRAGSGRUNDLAGE-UND-1569 | `aufwertungsfaktoren-hoechstbeitragsgrundlage-und-1569/` | 20001569 | 5 | 5 | 5 | 0 |
| AUFWERTUNGSFAKTOREN-UND-DIE-HOECHSTBEITRAGSGRUND | `aufwertungsfaktoren-und-die-hoechstbeitragsgrund/` | 20000622 | 4 | 4 | 4 | 0 |
| AUFWERTUNGSFAKTOREN-UND-HOECHSTBEITRAGSGRUNDLAGE | `aufwertungsfaktoren-und-hoechstbeitragsgrundlage/` | 20000383 | 4 | 4 | 4 | 0 |
| AUFWERTUNGSFAKTOREN-UND-HOECHSTBEITRAGSGRUNDLAGE-0669 | `aufwertungsfaktoren-und-hoechstbeitragsgrundlage-0669/` | 20000669 | 4 | 4 | 4 | 0 |
| AUS-UND-NACHPFLANZUNGEN-ZUGELASSENER-REBSORTEN | `aus-und-nachpflanzungen-zugelassener-rebsorten/` | 10000134 | 2 | 2 | 2 | 0 |
| AUSBAU-DER-GANZTAEGIGEN-SCHULFORMEN | `ausbau-der-ganztaegigen-schulformen/` | 20000865 | 12 | 11 | 12 | 0 |
| AUSBAU-DES-INSTITUTIONELLEN-KINDERBETREUUNGSANGE | `ausbau-des-institutionellen-kinderbetreuungsange/` | 20000866 | 27 | 14 | 27 | 0 |
| AUSBILDUNG-ZUR-DIPLOM-SOZIALBETREUERIN-ODER-ZUM | `ausbildung-zur-diplom-sozialbetreuerin-oder-zum/` | 20000971 | 25 | 18 | 25 | 0 |
| AUSBILDUNG-ZUR-FACH-SOZIALBETREUERIN-ODER-ZUM | `ausbildung-zur-fach-sozialbetreuerin-oder-zum/` | 20000970 | 25 | 18 | 25 | 0 |
| AusbVOHandwD | `ausbvohandwd/` | 20001031 | 16 | 16 | 16 | 0 |
| AusbVOHandwD-Gem | `ausbvohandwd-gem/` | 20001567 | 13 | 13 | 13 | 0 |
| AUSGESTALTUNG-UND-INHALT-ENTGELTLICHER-VEROEFFEN | `ausgestaltung-und-inhalt-entgeltlicher-veroeffen/` | 20000894 | 6 | 6 | 6 | 0 |
| AUSGLEICH-GESUNDHEITLICHER-BELASTUNGEN-FUER-DAS | `ausgleich-gesundheitlicher-belastungen-fuer-das/` | 10000409 | 2 | 2 | 2 | 0 |
| AUSSCHEIDEN-DER-GEMEINDE-OLBENDORF-AUS | `ausscheiden-der-gemeinde-olbendorf-aus/` | 20000493 | 4 | 4 | 4 | 0 |
| AUSSCHEIDEN-DER-GEMEINDE-OLLERSDORF | `ausscheiden-der-gemeinde-ollersdorf/` | 10000458 | 4 | 4 | 4 | 0 |
| AUSSCHEIDEN-DER-GEMEINDE-WOERTERBERG-AUS | `ausscheiden-der-gemeinde-woerterberg-aus/` | 20000119 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS | `ausschreibung-der-neuwahl-des-buergermeisters/` | 10000522 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0037 | `ausschreibung-der-neuwahl-des-buergermeisters-0037/` | 20000037 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0040 | `ausschreibung-der-neuwahl-des-buergermeisters-0040/` | 20000040 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0075 | `ausschreibung-der-neuwahl-des-buergermeisters-0075/` | 20000075 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0085 | `ausschreibung-der-neuwahl-des-buergermeisters-0085/` | 20000085 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0525 | `ausschreibung-der-neuwahl-des-buergermeisters-0525/` | 10000525 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0714 | `ausschreibung-der-neuwahl-des-buergermeisters-0714/` | 20000714 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0750 | `ausschreibung-der-neuwahl-des-buergermeisters-0750/` | 20000750 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0751 | `ausschreibung-der-neuwahl-des-buergermeisters-0751/` | 20000751 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0792 | `ausschreibung-der-neuwahl-des-buergermeisters-0792/` | 20000792 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0807 | `ausschreibung-der-neuwahl-des-buergermeisters-0807/` | 20000807 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0829 | `ausschreibung-der-neuwahl-des-buergermeisters-0829/` | 20000829 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-0846 | `ausschreibung-der-neuwahl-des-buergermeisters-0846/` | 20000846 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-1068 | `ausschreibung-der-neuwahl-des-buergermeisters-1068/` | 20001068 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-1177 | `ausschreibung-der-neuwahl-des-buergermeisters-1177/` | 20001177 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-1180 | `ausschreibung-der-neuwahl-des-buergermeisters-1180/` | 20001180 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-1316 | `ausschreibung-der-neuwahl-des-buergermeisters-1316/` | 20001316 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-1456 | `ausschreibung-der-neuwahl-des-buergermeisters-1456/` | 20001456 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-1506 | `ausschreibung-der-neuwahl-des-buergermeisters-1506/` | 20001506 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHL-DES-BUERGERMEISTERS-1578 | `ausschreibung-der-neuwahl-des-buergermeisters-1578/` | 20001578 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHLEN-DES-BUERGERMEISTERS | `ausschreibung-der-neuwahlen-des-buergermeisters/` | 20001001 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-NEUWAHLEN-DES-GEMEINDERATES | `ausschreibung-der-neuwahlen-des-gemeinderates/` | 20000585 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DER-MITGLIEDER | `ausschreibung-der-wahl-der-mitglieder/` | 20000187 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DER-MITGLIEDER-0651 | `ausschreibung-der-wahl-der-mitglieder-0651/` | 20000651 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DER-MITGLIEDER-0910 | `ausschreibung-der-wahl-der-mitglieder-0910/` | 20000910 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DER-MITGLIEDER-1146 | `ausschreibung-der-wahl-der-mitglieder-1146/` | 20001146 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DER-MITGLIEDER-1387 | `ausschreibung-der-wahl-der-mitglieder-1387/` | 20001387 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DES-BURGENLAENDISCHEN | `ausschreibung-der-wahl-des-burgenlaendischen/` | 10000453 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DES-BURGENLAENDISCHEN-0065 | `ausschreibung-der-wahl-des-burgenlaendischen-0065/` | 20000065 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DES-BURGENLAENDISCHEN-0350 | `ausschreibung-der-wahl-des-burgenlaendischen-0350/` | 20000350 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DES-BURGENLAENDISCHEN-0771 | `ausschreibung-der-wahl-des-burgenlaendischen-0771/` | 20000771 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DES-BURGENLAENDISCHEN-1017 | `ausschreibung-der-wahl-des-burgenlaendischen-1017/` | 20001017 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DES-LANDTAGES | `ausschreibung-der-wahl-des-landtages/` | 10000204 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-DES-LANDTAGES-0275 | `ausschreibung-der-wahl-des-landtages-0275/` | 10000275 | 4 | 4 | 4 | 0 |
| AUSSCHREIBUNG-DER-WAHL-IN-DIE | `ausschreibung-der-wahl-in-die/` | 10000203 | 2 | 2 | 2 | 0 |
| AUSSCHREIBUNG-DER-WAHL-IN-DIE-0308 | `ausschreibung-der-wahl-in-die-0308/` | 10000308 | 2 | 2 | 2 | 0 |
| AUSSCHREIBUNG-DER-WAHL-IN-DIE-0477 | `ausschreibung-der-wahl-in-die-0477/` | 10000477 | 2 | 2 | 2 | 0 |
| AUSSCHREIBUNG-DER-WIEDERHOLUNGSWAHLEN-DES-GEMEIN | `ausschreibung-der-wiederholungswahlen-des-gemein/` | 20000659 | 4 | 4 | 4 | 0 |
| AUSUEBUNG-DER-FUNKTION-DER-PRAESIDENTIN-DES | `ausuebung-der-funktion-der-praesidentin-des/` | 20001197 | 3 | 3 | 3 | 0 |
| B-LArchivBO | `b-larchivbo/` | 20001381 | 10 | 10 | 10 | 0 |
| BADEGEWAESSERVERORDNUNG-2020 | `badegewaesserverordnung-2020/` | 20001285 | 3 | 3 | 3 | 0 |
| Bgld. BANastV | `banastv/` | 20000975 | 16 | 6 | 16 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-BILDEIN | `bau-uebertragungs-verordnung-bildein/` | 20001492 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-DEUTSCH-KALTENBRUNN | `bau-uebertragungs-verordnung-deutsch-kaltenbrunn/` | 20001164 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-GERERSDORF-SULZ | `bau-uebertragungs-verordnung-gerersdorf-sulz/` | 20001429 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-GUESSING | `bau-uebertragungs-verordnung-guessing/` | 20001360 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-HACKERBERG | `bau-uebertragungs-verordnung-hackerberg/` | 20001577 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-HALBTURN | `bau-uebertragungs-verordnung-halbturn/` | 20001122 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-MOERBISCH-AM-SEE | `bau-uebertragungs-verordnung-moerbisch-am-see/` | 20001459 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-NEUSIEDL-AM-SEE | `bau-uebertragungs-verordnung-neusiedl-am-see/` | 20001015 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-RAUCHWART | `bau-uebertragungs-verordnung-rauchwart/` | 20001572 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-RUDERSDORF | `bau-uebertragungs-verordnung-rudersdorf/` | 20001165 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-SCHUETZEN-AM-GEBIRG | `bau-uebertragungs-verordnung-schuetzen-am-gebirg/` | 20001440 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-ST-MICHAEL-IM-BURGE | `bau-uebertragungs-verordnung-st-michael-im-burge/` | 20001573 | 2 | 2 | 2 | 0 |
| BAU-UEBERTRAGUNGS-VERORDNUNG-TADTEN | `bau-uebertragungs-verordnung-tadten/` | 20001411 | 2 | 2 | 2 | 0 |
| BEISTELLUNG-EINES-LEHRERS-FUER-SCHULVERSUCHE | `beistellung-eines-lehrers-fuer-schulversuche/` | 10000298 | 3 | 3 | 3 | 0 |
| BEKAEMPFUNG-DER-BAKTERIELLEN-BRAUNFAEULE-DER | `bekaempfung-der-bakteriellen-braunfaeule-der/` | 20000007 | 13 | 11 | 13 | 0 |
| BEKAEMPFUNG-DER-BAKTERIELLEN-RINGFAEULE-DER | `bekaempfung-der-bakteriellen-ringfaeule-der/` | 10000513 | 12 | 11 | 12 | 0 |
| BEKAEMPFUNG-DER-SAN-JOSE-SCHILDLAUS | `bekaempfung-der-san-jose-schildlaus/` | 10000481 | 11 | 11 | 11 | 0 |
| BEKAEMPFUNG-DER-TUBERKULOSE-DER-RINDER | `bekaempfung-der-tuberkulose-der-rinder/` | 10000059 | 13 | 13 | 13 | 0 |
| BEKAEMPFUNG-DES-FEUERBRANDES | `bekaempfung-des-feuerbrandes/` | 20000202 | 11 | 10 | 11 | 0 |
| BEKAEMPFUNG-DES-KARTOFFELKREBSES | `bekaempfung-des-kartoffelkrebses/` | 10000466 | 8 | 8 | 8 | 0 |
| BEKAEMPFUNG-DES-MAISWURZELBOHRERS | `bekaempfung-des-maiswurzelbohrers/` | 20000205 | 11 | 9 | 11 | 0 |
| BEKAEMPFUNG-VON-NELKENWICKLERN | `bekaempfung-von-nelkenwicklern/` | 10000467 | 6 | 6 | 6 | 0 |
| BEKAEMPFUNGSMASSNAHMEN-GEGEN-STARE | `bekaempfungsmassnahmen-gegen-stare/` | 20000217 | 3 | 3 | 3 | 0 |
| BEKAEMPFUNGSMASSNAHMEN-GEGEN-STARE-0271 | `bekaempfungsmassnahmen-gegen-stare-0271/` | 20000271 | 3 | 3 | 3 | 0 |
| BEKAEMPFUNGSMASSNAHMEN-GEGEN-STARE-0346 | `bekaempfungsmassnahmen-gegen-stare-0346/` | 20000346 | 3 | 3 | 3 | 0 |
| BEMESSUNGSGRUNDLAGE-FUER-DIE-BERECHNUNG-DER | `bemessungsgrundlage-fuer-die-berechnung-der/` | 20001418 | 10 | 4 | 10 | 0 |
| BESAMUNGSTARIF-FUER-DIE-KUENSTLICHE-BESAMUNG | `besamungstarif-fuer-die-kuenstliche-besamung/` | 20001494 | 3 | 3 | 3 | 0 |
| BESCHLUSS-ZUM-STRASSENVERWALTUNGSGESETZ | `beschluss-zum-strassenverwaltungsgesetz/` | 10000006 | 3 | 2 | 3 | 0 |
| BESCHRAENKUNG-DER-SCHIFFAHRT-AUF-DEM | `beschraenkung-der-schiffahrt-auf-dem/` | 10000171 | 2 | 2 | 2 | 0 |
| BESCHRAENKUNG-DER-SCHIFFAHRT-AUF-DEM-0172 | `beschraenkung-der-schiffahrt-auf-dem-0172/` | 10000172 | 2 | 2 | 2 | 0 |
| BESCHRAENKUNGEN-DER-SCHIFFFAHRT-AUF-BURGENLAENDI | `beschraenkungen-der-schifffahrt-auf-burgenlaendi/` | 20000632 | 9 | 5 | 9 | 0 |
| BESCHRAENKUNGEN-DER-SCHIFFFAHRT-AUF-DEM | `beschraenkungen-der-schifffahrt-auf-dem/` | 20001319 | 5 | 5 | 5 | 0 |
| BESORGUNG-VON-ANGELEGENHEITEN-DES-EIGENEN | `besorgung-von-angelegenheiten-des-eigenen/` | 10000328 | 5 | 3 | 5 | 0 |
| BESORGUNG-VON-ANGELEGENHEITEN-DES-EIGENEN-0360 | `besorgung-von-angelegenheiten-des-eigenen-0360/` | 10000360 | 2 | 2 | 2 | 0 |
| BESORGUNG-VON-ANGELEGENHEITEN-DES-EIGENEN-1106 | `besorgung-von-angelegenheiten-des-eigenen-1106/` | 20001106 | 8 | 2 | 7 | 2 |
| BESTIMMUNG-DES-STRASSENVERLAUFES-DER-B | `bestimmung-des-strassenverlaufes-der-b/` | 20000834 | 6 | 4 | 6 | 0 |
| BESTIMMUNG-DES-STRASSENVERLAUFES-DER-B-0985 | `bestimmung-des-strassenverlaufes-der-b-0985/` | 20000985 | 3 | 3 | 3 | 0 |
| BESTIMMUNG-DES-STRASSENVERLAUFES-DER-B-1166 | `bestimmung-des-strassenverlaufes-der-b-1166/` | 20001166 | 4 | 4 | 4 | 0 |
| BESTIMMUNG-DES-STRASSENVERLAUFS-DER-B | `bestimmung-des-strassenverlaufs-der-b/` | 20000757 | 3 | 3 | 3 | 0 |
| BESTIMMUNG-VON-MINDESTPREISEN-FUER-DIE | `bestimmung-von-mindestpreisen-fuer-die/` | 20000153 | 7 | 7 | 7 | 0 |
| BESTIMMUNGEN-DES-FLEISCHUNTERSUCHUNGSGESETZES | `bestimmungen-des-fleischuntersuchungsgesetzes/` | 20000168 | 4 | 4 | 4 | 0 |
| BETRIEB-OEFFENTLICHER-TANZSCHULEN | `betrieb-oeffentlicher-tanzschulen/` | 10000003 | 10 | 10 | 10 | 0 |
| BEWIRTSCHAFTUNG-BEIM-WEINBAU-SOWIE-DIE | `bewirtschaftung-beim-weinbau-sowie-die/` | 10000430 | 3 | 3 | 3 | 0 |
| BEZIRKSHAUPTMANNSCHAFTEN-GESETZ | `bezirkshauptmannschaften-gesetz/` | 20001220 | 20 | 11 | 20 | 0 |
| BEZUEGEANPASSUNGSGESETZ-2023 | `bezuegeanpassungsgesetz-2023/` | 20001581 | 2 | 2 | 2 | 0 |
| BEZUEGEANPASSUNGSGESETZ-2024 | `bezuegeanpassungsgesetz-2024/` | 20001463 | 2 | 2 | 2 | 0 |
| BEZUEGEANPASSUNGSGESETZ-2026 | `bezuegeanpassungsgesetz-2026/` | 20001589 | 2 | 2 | 2 | 0 |
| BEZUEGEGESETZ | `bezuegegesetz/` | 10000099 | 197 | 59 | 194 | 8 |
| BH-UEBERTRAGUNGSVERORDNUNG-GWTF | `bh-uebertragungsverordnung-gwtf/` | 20001539 | 3 | 3 | 3 | 0 |
| BIENENZUCHTGESETZ | `bienenzuchtgesetz/` | 10000056 | 28 | 22 | 28 | 0 |
| BILDUNG-DES-GEMEINDEBEDIENSTETENVERBANDES-INZENH | `bildung-des-gemeindebedienstetenverbandes-inzenh/` | 20001182 | 5 | 5 | 5 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-ABWASSERVERBAND-GA | `bildung-des-gemeindeverbandes-abwasserverband-ga/` | 20000313 | 3 | 3 | 3 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-ABWASSERVERBAND-SC | `bildung-des-gemeindeverbandes-abwasserverband-sc/` | 10000416 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-BILDUNGSCAMPUS-PAN | `bildung-des-gemeindeverbandes-bildungscampus-pan/` | 20001365 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-DRASSBURG-BAUMGART | `bildung-des-gemeindeverbandes-drassburg-baumgart/` | 10000287 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-GEMEINDEVERBAND-KI | `bildung-des-gemeindeverbandes-gemeindeverband-ki/` | 20001488 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-GRAFENSCHACHEN | `bildung-des-gemeindeverbandes-grafenschachen/` | 10000227 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-LACKENBACH-RITZING | `bildung-des-gemeindeverbandes-lackenbach-ritzing/` | 20000495 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-LUTZMANNSBURG | `bildung-des-gemeindeverbandes-lutzmannsburg/` | 10000350 | 3 | 3 | 3 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-OLLERSDORF-IM | `bildung-des-gemeindeverbandes-ollersdorf-im/` | 10000282 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-PIRINGSDORF-UNTERR | `bildung-des-gemeindeverbandes-piringsdorf-unterr/` | 10000281 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-POETTELSDORF-ZEMEN | `bildung-des-gemeindeverbandes-poettelsdorf-zemen/` | 10000280 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-STEINBRUNN-ZILLING | `bildung-des-gemeindeverbandes-steinbrunn-zilling/` | 10000279 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-STOTZING-LORETTO | `bildung-des-gemeindeverbandes-stotzing-loretto/` | 10000278 | 4 | 4 | 4 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-STREM-GROSSMUERBIS | `bildung-des-gemeindeverbandes-strem-grossmuerbis/` | 20001410 | 3 | 3 | 3 | 0 |
| BILDUNG-DES-GEMEINDEVERBANDES-WASSERREINHALTEVER | `bildung-des-gemeindeverbandes-wasserreinhaltever/` | 20000654 | 3 | 3 | 3 | 0 |
| BILDUNG-DES-STANDESAMTSVERBANDES-BEZIRK-JENNERSD | `bildung-des-standesamtsverbandes-bezirk-jennersd/` | 20001249 | 5 | 3 | 5 | 0 |
| BILDUNG-DES-STANDESAMTSVERBANDES-BEZIRK-MATTERSB | `bildung-des-standesamtsverbandes-bezirk-mattersb/` | 20001054 | 6 | 3 | 6 | 0 |
| BILDUNG-DES-STANDESAMTSVERBANDES-BEZIRK-NEUSIEDL | `bildung-des-standesamtsverbandes-bezirk-neusiedl/` | 20001095 | 11 | 3 | 11 | 0 |
| BILDUNG-DES-STANDESAMTSVERBANDES-BEZIRK-OBERWART | `bildung-des-standesamtsverbandes-bezirk-oberwart/` | 20001090 | 3 | 3 | 3 | 0 |
| BILDUNG-DES-STANDESAMTSVERBANDES-EISENSTADT-UND | `bildung-des-standesamtsverbandes-eisenstadt-und/` | 20001156 | 6 | 4 | 6 | 0 |
| BILDUNG-DES-STANDESAMTSVERBANDES-GUESSING-UND | `bildung-des-standesamtsverbandes-guessing-und/` | 20001053 | 5 | 3 | 5 | 0 |
| BILDUNG-DES-STANDESAMTSVERBANDES-MITTELBURGENLAN | `bildung-des-standesamtsverbandes-mittelburgenlan/` | 20000972 | 11 | 3 | 11 | 0 |
| BILDUNG-VON-HEGERINGEN-IN-DEN | `bildung-von-hegeringen-in-den/` | 20000734 | 3 | 3 | 3 | 0 |
| BILDUNGSDIREKTION-ZUSTAENDIGKEITEN-UEBERTRAGUNGS | `bildungsdirektion-zustaendigkeiten-uebertragungs/` | 20001547 | 3 | 3 | 3 | 0 |
| BILDUNGSREFORMGESETZ-2018 | `bildungsreformgesetz-2018/` | 20001201 | 2 | 2 | 2 | 0 |
| BLAUSCHIMMEL-PERONOSPORA-TABACINA-ADAM | `blauschimmel-peronospora-tabacina-adam/` | 10000042 | 9 | 8 | 9 | 0 |
| BODENEROSIONSVERMINDERUNGSVERORDNUNG | `bodenerosionsverminderungsverordnung/` | 20001244 | 4 | 4 | 4 | 0 |
| BODENSCHUTZGESETZ | `bodenschutzgesetz/` | 10000236 | 30 | 17 | 30 | 0 |
| BPG 1979 | `bpg-1979/` | 10000133 | 66 | 28 | 63 | 5 |
| Bgld. BPMG 2016 | `bpmg-2016/` | 20001084 | 73 | 48 | 73 | 0 |
| BRUNNENFELD-HEILIGENKREUZ-WALLENDORF | `brunnenfeld-heiligenkreuz-wallendorf/` | 10000244 | 7 | 7 | 7 | 0 |
| Bgld. BSchG 2001 | `bschg-2001/` | 20000122 | 160 | 111 | 160 | 0 |
| BUERGERINNEN-UND-BUERGERINITIATIVE-SOWIE-DIE | `buergerinnen-und-buergerinitiative-sowie-die/` | 10000145 | 36 | 17 | 35 | 2 |
| BUNDESWEITE-BEDARFSORIENTIERTE-MINDESTSICHERUNG | `bundesweite-bedarfsorientierte-mindestsicherung/` | 20000808 | 26 | 26 | 26 | 0 |
| BURGENLAENDISCHER-LANDTAG-BEENDIGUNG-XXI-GESETZG | `burgenlaendischer-landtag-beendigung-xxi-gesetzg/` | 20001233 | 3 | 3 | 3 | 0 |
| BUSCHENSCHANKGESETZ | `buschenschankgesetz/` | 10000132 | 28 | 12 | 28 | 0 |
| BUV | `buv/` | 10000402 | 29 | 27 | 29 | 0 |
| BVB-UEBERTRAGUNGSVERORDNUNG-VERFAHREN-NACH-DEM | `bvb-uebertragungsverordnung-verfahren-nach-dem/` | 20001379 | 3 | 3 | 3 | 0 |
| CAESIUMGRENZWERT-VON-SCHALENOBST | `caesiumgrenzwert-von-schalenobst/` | 10000181 | 3 | 3 | 3 | 0 |
| CAMPING-UND-MOBILHEIMPLATZGESETZ | `camping-und-mobilheimplatzgesetz/` | 10000156 | 98 | 35 | 97 | 2 |
| Bgld. ChG | `chg/` | 20001461 | 59 | 57 | 59 | 0 |
| Bgld. ChG-VO | `chg-vo/` | 20001499 | 13 | 13 | 13 | 0 |
| COVID-19-BASISMASSNAHMENBEGLEITVERORDNUNG-AUFHEB | `covid-19-basismassnahmenbegleitverordnung-aufheb/` | 20001389 | 3 | 3 | 3 | 0 |
| COVID-19-MASSNAHMENBEGLEITVERORDNUNG-2021-AUFHEB | `covid-19-massnahmenbegleitverordnung-2021-aufheb/` | 20001366 | 3 | 3 | 3 | 0 |
| DATENSCHUTZ-GRUNDVERORDNUNG-DSGVO-IM-AGRARWESEN | `datenschutz-grundverordnung-dsgvo-im-agrarwesen/` | 20001204 | 2 | 2 | 2 | 0 |
| DATENSCHUTZGESETZ-BGLD-DSG | `datenschutzgesetz-bgld-dsg/` | 20000361 | 104 | 41 | 104 | 0 |
| DATENSCHUTZGESETZ-LANDES-HYPOTHEKENBANK-BURGENLA | `datenschutzgesetz-landes-hypothekenbank-burgenla/` | 10000136 | 3 | 3 | 3 | 0 |
| DIENSTABZEICHEN-UND-DIENSTAUSWEIS-BGLD-KURZPARKZ | `dienstabzeichen-und-dienstausweis-bgld-kurzparkz/` | 10000336 | 3 | 3 | 3 | 0 |
| DIENSTAUSWEIS-UND-DAS-DIENSTABZEICHEN-DER | `dienstausweis-und-das-dienstabzeichen-der/` | 20000727 | 4 | 4 | 4 | 0 |
| DORFERNEUERUNGS-VERORDNUNG-2003 | `dorferneuerungs-verordnung-2003/` | 20000241 | 18 | 18 | 18 | 0 |
| Bgld. DS-APG 2018 | `ds-apg-2018/` | 20001200 | 2 | 2 | 2 | 0 |
| DURCHFUEHRUNG-PERIODISCHER-UNTERSUCHUNGEN-AUF-IB | `durchfuehrung-periodischer-untersuchungen-auf-ib/` | 20000045 | 5 | 5 | 5 | 0 |
| DURCHFUEHRUNG-VON-HEILVORKOMMEN-ANALYSEN-ZUGELAS | `durchfuehrung-von-heilvorkommen-analysen-zugelas/` | 20001540 | 3 | 3 | 3 | 0 |
| DURCHFUEHRUNGSBESTIMMUNGEN-AUF-GRUND-DES-TIERZUC | `durchfuehrungsbestimmungen-auf-grund-des-tierzuc/` | 20001491 | 3 | 3 | 3 | 0 |
| Bgld. EbBG | `ebbg/` | 20001369 | 2 | 2 | 2 | 0 |
| Bgld. EEG | `eeg/` | 20001550 | 19 | 19 | 19 | 0 |
| EHRENMEDAILLENVERORDNUNG-FEUERWEHR | `ehrenmedaillenverordnung-feuerwehr/` | 20001274 | 5 | 5 | 5 | 0 |
| Bgld. EhrenZG | `ehrenzg/` | 10000043 | 25 | 13 | 24 | 1 |
| EHRUNGSGESETZ | `ehrungsgesetz/` | 20000728 | 9 | 8 | 9 | 0 |
| EIGNUNGSKRITERIEN-FUER-NETZE-ZUR-STAREABWEHR | `eignungskriterien-fuer-netze-zur-stareabwehr/` | 20000693 | 4 | 4 | 4 | 0 |
| EINBRINGUNG-DER-ENTFALLENEN-SCHULZEIT-FUER | `einbringung-der-entfallenen-schulzeit-fuer/` | 20001268 | 3 | 3 | 3 | 0 |
| EINFUEHRUNG-DER-FRUEHEN-FOERDERUNG-IN | `einfuehrung-der-fruehen-foerderung-in/` | 20000949 | 3 | 3 | 3 | 0 |
| EINFUEHRUNG-DER-HALBTAEGIG-KOSTENLOSEN-UND | `einfuehrung-der-halbtaegig-kostenlosen-und/` | 20000746 | 22 | 16 | 22 | 0 |
| EINFUEHRUNG-DER-HALBTAEGIG-KOSTENLOSEN-UND-0952 | `einfuehrung-der-halbtaegig-kostenlosen-und-0952/` | 20000952 | 2 | 2 | 2 | 0 |
| EINFUEHRUNG-DES-NEUEN-KENNZEICHNUNGSSYSTEMS-INKR | `einfuehrung-des-neuen-kennzeichnungssystems-inkr/` | 10000214 | 3 | 3 | 3 | 0 |
| EINHEBUNG-EINER-WASSERLEITUNGSABGABE-DURCH-DIE | `einhebung-einer-wasserleitungsabgabe-durch-die/` | 10000046 | 30 | 11 | 30 | 0 |
| EINREIHUNG-IN-DIE-EINZELNEN-MODELLFUNKTIONEN | `einreihung-in-die-einzelnen-modellfunktionen/` | 20001254 | 45 | 30 | 45 | 0 |
| EINRICHTUNG-DER-GEMEINSAMEN-FILMBEWERTUNGSKOMMIS | `einrichtung-der-gemeinsamen-filmbewertungskommis/` | 10000125 | 15 | 13 | 15 | 1 |
| EINRICHTUNG-EINER-AGRARBEHOERDE | `einrichtung-einer-agrarbehoerde/` | 10000016 | 10 | 6 | 10 | 0 |
| EINRICHTUNG-EINER-GEMEINSAMEN-KOMMISSION-ZUR | `einrichtung-einer-gemeinsamen-kommission-zur/` | 10000216 | 13 | 13 | 13 | 0 |
| EINSATZ-VON-JAGDHUNDEN-FALLEN-UND | `einsatz-von-jagdhunden-fallen-und/` | 20001129 | 18 | 12 | 18 | 0 |
| EINSPARUNG-VON-ENERGIE | `einsparung-von-energie/` | 10000412 | 19 | 19 | 19 | 0 |
| EINTEILUNG-DER-GEMEINDEN-IN-ORTSKLASSEN | `einteilung-der-gemeinden-in-ortsklassen/` | 20001565 | 3 | 3 | 3 | 0 |
| EINVERLEIBUNG-EINIGER-PARZELLEN-DER-GEMEINDE | `einverleibung-einiger-parzellen-der-gemeinde/` | 20000481 | 2 | 2 | 2 | 0 |
| EINVERLEIBUNG-VON-PARZELLENTRENNSTUECKEN-IM-GEBI | `einverleibung-von-parzellentrennstuecken-im-gebi/` | 20000479 | 2 | 2 | 2 | 0 |
| EINZUGSGEBIETE-DER-WILDBAECHE | `einzugsgebiete-der-wildbaeche/` | 10000540 | 6 | 5 | 6 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-BREITENBRUNN-GATTEND | `eisenbahnzufahrtsstrasse-in-breitenbrunn-gattend/` | 10000423 | 5 | 5 | 5 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-GROSSPETERSDORF-AUFL | `eisenbahnzufahrtsstrasse-in-grosspetersdorf-aufl/` | 20000154 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-NEUFELD-LEITHA-AUFLA | `eisenbahnzufahrtsstrasse-in-neufeld-leitha-aufla/` | 20000006 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-NEUSIEDL-AM-SEE | `eisenbahnzufahrtsstrasse-in-neusiedl-am-see/` | 20000331 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-NICKELSDORF-AUFLASSU | `eisenbahnzufahrtsstrasse-in-nickelsdorf-auflassu/` | 20000577 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-PINKAFELD-AUFLASSUNG | `eisenbahnzufahrtsstrasse-in-pinkafeld-auflassung/` | 10000512 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-RECHNITZ-AUFLASSUNG | `eisenbahnzufahrtsstrasse-in-rechnitz-auflassung/` | 20000160 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-SCHACHENDORF-AUFLASS | `eisenbahnzufahrtsstrasse-in-schachendorf-auflass/` | 20000238 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-STOOB-AUFLASSUNG | `eisenbahnzufahrtsstrasse-in-stoob-auflassung/` | 20000184 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-IN-WALLERN-AUFLASSUNG | `eisenbahnzufahrtsstrasse-in-wallern-auflassung/` | 20000209 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSE-WULKAPRODERSDORF-AUFLAS | `eisenbahnzufahrtsstrasse-wulkaprodersdorf-auflas/` | 10000424 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSEN-IN-NEUDORF-HANNERSDORF | `eisenbahnzufahrtsstrassen-in-neudorf-hannersdorf/` | 20000319 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSEN-IN-OBERPULLENDORF-STRE | `eisenbahnzufahrtsstrassen-in-oberpullendorf-stre/` | 20000901 | 3 | 3 | 3 | 0 |
| EISENBAHNZUFAHRTSSTRASSEN-IN-PAMA-OGGAU-UND | `eisenbahnzufahrtsstrassen-in-pama-oggau-und/` | 20000366 | 3 | 3 | 3 | 0 |
| EisStR 2003 | `eisstr-2003/` | 20000222 | 242 | 117 | 241 | 3 |
| ELEMENTARPAEDAGOGIK-FUER-DIE-KINDERGARTENJAHRE-2 | `elementarpaedagogik-fuer-die-kindergartenjahre-2/` | 20001195 | 30 | 30 | 30 | 0 |
| ELEMENTARPAEDAGOGIK-FUER-DIE-KINDERGARTENJAHRE-2-1382 | `elementarpaedagogik-fuer-die-kindergartenjahre-2-1382/` | 20001382 | 29 | 29 | 29 | 0 |
| Bgld. ElWG 2006 | `elwg-2006/` | 20000597 | 229 | 75 | 229 | 1 |
| ENTSCHAEDIGUNG-FUER-DIE-AUSUEBUNG-DES | `entschaedigung-fuer-die-ausuebung-des/` | 10000135 | 6 | 4 | 5 | 1 |
| ENTSCHAEDIGUNG-FUER-DIE-MITBENUETZUNG-VON | `entschaedigung-fuer-die-mitbenuetzung-von/` | 20000759 | 4 | 3 | 4 | 0 |
| ENTWICKLUNGSPROGRAMM-FUER-DIE-REGION-EISENSTADT | `entwicklungsprogramm-fuer-die-region-eisenstadt/` | 20001487 | 29 | 29 | 29 | 0 |
| ENTWICKLUNGSPROGRAMM-FUER-DIE-REGION-MITTELBURGE | `entwicklungsprogramm-fuer-die-region-mittelburge/` | 20001439 | 29 | 29 | 29 | 0 |
| ENTWICKLUNGSPROGRAMM-FUER-DIE-REGION-NEUSIEDLER | `entwicklungsprogramm-fuer-die-region-neusiedler/` | 20001400 | 29 | 29 | 29 | 0 |
| ENTWICKLUNGSPROGRAMM-FUER-DIE-REGION-SUEDBURGENL | `entwicklungsprogramm-fuer-die-region-suedburgenl/` | 20001431 | 29 | 29 | 29 | 0 |
| ENTWICKLUNGSPROGRAMM-UNTERES-PINKA-UND-STREMTAL | `entwicklungsprogramm-unteres-pinka-und-stremtal/` | 10000122 | 34 | 16 | 34 | 0 |
| ERGAENZUNGSZULAGENVERORDNUNG-2026 | `ergaenzungszulagenverordnung-2026/` | 20001570 | 3 | 3 | 3 | 0 |
| ERHALTUNG-UND-WEITERENTWICKLUNG-DES-NATIONALPARK | `erhaltung-und-weiterentwicklung-des-nationalpark/` | 10000532 | 27 | 16 | 27 | 0 |
| ERHALTUNG-UND-WEITERENTWICKLUNG-DES-NATIONALPARK-1553 | `erhaltung-und-weiterentwicklung-des-nationalpark-1553/` | 20001553 | 1 | 1 | 1 | 0 |
| ERHEBUNG-EINES-ZUSCHLAGS-ZUR-BUNDESAUTOMATEN | `erhebung-eines-zuschlags-zur-bundesautomaten/` | 20000810 | 4 | 4 | 4 | 0 |
| ERHEBUNGSBOGEN-DES-BEZIRKSWEINBAUKATASTERS | `erhebungsbogen-des-bezirksweinbaukatasters/` | 10000152 | 3 | 3 | 3 | 0 |
| ERHOEHUNG-AUSGEWAEHLTER-KOSTENHOECHSTSAETZE-DES | `erhoehung-ausgewaehlter-kostenhoechstsaetze-des/` | 20001388 | 9 | 9 | 9 | 0 |
| ERHOEHUNG-DER-ORTSTAXE-NACH-DEM | `erhoehung-der-ortstaxe-nach-dem/` | 20000219 | 3 | 3 | 3 | 0 |
| ERKLAERUNG-DER-MINERALQUELLE-ZUR-HEILQUELLE | `erklaerung-der-mineralquelle-zur-heilquelle/` | 10000047 | 2 | 2 | 2 | 0 |
| ERKLAERUNG-DER-VITAQUELLEN-ALS-HEILQUELLEN | `erklaerung-der-vitaquellen-als-heilquellen/` | 10000040 | 2 | 2 | 2 | 0 |
| ERKLAERUNG-EINES-TEILES-DES-NEUSIEDLERSEES | `erklaerung-eines-teiles-des-neusiedlersees/` | 10000487 | 2 | 2 | 2 | 0 |
| ERKLAERUNG-EINES-TEILES-DES-NEUSIEDLERSEES-0161 | `erklaerung-eines-teiles-des-neusiedlersees-0161/` | 20000161 | 5 | 5 | 5 | 0 |
| ERKLAERUNG-VON-STRASSEN-ALS-EISENBAHNZUFAHRTSSTR | `erklaerung-von-strassen-als-eisenbahnzufahrtsstr/` | 10000013 | 28 | 2 | 27 | 1 |
| ERKLAERUNG-VON-STRASSEN-ALS-EISENBAHNZUFAHRTSSTR-0782 | `erklaerung-von-strassen-als-eisenbahnzufahrtsstr-0782/` | 20000782 | 2 | 2 | 2 | 0 |
| ERLASSUNG-EINES-FAHRVERBOTES-FUER-LASTKRAFTFAHRZ | `erlassung-eines-fahrverbotes-fuer-lastkraftfahrz/` | 20000486 | 5 | 5 | 5 | 0 |
| ERLASSUNG-VON-FAHRVERBOTEN-FUER-LASTKRAFTFAHRZEU | `erlassung-von-fahrverboten-fuer-lastkraftfahrzeu/` | 20000665 | 5 | 5 | 5 | 0 |
| ERMAECHTIGUNG-VON-VERSICHERUNGSUNTERNEHMEN-ZUR-E | `ermaechtigung-von-versicherungsunternehmen-zur-e/` | 20000008 | 8 | 5 | 8 | 0 |
| ERRICHTUNG-DER-BURGENLAND-TOURISMUS-GMBH | `errichtung-der-burgenland-tourismus-gmbh/` | 20001066 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-DES-TOURISTISCHEN-REGIONALVERBANDES-G | `errichtung-des-touristischen-regionalverbandes-g/` | 20000526 | 4 | 3 | 4 | 0 |
| ERRICHTUNG-EINER-ERSTAUFNAHMESTELLE-FUER-ASYLWER | `errichtung-einer-erstaufnahmestelle-fuer-asylwer/` | 20000760 | 5 | 5 | 5 | 0 |
| ERRICHTUNG-EINER-LANDWIRTSCHAFTSKRANKENKASSE | `errichtung-einer-landwirtschaftskrankenkasse/` | 10000002 | 11 | 11 | 11 | 0 |
| ERRICHTUNG-EINER-PLANUNGSGEMEINSCHAFT-ZWISCHEN-D | `errichtung-einer-planungsgemeinschaft-zwischen-d/` | 10000126 | 11 | 11 | 11 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES | `errichtung-eines-oertlichen-tourismusverbandes/` | 10000419 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-0179 | `errichtung-eines-oertlichen-tourismusverbandes-0179/` | 20000179 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-0439 | `errichtung-eines-oertlichen-tourismusverbandes-0439/` | 10000439 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-D | `errichtung-eines-oertlichen-tourismusverbandes-d/` | 20000078 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-I | `errichtung-eines-oertlichen-tourismusverbandes-i/` | 20000191 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-L | `errichtung-eines-oertlichen-tourismusverbandes-l/` | 20000800 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-M | `errichtung-eines-oertlichen-tourismusverbandes-m/` | 10000463 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-M-0269 | `errichtung-eines-oertlichen-tourismusverbandes-m-0269/` | 20000269 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-O | `errichtung-eines-oertlichen-tourismusverbandes-o/` | 10000521 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-P | `errichtung-eines-oertlichen-tourismusverbandes-p/` | 10000448 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-R | `errichtung-eines-oertlichen-tourismusverbandes-r/` | 20000695 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-EINES-OERTLICHEN-TOURISMUSVERBANDES-S | `errichtung-eines-oertlichen-tourismusverbandes-s/` | 20000227 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-VON-OERTLICHEN-TOURISMUSVERBAENDEN | `errichtung-von-oertlichen-tourismusverbaenden/` | 10000325 | 3 | 2 | 3 | 0 |
| ERRICHTUNG-VON-OERTLICHEN-TOURISMUSVERBAENDEN-0355 | `errichtung-von-oertlichen-tourismusverbaenden-0355/` | 10000355 | 3 | 2 | 3 | 0 |
| ERRICHTUNG-VON-OERTLICHEN-TOURISMUSVERBAENDEN-0356 | `errichtung-von-oertlichen-tourismusverbaenden-0356/` | 10000356 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-VON-OERTLICHEN-TOURISMUSVERBAENDEN-0385 | `errichtung-von-oertlichen-tourismusverbaenden-0385/` | 10000385 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-VON-OERTLICHEN-TOURISMUSVERBAENDEN-0386 | `errichtung-von-oertlichen-tourismusverbaenden-0386/` | 10000386 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-VON-OERTLICHEN-TOURISMUSVERBAENDEN-PA | `errichtung-von-oertlichen-tourismusverbaenden-pa/` | 20000686 | 2 | 2 | 2 | 0 |
| ERRICHTUNG-VON-TOURISTISCHEN-TOURISMUSVERBAENDEN | `errichtung-von-touristischen-tourismusverbaenden/` | 10000418 | 2 | 2 | 2 | 0 |
| ETABLIERUNG-EINER-GEBIETSKOERPERSCHAFTENUEBERGRE | `etablierung-einer-gebietskoerperschaftenuebergre/` | 20001475 | 12 | 12 | 12 | 0 |
| Bgld. EU-BA-G | `eu-ba-g/` | 20001056 | 48 | 23 | 48 | 0 |
| EU-BERUFSANERKENNUNG-SAMMELNOVELLE-2016 | `eu-berufsanerkennung-sammelnovelle-2016/` | 20001082 | 2 | 2 | 2 | 0 |
| EURO-ANPASSUNGSGESETZ-2001 | `euro-anpassungsgesetz-2001/` | 20000123 | 76 | 76 | 76 | 0 |
| EUROPASCHUTZGEBIET-AUWIESEN-ZICKENBACHTAL | `europaschutzgebiet-auwiesen-zickenbachtal/` | 20000664 | 15 | 9 | 15 | 0 |
| EUROPASCHUTZGEBIET-BERNSTEIN-LOCKENHAUS-RECHNITZ | `europaschutzgebiet-bernstein-lockenhaus-rechnitz/` | 20000958 | 17 | 11 | 17 | 0 |
| EUROPASCHUTZGEBIET-BURGENLAENDISCHE-LEITHAAUEN | `europaschutzgebiet-burgenlaendische-leithaauen/` | 20001510 | 38 | 35 | 38 | 0 |
| EUROPASCHUTZGEBIET-FRONWIESEN-UND-JOHANNESBACH | `europaschutzgebiet-fronwiesen-und-johannesbach/` | 20000959 | 17 | 11 | 17 | 0 |
| EUROPASCHUTZGEBIET-LAFNITZTAL | `europaschutzgebiet-lafnitztal/` | 20000623 | 62 | 55 | 62 | 0 |
| EUROPASCHUTZGEBIET-LANGE-LEITN-NECKENMARKT | `europaschutzgebiet-lange-leitn-neckenmarkt/` | 20000667 | 15 | 9 | 15 | 0 |
| EUROPASCHUTZGEBIET-MATTERSBURGER-HUEGELLAND | `europaschutzgebiet-mattersburger-huegelland/` | 20000968 | 17 | 11 | 17 | 0 |
| EUROPASCHUTZGEBIET-NEUSIEDLER-SEE-NORDOESTLICHES | `europaschutzgebiet-neusiedler-see-nordoestliches/` | 20000935 | 18 | 11 | 18 | 0 |
| EUROPASCHUTZGEBIET-NICKELSDORFER-HAIDEL | `europaschutzgebiet-nickelsdorfer-haidel/` | 20000678 | 16 | 9 | 16 | 0 |
| EUROPASCHUTZGEBIET-PARNDORFER-HEIDE | `europaschutzgebiet-parndorfer-heide/` | 20000663 | 15 | 9 | 15 | 0 |
| EUROPASCHUTZGEBIET-PARNDORFER-PLATTE-HEIDEBODEN | `europaschutzgebiet-parndorfer-platte-heideboden/` | 20001281 | 88 | 67 | 88 | 0 |
| EUROPASCHUTZGEBIET-SIEGENDORFER-PUSSTA-UND-HEIDE | `europaschutzgebiet-siegendorfer-pussta-und-heide/` | 20000677 | 17 | 11 | 17 | 0 |
| EUROPASCHUTZGEBIET-SUEDBURGENLAENDISCHES-HUEGEL | `europaschutzgebiet-suedburgenlaendisches-huegel/` | 20000960 | 17 | 11 | 17 | 0 |
| EUROPASCHUTZGEBIET-WAASEN-HANS-G | `europaschutzgebiet-waasen-hans-g/` | 20000679 | 18 | 10 | 18 | 0 |
| EUROPASCHUTZGEBIET-ZURNDORFER-EICHENWALD-UND-HUT | `europaschutzgebiet-zurndorfer-eichenwald-und-hut/` | 20000680 | 16 | 9 | 16 | 0 |
| EVIDENTHALTUNG-UND-KENNZEICHNUNG-DER-HUNDE | `evidenthaltung-und-kennzeichnung-der-hunde/` | 10000001 | 2 | 2 | 2 | 0 |
| Bgld. EVTZG | `evtzg/` | 20000839 | 17 | 7 | 17 | 0 |
| FACHARBEITER-AUFSTIEGSPRUEFUNG | `facharbeiter-aufstiegspruefung/` | 10000102 | 6 | 6 | 6 | 0 |
| FAMILIENFOERDERUNGSGESETZ | `familienfoerderungsgesetz/` | 10000290 | 121 | 32 | 120 | 3 |
| FELDSCHUTZGESETZ | `feldschutzgesetz/` | 10000219 | 18 | 14 | 18 | 0 |
| FESTLEGUNG-DER-BEITRAGSGRUPPEN-FUER-DEN | `festlegung-der-beitragsgruppen-fuer-den/` | 20001566 | 4 | 4 | 4 | 0 |
| FESTLEGUNG-DER-EINKAUFSORTE | `festlegung-der-einkaufsorte/` | 20000240 | 7 | 3 | 7 | 0 |
| FESTLEGUNG-EINES-GRUNDWASSERSCHONGEBIETES | `festlegung-eines-grundwasserschongebietes/` | 10000069 | 6 | 6 | 6 | 0 |
| FESTLEGUNG-EINES-SCHUTZGEBIETES-FUER-EINE | `festlegung-eines-schutzgebietes-fuer-eine/` | 20000068 | 3 | 3 | 3 | 0 |
| FESTLEGUNG-VON-SCHUTZGEBIETEN-FUER-ANERKANNTE | `festlegung-von-schutzgebieten-fuer-anerkannte/` | 20000048 | 3 | 3 | 3 | 0 |
| FESTSETZUNG-DER-ANZAHL-DER-MITGLIEDER | `festsetzung-der-anzahl-der-mitglieder/` | 20000188 | 2 | 2 | 2 | 0 |
| FESTSETZUNG-DER-BAUSCHBETRAEGE-FUER-DIE | `festsetzung-der-bauschbetraege-fuer-die/` | 20000156 | 4 | 4 | 4 | 0 |
| FESTSETZUNG-DER-PFLICHTSPRENGEL-FUER-OEFFENTLICH | `festsetzung-der-pflichtsprengel-fuer-oeffentlich/` | 20000967 | 11 | 11 | 11 | 0 |
| FESTSETZUNG-DER-REISEZULAGEN-FUER-DIENSTVERRICHT | `festsetzung-der-reisezulagen-fuer-dienstverricht/` | 20000135 | 3 | 3 | 3 | 0 |
| FESTSETZUNG-DER-SCHULSPRENGEL-DER-OEFFENTLICHEN | `festsetzung-der-schulsprengel-der-oeffentlichen/` | 20000267 | 10 | 7 | 10 | 0 |
| FESTSETZUNG-DER-SCHULSPRENGEL-FUER-DIE | `festsetzung-der-schulsprengel-fuer-die/` | 20000218 | 6 | 5 | 6 | 0 |
| FESTSETZUNG-DER-SCHULSPRENGEL-OEA-SONDERSCHULEN | `festsetzung-der-schulsprengel-oea-sonderschulen/` | 10000158 | 11 | 9 | 11 | 1 |
| FESTSETZUNG-VON-BAUSCHBETRAEGEN-FUER-DIE | `festsetzung-von-bauschbetraegen-fuer-die/` | 10000440 | 2 | 2 | 2 | 0 |
| FESTSETZUNG-VON-BERECHTIGUNGSSPRENGELN-FUER-OEFF | `festsetzung-von-berechtigungssprengeln-fuer-oeff/` | 20000969 | 4 | 4 | 4 | 0 |
| FEUERBESCHAUORDNUNG-AUFHEBUNG | `feuerbeschauordnung-aufhebung/` | 20000996 | 2 | 2 | 2 | 0 |
| FEUERSTAETTENBESCHAUGESETZ | `feuerstaettenbeschaugesetz/` | 20001206 | 2 | 2 | 2 | 0 |
| FEUERWEHR-TARIFVERORDNUNG-2023-FWTARIFV-2023 | `feuerwehr-tarifverordnung-2023-fwtarifv-2023/` | 20001435 | 11 | 11 | 11 | 0 |
| Bgld. FGSVG | `fgsvg/` | 20001150 | 8 | 8 | 8 | 0 |
| FISCHEREIGESETZ-1949 | `fischereigesetz-1949/` | 10000019 | 106 | 84 | 106 | 0 |
| FISCHEREIKARTENABGABENVERORDNUNG-2026 | `fischereikartenabgabenverordnung-2026/` | 20001538 | 4 | 4 | 4 | 0 |
| FISCHEREIPRUEFUNGSVERORDNUNG-2023 | `fischereipruefungsverordnung-2023/` | 20001401 | 7 | 7 | 7 | 0 |
| FISCHEREIWESENVERORDNUNG-2022 | `fischereiwesenverordnung-2022/` | 20001353 | 19 | 13 | 19 | 1 |
| Bgld. FischG 2022 | `fischg-2022/` | 20001350 | 48 | 41 | 48 | 0 |
| FLAECHENMAESSIGE-BESCHRAENKUNG-DES-WEINBAUES-SOW | `flaechenmaessige-beschraenkung-des-weinbaues-sow/` | 10000140 | 18 | 16 | 17 | 1 |
| FLAECHENWIDMUNGSPLAN-FUER-DIE-GEMEINDE-MUELLENDO | `flaechenwidmungsplan-fuer-die-gemeinde-muellendo/` | 10000121 | 6 | 6 | 6 | 0 |
| FLAECHENWIDMUNGSPLAN-FUER-DIE-GEMEINDE-PURBACH | `flaechenwidmungsplan-fuer-die-gemeinde-purbach/` | 10000155 | 5 | 5 | 5 | 0 |
| FLEISCHUNTERSUCHUNGSGEBUEHREN-VERORDNUNG | `fleischuntersuchungsgebuehren-verordnung/` | 10000410 | 11 | 7 | 11 | 0 |
| FLURVERFASSUNGS-LANDESGESETZ | `flurverfassungs-landesgesetz/` | 10000082 | 217 | 119 | 217 | 0 |
| Bgld. FöG | `foeg/` | 20001446 | 12 | 12 | 12 | 0 |
| FOERDERUNG-DER-24-STUNDEN-BETREUUNG-AENDERUNG | `foerderung-der-24-stunden-betreuung-aenderung/` | 20001139 | 4 | 4 | 4 | 0 |
| FOERDERUNG-VON-BILDUNGSMASSNAHMEN-BASISBILDUNG-S | `foerderung-von-bildungsmassnahmen-basisbildung-s/` | 20001030 | 2 | 2 | 2 | 0 |
| FOERDERUNG-VON-BILDUNGSMASSNAHMEN-BASISBILDUNG-S-1035 | `foerderung-von-bildungsmassnahmen-basisbildung-s-1035/` | 20001035 | 2 | 2 | 2 | 0 |
| FOERDERUNG-VON-BILDUNGSMASSNAHMEN-IM-BEREICH | `foerderung-von-bildungsmassnahmen-im-bereich/` | 20001018 | 19 | 19 | 19 | 0 |
| FOERDERUNG-VON-BILDUNGSMASSNAHMEN-IM-BEREICH-1152 | `foerderung-von-bildungsmassnahmen-im-bereich-1152/` | 20001152 | 29 | 19 | 29 | 0 |
| FOERDERUNG-VON-BILDUNGSMASSNAHMEN-IM-BEREICH-1474 | `foerderung-von-bildungsmassnahmen-im-bereich-1474/` | 20001474 | 18 | 18 | 18 | 0 |
| FOERDERUNG-VON-LEHRGAENGEN-FUER-ERWACHSENE | `foerderung-von-lehrgaengen-fuer-erwachsene/` | 20000879 | 17 | 17 | 17 | 0 |
| FORM-DER-DRUCKSORTE-FUER-DEN | `form-der-drucksorte-fuer-den/` | 10000092 | 9 | 7 | 9 | 0 |
| FORSTAUSFUEHRUNGSGESETZ | `forstausfuehrungsgesetz/` | 10000196 | 57 | 26 | 57 | 0 |
| FRAUENFOERDERPROGRAMM | `frauenfoerderprogramm/` | 10000539 | 25 | 16 | 24 | 2 |
| FREMDDARLEHEN-HOECHSTVERZINSUNGS-VERORDNUNG-2012 | `fremddarlehen-hoechstverzinsungs-verordnung-2012/` | 20000891 | 3 | 3 | 3 | 0 |
| FREMDENVERKEHRSGEMEINDE-PAMHAGEN | `fremdenverkehrsgemeinde-pamhagen/` | 10000149 | 3 | 3 | 3 | 0 |
| FREMDENVERKEHRSGEMEINDEN | `fremdenverkehrsgemeinden/` | 10000124 | 3 | 3 | 3 | 0 |
| FRUEHE-HILFEN-VEREINBARUNG | `fruehe-hilfen-vereinbarung/` | 20001462 | 18 | 18 | 18 | 0 |
| FRUEHE-SPRACHLICHE-FOERDERUNG-IN-INSTITUTIONELLE | `fruehe-sprachliche-foerderung-in-institutionelle/` | 20001039 | 16 | 16 | 16 | 0 |
| FRUEHE-SPRACHLICHE-FOERDERUNG-IN-INSTITUTIONELLE-1083 | `fruehe-sprachliche-foerderung-in-institutionelle-1083/` | 20001083 | 2 | 2 | 2 | 0 |
| FSchVE | `fschve/` | 20001437 | 24 | 24 | 24 | 0 |
| Bgld. FTG | `ftg/` | 20001529 | 15 | 15 | 15 | 0 |
| FUER-DIE-DURCHFUEHRUNG-VON-HEILVORKOMMEN-ANALYSE | `fuer-die-durchfuehrung-von-heilvorkommen-analyse/` | 20000842 | 3 | 3 | 3 | 0 |
| Bgld. FwG 2019 | `fwg-2019/` | 20001250 | 92 | 92 | 92 | 0 |
| FwWahlV | `fwwahlv/` | 20001294 | 23 | 23 | 23 | 0 |
| Bgld. G-PVG | `g-pvg/` | 20000165 | 63 | 44 | 62 | 3 |
| Bgld. G-PVWO | `g-pvwo/` | 20000044 | 40 | 36 | 40 | 0 |
| Bgld. GADG | `gadg/` | 20001598 | 69 | 69 | 69 | 0 |
| GASSICHERHEITSVERORDNUNG-2011 | `gassicherheitsverordnung-2011/` | 20000843 | 9 | 9 | 9 | 0 |
| GAusbV-Gem | `gausbv-gem/` | 20001080 | 34 | 17 | 34 | 0 |
| GAusbV-Land | `gausbv-land/` | 20001482 | 26 | 18 | 26 | 0 |
| Bgld. GBG | `gbg/` | 10000510 | 83 | 42 | 81 | 3 |
| GEBIETSFESTLEGUNG-UND-VERMOEGENSAUSEINANDERSETZU | `gebietsfestlegung-und-vermoegensauseinandersetzu/` | 10000425 | 14 | 14 | 14 | 0 |
| GEBUEHREN-VON-TOTALISATEUR-UND-BUCHMACHERWETTEN | `gebuehren-von-totalisateur-und-buchmacherwetten/` | 20000338 | 54 | 32 | 54 | 0 |
| GefKat-V 2017 | `gefkat-v-2017/` | 20001149 | 6 | 6 | 6 | 0 |
| GEFLUEGELHYGIENEGEBUEHRENVERORDNUNG-2026 | `gefluegelhygienegebuehrenverordnung-2026/` | 20001597 | 3 | 3 | 3 | 0 |
| Bgld. GemBG 2014 | `gembg-2014/` | 20001002 | 555 | 235 | 551 | 12 |
| GemBÜG 2014 | `gembueg-2014/` | 20001003 | 16 | 14 | 16 | 0 |
| GEMEINDE-INVESTITIONSFONDSGESETZ-AUFHEBUNG | `gemeinde-investitionsfondsgesetz-aufhebung/` | 20001089 | 5 | 5 | 5 | 0 |
| GEMEINDE-VERWALTUNGSABGABENVERORDNUNG-2014 | `gemeinde-verwaltungsabgabenverordnung-2014/` | 20000965 | 8 | 5 | 8 | 0 |
| GEMEINDEBEDIENSTETENGESETZ-1971 | `gemeindebedienstetengesetz-1971/` | 10000095 | 220 | 54 | 216 | 9 |
| GEMEINDEBEDIENSTETENVERBAND-BOCKSDORF-HEUGRABEN | `gemeindebedienstetenverband-bocksdorf-heugraben/` | 20001425 | 6 | 6 | 6 | 0 |
| GEMEINDEBEDIENSTETENVERBAND-STOTZING-LORETTO | `gemeindebedienstetenverband-stotzing-loretto/` | 20001426 | 6 | 6 | 6 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHL-1997 | `gemeinderats-und-buergermeisterwahl-1997/` | 10000480 | 4 | 4 | 4 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHL-1997-0483 | `gemeinderats-und-buergermeisterwahl-1997-0483/` | 10000483 | 5 | 5 | 5 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHL-2002 | `gemeinderats-und-buergermeisterwahl-2002/` | 20000193 | 5 | 5 | 5 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-1992 | `gemeinderats-und-buergermeisterwahlen-1992/` | 10000303 | 5 | 5 | 5 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-1998 | `gemeinderats-und-buergermeisterwahlen-1998/` | 10000509 | 4 | 4 | 4 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-2002 | `gemeinderats-und-buergermeisterwahlen-2002/` | 20000167 | 4 | 4 | 4 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-2007 | `gemeinderats-und-buergermeisterwahlen-2007/` | 20000631 | 5 | 5 | 5 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-2012 | `gemeinderats-und-buergermeisterwahlen-2012/` | 20000889 | 4 | 4 | 4 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-2017 | `gemeinderats-und-buergermeisterwahlen-2017/` | 20001133 | 4 | 4 | 4 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-2017-MARKT | `gemeinderats-und-buergermeisterwahlen-2017-markt/` | 20001174 | 4 | 4 | 4 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-2022 | `gemeinderats-und-buergermeisterwahlen-2022/` | 20001371 | 4 | 4 | 4 | 0 |
| GEMEINDERATS-UND-BUERGERMEISTERWAHLEN-2022-1419 | `gemeinderats-und-buergermeisterwahlen-2022-1419/` | 20001419 | 4 | 4 | 4 | 0 |
| GEMEINDERECHTS-SAMMELNOVELLE | `gemeinderechts-sammelnovelle/` | 20001205 | 2 | 2 | 2 | 0 |
| GEMEINDESANITAETSGESETZ-1971 | `gemeindesanitaetsgesetz-1971/` | 10000094 | 124 | 52 | 124 | 0 |
| GEMEINDESTRUKTURVERBESSERUNGSGESETZ | `gemeindestrukturverbesserungsgesetz/` | 10000088 | 19 | 18 | 19 | 0 |
| GEMEINDEVERBAND-BOCKSDORF-BURGAUBERG-NEUDAUBERG | `gemeindeverband-bocksdorf-burgauberg-neudauberg/` | 10000316 | 4 | 4 | 4 | 0 |
| GEMEINDEVERBAND-BOCKSDORF-OLBENDORF-BURGAUBERG-N | `gemeindeverband-bocksdorf-olbendorf-burgauberg-n/` | 10000165 | 2 | 2 | 2 | 0 |
| GEMEINDEVERBAND-LEITHAPRODERSDORF-WIMPASSING-AN | `gemeindeverband-leithaprodersdorf-wimpassing-an/` | 10000228 | 4 | 4 | 4 | 0 |
| GEMEINDEVERBAND-LEITHAPRODERSDORF-WIMPASSING-AN-0286 | `gemeindeverband-leithaprodersdorf-wimpassing-an-0286/` | 10000286 | 4 | 4 | 4 | 0 |
| GEMEINDEVERBANDSGESETZ | `gemeindeverbandsgesetz/` | 10000202 | 44 | 32 | 43 | 1 |
| GEMEINDEVOLKSRECHTEGESETZ | `gemeindevolksrechtegesetz/` | 10000208 | 167 | 83 | 166 | 2 |
| GEMEINSAME-BEURTEILUNG-VON-BAUSTOFFEN-BAUTEILEN | `gemeinsame-beurteilung-von-baustoffen-bauteilen/` | 10000462 | 4 | 4 | 4 | 0 |
| GEMEINSAME-FOERDERUNG-DER-24-STUNDEN-BETREUUNG | `gemeinsame-foerderung-der-24-stunden-betreuung/` | 20000722 | 20 | 12 | 20 | 2 |
| GEMEINSAME-FOERDERUNG-DER-24-STUNDEN-BETREUUNG-A | `gemeinsame-foerderung-der-24-stunden-betreuung-a/` | 20000747 | 2 | 2 | 2 | 0 |
| GEMEINSAME-FOERDERUNG-DER-24-STUNDEN-BETREUUNG-A-0903 | `gemeinsame-foerderung-der-24-stunden-betreuung-a-0903/` | 20000903 | 4 | 4 | 4 | 0 |
| GEMEINSAME-FOERDERUNG-DER-24-STUNDEN-BETREUUNG-A-1477 | `gemeinsame-foerderung-der-24-stunden-betreuung-a-1477/` | 20001477 | 2 | 2 | 2 | 0 |
| GEMEINSAME-FOERDERUNG-DER-24-STUNDEN-BETREUUNG-U | `gemeinsame-foerderung-der-24-stunden-betreuung-u/` | 20001027 | 5 | 5 | 5 | 0 |
| GEMEINSAME-MASSNAHMEN-FUER-PFLEGEBEDUERFTIGE-PER | `gemeinsame-massnahmen-fuer-pflegebeduerftige-per/` | 10000368 | 20 | 20 | 20 | 0 |
| GEMEINSAME-WILLENSBILDUNG-DER-LAENDER-IN | `gemeinsame-willensbildung-der-laender-in/` | 10000342 | 11 | 11 | 11 | 0 |
| Bgld. GemfG | `gemfg/` | 20001497 | 16 | 12 | 16 | 0 |
| GEMFINANZG-2021 | `gemfinanzg-2021/` | 20001334 | 6 | 6 | 6 | 0 |
| Bgld. GemHOG 2018 | `gemhog-2018/` | 20001188 | 8 | 8 | 8 | 0 |
| Bgld. GemSanG 2013 | `gemsang-2013/` | 20000950 | 9 | 7 | 9 | 0 |
| GemWO 1992 | `gemwo-1992/` | 10000304 | 413 | 137 | 410 | 10 |
| Bgld. GeoDIG | `geodig/` | 20000825 | 30 | 24 | 30 | 0 |
| GESCHAEFSORDNUNG-DES-FAMILIENBEIRATES | `geschaefsordnung-des-familienbeirates/` | 10000299 | 10 | 10 | 10 | 0 |
| GESCHAEFTSEINTEILUNG-DES-AMTES-DER-BURGENLAENDIS | `geschaeftseinteilung-des-amtes-der-burgenlaendis/` | 20001070 | 31 | 5 | 31 | 0 |
| GESCHAEFTSORDNUNG-DES-ABFALLWIRTSCHAFTSBEIRATES | `geschaeftsordnung-des-abfallwirtschaftsbeirates/` | 10000407 | 10 | 9 | 10 | 0 |
| GESCHAEFTSORDNUNG-DES-AMTES-DER-BURGENLAENDISCHE | `geschaeftsordnung-des-amtes-der-burgenlaendische/` | 20001427 | 21 | 17 | 21 | 0 |
| GESCHAEFTSORDNUNG-DES-BURGENLAENDISCHEN-LANDTAGE | `geschaeftsordnung-des-burgenlaendischen-landtage/` | 10000142 | 270 | 95 | 268 | 4 |
| GESCHAEFTSORDNUNG-DES-NATURSCHUTZBEIRATES | `geschaeftsordnung-des-naturschutzbeirates/` | 10000261 | 9 | 9 | 9 | 0 |
| GESCHAEFTSORDNUNG-DES-RETTUNGSBEIRATES | `geschaeftsordnung-des-rettungsbeirates/` | 10000438 | 18 | 14 | 18 | 0 |
| GESCHAEFTSORDNUNG-FUER-DEN-SOZIALHILFE-UND | `geschaeftsordnung-fuer-den-sozialhilfe-und/` | 20001560 | 7 | 7 | 7 | 0 |
| GESCHAEFTSORDNUNG-FUER-DIE-OBJEKTIVIERUNGSKOMMIS | `geschaeftsordnung-fuer-die-objektivierungskommis/` | 10000224 | 9 | 9 | 9 | 0 |
| GESCHUETZTEN-LANDSCHAFTSTEIL-LAHNBACH | `geschuetzten-landschaftsteil-lahnbach/` | 20000564 | 6 | 6 | 6 | 0 |
| GESCHUETZTEN-LEBENSRAUM-STOTZINGER-HEIDE | `geschuetzten-lebensraum-stotzinger-heide/` | 20000595 | 10 | 10 | 10 | 0 |
| GESCHUETZTEN-LEBENSRAUM-WEHOFERBACHWIESE | `geschuetzten-lebensraum-wehoferbachwiese/` | 20000786 | 9 | 9 | 9 | 0 |
| GESCHUETZTER-LEBENSRAUM-ROCHUS-KAPELLE-UND-HETSC | `geschuetzter-lebensraum-rochus-kapelle-und-hetsc/` | 20000353 | 9 | 9 | 9 | 0 |
| GESCHUETZTER-LEBENSRAUM-WEISSES-KREUZ | `geschuetzter-lebensraum-weisses-kreuz/` | 20000815 | 8 | 8 | 8 | 0 |
| GESETZ-MIT-DEM-DIE-ANZUWENDENDE | `gesetz-mit-dem-die-anzuwendende/` | 20000764 | 9 | 9 | 9 | 0 |
| GESETZ-MIT-DEM-DIE-XVIII | `gesetz-mit-dem-die-xviii/` | 20000344 | 3 | 3 | 3 | 0 |
| GESETZ-UEBER-DEN-WASSERLEITUNGSVERBAND-NOERDLICH | `gesetz-ueber-den-wasserleitungsverband-noerdlich/` | 20000649 | 85 | 44 | 85 | 0 |
| GESETZ-UEBER-DIE-ERRICHTUNG-EINES | `gesetz-ueber-die-errichtung-eines/` | 20000994 | 5 | 5 | 5 | 0 |
| GESETZ-UEBER-DIE-TEILUNG-VON | `gesetz-ueber-die-teilung-von/` | 20000904 | 3 | 3 | 3 | 0 |
| GESETZE-BETREFFEND-DEN-EUROPAEISCHEN-WIRTSCHAFTS | `gesetze-betreffend-den-europaeischen-wirtschafts/` | 10000367 | 2 | 2 | 2 | 0 |
| GESUNDHEITS-PATIENTINNEN-PATIENTEN-UND-BEHINDERT | `gesundheits-patientinnen-patienten-und-behindert/` | 20000054 | 44 | 22 | 44 | 0 |
| GFD-VERORDNUNG-2026 | `gfd-verordnung-2026/` | 20001579 | 12 | 12 | 12 | 0 |
| Bgld. GFG | `gfg/` | 20001161 | 88 | 31 | 88 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-ANTAU | `grenzaenderung-zwischen-den-gemeinden-antau/` | 20000784 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH | `grenzaenderung-zwischen-den-gemeinden-deutsch/` | 20000253 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH-0254 | `grenzaenderung-zwischen-den-gemeinden-deutsch-0254/` | 20000254 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH-0256 | `grenzaenderung-zwischen-den-gemeinden-deutsch-0256/` | 20000256 | 11 | 11 | 11 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH-0307 | `grenzaenderung-zwischen-den-gemeinden-deutsch-0307/` | 20000307 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH-0437 | `grenzaenderung-zwischen-den-gemeinden-deutsch-0437/` | 20000437 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DEUTSCHKRE | `grenzaenderung-zwischen-den-gemeinden-deutschkre/` | 20000450 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DEUTSCHKRE-0451 | `grenzaenderung-zwischen-den-gemeinden-deutschkre-0451/` | 20000451 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-DRASSMARKT | `grenzaenderung-zwischen-den-gemeinden-drassmarkt/` | 20000371 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-EBERAU | `grenzaenderung-zwischen-den-gemeinden-eberau/` | 20000249 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-EBERAU-0255 | `grenzaenderung-zwischen-den-gemeinden-eberau-0255/` | 20000255 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-EBERAU-0257 | `grenzaenderung-zwischen-den-gemeinden-eberau-0257/` | 20000257 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-FRANKENAU | `grenzaenderung-zwischen-den-gemeinden-frankenau/` | 20000431 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSPETER | `grenzaenderung-zwischen-den-gemeinden-grosspeter/` | 20000250 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSPETER-0251 | `grenzaenderung-zwischen-den-gemeinden-grosspeter-0251/` | 20000251 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSPETER-0252 | `grenzaenderung-zwischen-den-gemeinden-grosspeter-0252/` | 20000252 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSPETER-0802 | `grenzaenderung-zwischen-den-gemeinden-grosspeter-0802/` | 20000802 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSPETER-0803 | `grenzaenderung-zwischen-den-gemeinden-grosspeter-0803/` | 20000803 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSWARAS | `grenzaenderung-zwischen-den-gemeinden-grosswaras/` | 20000109 | 5 | 5 | 5 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSWARAS-0441 | `grenzaenderung-zwischen-den-gemeinden-grosswaras-0441/` | 20000441 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GROSSWARAS-0455 | `grenzaenderung-zwischen-den-gemeinden-grosswaras-0455/` | 20000455 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-GUESSING | `grenzaenderung-zwischen-den-gemeinden-guessing/` | 20000660 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-HALBTURN | `grenzaenderung-zwischen-den-gemeinden-halbturn/` | 20000502 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-HORNSTEIN | `grenzaenderung-zwischen-den-gemeinden-hornstein/` | 20000470 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-KLINGENBAC | `grenzaenderung-zwischen-den-gemeinden-klingenbac/` | 20000703 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-KOHFIDISCH | `grenzaenderung-zwischen-den-gemeinden-kohfidisch/` | 20000433 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-KOHFIDISCH-0436 | `grenzaenderung-zwischen-den-gemeinden-kohfidisch-0436/` | 20000436 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-KUKMIRN | `grenzaenderung-zwischen-den-gemeinden-kukmirn/` | 20000439 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-KUKMIRN-0804 | `grenzaenderung-zwischen-den-gemeinden-kukmirn-0804/` | 20000804 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-LITZELSDOR | `grenzaenderung-zwischen-den-gemeinden-litzelsdor/` | 20000702 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-LOCKENHAUS | `grenzaenderung-zwischen-den-gemeinden-lockenhaus/` | 20000434 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-MISCHENDOR | `grenzaenderung-zwischen-den-gemeinden-mischendor/` | 20000435 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-MOENCHHOF | `grenzaenderung-zwischen-den-gemeinden-moenchhof/` | 20000440 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-MOENCHHOF-0443 | `grenzaenderung-zwischen-den-gemeinden-moenchhof-0443/` | 20000443 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-MOSCHENDOR | `grenzaenderung-zwischen-den-gemeinden-moschendor/` | 20000248 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-NEUFELD | `grenzaenderung-zwischen-den-gemeinden-neufeld/` | 20000603 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-NIKITSCH | `grenzaenderung-zwischen-den-gemeinden-nikitsch/` | 20000448 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-NIKITSCH-0449 | `grenzaenderung-zwischen-den-gemeinden-nikitsch-0449/` | 20000449 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-NIKTISCH | `grenzaenderung-zwischen-den-gemeinden-niktisch/` | 20000446 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-OBERPULLEN | `grenzaenderung-zwischen-den-gemeinden-oberpullen/` | 20000318 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-OBERPULLEN-0465 | `grenzaenderung-zwischen-den-gemeinden-oberpullen-0465/` | 20000465 | 8 | 8 | 8 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-OBERWART | `grenzaenderung-zwischen-den-gemeinden-oberwart/` | 20000445 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-OBERWART-0447 | `grenzaenderung-zwischen-den-gemeinden-oberwart-0447/` | 20000447 | 5 | 5 | 5 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-PILGERSDOR | `grenzaenderung-zwischen-den-gemeinden-pilgersdor/` | 20000438 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-POETTSCHIN | `grenzaenderung-zwischen-den-gemeinden-poettschin/` | 20000858 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-ROTENTURM | `grenzaenderung-zwischen-den-gemeinden-rotenturm/` | 20000704 | 8 | 8 | 8 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-STEINBERG | `grenzaenderung-zwischen-den-gemeinden-steinberg/` | 20000432 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-STEINBERG-0442 | `grenzaenderung-zwischen-den-gemeinden-steinberg-0442/` | 20000442 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-TADTEN | `grenzaenderung-zwischen-den-gemeinden-tadten/` | 20000107 | 5 | 5 | 5 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-UNTERFRAUE | `grenzaenderung-zwischen-den-gemeinden-unterfraue/` | 20000370 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-UNTERRABNI | `grenzaenderung-zwischen-den-gemeinden-unterrabni/` | 20000372 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEN-GEMEINDEN-WEINGRABEN | `grenzaenderung-zwischen-den-gemeinden-weingraben/` | 20000373 | 7 | 7 | 7 | 0 |
| GRENZAENDERUNG-ZWISCHEN-DEUTSCH-SCHUETZEN-EISENB | `grenzaenderung-zwischen-deutsch-schuetzen-eisenb/` | 20000247 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-EBERAU-UND-MOSCHENDORF | `grenzaenderung-zwischen-eberau-und-moschendorf/` | 20000017 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-MARKT-ALLHAU-UND | `grenzaenderung-zwischen-markt-allhau-und/` | 20000009 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-NECKENMARKT-UND-HORITSCH | `grenzaenderung-zwischen-neckenmarkt-und-horitsch/` | 20000023 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-NEUSIEDL-AM-SEE | `grenzaenderung-zwischen-neusiedl-am-see/` | 20000024 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-NEUSIEDL-AM-SEE-0025 | `grenzaenderung-zwischen-neusiedl-am-see-0025/` | 20000025 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNG-ZWISCHEN-WEPPERSDORF-UND-KOBERSDO | `grenzaenderung-zwischen-weppersdorf-und-kobersdo/` | 20000018 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-WEPPERSDORF-UND-KOBERSDO-0019 | `grenzaenderung-zwischen-weppersdorf-und-kobersdo-0019/` | 20000019 | 5 | 5 | 5 | 0 |
| GRENZAENDERUNG-ZWISCHEN-WEPPERSDORF-UND-LACKENBA | `grenzaenderung-zwischen-weppersdorf-und-lackenba/` | 20000021 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNG-ZWISCHEN-WEPPERSDORF-UND-SIEGGRAB | `grenzaenderung-zwischen-weppersdorf-und-sieggrab/` | 20000015 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH | `grenzaenderungen-zwischen-den-gemeinden-deutsch/` | 20000453 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH-0468 | `grenzaenderungen-zwischen-den-gemeinden-deutsch-0468/` | 20000468 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-DEUTSCH-0472 | `grenzaenderungen-zwischen-den-gemeinden-deutsch-0472/` | 20000472 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-EBERAU | `grenzaenderungen-zwischen-den-gemeinden-eberau/` | 20000471 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-GAAS | `grenzaenderungen-zwischen-den-gemeinden-gaas/` | 20000461 | 3 | 3 | 3 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-GUESSING | `grenzaenderungen-zwischen-den-gemeinden-guessing/` | 20000582 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-JENNERSD | `grenzaenderungen-zwischen-den-gemeinden-jennersd/` | 20000473 | 5 | 5 | 5 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-JENNERSD-0477 | `grenzaenderungen-zwischen-den-gemeinden-jennersd-0477/` | 20000477 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-KULM | `grenzaenderungen-zwischen-den-gemeinden-kulm/` | 20000459 | 3 | 3 | 3 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-LACKENDO | `grenzaenderungen-zwischen-den-gemeinden-lackendo/` | 20000462 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-MARZ | `grenzaenderungen-zwischen-den-gemeinden-marz/` | 20000463 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-MATTERSB | `grenzaenderungen-zwischen-den-gemeinden-mattersb/` | 20000466 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-NECKENMA | `grenzaenderungen-zwischen-den-gemeinden-neckenma/` | 20000460 | 5 | 5 | 5 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-NECKENMA-0464 | `grenzaenderungen-zwischen-den-gemeinden-neckenma-0464/` | 20000464 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-NEUFELD | `grenzaenderungen-zwischen-den-gemeinden-neufeld/` | 20000469 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-NIKITSCH | `grenzaenderungen-zwischen-den-gemeinden-nikitsch/` | 20000458 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-PILGERSD | `grenzaenderungen-zwischen-den-gemeinden-pilgersd/` | 20000476 | 6 | 6 | 6 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-PIRINGSD | `grenzaenderungen-zwischen-den-gemeinden-piringsd/` | 20000474 | 5 | 5 | 5 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-PODERSDO | `grenzaenderungen-zwischen-den-gemeinden-podersdo/` | 20000478 | 2 | 2 | 2 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-POETTELS | `grenzaenderungen-zwischen-den-gemeinden-poettels/` | 20000475 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-SANKT | `grenzaenderungen-zwischen-den-gemeinden-sankt/` | 20000454 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-STEGERSB | `grenzaenderungen-zwischen-den-gemeinden-stegersb/` | 20000457 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-STEINBRU | `grenzaenderungen-zwischen-den-gemeinden-steinbru/` | 20000452 | 4 | 4 | 4 | 0 |
| GRENZAENDERUNGEN-ZWISCHEN-DEN-GEMEINDEN-WEPPERSD | `grenzaenderungen-zwischen-den-gemeinden-weppersd/` | 20000456 | 5 | 5 | 5 | 0 |
| GRENZBEREINIGUNGSGESETZ-STEIERMARK-BURGENLAND | `grenzbereinigungsgesetz-steiermark-burgenland/` | 20001289 | 10 | 10 | 10 | 0 |
| GRUNDBETRAG-DER-KAMMERUMLAGEN | `grundbetrag-der-kammerumlagen/` | 20001548 | 3 | 3 | 3 | 0 |
| GRUNDBETRAG-DER-KAMMERUMLAGEN-NEUFESTSETZUNG | `grundbetrag-der-kammerumlagen-neufestsetzung/` | 20000666 | 3 | 3 | 3 | 0 |
| GRUNDSTEUERBEFREIUNGSGESETZ-1995 | `grundsteuerbefreiungsgesetz-1995/` | 10000392 | 26 | 9 | 25 | 2 |
| GRUNDVERSORGUNGS-VERORDNUNG | `grundversorgungs-verordnung/` | 20001441 | 5 | 5 | 5 | 0 |
| GRUNDVERSORGUNGSAENDERUNGSVEREINBARUNG | `grundversorgungsaenderungsvereinbarung/` | 20001503 | 2 | 2 | 2 | 0 |
| GRUNDVERSORGUNGSVEREINBARUNG-ART-15A-B-VG | `grundversorgungsvereinbarung-art-15a-b-vg/` | 20000312 | 21 | 19 | 21 | 0 |
| GruVe-VE | `gruve-ve/` | 10000348 | 42 | 23 | 42 | 0 |
| Bgld. GSG 2008 | `gsg-2008/` | 20000733 | 32 | 21 | 32 | 0 |
| Bgld. GtVG | `gtvg/` | 20000347 | 32 | 18 | 32 | 0 |
| Bgld. GVG 2007 | `gvg-2007/` | 20000615 | 58 | 35 | 58 | 0 |
| HALBTAEGIG-KOSTENLOSE-UND-VERPFLICHTENDE-FRUEHE | `halbtaegig-kostenlose-und-verpflichtende-fruehe/` | 20001044 | 18 | 18 | 18 | 0 |
| HALBTAEGIG-KOSTENLOSE-UND-VERPFLICHTENDE-FRUEHE-1057 | `halbtaegig-kostenlose-und-verpflichtende-fruehe-1057/` | 20001057 | 2 | 2 | 2 | 0 |
| Bgld. HAV | `hav/` | 20000845 | 22 | 15 | 22 | 1 |
| HEBAMMENGEBUEHRENVERORDNUNG | `hebammengebuehrenverordnung/` | 10000066 | 8 | 8 | 8 | 0 |
| HEBAMMENSPRENGEL | `hebammensprengel/` | 10000029 | 3 | 3 | 3 | 0 |
| HEILVORKOMMEN-UND-KURORTEGESETZ-1963 | `heilvorkommen-und-kurortegesetz-1963/` | 10000048 | 168 | 57 | 168 | 1 |
| HEIMBEITRAEGE-FUER-DIE-IM-HEIM | `heimbeitraege-fuer-die-im-heim/` | 20000789 | 2 | 2 | 2 | 0 |
| HEIMBEITRAEGE-FUER-LANDESBERUFSSCHULE-EISENSTADT | `heimbeitraege-fuer-landesberufsschule-eisenstadt/` | 20000987 | 2 | 2 | 2 | 0 |
| HEIMBEITRAEGE-LANDESBERUFSSCHULE-EISENSTADT-NEUF | `heimbeitraege-landesberufsschule-eisenstadt-neuf/` | 20000173 | 2 | 2 | 2 | 0 |
| HELFERINNEN-UND-HELFERAUSBILDUNGS-VERORDNUNG | `helferinnen-und-helferausbildungs-verordnung/` | 20001172 | 17 | 12 | 17 | 0 |
| HELMPFLICHT-BEIM-WINTERSPORT | `helmpflicht-beim-wintersport/` | 20000765 | 6 | 6 | 6 | 0 |
| Bgld. HK-VO 2019 | `hk-vo-2019/` | 20001228 | 201 | 104 | 201 | 0 |
| Bgld. HKG | `hkg/` | 20001217 | 131 | 60 | 131 | 0 |
| HOECHSTSATZVERORDNUNG | `hoechstsatzverordnung/` | 20001464 | 11 | 5 | 11 | 0 |
| HOECHSTTARIFE-FUER-DAS-BESTATTERGEWERBE | `hoechsttarife-fuer-das-bestattergewerbe/` | 10000421 | 16 | 10 | 15 | 2 |
| HOECHSTZULAESSIGER-SCHWEFELGEHALT-IM-HEIZOEL | `hoechstzulaessiger-schwefelgehalt-im-heizoel/` | 10000164 | 12 | 8 | 12 | 0 |
| HOEHE-DER-ENTSCHAEDIGUNG-DER-MITGLIEDER | `hoehe-der-entschaedigung-der-mitglieder/` | 20000799 | 3 | 3 | 3 | 0 |
| HOEHE-DER-GEBUEHREN-FUER-DAS | `hoehe-der-gebuehren-fuer-das/` | 10000138 | 4 | 3 | 4 | 0 |
| HOG-VEREINBARUNG | `hog-vereinbarung/` | 20001142 | 10 | 10 | 10 | 0 |
| Bgld. HSchG | `hschg/` | 20001358 | 28 | 24 | 28 | 0 |
| Bgld. HSchG Begleitgesetz | `hschg-begleitgesetz/` | 20001359 | 2 | 2 | 2 | 0 |
| Bgld. HSG | `hsg/` | 20001559 | 12 | 10 | 12 | 0 |
| HUNDEABGABEGESETZ | `hundeabgabegesetz/` | 10000022 | 30 | 14 | 30 | 0 |
| IG-L-MASSNAHMENKATALOG-2016 | `ig-l-massnahmenkatalog-2016/` | 20001098 | 21 | 15 | 21 | 0 |
| INBETRIEBNAHME-DER-TIERKOERPERVERWERTUNGSANSTALT | `inbetriebnahme-der-tierkoerperverwertungsanstalt/` | 10000116 | 2 | 2 | 2 | 0 |
| INFORMATIONSFREIHEITS-ANPASSUNGSGESETZ | `informationsfreiheits-anpassungsgesetz/` | 20001583 | 2 | 2 | 2 | 0 |
| INSTITUTIONELLES-KINDERBETREUUNGSANGEBOT-FRUEHE | `institutionelles-kinderbetreuungsangebot-fruehe/` | 20000689 | 16 | 16 | 16 | 0 |
| INTERKOMMUNALE-ZUSAMMENARBEIT-DER-GEMEINDEN | `interkommunale-zusammenarbeit-der-gemeinden/` | 20001186 | 18 | 7 | 18 | 0 |
| INVERKEHRBRINGEN-VON-KLEINFEUERUNGEN-UND-DIE | `inverkehrbringen-von-kleinfeuerungen-und-die/` | 20000908 | 35 | 35 | 35 | 0 |
| Bgld. ISG | `isg/` | 20000608 | 83 | 37 | 83 | 7 |
| Bgld. ISUG | `isug/` | 20000607 | 117 | 51 | 117 | 0 |
| JAGDAUSSCHUSSWAHLORDNUNG | `jagdausschusswahlordnung/` | 20001330 | 33 | 33 | 33 | 0 |
| JAGDGESETZ-2004 | `jagdgesetz-2004/` | 20000317 | 445 | 195 | 445 | 0 |
| JAGDKARTEN-UND-JAGDPRUEFUNGSVERORDNUNG | `jagdkarten-und-jagdpruefungsverordnung/` | 20001127 | 57 | 44 | 57 | 0 |
| JAGDKARTENABGABENVERORDNUNG-2026 | `jagdkartenabgabenverordnung-2026/` | 20001537 | 4 | 4 | 4 | 0 |
| JAGDVERORDNUNG | `jagdverordnung/` | 20000330 | 330 | 171 | 330 | 0 |
| Bgld. JFG 2007 | `jfg-2007/` | 20000637 | 40 | 11 | 39 | 1 |
| JUGENDSCHUTZGESETZ-2002 | `jugendschutzgesetz-2002/` | 20000152 | 49 | 17 | 48 | 1 |
| KAbG | `kabg/` | 10000169 | 52 | 19 | 51 | 2 |
| Bgld. KAG 2000 | `kag-2000/` | 20000055 | 389 | 107 | 388 | 2 |
| KANALANSCHLUSSGESETZ-1989 | `kanalanschlussgesetz-1989/` | 10000242 | 27 | 16 | 27 | 0 |
| KARTOFFELZYSTENNEMATODENVERORDNUNG | `kartoffelzystennematodenverordnung/` | 20000793 | 16 | 16 | 16 | 0 |
| KATASTROPHENHILFEGESETZ | `katastrophenhilfegesetz/` | 10000189 | 93 | 44 | 92 | 4 |
| KATASTROPHENSCHUTZDATENERFASSUNGSVERORDNUNG-KDE | `katastrophenschutzdatenerfassungsverordnung-kde/` | 20000995 | 6 | 6 | 6 | 0 |
| KATASTROPHENSCHUTZPLAENE | `katastrophenschutzplaene/` | 10000198 | 9 | 9 | 9 | 0 |
| KAUFPREISE-FUER-BAULANDGRUNDSTUECKE-IM-BURGENLAN | `kaufpreise-fuer-baulandgrundstuecke-im-burgenlan/` | 20001414 | 5 | 5 | 5 | 0 |
| Bgld. KehrG 2022 | `kehrg-2022/` | 20001373 | 25 | 25 | 25 | 0 |
| KEHRGEBIETSEINTEILUNG | `kehrgebietseinteilung/` | 10000260 | 3 | 3 | 3 | 0 |
| KENNZEICHNUNGS-VERORDNUNG | `kennzeichnungs-verordnung/` | 10000307 | 6 | 6 | 6 | 0 |
| KITE-SURFENS-AUF-TEILEN-DES-NEUSIEDLERSEES | `kite-surfens-auf-teilen-des-neusiedlersees/` | 20000738 | 7 | 4 | 7 | 0 |
| Bgld. KJHG | `kjhg/` | 20000955 | 154 | 65 | 154 | 0 |
| KLAERSCHLAMM-UND-MUELLKOMPOSTVERORDNUNG | `klaerschlamm-und-muellkompostverordnung/` | 10000264 | 21 | 14 | 20 | 2 |
| KLEINFEUERUNGEN-FEUERUNGSANLAGEN-UND-BLOCKHEIZKR | `kleinfeuerungen-feuerungsanlagen-und-blockheizkr/` | 20000944 | 2 | 2 | 2 | 0 |
| KLIMASCHUTZGESETZ-BGLD-KLIG | `klimaschutzgesetz-bgld-klig/` | 20001535 | 19 | 19 | 19 | 0 |
| KONSULTATIONSMECHANISMUS-UND-KUENFTIGER-STABILIT | `konsultationsmechanismus-und-kuenftiger-stabilit/` | 10000517 | 11 | 11 | 11 | 0 |
| KOSTENBEITRAG-2009-FESTSETZUNG | `kostenbeitrag-2009-festsetzung/` | 20000706 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2010-FESTSETZUNG | `kostenbeitrag-2010-festsetzung/` | 20000756 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2011-FESTSETZUNG | `kostenbeitrag-2011-festsetzung/` | 20000817 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2013-FESTSETZUNG | `kostenbeitrag-2013-festsetzung/` | 20000913 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2014 | `kostenbeitrag-2014/` | 20000976 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2016-FESTSETZUNG | `kostenbeitrag-2016-festsetzung/` | 20001043 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2017-FESTSETZUNG | `kostenbeitrag-2017-festsetzung/` | 20001091 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2018-FESTSETZUNG | `kostenbeitrag-2018-festsetzung/` | 20001151 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2019-FESTSETZUNG | `kostenbeitrag-2019-festsetzung/` | 20001191 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2020-FESTSETZUNG | `kostenbeitrag-2020-festsetzung/` | 20001257 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2021-FESTSETZUNG | `kostenbeitrag-2021-festsetzung/` | 20001317 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2022-FESTSETZUNG | `kostenbeitrag-2022-festsetzung/` | 20001349 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2023 | `kostenbeitrag-2023/` | 20001402 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2024 | `kostenbeitrag-2024/` | 20001442 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2025 | `kostenbeitrag-2025/` | 20001489 | 2 | 2 | 2 | 0 |
| KOSTENBEITRAG-2026 | `kostenbeitrag-2026/` | 20001544 | 2 | 2 | 2 | 0 |
| KOSTENERSATZ-IN-DEN-ANGELEGENHEITEN-DER | `kostenersatz-in-den-angelegenheiten-der/` | 10000127 | 2 | 2 | 2 | 0 |
| Kraftfahrwesen | `kraftfahrwesen/` | 10000484 | 4 | 4 | 4 | 0 |
| KREDITHILFE-AN-INHABER-VON-BETRIEBEN | `kredithilfe-an-inhaber-von-betrieben/` | 10000025 | 5 | 5 | 5 | 0 |
| KULTURFOERDERUNGSBEITRAGSGESETZ-2024 | `kulturfoerderungsbeitragsgesetz-2024/` | 20001438 | 12 | 9 | 12 | 0 |
| KULTURFOERDERUNGSGESETZ | `kulturfoerderungsgesetz/` | 10000143 | 32 | 11 | 32 | 0 |
| KUNDMACHUNG-UEBER-DIE-KUENDIGUNG-ZWEIER | `kundmachung-ueber-die-kuendigung-zweier/` | 20000612 | 2 | 2 | 2 | 0 |
| KUNDMACHUNG-UEBER-DIE-ZAHL-DER | `kundmachung-ueber-die-zahl-der/` | 20000186 | 3 | 3 | 3 | 0 |
| KURORDNUNG-FUER-DEN-KURORT-BAD | `kurordnung-fuer-den-kurort-bad/` | 10000398 | 73 | 31 | 73 | 0 |
| KURORDNUNG-FUER-DEN-KURORT-BAD-0399 | `kurordnung-fuer-den-kurort-bad-0399/` | 10000399 | 63 | 31 | 63 | 0 |
| KURZPARKZONENGEBUEHRENGESETZ | `kurzparkzonengebuehrengesetz/` | 10000297 | 35 | 15 | 34 | 2 |
| Bgld. KVöG 2024 | `kvoeg-2024/` | 20001469 | 11 | 11 | 11 | 0 |
| L-AM-V 2011 | `l-am-v-2011/` | 20000853 | 5 | 5 | 5 | 0 |
| L-AVV | `l-avv/` | 20000382 | 34 | 12 | 34 | 0 |
| L-BS-V | `l-bs-v/` | 20000489 | 18 | 18 | 18 | 0 |
| L-GWGÜV | `l-gwguev/` | 20000896 | 24 | 6 | 24 | 0 |
| Bgld. L-PSBG | `l-psbg/` | 20001009 | 6 | 6 | 6 | 0 |
| L-SVP-VO | `l-svp-vo/` | 20000230 | 7 | 7 | 7 | 0 |
| Bgld. L-UAG | `l-uag/` | 20000163 | 24 | 13 | 24 | 0 |
| L-VEXAT | `l-vexat/` | 20000345 | 4 | 4 | 4 | 0 |
| (L-VOLV 2010) | `l-volv-2010/` | 20000806 | 5 | 5 | 5 | 0 |
| L-VOPST | `l-vopst/` | 20000854 | 5 | 5 | 5 | 0 |
| LADENOEFFNUNGSZEITEN-FUER-DIE-EINKAUFSZENTREN-IN | `ladenoeffnungszeiten-fuer-die-einkaufszentren-in/` | 20001433 | 2 | 2 | 2 | 0 |
| LADENOEFFNUNGSZEITENVERORDNUNG-1997 | `ladenoeffnungszeitenverordnung-1997/` | 10000472 | 4 | 4 | 4 | 0 |
| LADENOEFFNUNGSZEITENVERORDNUNG-2004 | `ladenoeffnungszeitenverordnung-2004/` | 20000244 | 8 | 6 | 8 | 0 |
| LAND-UND-FORSTWIRTSCHAFTLICHE-DIENSTNEHMERSCHUTZ | `land-und-forstwirtschaftliche-dienstnehmerschutz/` | 10000097 | 47 | 47 | 47 | 0 |
| LANDES-ABFALLWIRTSCHAFTSPLAN-1997 | `landes-abfallwirtschaftsplan-1997/` | 10000469 | 26 | 23 | 26 | 0 |
| LANDES-HYPOTHEKENBANK-BURGENLAND-GESETZ | `landes-hypothekenbank-burgenland-gesetz/` | 10000268 | 30 | 18 | 27 | 4 |
| LANDES-PERSONALVERTRETUNGS-GESCHAEFTSORDNUNG | `landes-personalvertretungs-geschaeftsordnung/` | 10000150 | 40 | 36 | 39 | 1 |
| LANDES-PERSONALVERTRETUNGS-WAHLORDNUNG | `landes-personalvertretungs-wahlordnung/` | 10000151 | 58 | 44 | 57 | 2 |
| LANDES-PERSONALVERTRETUNGSGESETZ | `landes-personalvertretungsgesetz/` | 10000139 | 78 | 34 | 77 | 2 |
| LANDES-UEBERWACHUNGSGEBUEHRENVERORDNUNG-1984-AUF | `landes-ueberwachungsgebuehrenverordnung-1984-auf/` | 20001163 | 3 | 3 | 3 | 0 |
| LANDES-UND-GEMEINDEVERWALTUNGSABGABENGESETZ | `landes-und-gemeindeverwaltungsabgabengesetz/` | 10000075 | 34 | 15 | 33 | 2 |
| LANDES-WIEDERVERLAUTBARUNGSGESETZ | `landes-wiederverlautbarungsgesetz/` | 10000195 | 6 | 6 | 6 | 0 |
| LANDESFONDS-FUER-DIE-OPFER-DES | `landesfonds-fuer-die-opfer-des/` | 20001248 | 4 | 4 | 4 | 0 |
| LANDESGESELLSCHAFT-F-D-ALLGEMEINVERSORGUNG-MIT-E | `landesgesellschaft-f-d-allgemeinversorgung-mit-e/` | 10000037 | 6 | 5 | 6 | 0 |
| LANDESGESETZ-BETREFFEND-TANZLEHRANSTALTEN-AUFHEB | `landesgesetz-betreffend-tanzlehranstalten-aufheb/` | 20001130 | 3 | 3 | 3 | 0 |
| LANDESGRENZEN-UEBERSCHREITENDEN-BERUFSSCHULBESUC | `landesgrenzen-ueberschreitenden-berufsschulbesuc/` | 10000153 | 13 | 11 | 13 | 0 |
| LANDESGRENZEN-UEBERSCHREITENDEN-BERUFSSCHULBESUC-0748 | `landesgrenzen-ueberschreitenden-berufsschulbesuc-0748/` | 20000748 | 4 | 4 | 4 | 0 |
| LANDESGRENZEN-UEBERSCHREITENDEN-BESUCH-VON-LANDW | `landesgrenzen-ueberschreitenden-besuch-von-landw/` | 20000981 | 9 | 9 | 9 | 0 |
| LANDESGRENZEN-UEBERSCHREITENDEN-BESUCH-VON-LANDW-0983 | `landesgrenzen-ueberschreitenden-besuch-von-landw-0983/` | 20000983 | 2 | 2 | 2 | 0 |
| LANDESGRENZEN-UEBERSCHREITENDEN-BESUCH-VON-LANDW-0986 | `landesgrenzen-ueberschreitenden-besuch-von-landw-0986/` | 20000986 | 2 | 2 | 2 | 0 |
| LANDESKRANKENANSTALTENPLAN-2008-AUFHEBUNG | `landeskrankenanstaltenplan-2008-aufhebung/` | 20001403 | 3 | 3 | 3 | 0 |
| LANDESLEHRER-PERSONALVERTRETUNGS-GESCHAEFTSORDNU | `landeslehrer-personalvertretungs-geschaeftsordnu/` | 10000078 | 51 | 35 | 51 | 0 |
| LANDESLEHRER-PERSONALVERTRETUNGS-WAHLORDNUNG | `landeslehrer-personalvertretungs-wahlordnung/` | 10000064 | 79 | 47 | 79 | 0 |
| LANDESRAUMORDNUNGSPLAN | `landesraumordnungsplan/` | 10000301 | 5 | 5 | 5 | 0 |
| LANDESSPORTEHRENZEICHEN-VERORDNUNG-2004 | `landessportehrenzeichen-verordnung-2004/` | 20000322 | 5 | 5 | 5 | 0 |
| LANDESSTRASSENVERORDNUNG | `landesstrassenverordnung/` | 20000636 | 14 | 6 | 14 | 0 |
| LANDESSYMBOLE | `landessymbole/` | 10000252 | 30 | 19 | 28 | 2 |
| LANDESUMLAGEGESETZ | `landesumlagegesetz/` | 10000353 | 48 | 6 | 47 | 2 |
| LANDSCHAFT-UND-TEILNATURSCHUTZGEBIET-TEILE-DER | `landschaft-und-teilnaturschutzgebiet-teile-der/` | 20000565 | 9 | 9 | 9 | 0 |
| LANDSCHAFTSCHUTZGEBIET-SUEDBURGENLAENDISCHES-HUE | `landschaftschutzgebiet-suedburgenlaendisches-hue/` | 20000566 | 22 | 22 | 22 | 0 |
| LANDSCHAFTSSCHUTZABGABE-NEUFESTSETZUNG | `landschaftsschutzabgabe-neufestsetzung/` | 20001394 | 5 | 3 | 5 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-BIRI-NOPLERBERG-STOOB | `landschaftsschutzgebiet-biri-noplerberg-stoob/` | 20000956 | 9 | 9 | 9 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-KELLERVIERTEL-IN-DER-KG | `landschaftsschutzgebiet-kellerviertel-in-der-kg/` | 20000568 | 9 | 9 | 9 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-LANDSEER-BERGE-UND-NATUR | `landschaftsschutzgebiet-landseer-berge-und-natur/` | 20000069 | 12 | 12 | 12 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-RAAB-UND-NATURPARK-RAAB | `landschaftsschutzgebiet-raab-und-naturpark-raab/` | 10000478 | 12 | 12 | 12 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-ROSALIA-KOGELBERG-UND | `landschaftsschutzgebiet-rosalia-kogelberg-und/` | 20000594 | 13 | 13 | 13 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-UMGEBUNG-VON-BERNSTEIN-L | `landschaftsschutzgebiet-umgebung-von-bernstein-l/` | 20000569 | 9 | 9 | 9 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-UND-TEILNATURSCHUTZGEBIE | `landschaftsschutzgebiet-und-teilnaturschutzgebie/` | 20000562 | 10 | 10 | 10 | 0 |
| LANDSCHAFTSSCHUTZGEBIET-UND-TEILNATURSCHUTZGEBIE-0574 | `landschaftsschutzgebiet-und-teilnaturschutzgebie-0574/` | 20000574 | 7 | 7 | 7 | 0 |
| LANDSCHAFTSSCHUTZVERORDNUNG-FORCHTENSTEIN-ROSALI | `landschaftsschutzverordnung-forchtenstein-rosali/` | 20000570 | 8 | 8 | 8 | 0 |
| LANDSCHAFTSSCHUTZVERORDNUNG-FORCHTENSTEIN-ROSALI-1420 | `landschaftsschutzverordnung-forchtenstein-rosali-1420/` | 20001420 | 3 | 3 | 3 | 0 |
| LANDTAGSWAHL-2020 | `landtagswahl-2020/` | 20001236 | 4 | 4 | 4 | 0 |
| LANDTAGSWAHL-2025 | `landtagswahl-2025/` | 20001484 | 4 | 4 | 4 | 0 |
| LANDWIRTSCHAFTLICHE-BERUFSSCHULE-LAENDLICHE-HAUS | `landwirtschaftliche-berufsschule-laendliche-haus/` | 10000211 | 5 | 5 | 5 | 0 |
| LANDWIRTSCHAFTLICHE-BERUFSSCHULE-LANDWIRTSCHAFT | `landwirtschaftliche-berufsschule-landwirtschaft/` | 10000210 | 5 | 5 | 5 | 0 |
| LANDWIRTSCHAFTLICHE-FACHSCHUL-LEHRPLAENEVERORDNU | `landwirtschaftliche-fachschul-lehrplaeneverordnu/` | 20001157 | 25 | 21 | 25 | 0 |
| LANDWIRTSCHAFTLICHES-BRINGUNGSRECHT | `landwirtschaftliches-bringungsrecht/` | 10000018 | 35 | 29 | 35 | 0 |
| LANDWIRTSCHAFTLICHES-SCHULGESETZ | `landwirtschaftliches-schulgesetz/` | 10000175 | 191 | 110 | 190 | 2 |
| LANDWIRTSCHAFTLICHES-SIEDLUNGSGESETZ | `landwirtschaftliches-siedlungsgesetz/` | 10000080 | 18 | 13 | 18 | 0 |
| LANDWIRTSCHAFTSFOERDERUNGSGESETZ | `landwirtschaftsfoerderungsgesetz/` | 10000194 | 17 | 14 | 17 | 0 |
| LANDWIRTSCHAFTSKAMMERGESETZ | `landwirtschaftskammergesetz/` | 20000343 | 240 | 117 | 240 | 6 |
| Bgld. LAOG 2022 | `laog-2022/` | 20001384 | 17 | 14 | 17 | 0 |
| LBBG 2001 | `lbbg-2001/` | 20000136 | 575 | 166 | 572 | 8 |
| LBDG 1997 | `lbdg-1997/` | 10000508 | 637 | 239 | 634 | 5 |
| Bgld. LBetreuG | `lbetreug/` | 20000587 | 48 | 16 | 48 | 0 |
| Bgld. LBG | `lbg/` | 10000515 | 82 | 21 | 80 | 3 |
| LBPG 2002 | `lbpg-2002/` | 20000181 | 367 | 137 | 348 | 30 |
| Bgld. LBwG 2019 | `lbwg-2019/` | 20001189 | 45 | 45 | 45 | 0 |
| Bgld. LDAG | `ldag/` | 20000211 | 9 | 4 | 9 | 0 |
| Bgld. LDHG | `ldhg/` | 10000393 | 81 | 19 | 80 | 2 |
| Bgld. LDLG | `ldlg/` | 20000862 | 28 | 21 | 28 | 0 |
| LEHRGANGSDAUER-AN-DEN-BERUFSBILDENDEN-PFLICHTSCH | `lehrgangsdauer-an-den-berufsbildenden-pflichtsch/` | 10000415 | 3 | 3 | 3 | 0 |
| LEISTUNGSBEURTEILUNG-AN-LAND-UND-FORSTWIRTSCHAFT | `leistungsbeurteilung-an-land-und-forstwirtschaft/` | 10000464 | 55 | 29 | 55 | 0 |
| LFBAO | `lfbao/` | 10000339 | 131 | 57 | 131 | 0 |
| LICHTBILDAUSWEIS-FUER-DIE-MITGLIEDER-DER | `lichtbildausweis-fuer-die-mitglieder-der/` | 10000154 | 4 | 4 | 4 | 0 |
| LICHTSPIELGESETZ-1960-AUFHEBUNG | `lichtspielgesetz-1960-aufhebung/` | 20001240 | 4 | 4 | 4 | 0 |
| LKF-GEBUEHREN-PFLEGEGEBUEHREN-UND-WEITERE-ENTGEL | `lkf-gebuehren-pflegegebuehren-und-weitere-entgel/` | 20000671 | 9 | 9 | 9 | 0 |
| Bgld. LKFinG | `lkfing/` | 20000915 | 9 | 5 | 9 | 0 |
| Bgld. LKWO | `lkwo/` | 20001486 | 81 | 81 | 81 | 0 |
| Bgld. LMKG-VO 2019 | `lmkg-vo-2019/` | 20001194 | 14 | 8 | 14 | 0 |
| Bgld. LMKGG | `lmkgg/` | 20000657 | 22 | 11 | 22 | 0 |
| Bgld. LRHG | `lrhg/` | 20000143 | 47 | 20 | 47 | 0 |
| Bgld. LSG | `lsg/` | 20001216 | 37 | 35 | 37 | 0 |
| Bgld. LSRG 2005 | `lsrg-2005/` | 20000358 | 21 | 11 | 21 | 0 |
| LTWO 1995 | `ltwo-1995/` | 10000427 | 364 | 115 | 362 | 5 |
| LUSTBARKEITSABGABEGESETZ-1969 | `lustbarkeitsabgabegesetz-1969/` | 10000079 | 26 | 15 | 25 | 2 |
| Bgld. LVBG 2013 | `lvbg-2013/` | 20000963 | 431 | 161 | 431 | 1 |
| Bgld. LVwgBG | `lvwgbg/` | 20000964 | 83 | 83 | 83 | 0 |
| M-GOTV | `m-gotv/` | 20001022 | 33 | 28 | 33 | 0 |
| MANDATE-FUER-DIE-WAHL-DES | `mandate-fuer-die-wahl-des/` | 10000454 | 3 | 3 | 3 | 0 |
| MARKTUEBERWACHUNG-VON-BAUPRODUKTEN | `marktueberwachung-von-bauprodukten/` | 20000812 | 18 | 18 | 18 | 0 |
| MARKTUEBERWACHUNG-VON-BAUPRODUKTEN-BEITRITT-SALZ | `marktueberwachung-von-bauprodukten-beitritt-salz/` | 20000857 | 2 | 2 | 2 | 0 |
| MARKTUEBERWACHUNG-VON-BAUPRODUKTEN-BEITRITT-STEI | `marktueberwachung-von-bauprodukten-beitritt-stei/` | 20000841 | 2 | 2 | 2 | 0 |
| MASKENTRAGEPFLICHT-AN-STARK-FREQUENTIERTEN-BESTI | `maskentragepflicht-an-stark-frequentierten-besti/` | 20001318 | 3 | 3 | 3 | 0 |
| MASSNAHMEN-GEMAESS-PAR-38-ABS | `massnahmen-gemaess-par-38-abs/` | 10000184 | 8 | 6 | 8 | 0 |
| MASSNAHMEN-IM-GEBAEUDESEKTOR-ZUM-ZWECK | `massnahmen-im-gebaeudesektor-zum-zweck/` | 20000745 | 33 | 22 | 33 | 0 |
| MASSNAHMEN-ZUM-SCHUTZ-VON-WEINBAUKULTUREN | `massnahmen-zum-schutz-von-weinbaukulturen/` | 20001417 | 7 | 7 | 7 | 0 |
| MELDEBOGEN-NACH-DEM-WEINBAUGESETZ | `meldebogen-nach-dem-weinbaugesetz/` | 10000160 | 3 | 3 | 3 | 0 |
| MEV | `mev/` | 20000691 | 12 | 12 | 12 | 0 |
| MINDESTABSTAENDE-ZU-FREMDEN-GRUNDSTUECKEN | `mindestabstaende-zu-fremden-grundstuecken/` | 10000221 | 11 | 10 | 11 | 0 |
| MINDESTEINKOMMEN-DER-SPRENGELHEBAMMEN | `mindesteinkommen-der-sprengelhebammen/` | 10000098 | 9 | 7 | 9 | 0 |
| MITWIRKUNGSRECHTE-DER-LAENDER-UND-GEMEINDEN | `mitwirkungsrechte-der-laender-und-gemeinden/` | 10000343 | 16 | 16 | 16 | 0 |
| MOBILITAETSGESETZ-2024 | `mobilitaetsgesetz-2024/` | 20001483 | 8 | 8 | 8 | 0 |
| MODELLSTELLEN-VERORDNUNG | `modellstellen-verordnung/` | 20001253 | 61 | 60 | 61 | 0 |
| MOPEDAUSWEISVERORDNUNG-AUFHEBUNG | `mopedausweisverordnung-aufhebung/` | 20000939 | 2 | 2 | 2 | 0 |
| MUSIKSCHULFOERDERUNGSGESETZ | `musikschulfoerderungsgesetz/` | 10000337 | 19 | 10 | 19 | 0 |
| MUSIKSCHULPLAN | `musikschulplan/` | 10000333 | 3 | 3 | 3 | 0 |
| Bgld. MVKG | `mvkg/` | 20000326 | 114 | 47 | 113 | 2 |
| NAHVERSORGUNGSFOERDERUNG-FESTLEGUNG-VON-BEDINGUN | `nahversorgungsfoerderung-festlegung-von-bedingun/` | 10000256 | 4 | 4 | 4 | 0 |
| NASSE-GRENZEN-ZWISCHEN-DER-REPUBLIK | `nasse-grenzen-zwischen-der-republik/` | 10000061 | 3 | 3 | 3 | 0 |
| NATIONALPARK-KENNZEICHNUNGSVERORDNUNG | `nationalpark-kennzeichnungsverordnung/` | 10000387 | 5 | 5 | 5 | 0 |
| NATIONALPARKFLAECHEN-DES-NATIONALPARKS-NEUSIEDLE | `nationalparkflaechen-des-nationalparks-neusiedle/` | 20001564 | 21 | 16 | 21 | 0 |
| NATUR-UND-LANDSCHAFTSSCHUTZVERORDNUNG-NEUSIEDLER | `natur-und-landschaftsschutzverordnung-neusiedler/` | 20000374 | 9 | 9 | 9 | 0 |
| NATURPARK-GESCHRIEBENSTEIN | `naturpark-geschriebenstein/` | 10000535 | 5 | 5 | 5 | 0 |
| NATURPARK-GESCHRIEBENSTEIN-1587 | `naturpark-geschriebenstein-1587/` | 20001587 | 3 | 3 | 3 | 0 |
| NATURPARK-IN-DER-WEINIDYLLE | `naturpark-in-der-weinidylle/` | 10000528 | 5 | 5 | 5 | 0 |
| NATURPARK-NEUSIEDLER-SEE-LEITHAGEBIRGE | `naturpark-neusiedler-see-leithagebirge/` | 20000396 | 3 | 3 | 3 | 0 |
| NATURSCHUTZGEBIET-AUWIESEN-ZICKENBACHTAL | `naturschutzgebiet-auwiesen-zickenbachtal/` | 20000490 | 8 | 8 | 8 | 0 |
| NATURSCHUTZGEBIET-BATTHYANYFELD | `naturschutzgebiet-batthyanyfeld/` | 10000493 | 8 | 8 | 8 | 0 |
| NATURSCHUTZGEBIET-DONATUSKREUZ | `naturschutzgebiet-donatuskreuz/` | 20001596 | 14 | 14 | 14 | 0 |
| NATURSCHUTZGEBIET-FEUCHTMULDE-ALTE-SCHANZE-PARND | `naturschutzgebiet-feuchtmulde-alte-schanze-parnd/` | 20001243 | 10 | 10 | 10 | 0 |
| NATURSCHUTZGEBIET-FEUCHTWIESENGEBIET-BACHAUE-LUG | `naturschutzgebiet-feuchtwiesengebiet-bachaue-lug/` | 20001385 | 11 | 11 | 11 | 0 |
| NATURSCHUTZGEBIET-PARNDORFER-HEIDE | `naturschutzgebiet-parndorfer-heide/` | 10000294 | 9 | 9 | 9 | 0 |
| NATURSCHUTZGEBIET-SIEGENDORFER-PUSSTA-HEIDE-UND | `naturschutzgebiet-siegendorfer-pussta-heide-und/` | 20001534 | 15 | 15 | 15 | 0 |
| NATURSCHUTZGEBIET-THENAU-BREITENBRUNN | `naturschutzgebiet-thenau-breitenbrunn/` | 20000710 | 12 | 12 | 12 | 0 |
| NATURSCHUTZORGANE-BESTELLUNGSVERORDNUNG | `naturschutzorgane-bestellungsverordnung/` | 10000293 | 11 | 9 | 11 | 0 |
| NEUE-GRENZWERTE-FUER-FLEISCH-FRISCHKAESE | `neue-grenzwerte-fuer-fleisch-frischkaese/` | 10000183 | 3 | 3 | 3 | 0 |
| NEUERLICHE-ANPASSUNG-DER-BURGENLAENDISCHEN-LANDE | `neuerliche-anpassung-der-burgenlaendischen-lande/` | 20001301 | 31 | 31 | 31 | 0 |
| NEUERLICHE-ANPASSUNG-DES-BURGENLAENDISCHEN-GEMEI | `neuerliche-anpassung-des-burgenlaendischen-gemei/` | 20001303 | 4 | 4 | 4 | 0 |
| NEUFESTSETZUNG-DER-TOURISMUSABGABEN | `neufestsetzung-der-tourismusabgaben/` | 20001295 | 7 | 5 | 7 | 0 |
| Bgld. NotifG | `notifg/` | 20000763 | 26 | 11 | 26 | 0 |
| Bgld. NPG 2026 | `npg-2026/` | 20001561 | 34 | 34 | 34 | 0 |
| OBJEKTIVIERUNGSGESETZ | `objektivierungsgesetz/` | 10000207 | 75 | 19 | 74 | 2 |
| OBJEKTIVIERUNGSKATALOG | `objektivierungskatalog/` | 10000240 | 6 | 6 | 6 | 0 |
| OEFFENTLICHE-VERSTEIGERUNGEN-VON-GENOSSENSCHAFTS | `oeffentliche-versteigerungen-von-genossenschafts/` | 20001341 | 10 | 10 | 10 | 0 |
| Bgld. ÖFG | `oefg/` | 20000626 | 15 | 10 | 15 | 0 |
| OERTLICHER-TOURISMUSVERBAND-DER-GEMEINDE-LACKEND | `oertlicher-tourismusverband-der-gemeinde-lackend/` | 20000801 | 3 | 3 | 3 | 0 |
| OESTERREICHISCHER-STABILITAETSPAKT | `oesterreichischer-stabilitaetspakt/` | 10000533 | 7 | 7 | 7 | 0 |
| OESTERREICHISCHER-STABILITAETSPAKT-2012-BEITRITT | `oesterreichischer-stabilitaetspakt-2012-beitritt/` | 20000937 | 2 | 2 | 2 | 0 |
| ÖStP 2025 | `oestp-2025/` | 20001580 | 25 | 25 | 25 | 0 |
| ORGANISATION-UND-FINANZIERUNG-DES-GESUNDHEITSWES | `organisation-und-finanzierung-des-gesundheitswes/` | 20001501 | 58 | 58 | 58 | 0 |
| Bgld. PaFöG 2024 | `pafoeg-2024/` | 20001470 | 17 | 13 | 17 | 0 |
| Bgld. PBStützpVO 2024 | `pbstuetzpvo-2024/` | 20001490 | 29 | 24 | 29 | 0 |
| Bgld. PBÜ-G | `pbue-g/` | 20000259 | 29 | 15 | 28 | 1 |
| PENSIONSSICHERUNGSBEITRAGSVERORDNUNG-1996 | `pensionssicherungsbeitragsverordnung-1996/` | 10000447 | 4 | 4 | 4 | 0 |
| PERSONALAUFWAND-FUER-LEHRER-AN-PFLICHTSCHULEN | `personalaufwand-fuer-lehrer-an-pflichtschulen/` | 20000583 | 12 | 12 | 12 | 0 |
| PERSONALVERTRETUNG-FUER-DIE-LANDWIRTSCHAFTLICHEN | `personalvertretung-fuer-die-landwirtschaftlichen/` | 10000205 | 3 | 3 | 3 | 0 |
| PERSONENSTANDSBUECHER-IN-DEN-GEMEINDEN-EDELSTAL | `personenstandsbuecher-in-den-gemeinden-edelstal/` | 10000322 | 3 | 3 | 3 | 0 |
| PERSONENSTANDSBUECHER-IN-DEN-GEMEINDEN-GROSSPETE | `personenstandsbuecher-in-den-gemeinden-grosspete/` | 10000323 | 3 | 3 | 3 | 0 |
| PERSONENSTANDSBUECHER-IN-DEN-GEMEINDEN-SIEGENDOR | `personenstandsbuecher-in-den-gemeinden-siegendor/` | 10000324 | 3 | 3 | 3 | 0 |
| PFLANZENSCHUTZ-UEBERTRAGUNGSVERORDNUNG | `pflanzenschutz-uebertragungsverordnung/` | 10000461 | 7 | 4 | 7 | 0 |
| PFLANZENSCHUTZGERAETEUEBERPRUEFUNGSVERORDNUNG | `pflanzenschutzgeraeteueberpruefungsverordnung/` | 20001059 | 20 | 14 | 20 | 0 |
| PFLANZENSCHUTZMITTEL-AUSBILDUNGSBESCHEINIGUNGS-V | `pflanzenschutzmittel-ausbildungsbescheinigungs-v/` | 20001014 | 10 | 7 | 10 | 0 |
| PFLANZENSCHUTZMITTELGESETZ-2012-BGLD-PSMG | `pflanzenschutzmittelgesetz-2012-bgld-psmg/` | 20000886 | 51 | 22 | 51 | 0 |
| PFLANZENSCHUTZTECHNISCHE-UEBERWACHUNG-VON-BAUMSC | `pflanzenschutztechnische-ueberwachung-von-baumsc/` | 10000180 | 6 | 5 | 6 | 0 |
| PFLANZGUT-UEBERTRAGUNGSVERORDNUNG | `pflanzgut-uebertragungsverordnung/` | 10000485 | 3 | 3 | 3 | 0 |
| PFLEGEGEBUEHRENVERORDNUNG-2024 | `pflegegebuehrenverordnung-2024/` | 20001457 | 8 | 8 | 8 | 0 |
| PFLEGEGEBUEHRENVERORDNUNG-2025 | `pflegegebuehrenverordnung-2025/` | 20001520 | 8 | 8 | 8 | 0 |
| PFLEGEGEBUEHRENVERORDNUNG-2026 | `pflegegebuehrenverordnung-2026/` | 20001575 | 8 | 8 | 8 | 0 |
| PFLEGEKINDER-UND-FUERSORGEERZIEHUNGSHEIM-RICHTLI | `pflegekinder-und-fuersorgeerziehungsheim-richtli/` | 10000054 | 26 | 26 | 26 | 0 |
| Bgld. PflichtschulclusterVO | `pflichtschulclustervo/` | 20001183 | 6 | 6 | 6 | 0 |
| Bgld. PflSchG 1995 | `pflschg-1995/` | 10000390 | 385 | 79 | 384 | 5 |
| Bgld. PG-K | `pg-k/` | 10000335 | 16 | 7 | 16 | 0 |
| Bgld. PKB-V | `pkb-v/` | 20000749 | 3 | 3 | 3 | 0 |
| Bgld. PKVG | `pkvg/` | 10000511 | 22 | 22 | 22 | 0 |
| PLANZEICHENVERORDNUNG-FUER-DIGITALE-FLAECHENWIDM | `planzeichenverordnung-fuer-digitale-flaechenwidm/` | 20000724 | 15 | 5 | 15 | 0 |
| PLANZEICHENVERORDNUNG-FUER-OERTLICHE-ENTWICKLUNG | `planzeichenverordnung-fuer-oertliche-entwicklung/` | 20001335 | 6 | 6 | 6 | 0 |
| POLYTECHNISCHE-SCHULSPRENGELVERORDNUNG | `polytechnische-schulsprengelverordnung/` | 20001000 | 12 | 9 | 12 | 0 |
| PRUEFUNGSSTOFFABGRENZUNGS-VERORDNUNG | `pruefungsstoffabgrenzungs-verordnung/` | 20000576 | 2 | 2 | 2 | 0 |
| Bgld. PSA-V | `psa-v/` | 20001367 | 8 | 8 | 8 | 0 |
| Bgld. PSG 2019 | `psg-2019/` | 20001246 | 15 | 14 | 15 | 0 |
| QUALITAETSSTANDARDS-FUER-DIE-FOERDERUNG-DER | `qualitaetsstandards-fuer-die-foerderung-der/` | 20000378 | 15 | 15 | 15 | 0 |
| RAUMPLANUNGSGESETZ-2019-AENDERUNG-UND-RAUMPLANUN | `raumplanungsgesetz-2019-aenderung-und-raumplanun/` | 20001498 | 4 | 4 | 4 | 0 |
| Bgld. RBG | `rbg/` | 20001331 | 12 | 12 | 12 | 0 |
| REBENVERKEHRS-UEBERTRAGUNGSVERORDNUNG | `rebenverkehrs-uebertragungsverordnung/` | 10000460 | 6 | 4 | 5 | 1 |
| REBSCHNITTVERORDNUNG | `rebschnittverordnung/` | 10000272 | 2 | 2 | 2 | 0 |
| RECHTSBEREINIGUNGSGESETZ | `rechtsbereinigungsgesetz/` | 10000436 | 4 | 4 | 4 | 0 |
| REFERATSEINTEILUNG | `referatseinteilung/` | 20001504 | 6 | 6 | 6 | 0 |
| REGELUNG-DER-PREISE-FUER-BESTIMMTE | `regelung-der-preise-fuer-bestimmte/` | 10000457 | 5 | 5 | 5 | 0 |
| REGELUNG-DER-SATZUNGEN-NEUGEBILDETER-VERWALTUNGS | `regelung-der-satzungen-neugebildeter-verwaltungs/` | 10000085 | 3 | 3 | 3 | 0 |
| REGELUNG-DER-VERWENDBARKEIT-VON-BAUPRODUKTEN | `regelung-der-verwendbarkeit-von-bauprodukten/` | 10000543 | 21 | 21 | 21 | 0 |
| REGIONALER-STRUKTURPLAN-GESUNDHEIT-BURGENLAND-20 | `regionaler-strukturplan-gesundheit-burgenland-20/` | 20001352 | 3 | 3 | 3 | 0 |
| REGIONALER-STRUKTURPLAN-GESUNDHEIT-BURGENLAND-20-1479 | `regionaler-strukturplan-gesundheit-burgenland-20-1479/` | 20001479 | 3 | 3 | 3 | 0 |
| REGIONALPROGRAMM-ZUR-SICHERUNG-DER-QUALITAET | `regionalprogramm-zur-sicherung-der-qualitaet/` | 20001037 | 7 | 7 | 7 | 0 |
| REGIONALVERBAND-BEZIRK-JENNERSDORF-ERRICHTUNG | `regionalverband-bezirk-jennersdorf-errichtung/` | 10000351 | 6 | 2 | 6 | 1 |
| REGIONALVERBAND-LEITHAAUEN-NEUSIEDLERSEE-ERRICHT | `regionalverband-leithaauen-neusiedlersee-erricht/` | 10000384 | 7 | 3 | 7 | 0 |
| REGIONALVERBAND-MITTELBURGENLAND-ERRICHTUNG | `regionalverband-mittelburgenland-errichtung/` | 10000417 | 7 | 3 | 7 | 0 |
| REGIONALVERBAND-OBERWART-BAD-TATZMANNSDORF-ERRIC | `regionalverband-oberwart-bad-tatzmannsdorf-erric/` | 10000383 | 4 | 3 | 4 | 0 |
| REGIONALVERBAND-REGION-ROSALIA-ERRICHTUNG | `regionalverband-region-rosalia-errichtung/` | 10000352 | 4 | 2 | 4 | 0 |
| REISEKOSTEN-UND-AUFWANDSENTSCHAEDIGUNG-DER-GRUND | `reisekosten-und-aufwandsentschaedigung-der-grund/` | 10000117 | 7 | 5 | 7 | 0 |
| REISEKOSTEN-UND-AUFWANDSENTSCHAEDIGUNG-DER-OBJEK | `reisekosten-und-aufwandsentschaedigung-der-objek/` | 10000237 | 10 | 3 | 9 | 2 |
| RETTUNGSBEITRAGSVERORDNUNG-2026 | `rettungsbeitragsverordnung-2026/` | 20001576 | 3 | 3 | 3 | 0 |
| Bgld. RettungsG 2024 | `rettungsg-2024/` | 20001447 | 25 | 22 | 25 | 0 |
| RICHTLINIE-2016-801-EU-ERFORDERLICHE-ANPASSUNG | `richtlinie-2016-801-eu-erforderliche-anpassung/` | 20001202 | 2 | 2 | 2 | 0 |
| RICHTLINIEN-FUER-DEN-RETTUNGS-UND | `richtlinien-fuer-den-rettungs-und/` | 20001480 | 3 | 3 | 3 | 0 |
| RICHTLINIEN-UEBER-DEN-EINSATZ-VON | `richtlinien-ueber-den-einsatz-von/` | 20000712 | 10 | 10 | 10 | 0 |
| RICHTLINIEN-UEBER-DIE-VERMOEGENSBEWERTUNG-VON | `richtlinien-ueber-die-vermoegensbewertung-von/` | 10000213 | 15 | 15 | 15 | 0 |
| Bgld. RPEG | `rpeg/` | 20001225 | 15 | 13 | 15 | 0 |
| Ruster StR 2003 | `ruster-str-2003/` | 20000224 | 239 | 116 | 239 | 0 |
| SAEGERAETEVERORDNUNG | `saegeraeteverordnung/` | 20000844 | 5 | 5 | 5 | 0 |
| Bgld. SAG 2012 | `sag-2012/` | 20000934 | 8 | 8 | 8 | 0 |
| SAMMELGESETZ-ANPASSUNG-BLAUE-KARTE-EU-RICHTLINIE | `sammelgesetz-anpassung-blaue-karte-eu-richtlinie/` | 20001451 | 2 | 2 | 2 | 0 |
| SAMMELGESETZ-ANPASSUNG-RICHTLINIE-EU | `sammelgesetz-anpassung-richtlinie-eu/` | 20001584 | 2 | 2 | 2 | 0 |
| SAMMELGESETZ-DIENSTRECHT-2025 | `sammelgesetz-dienstrecht-2025/` | 20001582 | 2 | 2 | 2 | 0 |
| SAMMELGESETZ-DIENSTRECHT-2026 | `sammelgesetz-dienstrecht-2026/` | 20001585 | 2 | 2 | 2 | 0 |
| SAMMELGESETZ-EU-VERORDNUNGEN | `sammelgesetz-eu-verordnungen/` | 20001238 | 19 | 15 | 19 | 0 |
| SAMMELGESETZ-MINDESTLOHNRICHTLINIE | `sammelgesetz-mindestlohnrichtlinie/` | 20001586 | 2 | 2 | 2 | 0 |
| SAMMLUNGSGESETZ | `sammlungsgesetz/` | 10000086 | 16 | 13 | 16 | 0 |
| SANITAETSKREISE | `sanitaetskreise/` | 10000442 | 22 | 6 | 22 | 0 |
| SATZUNG-DER-LANDES-HYPOTHEKENBANK-BURGENLAND-HOL | `satzung-der-landes-hypothekenbank-burgenland-hol/` | 10000259 | 4 | 4 | 4 | 0 |
| Bgld. SBBG | `sbbg/` | 20000650 | 46 | 18 | 46 | 0 |
| SCHIFFAHRT-AUF-EINER-TEILFLAECHE-DES | `schiffahrt-auf-einer-teilflaeche-des/` | 10000217 | 9 | 6 | 9 | 0 |
| SCHIFFAHRTSVERBOT-SEEBADANLAGE-DER-STADTGEMEINDE | `schiffahrtsverbot-seebadanlage-der-stadtgemeinde/` | 10000163 | 2 | 2 | 2 | 0 |
| SCHONGEBIET-FRAUENKIRCHEN-GOLS-ZUR-SICHERUNG-DER | `schongebiet-frauenkirchen-gols-zur-sicherung-der/` | 20000797 | 8 | 8 | 8 | 0 |
| SCHONGEBIET-HORIZONTALFILTERBRUNNEN-GOLS-1-ZUR | `schongebiet-horizontalfilterbrunnen-gols-1-zur/` | 20001239 | 8 | 8 | 8 | 0 |
| SCHONGEBIET-HORIZONTALFILTERBRUNNEN-KLEYLEHOF-IN | `schongebiet-horizontalfilterbrunnen-kleylehof-in/` | 20001192 | 9 | 9 | 9 | 0 |
| SCHONGEBIET-KITTSEE-ZUR-SICHERUNG-DER | `schongebiet-kittsee-zur-sicherung-der/` | 20000796 | 8 | 8 | 8 | 0 |
| SCHONGEBIET-OBERWART-UNTERWART-ROTENTURM-ZUR-SIC | `schongebiet-oberwart-unterwart-rotenturm-zur-sic/` | 20001153 | 8 | 8 | 8 | 0 |
| SCHONGEBIET-OGGAU-ZUR-SICHERUNG-DER | `schongebiet-oggau-zur-sicherung-der/` | 20000798 | 8 | 8 | 8 | 0 |
| SCHONGEBIET-PURBACH-AM-NEUSIEDLER-SEE | `schongebiet-purbach-am-neusiedler-see/` | 20000847 | 8 | 8 | 8 | 0 |
| SCHONGEBIET-ZUR-SICHERUNG-DES-GRUNDWASSERVORKOMM | `schongebiet-zur-sicherung-des-grundwasservorkomm/` | 10000129 | 7 | 7 | 7 | 0 |
| SCHONGEBIET-ZUR-SICHERUNG-VON-HEILQUELLEN | `schongebiet-zur-sicherung-von-heilquellen/` | 10000115 | 7 | 7 | 7 | 0 |
| SCHONGEBIETSVERORDNUNG-NEUFELD-AN-DER-LEITHA | `schongebietsverordnung-neufeld-an-der-leitha/` | 20000867 | 8 | 8 | 8 | 0 |
| SCHULBAU-UND-EINRICHTUNGSVERORDNUNG | `schulbau-und-einrichtungsverordnung/` | 10000209 | 39 | 39 | 39 | 0 |
| SCHULBEHOERDEN-NOVELLE-2014 | `schulbehoerden-novelle-2014/` | 20000997 | 5 | 5 | 5 | 0 |
| SCHULFESTIGKEIT-VON-LEHRERSTELLEN | `schulfestigkeit-von-lehrerstellen/` | 10000241 | 12 | 10 | 11 | 1 |
| SCHULFESTIGKEIT-VON-LEITER-UND-LEHRERSTELLEN | `schulfestigkeit-von-leiter-und-lehrerstellen/` | 10000108 | 4 | 2 | 3 | 1 |
| SCHULKOOPERATION-LANDWIRTSCHAFTLICHEN-FACHSCHULE | `schulkooperation-landwirtschaftlichen-fachschule/` | 10000524 | 13 | 9 | 13 | 0 |
| SCHULSPRENGEL-DER-VORSCHULKLASSEN | `schulsprengel-der-vorschulklassen/` | 10000168 | 5 | 5 | 5 | 0 |
| SCHULVERSUCHSGESETZ-1989 | `schulversuchsgesetz-1989/` | 10000231 | 3 | 3 | 3 | 0 |
| SCHUTZ-DES-GRUNDWASSERS-IN-NEUDOERFL | `schutz-des-grundwassers-in-neudoerfl/` | 10000166 | 9 | 8 | 9 | 0 |
| SCHUTZGEBIET-FUER-EINE-ANERKANNTE-BELEGSTELLE | `schutzgebiet-fuer-eine-anerkannte-belegstelle/` | 20001178 | 4 | 4 | 4 | 0 |
| SCHUTZMASSNAHMEN-BETREFFEND-KLEINFEUERUNGEN | `schutzmassnahmen-betreffend-kleinfeuerungen/` | 10000411 | 14 | 14 | 14 | 0 |
| SCHUTZRAUMVERORDNUNG | `schutzraumverordnung/` | 10000177 | 15 | 15 | 15 | 0 |
| SCHUTZRAUMVERORDNUNG-0178 | `schutzraumverordnung-0178/` | 10000178 | 15 | 15 | 15 | 0 |
| Bgld. SEG 2023 | `seg-2023/` | 20001404 | 62 | 35 | 62 | 0 |
| SENIORENGESETZ-2002 | `seniorengesetz-2002/` | 20000170 | 17 | 10 | 17 | 0 |
| SENIORINNENTAGESZENTRENVERORDNUNG | `seniorinnentageszentrenverordnung/` | 20001291 | 15 | 11 | 15 | 0 |
| SEVESO-III-RICHTLINIE-ANPASSUNG | `seveso-iii-richtlinie-anpassung/` | 20001450 | 2 | 2 | 2 | 0 |
| Bgld. SGKennV | `sgkennv/` | 20001081 | 9 | 7 | 9 | 0 |
| SICHERSTELLUNG-DER-PATIENTENRECHTE | `sicherstellung-der-patientenrechte/` | 20000102 | 38 | 38 | 38 | 0 |
| SICHERUNG-DES-HEILQUELLEN-UND-MINERALWASSERVORKO | `sicherung-des-heilquellen-und-mineralwasservorko/` | 10000110 | 7 | 7 | 7 | 0 |
| SONN-UND-FEIERTAGSRUHE | `sonn-und-feiertagsruhe/` | 10000027 | 14 | 9 | 14 | 0 |
| SONN-UND-FEIERTAGSRUHE-VERORDNUNG-1997 | `sonn-und-feiertagsruhe-verordnung-1997/` | 10000468 | 3 | 3 | 3 | 0 |
| SOZIALBETREUUNGSBERUFE | `sozialbetreuungsberufe/` | 20000349 | 22 | 18 | 22 | 1 |
| SOZIALBETREUUNGSBERUFE-AENDERUNG | `sozialbetreuungsberufe-aenderung/` | 20001495 | 2 | 2 | 2 | 0 |
| SOZIALHILFE-KOSTENBEITRAGSVERORDNUNG | `sozialhilfe-kostenbeitragsverordnung/` | 20001507 | 6 | 6 | 6 | 0 |
| SPERRZEITENVERORDNUNG-1997 | `sperrzeitenverordnung-1997/` | 10000451 | 6 | 6 | 6 | 0 |
| SPG-NOVELLE-2005-UND-SPG-NOVELLE-2005 | `spg-novelle-2005-und-spg-novelle-2005/` | 20000762 | 5 | 5 | 5 | 0 |
| SPORTFOERDERUNGSGESETZ-2004 | `sportfoerderungsgesetz-2004/` | 20000258 | 25 | 14 | 25 | 0 |
| SPRENGEL-DER-POLITISCHEN-BEZIRKE-DES | `sprengel-der-politischen-bezirke-des/` | 20000617 | 9 | 9 | 9 | 0 |
| SPRENGELHEBAMMENGESETZ-AUFHEBUNG | `sprengelhebammengesetz-aufhebung/` | 20001067 | 3 | 3 | 3 | 0 |
| STANDESAMTSVERBAND-BOCKSDORF-AUSSCHEIDEN-VON-BUR | `standesamtsverband-bocksdorf-ausscheiden-von-bur/` | 10000377 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-BOCKSDORF-IN-STEGERSBACH-UMBI | `standesamtsverband-bocksdorf-in-stegersbach-umbi/` | 10000313 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-EBERAU-BILDUNG | `standesamtsverband-eberau-bildung/` | 10000321 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-ELTENDORF-BILDUNG | `standesamtsverband-eltendorf-bildung/` | 10000318 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-GRAFENSCHACHEN-BILDUNG | `standesamtsverband-grafenschachen-bildung/` | 10000229 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-KAISERSDORF-WEINGRABEN-BILDUN | `standesamtsverband-kaisersdorf-weingraben-bildun/` | 10000288 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-KOHFIDISCH-BILDUNG | `standesamtsverband-kohfidisch-bildung/` | 10000319 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-MANNERSDORF-AN-DER-RABNITZ | `standesamtsverband-mannersdorf-an-der-rabnitz/` | 10000413 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-NEUHAUS-AM-KLAUSENBACH-BILDUN | `standesamtsverband-neuhaus-am-klausenbach-bildun/` | 10000317 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-PIRINGSDORF-UNTERRABNITZ-BILD | `standesamtsverband-piringsdorf-unterrabnitz-bild/` | 10000284 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-POETTELSDORF-ZEMENDORF-STOETT | `standesamtsverband-poettelsdorf-zemendorf-stoett/` | 10000285 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-SANKT-MICHAEL-BILDUNG | `standesamtsverband-sankt-michael-bildung/` | 10000320 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-SCHACHENDORF-BILDUNG | `standesamtsverband-schachendorf-bildung/` | 10000414 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-SIGLESS-BILDUNG | `standesamtsverband-sigless-bildung/` | 10000473 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-STINATZ-AUFLOESUNG | `standesamtsverband-stinatz-aufloesung/` | 20001052 | 3 | 3 | 3 | 0 |
| STANDESAMTSVERBAND-STINATZ-UMBILDUNG | `standesamtsverband-stinatz-umbildung/` | 10000277 | 4 | 4 | 4 | 0 |
| STANDESAMTSVERBAND-STREM-BILDUNG | `standesamtsverband-strem-bildung/` | 10000381 | 4 | 4 | 4 | 0 |
| STANDESBEAMTEN-PRUEFUNGSGESETZ | `standesbeamten-pruefungsgesetz/` | 10000267 | 9 | 8 | 9 | 0 |
| STARE-VERTREIBUNGS-VERORDNUNG-2023 | `stare-vertreibungs-verordnung-2023/` | 20001416 | 8 | 8 | 8 | 0 |
| STARKSTROMWEGEGESETZ | `starkstromwegegesetz/` | 10000091 | 46 | 29 | 46 | 0 |
| STATUT-FUER-DAS-EHRENZEICHEN-DES | `statut-fuer-das-ehrenzeichen-des/` | 20001276 | 9 | 9 | 9 | 0 |
| STELLENBESETZUNGSGESETZ | `stellenbesetzungsgesetz/` | 10000516 | 5 | 5 | 5 | 0 |
| STIFTUNGS-UND-FONDSGESETZ | `stiftungs-und-fondsgesetz/` | 10000396 | 50 | 29 | 50 | 0 |
| STRASSENGESETZ-2005 | `strassengesetz-2005/` | 20000352 | 78 | 50 | 78 | 0 |
| STRASSENPOLIZEILICHE-REGELUNG-FUER-DAS-GEMEINDEG | `strassenpolizeiliche-regelung-fuer-das-gemeindeg/` | 20000354 | 2 | 2 | 2 | 0 |
| STROMKENNZEICHNUNGSVERORDNUNG | `stromkennzeichnungsverordnung/` | 20000138 | 6 | 6 | 6 | 0 |
| STROMPREISE-KLEINE-UND-MITTLERE-ELEKTRIZITAETSVE | `strompreise-kleine-und-mittlere-elektrizitaetsve/` | 10000306 | 4 | 4 | 4 | 0 |
| Bgld. SUG | `sug/` | 20001445 | 56 | 40 | 56 | 0 |
| TEILNATURSCHUTZGEBIET-BEREICH-DES-GALGENBERGES-I | `teilnaturschutzgebiet-bereich-des-galgenberges-i/` | 20000548 | 7 | 7 | 7 | 0 |
| TEILNATURSCHUTZGEBIET-BEREICH-DES-ZYLINDERTEICHE | `teilnaturschutzgebiet-bereich-des-zylinderteiche/` | 20000544 | 7 | 7 | 7 | 0 |
| TEILNATURSCHUTZGEBIET-BEREICHE-DER-RIED-BUBANJ | `teilnaturschutzgebiet-bereiche-der-ried-bubanj/` | 20000541 | 7 | 7 | 7 | 0 |
| TEILNATURSCHUTZGEBIET-FEUCHTWIESENGEBIET-BACHAUE | `teilnaturschutzgebiet-feuchtwiesengebiet-bachaue/` | 10000265 | 9 | 9 | 9 | 0 |
| TEILNATURSCHUTZGEBIET-FEUCHTWIESENGEBIET-IM-BERE | `teilnaturschutzgebiet-feuchtwiesengebiet-im-bere/` | 10000257 | 9 | 9 | 9 | 0 |
| TEILNATURSCHUTZGEBIET-GRUNDSTUECKE-IN-DER-KG | `teilnaturschutzgebiet-grundstuecke-in-der-kg/` | 20000567 | 8 | 8 | 8 | 0 |
| TEILNATURSCHUTZGEBIET-HAIDEL-IN-DER-KG | `teilnaturschutzgebiet-haidel-in-der-kg/` | 20000563 | 8 | 8 | 8 | 0 |
| TEILNATURSCHUTZGEBIET-KG-RECHNITZ | `teilnaturschutzgebiet-kg-rechnitz/` | 10000262 | 9 | 9 | 9 | 0 |
| TEILNATURSCHUTZGEBIET-RIED-FRIEDHOFSWIESEN-IN-DE | `teilnaturschutzgebiet-ried-friedhofswiesen-in-de/` | 20000547 | 7 | 7 | 7 | 0 |
| TEILNATURSCHUTZGEBIET-RIED-FRONWIESEN-UND-TEILE | `teilnaturschutzgebiet-ried-fronwiesen-und-teile/` | 20000542 | 6 | 6 | 6 | 0 |
| TEILNATURSCHUTZGEBIET-ROHRBACHER-KOGEL | `teilnaturschutzgebiet-rohrbacher-kogel/` | 20000543 | 7 | 7 | 7 | 0 |
| TEILNATURSCHUTZGEBIET-TEILE-DER-KG-LEITHAPRODERS | `teilnaturschutzgebiet-teile-der-kg-leithaproders/` | 20000571 | 9 | 9 | 9 | 0 |
| TEILNATURSCHUTZGEBIET-ZURNDORFER-EICHENWALD-UND | `teilnaturschutzgebiet-zurndorfer-eichenwald-und/` | 20000573 | 7 | 7 | 7 | 0 |
| Bgld. TG 2021 | `tg-2021/` | 20001302 | 102 | 39 | 102 | 0 |
| TIERHALTEVERBOTSVERORDNUNG | `tierhalteverbotsverordnung/` | 20001227 | 3 | 3 | 3 | 0 |
| TIERZUCHTRAT | `tierzuchtrat/` | 20000707 | 12 | 12 | 12 | 0 |
| TIERZUCHTRAT-BEITRITT-OBEROESTERREICH-UND-KAERNT | `tierzuchtrat-beitritt-oberoesterreich-und-kaernt/` | 20000725 | 2 | 2 | 2 | 0 |
| Bgld. TMV 2024 | `tmv-2024/` | 20001476 | 11 | 9 | 11 | 0 |
| TOURISMUSABGABEN-NEUFESTSETZUNG | `tourismusabgaben-neufestsetzung/` | 10000422 | 7 | 7 | 7 | 0 |
| TOURISMUSVERBAENDE-DELEGIERTE | `tourismusverbaende-delegierte/` | 20001530 | 8 | 6 | 8 | 0 |
| TOURISMUSVERBAND-BADERSDORF-AUFLOESUNG | `tourismusverband-badersdorf-aufloesung/` | 20000627 | 3 | 3 | 3 | 0 |
| TRANSPARENZDATENBANK | `transparenzdatenbank/` | 20000936 | 22 | 22 | 22 | 0 |
| TRENNUNG-DER-GEMEINDE-BOCKSDORF | `trennung-der-gemeinde-bocksdorf/` | 20000285 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-DRASSBURG-BAUMGARTEN | `trennung-der-gemeinde-drassburg-baumgarten/` | 20000301 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-EBERAU | `trennung-der-gemeinde-eberau/` | 20000280 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-ELTENDORF | `trennung-der-gemeinde-eltendorf/` | 20000282 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-GATTENDORF-NEUDORF | `trennung-der-gemeinde-gattendorf-neudorf/` | 20000288 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-GRAFENSCHACHEN | `trennung-der-gemeinde-grafenschachen/` | 20000290 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-GROSSPETERSDORF | `trennung-der-gemeinde-grosspetersdorf/` | 20000284 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-HIRM-ANTAU | `trennung-der-gemeinde-hirm-antau/` | 20000298 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-KAISERSDORF | `trennung-der-gemeinde-kaisersdorf/` | 20000295 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-KITTSEE | `trennung-der-gemeinde-kittsee/` | 20000283 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-KOHFIDISCH | `trennung-der-gemeinde-kohfidisch/` | 20000281 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-MANNERSDORF-AN | `trennung-der-gemeinde-mannersdorf-an/` | 20000292 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-NEUHAUS-AM | `trennung-der-gemeinde-neuhaus-am/` | 20000286 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-OLLERSDORF-IM | `trennung-der-gemeinde-ollersdorf-im/` | 20000297 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-PIRINGSDORF-UNTERRABNITZ | `trennung-der-gemeinde-piringsdorf-unterrabnitz/` | 20000296 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-POETTELSDORF | `trennung-der-gemeinde-poettelsdorf/` | 20000299 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-SANKT-MICHAEL | `trennung-der-gemeinde-sankt-michael/` | 20000279 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-SCHACHENDORF | `trennung-der-gemeinde-schachendorf/` | 20000293 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-SIEGENDORF-IM | `trennung-der-gemeinde-siegendorf-im/` | 20000287 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-SIGLESS | `trennung-der-gemeinde-sigless/` | 20000294 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-STEINBRUNN-ZILLINGTAL | `trennung-der-gemeinde-steinbrunn-zillingtal/` | 20000300 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-GEMEINDE-STREM | `trennung-der-gemeinde-strem/` | 20000278 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-MARKTGEMEINDE-LEITHAPRODERSDORF | `trennung-der-marktgemeinde-leithaprodersdorf/` | 20000289 | 5 | 5 | 5 | 0 |
| TRENNUNG-DER-MARKTGEMEINDE-RAIDING-UNTERFRAUENHA | `trennung-der-marktgemeinde-raiding-unterfrauenha/` | 20000291 | 5 | 5 | 5 | 0 |
| TUBERKULOSE-REIHENUNTERSUCHUNGSVERORDNUNG-2018 | `tuberkulose-reihenuntersuchungsverordnung-2018/` | 20001173 | 8 | 8 | 8 | 0 |
| TV-VO-EISENSTADT-LEITHALAND | `tv-vo-eisenstadt-leithaland/` | 20001092 | 4 | 4 | 4 | 0 |
| TV-VO-GEMEINDEN | `tv-vo-gemeinden/` | 20001050 | 4 | 4 | 4 | 0 |
| TV-VO-JENNERSDORF | `tv-vo-jennersdorf/` | 20001048 | 8 | 5 | 8 | 0 |
| TV-VO-LUTZMANNSBURG-MITTELBURGENLAND | `tv-vo-lutzmannsburg-mittelburgenland/` | 20001094 | 5 | 5 | 5 | 0 |
| TV-VO-REGION-GUESSING-UND-GOLF | `tv-vo-region-guessing-und-golf/` | 20001047 | 8 | 6 | 8 | 0 |
| TV-VO-REGION-NEUSIEDLER-SEE | `tv-vo-region-neusiedler-see/` | 20001045 | 11 | 5 | 11 | 0 |
| TV-VO-REGION-OBERWART | `tv-vo-region-oberwart/` | 20001046 | 11 | 5 | 11 | 0 |
| TV-VO-REGION-ROSALIA-NEUFELDER-SEENPLATTE | `tv-vo-region-rosalia-neufelder-seenplatte/` | 20001093 | 5 | 5 | 5 | 0 |
| TV-VO-TOURISMUSGEMEINDEN | `tv-vo-tourismusgemeinden/` | 20001049 | 4 | 4 | 4 | 0 |
| Bgld. TZG 2019 | `tzg-2019/` | 20001235 | 30 | 24 | 30 | 0 |
| Bgld. TZVO 2024 | `tzvo-2024/` | 20001455 | 20 | 20 | 20 | 0 |
| UEBERLEITUNGSREGELUNGEN-UEBER-DIE-ERRICHTUNG-DES | `ueberleitungsregelungen-ueber-die-errichtung-des/` | 20001024 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-BESTIMMTER-POLIZEILICHER-GESCHAEFTE | `uebertragung-bestimmter-polizeilicher-geschaefte/` | 10000032 | 4 | 4 | 4 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE | `uebertragung-der-besorgung-einzelner-angelegenhe/` | 10000486 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0027 | `uebertragung-der-besorgung-einzelner-angelegenhe-0027/` | 20000027 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0039 | `uebertragung-der-besorgung-einzelner-angelegenhe-0039/` | 20000039 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0310 | `uebertragung-der-besorgung-einzelner-angelegenhe-0310/` | 20000310 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0488 | `uebertragung-der-besorgung-einzelner-angelegenhe-0488/` | 10000488 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0505 | `uebertragung-der-besorgung-einzelner-angelegenhe-0505/` | 20000505 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0506 | `uebertragung-der-besorgung-einzelner-angelegenhe-0506/` | 20000506 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0507 | `uebertragung-der-besorgung-einzelner-angelegenhe-0507/` | 20000507 | 7 | 5 | 7 | 2 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0508 | `uebertragung-der-besorgung-einzelner-angelegenhe-0508/` | 20000508 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0509 | `uebertragung-der-besorgung-einzelner-angelegenhe-0509/` | 20000509 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0510 | `uebertragung-der-besorgung-einzelner-angelegenhe-0510/` | 20000510 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0512 | `uebertragung-der-besorgung-einzelner-angelegenhe-0512/` | 20000512 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0513 | `uebertragung-der-besorgung-einzelner-angelegenhe-0513/` | 20000513 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0516 | `uebertragung-der-besorgung-einzelner-angelegenhe-0516/` | 20000516 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0517 | `uebertragung-der-besorgung-einzelner-angelegenhe-0517/` | 20000517 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0518 | `uebertragung-der-besorgung-einzelner-angelegenhe-0518/` | 20000518 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0519 | `uebertragung-der-besorgung-einzelner-angelegenhe-0519/` | 20000519 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0520 | `uebertragung-der-besorgung-einzelner-angelegenhe-0520/` | 20000520 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0521 | `uebertragung-der-besorgung-einzelner-angelegenhe-0521/` | 20000521 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-EINZELNER-ANGELEGENHE-0579 | `uebertragung-der-besorgung-einzelner-angelegenhe-0579/` | 20000579 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-VON-ANGELEGENHEITEN | `uebertragung-der-besorgung-von-angelegenheiten/` | 10000326 | 2 | 2 | 2 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-VON-ANGELEGENHEITEN-0498 | `uebertragung-der-besorgung-von-angelegenheiten-0498/` | 10000498 | 3 | 2 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-VON-ANGELEGENHEITEN-0523 | `uebertragung-der-besorgung-von-angelegenheiten-0523/` | 20000523 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-VON-ANGELEGENHEITEN-0524 | `uebertragung-der-besorgung-von-angelegenheiten-0524/` | 20000524 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-DER-BESORGUNG-VON-ANGELEGENHEITEN-0951 | `uebertragung-der-besorgung-von-angelegenheiten-0951/` | 20000951 | 7 | 4 | 7 | 0 |
| UEBERTRAGUNG-EINZELNER-ANGELEGENHEITEN-DES-EIGEN | `uebertragung-einzelner-angelegenheiten-des-eigen/` | 20001405 | 3 | 3 | 3 | 0 |
| UEBERTRAGUNG-VON-BEHOERDLICHEN-ZUSTAENDIGKEITEN | `uebertragung-von-behoerdlichen-zustaendigkeiten/` | 20001574 | 4 | 4 | 4 | 0 |
| UEBETRAGUNG-DER-BESORGUNG-VON-ANGELEGENHEITEN | `uebetragung-der-besorgung-von-angelegenheiten/` | 20000515 | 3 | 3 | 3 | 0 |
| Bgld. UHG | `uhg/` | 20000761 | 32 | 21 | 32 | 0 |
| UMFAHRUNG-THERME-LUTZMANNSBURG | `umfahrung-therme-lutzmannsburg/` | 20001138 | 4 | 4 | 4 | 0 |
| UMSETZUNG-DER-EG-BAUPRODUKTENRICHTLINIE | `umsetzung-der-eg-bauproduktenrichtlinie/` | 10000349 | 35 | 35 | 35 | 0 |
| UMSETZUNG-DER-RICHTLINIE-2006-32-EG-UEBER | `umsetzung-der-richtlinie-2006-32-eg-ueber/` | 20000826 | 18 | 18 | 18 | 0 |
| UNTERSAGUNG-DER-BENUETZUNG-VON-PRIVATSCHLACHTSTA | `untersagung-der-benuetzung-von-privatschlachtsta/` | 10000050 | 4 | 4 | 4 | 0 |
| UNVEREINBARKEITSGESETZ | `unvereinbarkeitsgesetz/` | 10000005 | 10 | 10 | 10 | 0 |
| Bgld. VEMF | `vemf/` | 20001116 | 6 | 6 | 6 | 0 |
| VERANSTALTUNGSGESETZ | `veranstaltungsgesetz/` | 10000372 | 151 | 56 | 151 | 0 |
| VERBESSERUNG-DER-SICHERHEIT-DER-SCHIFFAHRT | `verbesserung-der-sicherheit-der-schiffahrt/` | 10000456 | 6 | 6 | 6 | 0 |
| VERBOT-DER-ABGABE-VON-MOLKE | `verbot-der-abgabe-von-molke/` | 20000779 | 2 | 2 | 2 | 0 |
| VERBOT-DER-ABGABE-VON-MOLKE-0780 | `verbot-der-abgabe-von-molke-0780/` | 20000780 | 4 | 3 | 4 | 0 |
| VERBOT-DES-BEFAHRENS-UND-STILLLIEGENS | `verbot-des-befahrens-und-stillliegens/` | 20000129 | 5 | 5 | 5 | 0 |
| VERBOT-DES-VERKAUFES-DES-FLEISCHES | `verbot-des-verkaufes-des-fleisches/` | 10000186 | 4 | 4 | 4 | 0 |
| VERBOT-DES-VERKAUFES-VON-KAESE | `verbot-des-verkaufes-von-kaese/` | 10000191 | 4 | 4 | 4 | 0 |
| VERBOT-DES-VERKAUFES-VON-MILCHERZEUGNISSEN | `verbot-des-verkaufes-von-milcherzeugnissen/` | 10000190 | 3 | 3 | 3 | 0 |
| VERBOT-DES-VERKAUFES-VON-SCHAF | `verbot-des-verkaufes-von-schaf/` | 10000182 | 6 | 5 | 6 | 0 |
| VERBRENNEN-VON-MIT-FEUERBRAND-BEFALLENEN | `verbrennen-von-mit-feuerbrand-befallenen/` | 10000541 | 3 | 3 | 3 | 0 |
| VEREINBARUNG-UEBER-DEN-AUSBAU-DES | `vereinbarung-ueber-den-ausbau-des/` | 20001005 | 3 | 3 | 3 | 0 |
| VEREINBARUNG-UEBER-DEN-KOSTENERSATZ-IN | `vereinbarung-ueber-den-kostenersatz-in/` | 20001135 | 2 | 2 | 2 | 0 |
| VEREINBARUNG-UEBER-DIE-ANWENDUNG-UND | `vereinbarung-ueber-die-anwendung-und/` | 20001528 | 6 | 6 | 6 | 0 |
| VEREINBARUNG-UEBER-DIE-KINDER-UND | `vereinbarung-ueber-die-kinder-und/` | 20001245 | 8 | 8 | 8 | 0 |
| VEREINBARUNGEN-UEBER-DEN-AUSBAU-GANZTAEGIGER | `vereinbarungen-ueber-den-ausbau-ganztaegiger/` | 20001013 | 4 | 4 | 4 | 0 |
| Bgld. VergRSG | `vergrsg/` | 20000601 | 96 | 33 | 96 | 0 |
| VERKAUF-VON-CHRISTBAEUMEN-AN-BESTIMMTEN | `verkauf-von-christbaeumen-an-bestimmten/` | 10000170 | 3 | 3 | 3 | 0 |
| VERKAUFSSTELLEN-IN-DER-MARKTGEMEINDE-HEILIGENKRE | `verkaufsstellen-in-der-marktgemeinde-heiligenkre/` | 10000245 | 2 | 2 | 2 | 0 |
| VERKAUFSTAETIGKEITEN-AN-WOCHENENDEN | `verkaufstaetigkeiten-an-wochenenden/` | 20001467 | 8 | 6 | 8 | 0 |
| VERLAENGERUNG-DER-ANPASSUNGSFRIST-FUER-DAS | `verlaengerung-der-anpassungsfrist-fuer-das/` | 20000246 | 5 | 5 | 5 | 0 |
| VERLAENGERUNG-DER-AUSNAHME-VON-DER | `verlaengerung-der-ausnahme-von-der/` | 20000367 | 7 | 7 | 7 | 0 |
| VERLAENGERUNG-DER-EISENBAHNZUFAHRTSSTRASSE-IN-RE | `verlaengerung-der-eisenbahnzufahrtsstrasse-in-re/` | 20000578 | 2 | 2 | 2 | 0 |
| VERLAENGERUNG-DER-FINANZAUSGLEICHSPERIODE-BIS-EN | `verlaengerung-der-finanzausgleichsperiode-bis-en/` | 20001396 | 6 | 6 | 6 | 0 |
| VERLAUF-DER-L-274-ZUFAHRT | `verlauf-der-l-274-zufahrt/` | 20001364 | 4 | 4 | 4 | 0 |
| VERLAUF-DER-STAATSGRENZE-ZWISCHEN-DER | `verlauf-der-staatsgrenze-zwischen-der/` | 20000641 | 11 | 11 | 11 | 0 |
| VERLAUF-UND-BERICHTIGUNGEN-DER-STAATSGRENZE | `verlauf-und-berichtigungen-der-staatsgrenze/` | 10000234 | 9 | 9 | 9 | 0 |
| Bgld. VerlautG 2015 | `verlautg-2015/` | 20001010 | 29 | 18 | 29 | 0 |
| VERLEGUNG-DES-KRAEMERMARKTES-IN-DER | `verlegung-des-kraemermarktes-in-der/` | 10000051 | 2 | 2 | 2 | 0 |
| VERLEGUNG-DES-STRASSENVERLAUFES-DER-B | `verlegung-des-strassenverlaufes-der-b/` | 20001213 | 4 | 4 | 4 | 0 |
| VERLEGUNG-DES-STRASSENVERLAUFES-DER-L | `verlegung-des-strassenverlaufes-der-l/` | 20001599 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG | `verleihung-des-rechtes-zur-fuehrung/` | 20000036 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0158 | `verleihung-des-rechtes-zur-fuehrung-0158/` | 20000158 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0207 | `verleihung-des-rechtes-zur-fuehrung-0207/` | 20000207 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0270 | `verleihung-des-rechtes-zur-fuehrung-0270/` | 20000270 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0273 | `verleihung-des-rechtes-zur-fuehrung-0273/` | 20000273 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0302 | `verleihung-des-rechtes-zur-fuehrung-0302/` | 20000302 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0305 | `verleihung-des-rechtes-zur-fuehrung-0305/` | 20000305 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0306 | `verleihung-des-rechtes-zur-fuehrung-0306/` | 20000306 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0386 | `verleihung-des-rechtes-zur-fuehrung-0386/` | 20000386 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0387 | `verleihung-des-rechtes-zur-fuehrung-0387/` | 20000387 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0388 | `verleihung-des-rechtes-zur-fuehrung-0388/` | 20000388 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0389 | `verleihung-des-rechtes-zur-fuehrung-0389/` | 20000389 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0390 | `verleihung-des-rechtes-zur-fuehrung-0390/` | 20000390 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0391 | `verleihung-des-rechtes-zur-fuehrung-0391/` | 20000391 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0392 | `verleihung-des-rechtes-zur-fuehrung-0392/` | 20000392 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0393 | `verleihung-des-rechtes-zur-fuehrung-0393/` | 20000393 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0394 | `verleihung-des-rechtes-zur-fuehrung-0394/` | 20000394 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0395 | `verleihung-des-rechtes-zur-fuehrung-0395/` | 20000395 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0397 | `verleihung-des-rechtes-zur-fuehrung-0397/` | 20000397 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0398 | `verleihung-des-rechtes-zur-fuehrung-0398/` | 20000398 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0399 | `verleihung-des-rechtes-zur-fuehrung-0399/` | 20000399 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0400 | `verleihung-des-rechtes-zur-fuehrung-0400/` | 20000400 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0401 | `verleihung-des-rechtes-zur-fuehrung-0401/` | 20000401 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0402 | `verleihung-des-rechtes-zur-fuehrung-0402/` | 20000402 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0403 | `verleihung-des-rechtes-zur-fuehrung-0403/` | 20000403 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0404 | `verleihung-des-rechtes-zur-fuehrung-0404/` | 20000404 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0405 | `verleihung-des-rechtes-zur-fuehrung-0405/` | 20000405 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0406 | `verleihung-des-rechtes-zur-fuehrung-0406/` | 20000406 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0407 | `verleihung-des-rechtes-zur-fuehrung-0407/` | 20000407 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0408 | `verleihung-des-rechtes-zur-fuehrung-0408/` | 20000408 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0409 | `verleihung-des-rechtes-zur-fuehrung-0409/` | 20000409 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0410 | `verleihung-des-rechtes-zur-fuehrung-0410/` | 20000410 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0411 | `verleihung-des-rechtes-zur-fuehrung-0411/` | 20000411 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0412 | `verleihung-des-rechtes-zur-fuehrung-0412/` | 20000412 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0413 | `verleihung-des-rechtes-zur-fuehrung-0413/` | 20000413 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0414 | `verleihung-des-rechtes-zur-fuehrung-0414/` | 20000414 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0415 | `verleihung-des-rechtes-zur-fuehrung-0415/` | 20000415 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0416 | `verleihung-des-rechtes-zur-fuehrung-0416/` | 20000416 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0417 | `verleihung-des-rechtes-zur-fuehrung-0417/` | 20000417 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0418 | `verleihung-des-rechtes-zur-fuehrung-0418/` | 20000418 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0419 | `verleihung-des-rechtes-zur-fuehrung-0419/` | 20000419 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0422 | `verleihung-des-rechtes-zur-fuehrung-0422/` | 20000422 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0423 | `verleihung-des-rechtes-zur-fuehrung-0423/` | 20000423 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0424 | `verleihung-des-rechtes-zur-fuehrung-0424/` | 20000424 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0425 | `verleihung-des-rechtes-zur-fuehrung-0425/` | 20000425 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0426 | `verleihung-des-rechtes-zur-fuehrung-0426/` | 20000426 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0487 | `verleihung-des-rechtes-zur-fuehrung-0487/` | 20000487 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0638 | `verleihung-des-rechtes-zur-fuehrung-0638/` | 20000638 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0735 | `verleihung-des-rechtes-zur-fuehrung-0735/` | 20000735 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0909 | `verleihung-des-rechtes-zur-fuehrung-0909/` | 20000909 | 2 | 2 | 2 | 0 |
| VERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-1521 | `verleihung-des-rechtes-zur-fuehrung-1521/` | 20001521 | 3 | 3 | 3 | 0 |
| VERLEIHUNG-DES-RECHTS-ZUR-FUEHRUNG | `verleihung-des-rechts-zur-fuehrung/` | 20000614 | 2 | 2 | 2 | 0 |
| VERMOEGENSRECHTSNACHFOLGE-NACH-DER-AUFLOESUNG-DE | `vermoegensrechtsnachfolge-nach-der-aufloesung-de/` | 20001374 | 4 | 4 | 4 | 0 |
| VERMOEGENSWERTE-NACH-DEN-EHEMALIGEN-LANDKREISEN | `vermoegenswerte-nach-den-ehemaligen-landkreisen/` | 10000087 | 7 | 7 | 7 | 0 |
| VERORDNUNG-DER-GEMEINDE-OBERSCHUETZEN-MIT | `verordnung-der-gemeinde-oberschuetzen-mit/` | 20000716 | 2 | 2 | 2 | 0 |
| VERORDNUNG-DER-MARKTGEMEINDE-GROSSPETERSDORF-AUF | `verordnung-der-marktgemeinde-grosspetersdorf-auf/` | 20001218 | 2 | 2 | 2 | 0 |
| VERORDNUNG-DES-BUERGERMEISTERS-DER-GEMEINDE | `verordnung-des-buergermeisters-der-gemeinde/` | 20001320 | 2 | 2 | 2 | 0 |
| VERORDNUNG-DES-GEMEINDERATES-DER-STADTGEMEINDE | `verordnung-des-gemeinderates-der-stadtgemeinde/` | 20000697 | 2 | 2 | 2 | 0 |
| VERORDNUNG-DES-GEMEINDERATES-DER-STADTGEMEINDE-1532 | `verordnung-des-gemeinderates-der-stadtgemeinde-1532/` | 20001532 | 2 | 2 | 2 | 0 |
| VERORDNUNG-UEBER-DIE-AUFTEILUNG-VON | `verordnung-ueber-die-aufteilung-von/` | 10000526 | 3 | 3 | 3 | 0 |
| VERORDNUNG-UEBER-DIE-SCHUL-UND | `verordnung-ueber-die-schul-und/` | 20000084 | 16 | 16 | 16 | 0 |
| VERORDNUNG-UEBER-DIE-ZUR-LEICHENUEBERFUEHRUNG | `verordnung-ueber-die-zur-leichenueberfuehrung/` | 20000875 | 6 | 6 | 6 | 0 |
| VERTRAGSSCHABLONEN-GEMAESS-DEM-BURGENLAENDISCHEN | `vertragsschablonen-gemaess-dem-burgenlaendischen/` | 20001259 | 10 | 6 | 10 | 0 |
| VERWALTUNG-DER-BEZIRKS-UND-EISENBAHNZUFAHRTSSTRA | `verwaltung-der-bezirks-und-eisenbahnzufahrtsstra/` | 10000010 | 14 | 14 | 14 | 0 |
| VERWALTUNGS-UND-KONTROLLSYSTEM-IN-OESTERREICH | `verwaltungs-und-kontrollsystem-in-oesterreich/` | 20000673 | 20 | 20 | 20 | 0 |
| VERWALTUNGS-UND-KONTROLLSYSTEM-IN-OESTERREICH-1132 | `verwaltungs-und-kontrollsystem-in-oesterreich-1132/` | 20001132 | 21 | 21 | 21 | 0 |
| VERWALTUNGS-UND-KONTROLLSYSTEM-IN-OESTERREICH-1378 | `verwaltungs-und-kontrollsystem-in-oesterreich-1378/` | 20001378 | 21 | 21 | 21 | 0 |
| VERZEICHNIS-DER-GEMEINDE-SONDERWAHLBEHOERDEN-BEI | `verzeichnis-der-gemeinde-sonderwahlbehoerden-bei/` | 10000159 | 3 | 3 | 3 | 0 |
| VETERINAERPOLIZEILICHE-VORSCHRIFTEN-PFERDE | `veterinaerpolizeiliche-vorschriften-pferde/` | 10000015 | 2 | 2 | 2 | 0 |
| VETERINAERPOLIZEILICHE-VORSCHRIFTEN-ZUCHT-UND-NU | `veterinaerpolizeiliche-vorschriften-zucht-und-nu/` | 10000014 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DER-PARPAR | `vfgh-aufhebung-der-parpar/` | 20001193 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DER-PARPAR-1214 | `vfgh-aufhebung-der-parpar-1214/` | 20001214 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DER-PARPAR-1391 | `vfgh-aufhebung-der-parpar-1391/` | 20001391 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DER-VERORDNUNG | `vfgh-aufhebung-der-verordnung/` | 20000329 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DER-VERORDNUNG-1600 | `vfgh-aufhebung-der-verordnung-1600/` | 20001600 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DER-WORTE | `vfgh-aufhebung-der-worte/` | 20001542 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR | `vfgh-aufhebung-des-par/` | 20000332 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR-0593 | `vfgh-aufhebung-des-par-0593/` | 20000593 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR-0619 | `vfgh-aufhebung-des-par-0619/` | 20000619 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR-0721 | `vfgh-aufhebung-des-par-0721/` | 20000721 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR-0868 | `vfgh-aufhebung-des-par-0868/` | 20000868 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR-1283 | `vfgh-aufhebung-des-par-1283/` | 20001283 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR-1305 | `vfgh-aufhebung-des-par-1305/` | 20001305 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-DES-PAR-1397 | `vfgh-aufhebung-des-par-1397/` | 20001397 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-EINER-VERORDNUNG | `vfgh-aufhebung-einer-verordnung/` | 20000333 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-EINER-WORTFOLGE | `vfgh-aufhebung-einer-wortfolge/` | 20000605 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-EINER-WORTFOLGE-0606 | `vfgh-aufhebung-einer-wortfolge-0606/` | 20000606 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-EINER-WORTFOLGE-0690 | `vfgh-aufhebung-einer-wortfolge-0690/` | 20000690 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-EINER-WORTFOLGE-1448 | `vfgh-aufhebung-einer-wortfolge-1448/` | 20001448 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-EINES-SATZES | `vfgh-aufhebung-eines-satzes/` | 20000740 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-FAHRVERBOT-VERBINDUNGSWEG | `vfgh-aufhebung-fahrverbot-verbindungsweg/` | 20000369 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-TEILBEBAUUNGSPLAN-ORTSKERN | `vfgh-aufhebung-teilbebauungsplan-ortskern/` | 20001028 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-VON-PUNKT | `vfgh-aufhebung-von-punkt/` | 20001571 | 2 | 2 | 2 | 0 |
| VFGH-AUFHEBUNG-VON-TEILEN | `vfgh-aufhebung-von-teilen/` | 20001428 | 2 | 2 | 2 | 0 |
| VFGH-AUSSPRUCH-BETREFFEND-GESETZWIDRIGKEIT | `vfgh-ausspruch-betreffend-gesetzwidrigkeit/` | 20001590 | 2 | 2 | 2 | 0 |
| VFGH-AUSSPRUCH-DES-VERFASSUNGSGERICHTSHOFES | `vfgh-ausspruch-des-verfassungsgerichtshofes/` | 10000137 | 2 | 2 | 2 | 0 |
| VFGH-GESETZWIDRIGKEIT-VON-VERORDNUNGEN | `vfgh-gesetzwidrigkeit-von-verordnungen/` | 20001377 | 2 | 2 | 2 | 0 |
| VFGH-PAR-36-ABS | `vfgh-par-36-abs/` | 20000720 | 2 | 2 | 2 | 0 |
| VFGH-TEILWEISE-AUFHEBUNG-DER | `vfgh-teilweise-aufhebung-der/` | 20001134 | 2 | 2 | 2 | 0 |
| VFHG-AUFHEBUNG-EINER-WORTFOLGE | `vfhg-aufhebung-einer-wortfolge/` | 20001541 | 2 | 2 | 2 | 0 |
| VIGNETTE-FUER-DIE-ENTRICHTUNG-DES | `vignette-fuer-die-entrichtung-des/` | 20001375 | 5 | 5 | 5 | 0 |
| VOLKSABSTIMMUNGSGESETZ | `volksabstimmungsgesetz/` | 10000148 | 80 | 37 | 79 | 2 |
| VOLKSBEFRAGUNG-IM-BEZIRK-GUESSING | `volksbefragung-im-bezirk-guessing/` | 20001313 | 5 | 5 | 5 | 0 |
| VOLKSBEFRAGUNGSGESETZ | `volksbefragungsgesetz/` | 10000146 | 80 | 33 | 79 | 2 |
| VOLKSBEGEHRENSGESETZ | `volksbegehrensgesetz/` | 10000147 | 69 | 33 | 68 | 2 |
| VOLLNATURSCHUTZGEBIET-BEREICH-DER-RIED-PFARRWIES | `vollnaturschutzgebiet-bereich-der-ried-pfarrwies/` | 20000550 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DER-FUCHSLOCHLACKE | `vollnaturschutzgebiet-gebiet-der-fuchslochlacke/` | 20000555 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DER-LAFNITZ-STOEGER | `vollnaturschutzgebiet-gebiet-der-lafnitz-stoeger/` | 10000247 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DER-LANGEN-LACKE | `vollnaturschutzgebiet-gebiet-der-langen-lacke/` | 20000554 | 8 | 7 | 7 | 1 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DER-NEUBRUCHLACKE-I | `vollnaturschutzgebiet-gebiet-der-neubruchlacke-i/` | 20000540 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DER-WOERTENLACKE-IN | `vollnaturschutzgebiet-gebiet-der-woertenlacke-in/` | 20000561 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DES-HACKELSBERGES-I | `vollnaturschutzgebiet-gebiet-des-hackelsberges-i/` | 20000539 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DES-ILLMITZER-ZICKS | `vollnaturschutzgebiet-gebiet-des-illmitzer-zicks/` | 20000558 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DES-JUNGER-BERGES-I | `vollnaturschutzgebiet-gebiet-des-junger-berges-i/` | 20000560 | 6 | 6 | 6 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DES-KIRCHSEES-IN | `vollnaturschutzgebiet-gebiet-des-kirchsees-in/` | 20000556 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DES-OBEREN-STINKERS | `vollnaturschutzgebiet-gebiet-des-oberen-stinkers/` | 20000557 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GEBIET-DES-UNTEREN-STINKER | `vollnaturschutzgebiet-gebiet-des-unteren-stinker/` | 20000559 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-GOLDBERG-SCHUETZENER-KOGEL | `vollnaturschutzgebiet-goldberg-schuetzener-kogel/` | 20000545 | 5 | 5 | 5 | 0 |
| VOLLNATURSCHUTZGEBIET-GROSSBACHGRABEN-IN-DER-KG | `vollnaturschutzgebiet-grossbachgraben-in-der-kg/` | 20000549 | 8 | 8 | 8 | 0 |
| VOLLNATURSCHUTZGEBIET-GRUNDSTUECK-NR-6497-DER | `vollnaturschutzgebiet-grundstueck-nr-6497-der/` | 20000552 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-HANS-G | `vollnaturschutzgebiet-hans-g/` | 10000388 | 3 | 3 | 3 | 0 |
| VOLLNATURSCHUTZGEBIET-RIEDE-IN-DER-KG | `vollnaturschutzgebiet-riede-in-der-kg/` | 20000553 | 15 | 8 | 8 | 7 |
| VOLLNATURSCHUTZGEBIET-TEIL-DER-ZITZMANNSDORFER-W | `vollnaturschutzgebiet-teil-der-zitzmannsdorfer-w/` | 20000572 | 7 | 7 | 7 | 0 |
| VOLLNATURSCHUTZGEBIET-THENAU-IN-DER-KG | `vollnaturschutzgebiet-thenau-in-der-kg/` | 20000551 | 8 | 8 | 8 | 0 |
| VORAUSSETZUNGEN-FUER-DIE-UEBERNAHME-VON | `voraussetzungen-fuer-die-uebernahme-von/` | 20000895 | 11 | 11 | 11 | 0 |
| VORNAHME-DER-TIERAERZTLICHEN-UNTERSUCHUNG-BEI | `vornahme-der-tieraerztlichen-untersuchung-bei/` | 10000039 | 37 | 29 | 37 | 0 |
| VORSCHRIFTEN-UEBER-DIE-BEFOERDERUNG-VON | `vorschriften-ueber-die-befoerderung-von/` | 10000036 | 2 | 2 | 2 | 0 |
| VORZEITIGE-BEENDIGUNG-DER-XVII-GESETZGEBUNGSPERI | `vorzeitige-beendigung-der-xvii-gesetzgebungsperi/` | 20000064 | 3 | 3 | 3 | 0 |
| WAEHLEREVIDENZ-GESETZ | `waehlerevidenz-gesetz/` | 10000426 | 56 | 21 | 55 | 3 |
| WAERMESCHUTZ-UND-HEIZUNGSVERORDNUNG | `waermeschutz-und-heizungsverordnung/` | 10000157 | 13 | 13 | 13 | 0 |
| WAERMESCHUTZ-UND-HEIZUNGSVERORDNUNG-0161 | `waermeschutz-und-heizungsverordnung-0161/` | 10000161 | 13 | 13 | 13 | 0 |
| WAHLKARTENVERORDNUNG-2012 | `wahlkartenverordnung-2012/` | 20000890 | 30 | 11 | 30 | 0 |
| WASHINGTONER-ARTENSCHUTZUEBEREINKOMMEN | `washingtoner-artenschutzuebereinkommen/` | 10000249 | 16 | 12 | 15 | 1 |
| Bgld. WbfbtG | `wbfbtg/` | 20001159 | 3 | 3 | 3 | 0 |
| WEB-ZUGAENGLICHKEITS-VERORDNUNG | `web-zugaenglichkeits-verordnung/` | 20001219 | 6 | 4 | 6 | 0 |
| Bgld. WeinbauG 2019 | `weinbaug-2019/` | 20001242 | 31 | 18 | 31 | 0 |
| WEINBAUGESETZ-2001 | `weinbaugesetz-2001/` | 20000157 | 31 | 19 | 31 | 0 |
| WEINBAUVERORDNUNG-2020 | `weinbauverordnung-2020/` | 20001267 | 4 | 4 | 4 | 0 |
| WEITERER-AUSBAU-GANZTAEGIGER-SCHULFORMEN | `weiterer-ausbau-ganztaegiger-schulformen/` | 20000948 | 13 | 11 | 13 | 0 |
| WEITERER-AUSBAU-GANZTAEGIGER-SCHULFORMEN-LAENDER | `weiterer-ausbau-ganztaegiger-schulformen-laender/` | 20000977 | 2 | 2 | 2 | 0 |
| WEITERVERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG | `weiterverleihung-des-rechtes-zur-fuehrung/` | 20000420 | 3 | 3 | 3 | 0 |
| WEITERVERLEIHUNG-DES-RECHTES-ZUR-FUEHRUNG-0421 | `weiterverleihung-des-rechtes-zur-fuehrung-0421/` | 20000421 | 3 | 3 | 3 | 0 |
| WERT-BAULANDGRUNDSTUECKE-FUER-GEMEINDEN | `wert-baulandgrundstuecke-fuer-gemeinden/` | 20001533 | 4 | 4 | 4 | 0 |
| Bgld. WFG 2018 | `wfg-2018/` | 20001187 | 31 | 25 | 31 | 0 |
| WIEDERERRICHTUNG-DER-ORTSGEMEINDE-KAISERSTEINBRU | `wiedererrichtung-der-ortsgemeinde-kaisersteinbru/` | 20001026 | 3 | 3 | 3 | 0 |
| WiföG | `wifoeg/` | 10000371 | 38 | 16 | 38 | 0 |
| WILDSCHADENSERMITTLUNGSVERORDNUNG | `wildschadensermittlungsverordnung/` | 20001148 | 27 | 27 | 27 | 0 |
| WILDSTANDREGULIERUNGSVERORDNUNG | `wildstandregulierungsverordnung/` | 20001125 | 34 | 15 | 34 | 0 |
| Bgld. WKSchG 2024 | `wkschg-2024/` | 20001468 | 19 | 19 | 19 | 0 |
| WohnVergV 2016 | `wohnvergv-2016/` | 20001064 | 11 | 11 | 11 | 0 |
| ZAHL-DER-AUF-JEDEN-WAHLKREIS | `zahl-der-auf-jeden-wahlkreis/` | 20000314 | 3 | 3 | 3 | 0 |
| ZAHL-DER-AUF-JEDEN-WAHLKREIS-0957 | `zahl-der-auf-jeden-wahlkreis-0957/` | 20000957 | 3 | 3 | 3 | 0 |
| ZAHL-DER-AUF-JEDEN-WAHLKREIS-1415 | `zahl-der-auf-jeden-wahlkreis-1415/` | 20001415 | 3 | 3 | 3 | 0 |
| ZIELSTEUERUNG-GESUNDHEIT | `zielsteuerung-gesundheit/` | 20001502 | 32 | 32 | 32 | 0 |
| ZIVILRECHTLICHE-BESTIMMUNGEN-BETREFFEND-DEN-VERK | `zivilrechtliche-bestimmungen-betreffend-den-verk/` | 20000340 | 4 | 4 | 4 | 0 |
| ZIVILRECHTLICHE-BESTIMMUNGEN-BETREFFEND-DEN-VERK-0732 | `zivilrechtliche-bestimmungen-betreffend-den-verk-0732/` | 20000732 | 4 | 4 | 4 | 0 |
| ZONIERUNG-FUER-WINDKRAFTANLAGEN-IM-BURGENLAND | `zonierung-fuer-windkraftanlagen-im-burgenland/` | 20001399 | 16 | 6 | 16 | 0 |
| ZUORDNUNG-DER-GEMEINDEN-ZUM-TOURISMUSVERBAND | `zuordnung-der-gemeinden-zum-tourismusverband/` | 20001555 | 3 | 3 | 3 | 0 |
| ZUORDNUNG-DER-GEMEINDEN-ZUM-TOURISMUSVERBAND-1556 | `zuordnung-der-gemeinden-zum-tourismusverband-1556/` | 20001556 | 3 | 3 | 3 | 0 |
| ZUORDNUNG-DER-GEMEINDEN-ZUM-TOURISMUSVERBAND-1557 | `zuordnung-der-gemeinden-zum-tourismusverband-1557/` | 20001557 | 3 | 3 | 3 | 0 |
| ZURUECKNAHME-DER-ANERKENNUNG-DER-VITA-QUELLE | `zuruecknahme-der-anerkennung-der-vita-quelle/` | 10000068 | 2 | 2 | 2 | 0 |
| ZUSAETZLICHE-MASSNAHMEN-ZUR-BEKAEMPFUNG-DER | `zusaetzliche-massnahmen-zur-bekaempfung-der/` | 20001293 | 3 | 3 | 3 | 0 |
| ZUSAMMENARBEIT-IM-BAUWESEN-SOWIE-DIE | `zusammenarbeit-im-bauwesen-sowie-die/` | 20000945 | 34 | 34 | 34 | 0 |
| ZUSAMMENARBEIT-IM-BEREICH-DER-STATISTIK | `zusammenarbeit-im-bereich-der-statistik/` | 10000179 | 10 | 10 | 10 | 0 |
| ZUSAMMENARBEIT-IM-BEREICH-DER-VERKEHRSDATENINFRA | `zusammenarbeit-im-bereich-der-verkehrsdateninfra/` | 20001055 | 8 | 8 | 8 | 0 |
| ZUSAMMENARBEIT-VERKEHRSDATENINFRASTRUKTUR-DURCH | `zusammenarbeit-verkehrsdateninfrastruktur-durch/` | 20001058 | 2 | 2 | 2 | 0 |
| ZUSCHLAGSVERORDNUNG-2002 | `zuschlagsverordnung-2002/` | 20000169 | 4 | 4 | 4 | 0 |
| ZUSTAENDIGKEITEN-DER-BILDUNGSDIREKTION-FUER-BURG | `zustaendigkeiten-der-bildungsdirektion-fuer-burg/` | 20001282 | 4 | 4 | 4 | 0 |
| ZUWEISUNG-ABGETRENNTER-GRUNDFLAECHEN-AN-BURGENLA | `zuweisung-abgetrennter-grundflaechen-an-burgenla/` | 20001025 | 3 | 3 | 3 | 0 |
| ZUWEISUNG-DEM-LAND-BURGENLAND-ZUFALLENDEN | `zuweisung-dem-land-burgenland-zufallenden/` | 20000581 | 4 | 4 | 4 | 0 |
| ZUWEISUNG-DER-DEM-LAND-BURGENLAND | `zuweisung-der-dem-land-burgenland/` | 20000503 | 3 | 3 | 3 | 0 |
| ZUWEISUNG-DER-DEM-LAND-BURGENLAND-0504 | `zuweisung-der-dem-land-burgenland-0504/` | 20000504 | 5 | 5 | 5 | 0 |
| ZUWEISUNG-VON-DER-UNGARISCHEN-GEMEINDE | `zuweisung-von-der-ungarischen-gemeinde/` | 20000483 | 2 | 2 | 2 | 0 |
| ZUWEISUNG-VON-DER-UNGARISCHEN-GEMEINDE-0484 | `zuweisung-von-der-ungarischen-gemeinde-0484/` | 20000484 | 2 | 2 | 2 | 0 |
| ZUWEISUNG-VON-GEBIETSTEILE-AN-DIE | `zuweisung-von-gebietsteile-an-die/` | 20000646 | 4 | 4 | 4 | 0 |
| ZUWEISUNG-VON-GEBIETSTEILEN-AN-DIE | `zuweisung-von-gebietsteilen-an-die/` | 20001336 | 4 | 4 | 4 | 0 |
| ZUWEISUNG-VON-UNGARISCHEN-GEMEINDEN-ABGETRENNTEN | `zuweisung-von-ungarischen-gemeinden-abgetrennten/` | 20000485 | 2 | 2 | 2 | 0 |

## Commits

- **2908** law-day commits on `main` (from `1919-09-01` to `2026-11-10`) + 1 documentation commit.
- **0** future law-day commits on `future` (for amendments promulgated in the Gazette with an `In-force` date after `2026-11-13`).

## Attribution & Licence

Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter CC BY 4.0.
Repository structure, commit history, tables and tools: CC0 1.0 Universal (see [`LICENSE`](LICENSE)).
