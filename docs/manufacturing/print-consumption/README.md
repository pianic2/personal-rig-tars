# RTARS-34 — Registro stampa 3D

Registro incrementale dei piatti di stampa del progetto RIG-TARS. `plates.json` contiene dichiarazioni dell'utente; non costituisce prova autonoma dell'esecuzione di una stampa.

## Regole di acquisizione

- `status: pending`: nessuna stampa fisica attestata. I valori in `slicing_estimate` sono **stime di slicing**, non consuntivi.
- `actual_print`: compilare soltanto con misurazioni e log della stampa effettivamente eseguita. Lasciare `null` per dati mancanti; `0` significa zero verificato.
- Salvare per ogni piatto materiale, profilo/versione dello slicer, eventuale identificativo della stampante, durata effettiva, massa consumata, esito e scarti.
- Conservare separatamente tentativi e ristampe; non sovrascrivere la storia e non sommare scarti due volte. Precisare se massa consumata include gli scarti.
- Associare esportazioni e log dello slicer, log stampa, pesature e fotografie solo quando disponibili; anonimizzare informazioni personali e percorsi locali prima del commit.
- La massa scartata dello slicing può rappresentare supporti, purge o altra categoria: non assegnarle una categoria senza prova.

## Consuntivo

Aggregare le durate e masse effettive **solo** dai tentativi eseguiti con valori noti, indicandone sempre il numero. Riportare separatamente le somme delle stime dello slicer e i valori non disponibili. Elencare tutti i piatti pending senza attribuire esito PASS/FAIL. Prima di dichiarare completo il consuntivo, confrontare il registro con l'elenco canonico dei piatti previsti da RTARS-32 e riconciliare anche ristampe o tentativi parziali.

## Stato acquisizione (2026-11-22)

Riepilogo fotografico dello slicer acquisito per **4 piatti**. Le durate sono PLATE-01 59m14s, PLATE-02 2h14m, PLATE-03 4h1m, PLATE-04 4h49m. Somma: **12h03m14s**, mentre il riquadro dello slicer visualizza `12h3m`.

Il riquadro del modello mostra **90.48 m** e **269.85 g** aggregati, più costo `5.63` senza valuta: **non** attribuire massa e costo ai singoli piatti senza dettagli. Il dato precedente di PLATE-01 (63 min) è stato conservato come stima precedente e sostituito dalla nuova evidenza fotografica; i 24.5 g e 0.12 g rimangono precedenti dichiarazioni non corroborate dallo screenshot.

- PLATE-01: `pending` dichiarato dall'utente.
- PLATE-02–04: `unconfirmed` (lo screenshot non prova se siano state stampate).
- Nessun tempo, consumo, scarto o esito effettivo rilevato.
- Materiale non specificato; profilo di PLATE-01 da verificare (nome Elegoo Neptune4 contro Bambu Lab riferito dall'utente).
- Foto originale disponibile solamente nella conversazione; nel repository sono versionate trascrizione e hash SHA-256, non il JPEG.

[Consuntivo provvisorio](summary.md) · [Trascrizione evidenza](evidence/slicer-summary-2026-11-22.md)

## Acceptance criteria (stato parziale)

- Per ogni piatto dati completi: **NOT TESTED** — PLATE-01 pending, PLATE-02–04 non confermati; nessun dato reale.
- Consuntivo aggregato e piatti non eseguiti: **PARTIAL** — struttura pronta; stima aggregata e riepilogo provvisorio prodotti; manca inventario definitivo e consuntivo delle stampe realmente eseguite.
- Artefatto versionato: **PASS sul branch**, merge e ulteriori evidenze ancora da verificare.

Dipendenza di chiusura: RTARS-32, raccolta log effettivi e superamento DoD.
