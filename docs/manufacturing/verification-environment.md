# RTARS-27 — Ambiente ed esecuzione

- Data verifica: 2026-11-22 (Europe/Rome).
- Interprete: Python 3.13.
- Dipendenze runtime aggiunte: nessuna; script e test usano la libreria standard.
- Test: `python3 -m unittest discover -s scripts -p 'test*.py' -v` — 27/27 PASS.
- `python3 -m py_compile scripts/verify_3d_models.py scripts/test_verify_3d_models.py` — PASS.
- Generazione manifest sull'upstream locale — PASS; 3MF package/grafo/mesh tutti PASS, nessun issue.
- Confronto rigenerato `--check-manifest` — PASS, hash e JSON corrispondenti.
- `git diff --check` — PASS.
- Input: archivio ZIP SHA-256 `73f824fa02f36a52d28e1931989fcd17b53dbbba5dd7d9e73a874f45c8ca7fa9`; 3MF SHA-256 `42912423fb2d91076ccc4721f9568fff6115fe686e7e3e51ca7572c15b5bc7c7`.
- Estrazioni di verifica: directory indipendenti sotto `/tmp/rtars27-*`; nessuna scrittura in `assets/3d/upstream/`.
- Pagina MakerWorld: accesso diretto non riuscito, Cloudflare HTTP 403; autore, cronologia/revisione e licenza non verificati indipendentemente.

I risultati sono riferiti all'input locale hashato. I metadata locali e l'attestazione del proprietario non sostituiscono una verifica del file pubblicato o della licenza sul sito primario. Il manifest esclude data, ambiente e percorsi temporanei per restare deterministico.
