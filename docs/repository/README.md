# Repository architecture and source of truth

Issue: RTARS-11. Repository: `pianic2/personal-rig-tars`.

| Path | Purpose |
| --- | --- |
| `firmware/` | Personal ESP-IDF components, patches, configs and integration code; not an untracked upstream fork |
| `hardware/` | Personal CAD, schematics, pin mapping and hardware integration |
| `software/` | Host integrations, APIs, assistants and tooling |
| `scripts/` | Repeatable build, diagnostics and validation scripts |
| `docs/` | Technical decisions, BOM, official-source index, procedures |
| `evidence/RTARS-N/` | Sanitized, reproducible evidence related to Jira tasks |
| `.github/` | CI checks, PR templates and repository automation |

Existing `docs/hardware/bom/` and `docs/references/` stay in place. Hardware BOM is documentation; `hardware/` hosts original project engineering assets.

## Ownership boundaries
- Jira RTARS: planning, acceptance criteria, workflow, closure.
- GitHub: versioned engineering deliverables, commits, reviews, verification artifacts.
- Confluence RTARS: planning notes and material not suited to version control.
- Upstream: https://github.com/LuwuDynamics/rig_omni/tree/main/main/boards/tars

Capture the upstream revision SHA/tag in work that depends on it. Do not rely solely on moving `main` to reproduce builds. Read the official source index before importing assets. Upstream license terms govern reuse; this repository does not grant new rights to upstream artifacts.

## Team conventions
See [CONTRIBUTING.md](../../CONTRIBUTING.md). Use Jira issue keys consistently in branch, commit subject, PR title and evidence folder. Source references in docs should include URL, revision and verification date.
