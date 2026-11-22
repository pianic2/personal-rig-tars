# RTARS-18 automated validation

The validator in `scripts/validate_rtars18.py` is pinned to the dedicated
`LuwuDynamics/rig_tars_rl` revision `456e3ee95ccbe94deae9484568719e8686b4b68b`,
ESP-IDF **5.5.3**, ESP32-S3, and the TARS Global/English profile. It rejects other
source revisions and does not use `rig_omni`. No firmware sources are vendored
or modified here.

## Prepare and run

Use an activated ESP-IDF 5.5.3 shell. Keep a clean upstream checkout at the
required commit and install the Python serial tools in that same environment.
The first command below is an example pinned checkout; do not run it in place
of an existing source tree with local work.

```bash
git clone https://github.com/LuwuDynamics/rig_tars_rl.git /path/to/rig_tars_rl-rtars18
git -C /path/to/rig_tars_rl-rtars18 checkout --detach 456e3ee95ccbe94deae9484568719e8686b4b68b
python3 -m pip install pyserial esptool
python3 scripts/validate_rtars18.py --source /path/to/rig_tars_rl-rtars18
```

The default is **dry-run**. It checks tool availability/version, the source SHA
and clean state, target/configuration and component manifest; validates an
existing saved `sdkconfig` without creating one; reuses
`build/packages/tars-gb` artifacts only when a validator provenance marker
matches the source, configuration, dependency lock and every artifact hash. It
validates `flash_args`, the generated partition table, image capacities, asset
presence and SHA-256. Unmarked artifacts are not assumed valid. Add `--build`
to run `idf.py build` when needed; this can resolve/download upstream
components and needs network access. It does not flash. Global and CN asset
staging share upstream build resources, so do not run their builds
concurrently.

ESP-IDF may create an untracked `dependencies.lock` in the upstream checkout
during the first build. The validator permits only this generated lock in an
otherwise clean source tree, verifies it as YAML, and includes its checksum in
the report. Preserve that lock with the build to keep dependency resolution
repeatable; any other source-tree change fails preflight. The validator does
not edit or commit upstream firmware sources. A successful artifact validation
also writes `.rtars18-validation.json` inside the local build directory; it
contains only the pinned source/config/lock/artifact checksums and allows a
later dry-run to verify a reusable build. See the [official ESP Component
Manager lockfile reference](https://docs.espressif.com/projects/idf-component-manager/en/latest/reference/dependencies_lock.html).

The script writes the sanitized result to
`evidence/RTARS-18/validation-report.md`. Inspect it before publication. It
never writes port paths, serial/chip identifiers, MAC addresses, raw command
logs, credentials, usernames or host paths into the report. A failed check
returns nonzero. `NOT TESTED` is never promoted to PASS.

## Optional physical probe

The validator always enumerates serial interfaces when `pyserial` is present,
but never guesses which interface belongs to TARS. For read-only chip/flash
queries, explicitly select a currently detected port after physically
identifying the board and ensuring no other serial consumer is active:

```bash
python3 scripts/validate_rtars18.py --source /path/to/rig_tars_rl-rtars18 \
  --port "$PORT" --probe
```

Set `PORT` to the path the operator physically identified from
`/dev/serial/by-id/`; do not copy a guessed device path.

The script verifies the selected path is presently enumerated, then runs only
`esptool chip_id` and `flash_id` for ESP32-S3 and records the result and whether
capacity is at least 16 MiB. It discards query output containing unique IDs.
No explicitly selected, currently detected port means no chip query. Port
detection and physical flash capacity remain `NOT TESTED` when no board is
attached.

## Separate flash mode

Flashing is an explicit write operation. First build/validate and inspect a
successful dry-run report, identify the device physically, inspect every
manifest offset and image, and confirm that settings/calibration can be
preserved. Then run the following with the exact confirmation phrase:

```bash
python3 scripts/validate_rtars18.py --source /path/to/rig_tars_rl-rtars18 \
  --port "$PORT" --probe --flash \
  --confirm 'FLASH RTARS-18 TARS GLOBAL'
```

Flash mode requires a provenance marker from an earlier successful validation
run, repeats all applicable preflight checks, requires the explicitly
detected port, verifies the chip and at least 16 MiB flash, validates the
build-generated manifest and partition table, and only then writes
`@flash_args` from the exact build directory. Missing confirmation or any
preflight failure blocks the write. It never invokes `erase_flash`, reset
flows that clear calibration, or a generic hard-coded address list. A write
can still interrupt the device; follow [RECOVERY.md](RECOVERY.md) if it fails.

## Current evidence and gaps

The checked-in [evidence register](../../evidence/RTARS-18/README.md) separates
source review from actual local build and physical checks. Do not mark RTARS-18
Done until the mandatory AC have reproducible evidence. In particular,
physical port/chip/capacity evidence, generated build artifacts, and any AC
requiring a flash/boot/recovery demonstration must be collected on the actual
board. No result may be inferred from this procedure alone.
