# Scripts

## 3D upstream inventory (RTARS-27)

`verify_3d_models.py` inventories local source files, safely extracts ZIP members to an explicit temporary work directory, hashes archive/member content, inspects 3MF object and mesh metadata, and can compare a regenerated result with the committed manifest. It uses only Python's standard library. Upstream geometry stays ignored and outside version control.

```sh
python3 -m unittest scripts/test_verify_3d_models.py -v
python3 scripts/verify_3d_models.py --upstream assets/3d/upstream --extract-dir /tmp/rtars27-extract --manifest docs/manufacturing/MODEL_MANIFEST.json
python3 scripts/verify_3d_models.py --upstream assets/3d/upstream --extract-dir /tmp/rtars27-check --manifest docs/manufacturing/MODEL_MANIFEST.json --check-manifest
```

See `docs/manufacturing/MODEL_VERIFICATION.md` for the interpretation and limits of the results.

Script riproducibili per sviluppo e validazione. Documentare prerequisiti, parametri ed effetti collaterali.
