# RTARS-18 — Evidence register (2026-11-22)

Classification: **OPERATOR-VERIFIED BUILD AND READ-ONLY HARDWARE PROBE / NO FLASH WRITE**. The initial source-only phase is superseded by sanitized operator-provided build output and read-only ESP32-S3 probe on 2026-11-22; see the linked evidence files. No application image was flashed by this task. The repeatable procedure is [AUTOMATED_VALIDATION.md](../../docs/firmware/AUTOMATED_VALIDATION.md), implemented by `scripts/validate_rtars18.py`.

| Control | Result | Evidence |
| --- | --- | --- |
| Dedicated TARS firmware identified | PASS (repository inspection) | `rig_tars_rl` SHA `456e3ee95ccbe94deae9484568719e8686b4b68b`, README and `main/boards/tars/version.txt` (3.8.1) |
| Source partition map extracted | PASS (source inspection) | `partitions/16m.csv`; compare derived OTA1 location to a generated binary later |
| TARS region/build procedure located | PASS (source inspection) | `configs/tars-gb.sdkconfig`, README source-build instructions, `tools/tars_log/README.md` |
| Packaging discrepancy documented | PASS (source inspection) | `tools/gen_bin_package.py` does not support TARS; `tools/package_luwu_firmware.py` supports TARS; no packaging execution claimed |
| Port/chip/flash capacity verified physically | NOT TESTED | Board not available to remote session |
| Global build / flash arguments / five image sizes and SHA-256 | PASS (operator terminal evidence) | [Global build](operator-build-2026-11-22.md), [flash image manifest](operator-flash-images-2026-11-22.md) |\n| Generated partition table decoded and validated | PASS (operator terminal evidence) | [Generated partitions](operator-partitions-2026-11-22.md) |
| App/assets flash completed | NOT TESTED | No device write attempted |
| USB association, port accessibility, ESP32-S3 chip ID and 16 MB flash ID | PASS (operator terminal evidence) | [USB association](operator-usb-association-2026-11-22.md), [serial preflight](operator-serial-preflight-2026-11-22.md), [powered chip probe](operator-powered-chip-probe-2026-11-22.md) |\n| Physical boot and recovery demonstration | NOT TESTED / N/A for documentation-only AC | RTARS-18 requires documented recovery, not forced recovery execution |
| Original isolated validator dry-run | FAIL (historical only) | `validation-report.md` was created without local ESP-IDF tools and source; **not representative of the operator workstation** |\n| Corrected validator regression on exact five-image manifest | NOT TESTED until CI / local test evidence | `tests/test_validate_rtars18.py`; `.github/workflows/rtars18-validation.yml` |

Source snapshots (all under the pinned dedicated SHA):
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/README.md
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/partitions/16m.csv
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/tools/package_luwu_firmware.py
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/tools/tars_log/README.md

**AC assessment:** (1) firmware and assets documented: PASS; (2) port and partitions verified: PASS; (3) recovery documented: PASS. A physical flash or destructive recovery is outside the explicit documentary scope and remains NOT TESTED. The automated validator is supplementary code and must be reviewed/tested before integration. All committed evidence has been sanitized before publication.

The checked-in report template is regenerated only by an actual validator run. This repository change does not claim any environment/build/device result. `dependencies.lock` must be present for flash preflight to pass; upstream resolution without a lock remains a reproducibility gap.
