# RTARS-31 — Protocollo di verifica homing, spurgo e primo layer

**Lotto**: tre pezzi — staffa/supporto, base posteriore schermo, copertura servo. G-code locale `3_parts.gcode`, SHA-256 `32fec82a5f94c0d36b87587c2e853acb7f2462dc7703ec7e0fd6e9e1563a99fa` (non redistribuire file, G-code contiene geometria soggetta a MakerWorld Exclusive). Machine: ELEGOO Neptune 4 Standard, 0.4 mm acciaio temprato (dichiarato). Process: `RTARS-FUNCTIONAL CANDIDATE 0.20mm`. Filamento: ELEGOO PLA Metallic Metal Bronze / Generic PLA @Elegoo nel file. Temperatura nozzle primo layer 210 °C, resto 205 °C; bed 60 °C. Slicer estimate 2h32m12s / 20.59 g, **non consuntivo**.

## Stato aggiornato al 22/11/2026 — esito primo layer
- I **5 preflight** sono stati confermati **PASS** dall'operatore. [Verbale condizioni e preflight](RTARS-31-DRYING-ENVIRONMENT-PREFLIGHT.md).
- **Avvio effettivo: SI**, **L01 Homing: PASS**, **L02 Spurgo: PASS**, **L03 Primo layer: PASS**, **3/3 pezzi aderenti**, **anomalie riferite: nessuna**. Fonte: risposta diretta dell'operatore. **Non** sono esiti verificati da log macchina indipendenti.
- Foto ravvicinata ricevuta, non pubblicata per licenza; visibilità parziale (non dimostra l'intero 3/3). Dettagli e hash nel [verbale first-layer](RTARS-31-FIRST-LAYER-RESULTS.md).
- Stato: **PRINTING_IN_PROGRESS**; **CONTINUE_WITH_MONITORING**. La stampa finita, le misurazioni e i fit test restano **NOT TESTED**.

## Esecuzione: tre controlli sequenziali

### Gate L01 — Homing / riscaldamento
- Verifica visuale sul display: caricamento file corretto, temperature verso setpoint configurati; osserva l'homing X/Y/Z senza urti, raschiamenti o movimenti inattesi.
- **PASS** solo se procedura terminata regolarmente, nessuna collisione o errore firmware.
- **STOP/FAIL** immediato in caso di collisione, moto anomalo, allarme termico o firmware: interrompi, non provare ad aggiustare l'offset mentre ci sono rischi meccanici.

### Gate L02 — Spurgo / estrusione
- Osserva la linea di spurgo: flusso di materiale regolare, continuità, nessun rumore anomalo/salti estrusore, nessun accumulo di plastica sull'ugello.
- **PASS** se l'estrusione è continua e l'ugello non trascina accumuli.
- **STOP/FAIL** se l'ugello raschia il piano, il materiale non esce o si accumula pericolosamente, o compaiono errori.

### Gate L03 — Primo layer del lotto
- Osserva **tutti e tre** i componenti: linee continue e adiacenti, buona adesione del perimetro/primo strato, nessun distacco/arricciamento, ugello senza trascinamento.
- **PASS** solo se il primo layer è uniforme e ogni oggetto resta aderente.
- **STOP/FAIL** se uno dei tre pezzi si stacca, se ci sono collisioni, oppure se estrusione/adesione risultano anomale. Non lasciare la stampa non supervisionata in caso di anomalia.
- **NOT TESTED** se un punto non è stato osservato: non convertirlo in PASS.

## Risposta sintetica che serve all'utente

```text
RTARS-31 — Primo layer
Avvio: SI/NO
Homing: PASS/FAIL
Spurgo: PASS/FAIL
Primo layer: PASS/FAIL
Pezzi aderenti: 3/3 oppure N/3
Anomalie: nessuna / descrizione
```

Il valore `Avvio: SI` deve essere dichiarato solo dopo che la stampa è effettivamente partita. In caso di FAIL descrivere la situazione e interrompere la stampa se necessario. Se la partenza viene differita, segnare `Avvio: NO` e gli altri gate `NOT TESTED`.

## Successivo al primo layer
- Se tre gate PASS e **3/3** pezzi aderenti, documentare `PRINTING_IN_PROGRESS`; ciò non significa stampa terminata, materiale caratterizzato né fit approvato.
- A stampa conclusa e raffreddata: annotare ora inizio/fine o durata effettiva, esito di ciascuno dei tre oggetti, eventuali difetti, supporti rimossi correttamente, massa/scarti se misurabili, e quote nominali misurate con calibro e accoppiamenti con parti reali. Tolleranze non inventate: confrontare quote nominali dal modello originale locale.
- Jira RTARS-31 resta **In corso**, PR #32 **Draft** fino ai risultati fisici e agli AC completi. Non pubblicare modelli né foto di geometria licenziata senza verificare i diritti di distribuzione.
