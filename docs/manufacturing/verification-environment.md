# RTARS-27 — Ambiente ed esecuzione

- Data verifica: 2026-11-22 (Europe/Rome, data del task).
- Interprete: Python 3.13 (ambiente locale).
- Dipendenze aggiunte: nessuna; lo script usa solo la libreria standard.
- Estrazione e ripetizione indipendente: directory temporanee sotto `/tmp/rtars27-extract/`.
- Esito: test unitari `7/7 PASS`; rigenerazione manifest `PASS`; confronto manifest `--check-manifest` `PASS`.
- Input: ZIP SHA-256 `73f824fa02f36a52d28e1931989fcd17b53dbbba5dd7d9e73a874f45c8ca7fa9`; 3MF SHA-256 `42912423fb2d91076ccc4721f9568fff6115fe686e7e3e51ca7572c15b5bc7c7`.
- L'ambiente Python registrato è quello usato per i test e la generazione locale; l'archivio e il suo 3MF sono rimasti fuori dal versionamento.
