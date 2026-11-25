# RTARS-31 — Secondo fallimento: alimentazione intermittente e scoppiettii (25 novembre 2026)

**Stato attuale: HOLD — EXTRUSION FAULT / PRINT FAILED.** Non procedere con le stampe dei componenti TARS e non modificare i preset di RTARS-30 fino alla localizzazione del guasto.

## Fatti direttamente dichiarati dall'operatore
- Il PLA Metallic ELEGOO Metal Bronze è stato asciugato **per 10 ore** per ridurne l'umidità. **Temperatura effettiva e setpoint di questa nuova essiccazione non specificati**; non assumere che fosse a 45 °C come l'evento precedente né sommare automaticamente 4 + 10 ore.
- L'operatore ha **rifatto la stampa con un solo pezzo**, anziché il lotto originario di tre.
- **Esito FAIL:** il flusso del filamento si è nuovamente bloccato, estrusione/stampa non uniforme, filamento percepito come «scoppiettava».
- Non sono stati forniti nuovo file G-code, hash, durata, letture reali temperatura nozzle, video, fotografie, nome univoco del pezzo, dimensioni o esito del feed a vuoto. Non inferirli.
- L'evento precedente (lotto di tre pezzi) è già documentato in [FIRST-LAYER-RESULTS.md](RTARS-31-FIRST-LAYER-RESULTS.md): interrotto per primo layer non uniforme. L'operatore ha dichiarato di avere già ripetuto il livellamento. Non richiederlo nuovamente senza diagnosi.

## Interpretazione tecnica, NON diagnosi conclusiva
1. **Rumore all'uscita ugello / bolle-vapore**: scoppiettii sono compatibili con umidità residua che vaporizza nel filamento, ma l'essiccazione di dieci ore non è di per sé una misura dell'umidità interna della bobina.
2. **Rumore tipo click dall'estrusore**: indica possibile perdita di presa ingranaggi o contropressione da parziale intasamento; non chiamarlo automaticamente filamento umido.
3. **Interruzione effettiva della portata**: possibile intasamento parziale di ugello/hotend, feed path o heat creep (verificare ventola dissipatore hotend); la macchina può anche presentare restrizione causata da cambio ugello.
4. **Flow ratio aumentato** aumenta la richiesta al sistema e non risolve un percorso del fuso ostruito. Il precedente esperimento A/B 0.98→1.03 o initial-layer 1.00→1.05 è **SOSPESO**, non eseguito/validato. Non modificare Z-offset, flow, temperatura e velocity in parallelo.

### Riferimenti produttore
- Scheda ELEGOO PLA Metallic: asciugatura **50 ± 5°C per 8 h**; hotend **190–230°C**: https://www.elegoo.com/products/pla-metal-filament-1-75-mm-colored-1-kg
- Guida ufficiale ELEGOO: nozzle clogging e controllo **ventola heatbreak** quando nozzle supera 50 °C: https://wiki.elegoo.com/en/neptune/nozzle-clogging
- ELEGOO, sblocco ugello / alimentazione: https://wiki.elegoo.com/en/neptune/neptune-3-series-unclog-the-nozzle
- Prusa, differenza tra ostruzione parziale e flusso insufficiente: https://help.prusa3d.com/article/clogged-nozzle-core-one-core-one-l-xl-mk4-s-mk3-9-s_411823

## Test incrementali senza G-code MakerWorld
| Gate | Procedura | PASS | FAIL/conseguenza |
|---|---|---|---|
| E01 — origine rumore | Distinguere crepitio/bolle **alla punta ugello** da click/slittamento **dentro estrusore** | Origine osservata | UNKNOWN: nessuna attribuzione causale |
| E02 — feed libero senza stampa | Con ugello distante dal piatto, riscaldare a **210 °C** (setpoint già usato) e usare comando di carico macchina per ~**30–50 mm** di estrusione, senza forzare manualmente e senza toccare parti calde | Filamento esce continuo e regolare, senza arresti/click/bolle | Stop test; possibile ostruzione/trascinamento/umidità |
| E03 — verifica heatbreak | Controllare se ventola di dissipazione hotend gira quando dovrebbe, come da ELEGOO; verificare percorso bobina/PTFE/ingranaggi solo a macchina ferma/fredda | Ventola e feed path liberi, niente residui | STOP; riparare prima di stampare |
| E04 — controllo materiale | Solo se percorso estrusione libero e sicuro: caricare un **PLA base noto per funzionare**, usare setpoint appropriato a quel PLA, eseguire breve estrusione statica | PLA base uniforme: più probabile bobina Metallic specifica; non convalida del tutto hotend | Entrambi difettosi: più probabile guasto macchina |
| E05 — eventuale pulizia o cambio ugello | Se E02 fallisce: seguire procedura ufficiale di rimozione ostruzione Neptune 4; in caso di hotend smontato attenersi a precauzioni termiche/elettriche | Portata torna regolare con test a vuoto | Blocca ogni stampa TARS |
| E06 — qualità primo layer | Solo dopo E02+E03 PASS, quadrato semplice (non geometria MakerWorld), parametri invariati, osservare estrusione e adesione | Layer uniforme | Riprendere diagnosi Z-offset/flow separatamente |

**Vincoli:** Non effettuare stampe di più ore, non alzare il flow, non riessiccare indiscriminatamente e non aumentare la temperatura oltre i range produttore. Non dare per risolto un intasamento senza prova di estrusione libera. PLA base di controllo è suggerimento, non prova eseguita. Evitare contatto con ugello e hotend caldi; non forzare l'estrusore a caldo.

## Registro gate RTARS-31
- First attempt 3 parts: **ABORTED**.
- Second attempt 1 part: **FAIL — flow stopped / irregular, popping reported**.
- Drying 10 h: **OPERATOR_REPORT**, material moisture **NOT MEASURED**.
- Feeding/partial clog/heatbreak diagnostics: **NOT TESTED**.
- Successful printed parts / dimensional measurements / fit: **NOT TESTED**.
- RTARS-31 **In corso**, PR #32 **Draft**, RTARS-32 produzione **BLOCKED**.

Al momento il passo discriminante minimo è il **test E02** e la localizzazione del rumore E01: solo allora la diagnosi può essere aggiornata.
