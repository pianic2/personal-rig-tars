# RTARS-18 — Generated partition table verification

Date: 2026-11-22. Evidence origin: operator-provided terminal output from a read-only ESP-IDF 5.5.3 partition-table decoder executed on Debian. Source baseline: `LuwuDynamics/rig_tars_rl` commit `456e3ee95ccbe94deae9484568719e8686b4b68b`, firmware v3.8.1, TARS Global build. No raw host paths, identifiers or credentials are published.

The binary `build/packages/tars-gb/partition_table/partition-table.bin` was decoded using the ESP-IDF `gen_esp32part.py` utility and the resulting offsets/sizes were compared to the expected TARS partition map. The local parser accepted human-readable size units (e.g. `16K`).

| Partition | Offset | Size | Reported result |
| --- | --- | --- | --- |
| `nvs` | `0x9000` | `0x4000` | PASS |
| `otadata` | `0xD000` | `0x2000` | PASS |
| `phy_init` | `0xF000` | `0x1000` | PASS |
| `tars_err` | `0x10000` | `0x4000` | PASS |
| `ota_0` | `0x20000` | `0x3F0000` | PASS |
| `ota_1` | `0x410000` | `0x3F0000` | PASS |
| `assets` | `0x800000` | `0x800000` | PASS |

**Outcome:** `PASS: generated layout matches expected TARS partition map`.

Cross-reference: [operator build evidence](operator-build-2026-11-22.md) and [five-image manifest evidence](operator-flash-images-2026-11-22.md).

**Scope:** These results are based on operator-provided execution evidence; the assistant has not executed commands on the operator's host. USB enumeration, chip probing, installed flash size, physical flashing, boot and recovery are **NOT TESTED**. No flash was attempted during this phase.
