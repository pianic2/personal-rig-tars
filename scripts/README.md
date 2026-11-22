# Scripts

## 3D upstream inventory (RTARS-27)

`verify_3d_models.py` inventories local source files, safely extracts ZIP members to an explicit temporary work directory, hashes archive/member content, inspects standalone and archived 3MF object/mesh metadata, and can compare a regenerated result with the committed manifest. It uses only Python's standard library. Upstream geometry stays ignored and outside version control.

```sh
python3 -m unittest discover -s scripts -p 'test*.py' -v
python3 scripts/verify_3d_models.py --upstream assets/3d/upstream --extract-dir /tmp/rtars27-extract --manifest docs/manufacturing/MODEL_MANIFEST.json
python3 scripts/verify_3d_models.py --upstream assets/3d/upstream --extract-dir /tmp/rtars27-check --manifest docs/manufacturing/MODEL_MANIFEST.json --check-manifest
```

See `docs/manufacturing/MODEL_VERIFICATION.md` for the interpretation and limits of the results.

Script riproducibili per sviluppo e validazione. Documentare prerequisiti, parametri ed effetti collaterali.

- `validate_rtars18.py`: preflight dry-run per il firmware TARS Global, fissato a `rig_tars_rl` `456e3ee95ccbe94deae9484568719e8686b4b68b`. Uso, modalità build/probe/flash, conferma richiesta e privacy: [procedura RTARS-18](../docs/firmware/AUTOMATED_VALIDATION.md). Flash e probe sono opt-in; la scrittura richiede porta rilevata, preflight superato, lock dipendenze e frase di conferma.
