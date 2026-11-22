# RTARS-18 — Global firmware build, operator-reported evidence

Date: 2026-11-22. Evidence origin: terminal transcript supplied by operator from Debian host. These values have **not** been independently reproduced by the assistant on that host. Full build log remains local and was **not** uploaded.

## Provenance and environment
- Upstream: `https://github.com/LuwuDynamics/rig_tars_rl.git`
- Git HEAD: `456e3ee95ccbe94deae9484568719e8686b4b68b`; worktree clean before build
- Board firmware version: `3.8.1`
- ESP-IDF: `v5.5.3`; environment reported PASS for `idf.py`, `ninja`, `cmake`, `xtensa-esp-elf-gcc`, `serial`, `esptool`, `yaml`
- Python: 3.13.5, ESP-IDF virtual environment
- Configuration: `CONFIG_IDF_TARGET="esp32s3"`, `CONFIG_ESPTOOLPY_FLASHSIZE="16MB"`, `CONFIG_FIRMWARE_REGION_OVERSEAS=y`, `CONFIG_BOARD_TYPE_TARS=y`
- Build: `idf.py -B build/packages/tars-gb -DSDKCONFIG=build/package-configs/sdkconfig.tars-gb -DSDKCONFIG_DEFAULTS=... -DIDF_TARGET=esp32s3 build` reported **PASS**. Original command used absolute paths and the standard ESP-IDF defaults files, see `docs/firmware/FLASHING.md`.
- Original full build log preserved on operator workstation (not in this repository).

## Observed artifacts

| Relative artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `build/packages/tars-gb/rig-tars.bin` | 3951136 | `c480348bb154bc5bbeb489ba02675d938226669edfa99935211765845084766a` |
| `build/packages/tars-gb/board_assets.bin` | 2380815 | `99fd6cac6c81007604709220b3977c4b95fd2d94c5026bc8e25aba65e36882ee` |
| `build/packages/tars-gb/bootloader/bootloader.bin` | 16256 | `31156b630ef1bc8507cbe20eef5d6ce8e69fcf5e7c98a62f0cc2ef0a7237f9e7` |
| `build/packages/tars-gb/partition_table/partition-table.bin` | 3072 | `368b3425c8566b7fbbd9f497c3ffac929a1e0905536f736ba58b7ead74ae8235` |
| `dependencies.lock` | not reported | `cc3c668b3a3279d51082235c980a994a66002a303a11375a34b4cdab91815b2f` |

`build/packages/tars-gb/flash_args` was reported present and nonempty; its **contents not yet reviewed**.

## Preliminary capacity checks
- App `3951136 <= 0x3F0000 (4128768)`: **PASS — size only**, 177632 bytes remaining per OTA slot.
- Assets `2380815 <= 0x800000 (8388608)`: **PASS — size only**, 6007793 bytes remaining.
- Partition-table binary size `3072 <= 0x1000 (4096)`: **PASS — size only**.
- Bootloader size `16256 <= 0x8000 (32768)`: **PASS — size only**; actual bootloader location must be checked against generated flash manifest.

## Outstanding checks
- **NOT TESTED:** actual `flash_args` offsets/file correspondence, decoded `partition-table.bin`, overlap/alignment assertions, build artifact provenance marker and automated validator's report on operator host.
- **NOT TESTED:** USB device identification, chip/flash size probe, physical flash, boot and recovery.
- Never infer a successful physical flash from a successful build. No flash/erase/probe performed for this evidence.

This evidence records operator-provided output without storing host paths, user names, serial numbers, MACs or credentials.
