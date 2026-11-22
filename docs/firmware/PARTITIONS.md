# RTARS-18 — Flash layout (source review)

**Verified in source only**, not read back from physical flash. Primary source: [dedicated TARS partition CSV](https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/partitions/16m.csv). Default ESP32-S3 configuration declares 16 MiB flash, QIO.

| Partition | Type | Start | Size | End (exclusive) |
| --- | --- | ---: | ---: | ---: |
| nvs | data/nvs | 0x9000 | 0x4000 | 0xD000 |
| otadata | data/ota | 0xD000 | 0x2000 | 0xF000 |
| phy_init | data/phy | 0xF000 | 0x1000 | 0x10000 |
| tars_err | data/nvs | 0x10000 | 0x4000 | 0x14000 |
| ota_0 | app/ota_0 | 0x20000 | 0x3F0000 | 0x410000 |
| ota_1 | app/ota_1 | 0x410000 (derived by CSV auto-placement) | 0x3F0000 | 0x800000 |
| assets | data/spiffs | 0x800000 | 0x800000 | 0x1000000 |

All numbers above are hex. `0x1000000` is 16 MiB. The CSV leaves `ota_1` offset blank; `0x410000` is the expected aligned continuation, **to be confirmed against generated partition-table.bin**. Blank ranges are reserved/unallocated; do not infer their safety for arbitrary writes.

### Flash address safeguards
- The dedicated packaging script `tools/package_luwu_firmware.py` defines offsets bootloader `0x0`, partition table `0x8000`, application `0x20000`, assets `0x800000`. **These are script declarations, not device-verified addresses**.
- Treat the ESP-IDF-generated `flash_args` and partition-table binary as authoritative for an actual build. Confirm bootloader offset (varies with bootloader/layout configuration); don't blindly apply the packaging constant.
- Do not write the application to `0x20000` as an OTA update without checking active OTA selection, image state, and supported workflow. This address represents the first OTA slot, not necessarily the currently active one.
- Compare firmware binary byte lengths to `0x3F0000` per OTA slot and assets image to `0x800000`.
- Preserve `nvs` and `tars_err` unless a fully documented recovery justifies their deletion.

### Local checks when the build exists
```bash
cd build/packages/tars-gb
cat flash_args
python -m esptool image_info rig-tars.bin
python -m gen_esp32part partition_table/partition-table.bin
sha256sum rig-tars.bin board_assets.bin bootloader/bootloader.bin partition_table/partition-table.bin
```
Some installed ESP-IDF versions may use a different invocation for the partition decoder; use the tool in the activated 5.5.3 installation. Store sanitized outputs in `evidence/RTARS-18/` after running them.
