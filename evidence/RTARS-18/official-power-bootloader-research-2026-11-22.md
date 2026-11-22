# RTARS-18 — Official-source research: USB enumerates but ESP32-S3 does not answer

Date: 2026-11-22. **Documentary findings, not a successful hardware probe.** All information below is non-identifying.

## Observed evidence
- Operator's USB disconnect/reconnect association identified one newly attached USB-serial adapter (VID:PID `1A86:55D3`).
- Port exists, is readable/writable, and no competing process was detected.
- Repeated `esptool --chip esp32s3 chip_id` failed with `NO_SERIAL_DATA` / `DOWNLOAD_SYNC_FAILED`, even on a different computer USB-C port.
- **Operator confirmed:** controller switch ON, battery **disconnected**.
- Official Global TARS 3.8.1 build, matching flash manifest (five images including OTA initialization), generated partition table and sizes have already passed source/build verification; none of these checks establish hardware communication.

## Sources and conclusions
1. **Luwu official TARS assembly, original Chinese, step 2**: "使用支持数据传输的 USB 线将主板连接到电脑，并按套件说明连接电池、打开电源开关。" It explicitly instructs using a USB data cable, **connecting the battery according to the kit instructions** and turning on the power switch before flashing. [Original TARS assembly, step 2](https://wiki.xgorobot.com/kb/pet-tars/ce146b389ed40020944a3aef7). Corresponding [English TARS assembly](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly) requires power as instructed by kit.
2. [Official firmware/recovery guide](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_firmware) separately notes that Chinese assembly guides call for connected battery and switched-on controller during flash, and that serial enumeration does not establish correct model or supply arrangement.
3. [WCH CH343 Linux driver udev rules](https://github.com/WCHSoftGroup/ch343ser_linux/blob/main/udev/99-ch34x.rules): VID:PID `1a86:55d3` is a **CH343 USB-to-serial bridge**. Recognizing it proves only that the USB interface enumerated, **not** that ESP32-S3 is powered or in ROM download mode. No evidence justifies replacing the Linux serial driver; permissions and open-port checks passed.
4. [Espressif esptool troubleshooting ESP32-S3](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/troubleshooting.html): `No serial data received` means no serial bytes/successful SLIP packet, consistent with missing target power, TX/RX wiring, or download-mode/reset issues. It does not identify one cause.
5. [Espressif ESP32-S3 boot mode selection](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/advanced-topics/boot-mode-selection.html): the auto-reset circuit depends on DTR/RTS to GPIO0/EN; a USB bridge does **not** guarantee those lines are correctly connected. Manual download mode is board-specific; avoid arbitrary button/power sequences.
6. [Pinned TARS board firmware](https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/main/boards/tars/tars_board.cc) initializes the BOOT button on GPIO0, while a separate external touch input uses GPIO3. The TARS firmware also assigns a long BOOT press to settings reset; do not use a generic long press under operating firmware as a flashing instruction.

## Recommended resolution path (officially prescribed first)
1. **Stop repeated esptool attempts without the prescribed target power.**
2. With both USB and battery disconnected and the power switch OFF, identify and check the kit-supplied battery: exact compatibility, safe physical condition, battery connector orientation and silkscreen polarity. Do **not** guess voltage or reverse connectors.
3. If the supplied battery matches the verified kit electrical requirements, connect it **with the board switched OFF**, keep all loose electronics insulated, then switch ON and connect a known USB data cable. The source explicitly requires the kit's battery-powered arrangement. A display/startup indication is useful but insufficient proof by itself.
4. Repeat a **read-only** `esptool --chip esp32s3 --port [operator-verified port] --baud 115200 chip_id`; redact raw unique identifiers. Then `flash_id` only if the chip query succeeds.
5. If communication still fails **with the correct power**, investigate auto-reset DTR/RTS to GPIO0/EN and serial RX/TX according to this board's electrical schematic or contact Luwu support. No source inspected demonstrates a safe universal BOOT+power-switch sequence for this board.
6. Continue to prohibit `write_flash`, `erase_flash` or calibration reset pending hardware preflight and user authorization.

**Result classification:** official *power requirement and troubleshooting path VERIFIED IN DOCUMENTATION*; root cause of the operator's failure **UNCONFIRMED** pending a correctly powered chip probe. This is not an assertion that the USB interface cannot power the MCU on every revision.
