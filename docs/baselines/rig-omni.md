# RTARS-15 — Upstream source baseline

- Issue: RTARS-15
- Repository: https://github.com/LuwuDynamics/rig_omni
- Immutable upstream commit: `c2b42cd73ef65f5cd2a158d6949f0273869454dc`
- Upstream commit date: 2026-10-01 (UTC+08:00)
- Firmware board sources: `main/boards/tars/`
- ESP-IDF project root: repository root (`CMakeLists.txt`)
- Board-specific selection in CMake: `CONFIG_BOARD_TYPE_TARS=y` selects `rig-tars`
- Toolchain observed: ESP-IDF v5.5.3; Python 3.13.5; Git 2.47.3; Debian 13, x86_64
- Upstream declared ESP-IDF requirement: `>=5.5.2` in `main/idf_component.yml`
- Requirement check: **PASS** (5.5.3 satisfies >=5.5.2)
- Git submodules: none reported by `git submodule status --recursive`
- Build result: **NOT TESTED**. Manifest compatibility is not evidence of successful compilation or runtime behavior.
- Dependency resolution: **NOT TESTED**; no `dependencies.lock` appeared in the collected manifest inventory.
- Source: https://github.com/LuwuDynamics/rig_omni/tree/c2b42cd73ef65f5cd2a158d6949f0273869454dc

## Reproduction

```bash
git clone https://github.com/LuwuDynamics/rig_omni.git
cd rig_omni
git checkout --detach c2b42cd73ef65f5cd2a158d6949f0273869454dc
git rev-parse HEAD
# Use ESP-IDF v5.5.3 environment; select TARS board before building.
```

## Scope and limitations

This baseline pins source identity and registers declared dependencies via the immutable upstream manifest. It does not lock transitive dependency versions; a resolved component lockfile is required for fully deterministic rebuilds. No firmware was flashed or hardware tested.

## Privacy

Raw collection log and original archive were intentionally excluded: they contain user directory paths, temporary paths, host name and Git author identity. Only sanitized technical facts are preserved.
