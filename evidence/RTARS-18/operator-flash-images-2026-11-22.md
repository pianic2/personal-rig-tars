# RTARS-18 — Five-image flash manifest verification

Date: 2026-11-22. Origin: terminal output provided by operator, source checkout `LuwuDynamics/rig_tars_rl` at pinned commit `456e3ee95ccbe94deae9484568719e8686b4b68b`, Global TARS build. Results were obtained by running a read-only verification script on the operator host; no device write was performed. This evidence was sanitized before publication.

| Image | Offset | Bytes | SHA-256 | Result |
| --- | --- | ---: | --- | --- |
| `bootloader.bin` | `0x0` | 16256 | `31156b630ef1bc8507cbe20eef5d6ce8e69fcf5e7c98a62f0cc2ef0a7237f9e7` | PASS |
| `partition-table.bin` | `0x8000` | 3072 | `368b3425c8566b7fbbd9f497c3ffac929a1e0905536f736ba58b7ead74ae8235` | PASS |
| `ota_data_initial.bin` | `0xD000` | 8192 | `7d2c7ac4888bfd75cd5f56e8d61f69595121183afc81556c876732fd3782c62f` | PASS |
| `rig-tars.bin` | `0x20000` | 3951136 | `c480348bb154bc5bbeb489ba02675d938226669edfa99935211765845084766a` | PASS |
| `board_assets.bin` | `0x800000` | 2380815 | `99fd6cac6c81007604709220b3977c4b95fd2d94c5026bc8e25aba65e36882ee` | PASS |

- The set of detected binary images exactly matched the five expected images, including the additional standard ESP-IDF OTA initialization image at `0xD000`.
- All files existed and were nonempty; checks passed for expected offsets, bounded byte lengths and **absence of image-image overlaps**.
- **NOT TESTED:** generated partition-table semantic comparison. The subsequent decoder parsed successfully but the verifier crashed because its numeric parser did not support human-readable size units such as `16K`. This is a bug in the verification script, not evidence of an invalid binary partition table.
- **NOT TESTED:** chip interrogation, installed flash size, flash write and boot.
- Writing OTA initialization data can change the OTA selection state; do not infer that an image-size PASS authorizes a flash.

No personal paths, usernames, hostname, physical identifiers, MAC addresses or credentials are included.
