# RTARS-30 — Checklist orientamento e supporti per il lotto `3_parts.gcode`

**Provenienza**: analisi G-code utente SHA-256 `32fec82a5f94c0d36b87587c2e853acb7f2462dc7703ec7e0fd6e9e1563a99fa`; mesh/coordinate originali non pubblicate per licenza MakerWorld. Il G-code contiene **tre oggetti** distinti, identificabili semanticamente come (1) staffa/supporto, (2) base posteriore dello schermo, (3) copertura servo. Non dimostra automaticamente il contatto corretto con il piano, i supporti su superfici funzionali o la direzione degli sforzi.

## Procedura minima di accettazione (solo Bambu Studio locale)
1. Apri lo stesso progetto con le tre parti, seleziona `RTARS-FUNCTIONAL CANDIDATE 0.20mm`, macchina **Neptune 4 Standard 0.4 mm** e filamento Generic PLA @Elegoo documentato. Controlla che le tre parti siano appoggiate con una faccia stabile al piano; nessuna parte fluttua, nessuna intersezione fra oggetti/supporti e nessun out-of-bounds.
2. In **Preview → Color scheme: Line type**, scorri primi layer, layer intermedi e layer con supporti. Le parti devono essere completamente slice-ate senza messaggi di errore; appoggi e supporti devono avere percorso continuo. Le feature `floating vertical shell` e `overhang wall` nel G-code richiedono ispezione visiva; non sono automaticamente errori.
3. Per ciascun oggetto, **controlla che i supporti NON terminino all'interno di fori, sedi di viti, piani di accoppiamento e superfici che devono scorrere o innestarsi**. Se presenti, segnala quali: non rimuoverli automaticamente se sostengono un overhang critico.
4. Valuta l'orientamento rispetto alla funzione: per staffa/supporto, direzione delle sollecitazioni e pareti attorno ai fissaggi; per base posteriore schermo, faccia d'appoggio e sedi di fissaggio; per copertura servo, accessibilità e integrità di sedi, fori e tolleranze del coperchio. NON presumere dove si trovino gli elementi: convalidarli sulle mesh locali.
5. Controlla sufficiente contatto col piano per il primo layer, spazio per la rimozione dei supporti, seam non sulle superfici d'innesto e assenza di warning bloccanti. Se una superficie critica è supportata, annota l'eccezione e la mitigazione.
6. Registra un verbale **solo testuale**, senza fotografie o file geometrici protetti.

## Valori oggettivi estratti dai preset
| Campo | Valore | Interpretazione |
|---|---|---|
| Tipo supporti | `normal(auto)` | automatico, non garantisce collocazione corretta |
| Support threshold angle | 30° | soglia nominale del preset |
| Top Z-distance | 0.20 mm | distacco nominale, non tolleranza validata |
| Bottom Z-distance | 0.20 mm | distacco nominale |
| XY separation | 0.35 mm | distanza nominale |
| Top interface layers | 3 | strati di interfaccia |
| Supports in G-code | presenti | generati effettivamente per il lotto |
| Orientamenti convalidati | NO | richiede operatore davanti alla Preview |

## Verbale da compilare (NON TESTED fino alla conferma)
| Parte | Appoggio stabile (PASS/FAIL) | Supporti fuori da superfici di accoppiamento (PASS/FAIL) | Rimozione supporti possibile (PASS/FAIL) | Orientamento coerente con uso (PASS/FAIL) | Warning bloccanti (nessuno/elenco) |
|---|---|---|---|---|---|
| Staffa/supporto | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Base posteriore schermo | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Copertura servo | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |

**Gate Jira RTARS-30:** AC «orientamenti/supporti motivati per le parti» chiudibile solo dopo una revisione effettiva. Questa checklist definisce la modalità e le motivazioni, ma non è evidenza di revisione avvenuta. Validazione delle quote dopo stampa rimane RTARS-31.
