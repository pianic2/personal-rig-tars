# Contributing — RIG-TARS

Policy del repository personale. Ogni modifica deve essere collegata a una issue Jira `RTARS-N`.

## Tracciabilità
- Jira `RTARS` è la fonte di verità per scope, stato e criteri di accettazione.
- GitHub ospita codice, documentazione tecnica, evidenze e review.
- Una branch per issue; se l'issue richiede più PR, usa più branch con la stessa chiave e slug differenti.
- Non committare direttamente su `main`; usare PR e squash merge. Nessun merge automatico.
- Il collegamento a Jira richiede l'integrazione GitHub-for-Jira correttamente installata e autorizzata: il solo naming non prova che la sincronizzazione funzioni.

## Branch
Formato: `<kind>/RTARS-<numero>-<slug-kebab-case>`.
Kind: `feature`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `hotfix`.
Esempi:
- `feature/RTARS-25-voice-control`
- `fix/RTARS-31-servo-timeout`
- `docs/RTARS-11-repository-versioning`

Creare dalla `main` aggiornata. Preferire scope piccolo; evitare branch permanenti di sviluppo.

## Commit
Conventional Commits, con chiave Jira **nel subject**:
`<type>(<scope>): <azione breve> (RTARS-<numero>)`

Tipi: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `ci`, `chore`, `perf`, `revert`.
Scope consigliati: `firmware`, `hardware`, `software`, `docs`, `repo`, `ci`. Altri scope sono ammessi se descrittivi.
Subject in inglese, imperativo, senza punto finale; un tema logico per commit.
Esempi:
- `feat(firmware): add servo calibration (RTARS-25)`
- `fix(hardware): correct connector pinout (RTARS-31)`
- `docs(repo): define versioning policy (RTARS-11)`

Breaking change: `feat(firmware)!: change control protocol (RTARS-25)`; dettagliare `BREAKING CHANGE:` nel body. Mai includere segreti nei commit.

## Pull request
Titolo: `[RTARS-N] <descrizione breve>`. Base: `main`.
Usare il template PR, link Jira, test e prove; in assenza di test indicare esplicitamente perché. Una PR non chiude automaticamente una issue senza criteri di accettazione soddisfatti.
Workflow: Jira In Progress → branch/commit → PR → review + check → squash merge → evidenze su Jira → Done.
Il squash commit deve mantenere `RTARS-N` nel titolo; titolo consigliato: `docs(repo): define versioning policy (RTARS-11)`.
La review può essere self-review documentata se il progetto è personale; non dichiarare approvazioni indipendenti inesistenti.
Prima del merge verificare diff, licenze, test, sicurezza e allineamento AC.
Nessuna automazione di transizione Jira viene assunta finché non testata end-to-end.

## Versioni
Tag annotati `vMAJOR.MINOR.PATCH` secondo SemVer per release del progetto personale, solo dopo una baseline distribuibile. Non confondere release personale e release upstream. Pre-release: `v0.1.0-rc.1`.
Ogni release deve citare issue incluse, SHA, compatibilità HW/FW, istruzioni di rollback e limiti noti.

## Upstream e provenienza
Firmware/PCB/modelli ufficiali rimangono di LuwuDynamics; fonte: https://github.com/LuwuDynamics/rig_omni, cartella `main/boards/tars`.
Conservare link, commit/tag upstream, licenza e modifiche locali; non presentare derivati come ufficiali.
Non importare copie del firmware o modelli senza verificare licenze e attribuzione. Preferire riferimenti, patch tracciate e note di compatibilità.
La documentazione di riferimento si trova in `docs/references/OFFICIAL_SOURCES_INDEX.md`.

## Evidenze
Salvare prove riproducibili in `evidence/RTARS-N/` (log sanitizzati, screenshot, misure, test), e collegarle nella issue/PR. Non inserire credenziali, PII, seriali sensibili o dump non autorizzati.
