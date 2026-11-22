# RTARS-15 — Sanitized evidence

Source archive examined locally on 2026-11-22; raw archive deliberately not committed.

| Check | Observed result |
|---|---|
| Upstream | `https://github.com/LuwuDynamics/rig_omni.git` |
| Full commit SHA | `c2b42cd73ef65f5cd2a158d6949f0273869454dc` |
| Upstream commit date | 2026-10-01 |
| Board directory | `main/boards/tars` present |
| Root project entry | `CMakeLists.txt` |
| Dependencies declaration | `main/idf_component.yml` |
| Direct manifest declarations | 55 |
| Required ESP-IDF | `>=5.5.2` |
| Installed ESP-IDF | `v5.5.3` |
| Declared version compatibility | PASS |
| Recursive Git submodules | None reported |
| Resolved dependency lockfile | Not found in collected manifest inventory |
| Dependency installation/build | Not executed |
| Hardware/runtime compatibility | Not tested |

## Source of truth

Pinned component manifest: https://github.com/LuwuDynamics/rig_omni/blob/c2b42cd73ef65f5cd2a158d6949f0273869454dc/main/idf_component.yml

Manifest contains 55 direct declared dependencies, including conditional per-target entries. Version constraints are recorded in the immutable upstream manifest rather than retyped; not all of these dependencies necessarily apply to TARS ESP32-S3, and resolved transitive versions are not established by this collection.

## Privacy handling

Excluded raw log, username, hostname, absolute home and temporary paths, full kernel/system identifier, and the upstream commit's author email. No credentials or raw device identifiers published.
