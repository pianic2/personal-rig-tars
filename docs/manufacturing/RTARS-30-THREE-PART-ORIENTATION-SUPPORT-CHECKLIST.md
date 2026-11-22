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
| Orientamenti convalidati per **lotto di 3 oggetti** | PASS — dichiarazione operatore del 2026-11-22 | Review Preview riferita ai 3 componenti; non estesa ad altre parti |

## Verbale acquisito il 2026-11-22 — verifica operatore su Bambu Studio Preview
| Parte | Appoggio stabile (PASS/FAIL) | Supporti fuori da superfici di accoppiamento (PASS/FAIL) | Rimozione supporti possibile (PASS/FAIL) | Orientamento coerente con uso (PASS/FAIL) | Warning bloccanti (nessuno/elenco) |
|---|---|---|---|---|---|
| Staffa/supporto | PASS* | PASS* | PASS* | PASS* | Nessuno* |
| Base posteriore schermo | PASS* | PASS* | PASS* | PASS* | Nessuno* |
| Copertura servo | PASS* | PASS* | PASS* | PASS* | Nessuno* |

*L'operatore ha dichiarato **una sola valutazione aggregata per l'intero lotto**, non misure o risposte indipendenti per oggetto: «Appoggio sul piano: pass; supporti fuori dalle superfici critiche e rimovibili: pass; orientamento coerente con i carichi: pass; avvisi slicer: none». La tabella distribuisce il risultato dichiarato ai tre oggetti del lotto, non aggiunge tre osservazioni indipendenti. Evidenza = attestazione dell'operatore sulla Preview locale, senza screenshot geometrici ripubblicati. La conformità geometrica non è stata verificata da terzi, e il report non determina l'esito di stampe fisiche.

**Motivazione funzionale della review per il lotto:** la staffa è orientata per conservare appoggio/fissaggi e supporti rimovibili senza compromettere i fori; la base posteriore dello schermo per preservare appoggio e sedi di montaggio; la copertura servo per mantenere accessibili sedi, fori e incastri e non trasferire i supporti sulle interfacce. Questi **criteri di accettazione** sono stati confermati globalmente dall'operatore; non sono dati ricostruiti dalle coordinate del G-code.

**Portata dell'AC:** PASS dichiarativo per *queste tre parti del lotto pilota RTARS-31* con il profilo RTARS-FUNCTIONAL. Orientamenti delle altre parti del modello NON TESTED: vanno valutati prima dei successivi slicing/print, senza considerarli automaticamente certificati da questa attestazione. Misure e fit test restano RTARS-31.
