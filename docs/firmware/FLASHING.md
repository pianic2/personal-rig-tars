# RTARS-18 — Flashing ESP32-S3 (RIG-TARS)

**Scope:** documented and statically reviewed; **device flashing NOT TESTED**. Firmware is third-party; never mix binaries across editions or source repositories.

## Source of truth
- Dedicated TARS v3.8.1 source at `LuwuDynamics/rig_tars_rl`, pinned to `456e3ee95ccbe94deae9484568719e8686b4b68b`.
- Global/English edition: `configs/tars-gb.sdkconfig`; China edition: `configs/tars-cn.sdkconfig`. Target ESP32-S3, ESP-IDF 5.5.3, configured flash 16 MiB.
- The older multi-board `rig_omni` snapshot `c2b42cd73ef65f5cd2a158d6949f0273869454dc` is **not** an interchangeable firmware package.

## Prefer the official release
1. Identify the actual board as TARS, check power, USB data cable, physical safety (servo movement), and model/regional firmware.
2. Obtain the **Global v3.8.1** archive from https://github.com/LuwuDynamics/rig_tars_rl/releases/download/v3.8.1/rig-tars-3.8.1-gb.zip (or the CN archive only when CN is intended); retain original package, version, checksums and its included flashing instructions.
3. Alternatively use https://tools.xgorobot.com/ in desktop Chrome/Edge: select **RIG-TARS** and **EN** for Global or **中文** for China. Ensure the browser targets the expected serial device. This is an external service: verify the device/package before authorizing writes.
4. Do not use the source's legacy `tools/gen_bin_package.py` for TARS: it falls back to Puppy. The dedicated repository supports TARS in `tools/package_luwu_firmware.py`; its build/package operation has **not been executed** in RTARS-18.

## Reproducible source build (reference commands; NOT executed here)
Run from the pinned dedicated source checkout, with ESP-IDF 5.5.3 activated:
```bash
git clone https://github.com/LuwuDynamics/rig_tars_rl.git
cd rig_tars_rl
git checkout 456e3ee95ccbe94deae9484568719e8686b4b68b
mkdir -p build/package-configs
cp configs/tars-gb.sdkconfig build/package-configs/sdkconfig.tars-gb
idf.py -B build/packages/tars-gb \
  "-DSDKCONFIG=$PWD/build/package-configs/sdkconfig.tars-gb" \
  "-DSDKCONFIG_DEFAULTS=$PWD/sdkconfig.defaults;$PWD/sdkconfig.defaults.esp32s3" \
  -DIDF_TARGET=esp32s3 build
```
The documented expected build outputs include `rig-tars.bin`, `board_assets.bin`, `flash_args` and the matching bootloader/partition table. **Check actual output existence and `flasher_args.json`/`flash_args` before flashing.** The source's asset staging uses shared build resources: serialize CN and Global builds.

## Port identification (read-only)
On Linux, connect one device at a time and compare `ls -l /dev/serial/by-id/` and `python -m serial.tools.list_ports -v` before/after connection. Typical device names are not guaranteed. Set `PORT` to the confirmed device and ensure the current user has serial permission. Stop any monitor or serial tool before opening the port.
```bash
PORT=/dev/ttyACM0  # EXAMPLE ONLY: replace after physical verification
python -m esptool --chip esp32s3 -p "$PORT" chip_id
python -m esptool --chip esp32s3 -p "$PORT" flash_id
```
These commands interrogate the chip; they do not flash firmware. Serial readout **NOT TESTED**. Do not record raw unique IDs or credentials in public evidence.

## Full wired flash (WRITE — only after preflight)
The upstream TARS serial-tool documentation provides a `flash_args`-based flash of the matching build. Run **only** from the relevant build output directory, after manually inspecting every offset/file referenced by its `flash_args`; confirm 16 MiB flash and that app/assets share the region/profile/version. No generic hard-coded command is authorized as a substitute for the build-specific manifest.
```bash
# Example for an ALREADY VERIFIED Global build:
cd build/packages/tars-gb
python -m esptool --chip esp32s3 -p "$PORT" -b 460800 \
  --before default_reset --after hard_reset write_flash @flash_args
```
Before this command, inspect `flash_args`, check each referenced file exists and its byte length fits the partitions in [PARTITIONS.md](PARTITIONS.md), and record SHA-256 checksums locally. Avoid `erase_flash` in routine flashing. Physical flashing **NOT TESTED**.

## Validation after flashing
Use the dedicated upstream `tools/tars_log/tars_serial.py` for serial `ports`, `status`, `errors`, then monitor boot output (stop other serial consumers). Confirm correct TARS firmware/region, display, audio/asset rendering, and expected motion behavior only under safe hardware conditions. A successful esptool exit alone is not functional validation.

Related: [ASSETS.md](ASSETS.md), [PARTITIONS.md](PARTITIONS.md), [RECOVERY.md](RECOVERY.md), [evidence](../../evidence/RTARS-18/README.md).
