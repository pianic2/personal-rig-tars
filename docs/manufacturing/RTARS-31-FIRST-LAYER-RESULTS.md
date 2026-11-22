# RTARS-31 — Verbale primo layer e arresto del lotto (2026-11-22)

> **STATO AGGIORNATO: PRINT_ABORTED — L03 FAIL_VISUAL.** La sezione «Risultati operatore» seguente conserva il primo responso storico dichiarato, successivamente **superato** dalla nuova serie fotografica e dall'arresto comunicato dall'operatore. Non utilizzare `PRINTING_IN_PROGRESS` né `CONTINUE_WITH_MONITORING` come stato attuale.

## Provenienza

- **Fonte primaria**: dichiarazione testuale dell'operatore in chat dopo l'avvio del lotto da tre pezzi, conforme allo schema di [RTARS-31-FIRST-LAYER-RUNBOOK.md](RTARS-31-FIRST-LAYER-RUNBOOK.md).
- **Fonte integrativa**: fotografia ravvicinata fornita dall'operatore, SHA-256 `96bb78e8451c57d9dfbaa202d3df54cdef912a632dd825fd0e7757ada68d1ab3` (JPEG 1152×1536). **Fotografia non caricata su GitHub**: mostra geometria derivata da modello MakerWorld con licenza di distribuzione restrittiva.
- **File di produzione**: `3_parts.gcode`, SHA-256 `32fec82a5f94c0d36b87587c2e853acb7f2462dc7703ec7e0fd6e9e1563a99fa`, conservato privatamente; nessun G-code pubblicato nel repository.
- **Timestamp reale di inizio**: NON COMUNICATO; non inferire dalla data della conversazione o dai file.
- **Programma**: Bambu Studio RTARS-FUNCTIONAL CANDIDATE 0.20mm, Neptune 4 Standard, 0.4 mm, ELEGOO PLA Metallic Bronze. ETA slicer 2h32m12s / 20.59g **stima**, non risultati.

## Risultati operatore

| Campo | Risposta operatore | Valutazione |
|---|---|---|
| Avvio effettivo | SI | **PASS dichiarativo** |
| L01 — Homing | PASS | **PASS dichiarativo**, avvio senza anomalie riferite |
| L02 — Spurgo | PASS | **PASS dichiarativo**, estrusione regolare riferita |
| L03 — Primo layer | PASS | **PASS dichiarativo** |
| Pezzi aderenti | 3/3 | **PASS dichiarativo sul lotto completo** |
| Anomalie | Nessuna | Nessuna riferita |

L'operatore ha precedentemente confermato **5/5 gate preflight PASS**. Questa registrazione prova l'avanzamento della prova sulla base di testimonianza diretta; non sostituisce log firmware, time-lapse o misurazioni.

## Revisione visiva dell'immagine

La foto inquadra **una porzione ravvicinata della superficie di stampa**, non il piatto intero: si distinguono perimetri e linee di materiale depositato sulla superficie. **Nessun distacco macroscopico evidente** nell'area inquadrata. Tra alcune linee si intravedono spazi scuri e piccole irregolarità locali: da questa singola immagine, con prospettiva/illuminazione non controllate, **non si può stabilire** se costituiscano un problema di Z-offset o di flusso. Controllare il completamento dei successivi 2–3 layer e l'assenza di trascinamenti, spigoli rialzati o distacchi.

La fotografia **non** dimostra da sola l'adesione 3/3, né il successo di homing/spurgo, che rimangono PASS **su dichiarazione dell'operatore**.

## Gate e decisione

- L01/L02/L03: **PASS su testimonianza operatore**, 3/3 pezzi aderenti; immagine parzialmente corroborante per un'area visibile.
- **Stato prova:** `PRINTING_IN_PROGRESS`.
- **Decisione:** `CONTINUE_WITH_MONITORING`. Procedere solo se la stampa rimane stabile; monitorare almeno i successivi strati. Arrestare in presenza di distacchi, collisioni, estrusione anomala, accumuli di plastica sull'ugello o allarmi.
- **NON TESTED:** termine stampa, integrità dei tre componenti finiti, supporti reali, durata/consumo consuntivi, misure nominali e reali, foto consentite delle prove, fit test, correzioni.
- **Jira RTARS-31 rimane In corso**; **PR #32 rimane Draft**. RTARS-32 non autorizzata.

Non interpretare PASS primo layer come stampa riuscita o validazione dimensionale dei preset.

## Evento successivo — nuove fotografie e arresto volontario (stato vigente)

Il 22/11/2026 l'operatore ha fornito **tre ulteriori fotografie del primo layer** e ha dichiarato testualmente **«Ho interrotto la stampa»**. Dalle immagini sono osservabili perimetri del pezzo, linee di riempimento diagonali in diversi punti non coese/unite in modo uniforme, piccoli spazi fra passate ed irregolarità localizzate. Le foto non provano da sole distacco macroscopico, né permettono di stabilire una causa unica. L'ipotesi primaria da verificare è **ugello eccessivamente distante dal piano / Z-offset troppo alto**; alternativa: primo layer con flusso insufficiente, mesh/altezza locali o altro. Non si conclude automaticamente che l'essiccazione sia fallita.

### Nuove evidenze (originali NON pubblicati)
- Foto 1: SHA-256 `02b8fc1c7d3343ec2ebb3d13f4e24d0498e4d3a3df0721c0fc05fbac3c083171`.
- Foto 2: SHA-256 `728f89b4707b48822f2ac40710c1275fc3d30e5e69617d7fb69b8fac62a55359`.
- Foto 3: SHA-256 `8bff444e496ab509e6d962ea206b16a89044464768dfc507fa6f0b90f465e8b2`.

Fotografie 1152x1536 JPEG; solo identificativi SHA-256 e osservazioni testuali in GitHub per limitazioni MakerWorld. Nessuna immagine, coordinate G-code o geometria derivata pubblicata.

### Matrice gate riconsiderata — prevale su quella storica
| Gate | Stato vigente | Evidenza |
|---|---|---|
| Preflight 5/5 | PASS dichiarato in precedenza | Operatore |
| Avvio effettivo | PASS — stampa eseguita e poi interrotta | Dichiarazione «Ho interrotto la stampa» |
| L01 Homing | PASS dichiarato in precedenza | Non contestato dalle nuove foto |
| L02 Spurgo | PASS dichiarato in precedenza | Non contestato dalle nuove foto |
| L03 Primo layer | **FAIL_VISUAL** | Nuove immagini con linee non uniformemente coese; campione non approvato |
| Adesione di tutti e tre i pezzi fino all'arresto | **NOT VERIFIED** | Nuove foto mostrano solo parte del piatto; nessuna conclusione 3/3 |
| Completamento stampa | **ABORTED** | Interruzione dichiarata |
| Fit test e quote | **NOT TESTED** | Non esistono provini completati per questa esecuzione |
| Jira RTARS-31 | **In corso** | Non chiudere, non approvare PR #32 |

### Recovery documentata, non ancora eseguita
1. Attendere raffreddamento, rimuovere residui dal piatto senza danneggiarlo e controllare pulizia/adesione della superficie.
2. Poiché ugello da 0,4 mm è stato sostituito (RTARS-29), verificare **Z-offset, parallelismo e livellamento**, e caricare una bed mesh aggiornata nel sistema Neptune 4. Riferimenti ufficiali:
   - https://wiki.elegoo.com/en/neptune/neptune-4-series-firs-layer-not-sticking-to-pei-plate
   - https://wiki.elegoo.com/en/neptune/neptune-4/abnormal-z-offset
   - https://elegoo-downloads.oss-us-west-1.aliyuncs.com/download.elegoo.com/06%20FDM%20Printer/02%20ELEGOO%20Neptune%20Series%20Files/Neptune%204/3.%20User%27s%20Guide/1.User%20Manual/NEPTUNE%204%20User%20Manual-English-B-V2.2.pdf
3. Prima del lotto completo, generare **piccolo quadrato test di un singolo layer**, distinto dalla geometria MakerWorld, con lo stesso preset Neptune 4/Generic PLA/RTARS-FUNCTIONAL e stessi setpoint; controllare visivamente la coesione fra linee.
4. Se vi sono ancora spazi e l'ugello è chiaramente lontano dal piano, durante il test e senza raschiamenti, regolare gradualmente Z-offset in passi **di 0,01 mm**, secondo UI/manuale, verificando dopo ogni singolo passo. Rendere più negativo = avvicinare l'ugello **solo se il sistema usa la convenzione indicata da ELEGOO**. In presenza di schiacciamento eccessivo, trasparenze o raschiamento, arrestare e allontanare l'ugello. Evitare variazioni drastiche; non modificare flow e temperatura contemporaneamente.
5. Riprovare `3_parts.gcode` solo dopo un test primo layer con linee fuse senza sovraestrusione o distacchi, e solo dopo nuovo preflight. Registrare nuovi valori **prima/dopo** e risultati; non alterare la versione approvata dei preset senza tracciamento.

**Decisione: HOLD / RE-CALIBRATE BEFORE REPRINT.** Ipotesi tecnica, non certezza strumentale. L'evento rende non valido l'originario «L03 PASS» per la riuscita del lotto. Nessun nuovo risultato sperimentale è inventato.
