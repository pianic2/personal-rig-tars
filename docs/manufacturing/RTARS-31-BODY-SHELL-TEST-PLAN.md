# RTARS-31 — Piano minimo di prova con `body_shell` (non ancora eseguita)

**Riferimenti:** [audit G-code](RTARS-30-BODY-SHELL-GCODE-AUDIT.md), [classificazione RTARS-28](PART_CLASSIFICATION.csv), DoR/DoD, Jira RTARS-31.

**Oggetto:** `body_shell` / P04, guscio estetico-funzionale (P1). Il file disponibile è un G-code esistente, non un nuovo provino isolato. **Durata slicer prevista: 2h22m03s; materiale modello: 21.73 g**, e non un risultato osservato. Non ristampare automaticamente soltanto per certificare la macchina.

## Finalità e criteri
| Prova | Criterio | Stato |
|---|---|---|
| Coerenza profilo | G-code contiene RTARS-FUNCTIONAL CANDIDATE 0.20 mm | PASS statico |
| Temperatura filamento | 210/205°C ugello e 60°C piano entro range dichiarati ELEGOO | PASS documentale |
| Identificazione macchina | Neptune 4 Standard 0.4 mm, ugello acciaio temprato dichiarato e preset Klipper nel file | PASS documentale; configurazione firmware corrente non riletta |
| G-code superficiale | Sequenze inizio/fine, riscaldamenti e comandi movimento presenti; coordinate esplicite entro nominale | PASS statico limitato, **non** test di sicurezza esecutivo |
| Orientamento e supporti | Ispezione visiva locale delle superfici, appoggi e interfacce prima della stampa | NOT TESTED |
| First-layer safety | Home/probe/offset/linea di spurgo verificati sulla stampante, senza interferenze; supervisione continua fase iniziale | NOT TESTED |
| Dimensioni | Misure con calibro su punti funzionali del guscio, valori nominali ricavati dall'originale locale e registrati, non stimati | NOT TESTED |
| Fit | Accoppiamento non forzato del guscio con componente correlato, osservazioni e foto autorizzate | NOT TESTED |
| Conclusione provini critici | P0 P01/P05/P08/P13 verificati separatamente | NOT TESTED |

## Checklist pratica minima
1. **Prima dell'esecuzione**, sul dispositivo confermare preset macchina Neptune 4 Standard, versione firmware e che start/end/homing/purge siano adatti a hardware e piatto in uso; controllare fisicamente superficie, ugello, presenza e comportamento dei supporti generati, oltre ad assenza di avvisi in Preview. **Non usare** il G-code se un comando o l'orientamento è dubbio.
2. Per la fase di RTARS-31, scegliere **un punto misurabile e funzionalmente significativo**, associandolo a una dimensione nominale verificata sul file originale locale. Nessuna quota inventata e nessuna modifica geometrica.
3. Eseguire solo una stampa sicura e presidiata, controllando primo layer e progressione; interrompere in caso di collisioni, distacco, estrusione anomala o comportamento inatteso. Non avviare stampe notturne non presidiate.
4. Dopo raffreddamento, annotare tempi effettivi, massa misurata se bilancia disponibile, scarti, eventuali difetti, quota nominale e quota misurata (mm), differenza (mm), misura ripetuta, fit PASS/FAIL, fotografie ammesse e controlli di licenza.
5. Se `body_shell` viene usato come smoke test, non usarlo come sostituto di prova dell'articolazione/braccio servo P0. Per chiudere RTARS-31 servono almeno provini/fit delle interfacce critiche effettivamente identificate, secondo gli AC Jira.

## Schema risultato (da compilare dopo prova)
```json
{
  "task": "RTARS-31",
  "part": "P04/body_shell",
  "source_gcode_sha256": "a9a79772de096e8b95d49a76dea16c5df548bd25ac56695a267a5039aabdff11",
  "process": "RTARS-FUNCTIONAL CANDIDATE 0.20mm",
  "preflight": null,
  "printed": false,
  "actual_duration_seconds": null,
  "actual_mass_g": null,
  "waste_mass_g": null,
  "dimension_nominal_mm": null,
  "dimension_measured_mm": null,
  "fit_result": null,
  "notes": null
}
```

Questo schema è una **bozza**, non risultati sperimentali. Un G-code derivato dal modello può contenere geometria protetta: conservarlo localmente e committare soltanto dati/evidenze anonimizzati senza geometrie non distribuibili.
