# RTARS-31 — Verbale di avvio e controllo primo layer (2026-11-22)

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
