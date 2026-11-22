# RTARS-18 automated validation — historical isolated-environment dry-run

Generated: 2026-11-22 14:39 UTC
Mode: DRY-RUN
Firmware source: `https://github.com/LuwuDynamics/rig_tars_rl.git` at `456e3ee95ccbe94deae9484568719e8686b4b68b`; ESP-IDF v5.5.3; profile TARS Global/English.
No raw command output, username, hostname, serial path, chip identifier, MAC, or credentials are recorded.

| Check | Result | Sanitized detail |
| --- | --- | --- |
| git available | **PASS** | git executable detected |
| ESP-IDF available | **FAIL** | idf.py missing |
| upstream checkout | **FAIL** | source directory not found |
| IDF_PATH | **PASS** | ESP-IDF installation found |
| build tools | **FAIL** | missing: ninja |
| serial dependencies | **FAIL** | pyserial or esptool missing; port probe/flash unavailable |
| source build | **NOT TESTED** | no verified build provenance marker; pass --build to build |
| flash_args | **NOT TESTED** | build manifest unavailable |
| resolved dependency lock for writes | **NOT TESTED** | no valid dependencies.lock; flash is blocked |
| generated partition table | **NOT TESTED** | partition-table.bin unavailable |
| image sizes | **NOT TESTED** | manifest and generated partition table required |
| artifact SHA-256 | **NOT TESTED** | build artifacts unavailable |
| serial port detection | **NOT TESTED** | pyserial unavailable; device enumeration not tested |
| chip interrogation | **NOT TESTED** | read-only probe disabled; pass --probe to interrogate a detected serial device |
| flash write | **NOT TESTED** | dry-run is the default; no device write was attempted |

## Artifact manifest

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| No validated build artifacts | — | — |

A `NOT TESTED` result is not a pass. Do not close RTARS-18 while required evidence remains missing.
The report is regenerated on each run; review it for accidental sensitive data before publishing.
