# RTARS-18 — Evidence register (2026-11-22)

Classification: **SOURCE REVIEW / NOT HARDWARE TESTED**. No logs from a device or local ESP-IDF build were produced in this session; no checksums of binary artifacts are claimed.

| Control | Result | Evidence |
| --- | --- | --- |
| Dedicated TARS firmware identified | PASS (repository inspection) | `rig_tars_rl` SHA `456e3ee95ccbe94deae9484568719e8686b4b68b`, README and `main/boards/tars/version.txt` (3.8.1) |
| Source partition map extracted | PASS (source inspection) | `partitions/16m.csv`; compare derived OTA1 location to a generated binary later |
| TARS region/build procedure located | PASS (source inspection) | `configs/tars-gb.sdkconfig`, README source-build instructions, `tools/tars_log/README.md` |
| Packaging discrepancy documented | PASS (source inspection) | `tools/gen_bin_package.py` does not support TARS; `tools/package_luwu_firmware.py` supports TARS; no packaging execution claimed |
| Port/chip/flash capacity verified physically | NOT TESTED | Board not available to remote session |
| Generated flash arguments, generated partitions and binary sizes/hashes verified | NOT TESTED | No matching local build artifacts available to remote session |
| App/assets flash completed | NOT TESTED | No device write attempted |
| Physical boot and recovery demonstrated | NOT TESTED | No device attached |

Source snapshots (all under the pinned dedicated SHA):
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/README.md
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/partitions/16m.csv
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/tools/package_luwu_firmware.py
- https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/tools/tars_log/README.md

**Outstanding for completion**: collect sanitized local build `flash_args`, generated partition decode, actual flash size/serial device detection, image hashes/sizes; classify whether physical flash is necessary for the documented AC. Do not mark unexecuted checks PASS. All logs must be sanitized before commit.
