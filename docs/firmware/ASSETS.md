# RTARS-18 — Firmware assets

**Status: static upstream review only; device rendering and asset image not tested.**

The dedicated TARS v3.8.1 README states each regional offline package includes matching app, assets, bootloader and partition table. A local source build puts `board_assets.bin` in the region-specific build directory. The package generator stages that file as `assets.bin`; this is a **filename change**, not proof of content equivalence for arbitrary packages.

- Flash partition `assets`: data/spiffs at `0x800000`, size 8 MiB; see [PARTITIONS.md](PARTITIONS.md).
- Choose exactly one region: `tars-gb` (Global/English) or `tars-cn` (China/Chinese). Do not combine artifacts from different regions, build runs or upstream repositories.
- `main/Kconfig.projbuild` defines the selectable asset configurations and the dedicated profiles specify TARS. Don't assume defaults intended for Puppy.
- The historical `tools/gen_bin_package.py` in the dedicated repository does **not** identify the TARS board; use the documented source-build `board_assets.bin` or the TARS-aware `tools/package_luwu_firmware.py`, subject to artifact checks.
- Hash the exact application and assets files and keep them together in an evidence manifest. Verify build-generated paths/offsets, contents and file size before the first write. Never flash an asset image to an application slot.

### Asset-only flashing
The TARS-aware packaging tool defines an assets-only manifest at `0x800000`, but **the workflow is not hardware-tested**. Prefer the official regional package and use the build-specific flash instructions. If writing only assets, first confirm the installed partition layout is compatible, verify hash/version, and preserve other partitions.

### Validation
After boot, visually verify display animations, sounds/voice prompts, language and any asset loading errors. Record actual firmware version and output only after physically observed. On failures, restore an entire matched firmware+asset package rather than guessing individual file compatibility.

Sources: [dedicated README](https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/README.md), [package tool](https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/tools/package_luwu_firmware.py).
