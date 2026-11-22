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

## PLATE-01

Primo record basato esclusivamente su dati comunicati dall'utente il 2026-11-22: 63 min, 24.5 g e 0.12 g **stimati da slicing Bambu Studio**. Materiale non dichiarato. Il nome profilo contiene `Elegoo Neptune4` mentre l'utente riferisce Bambu Lab: verificare la configurazione della stampante reale e conservare un export del progetto/profilo. Nessuna evidenza tecnica o stampa fisica dichiarata.

## Acceptance criteria (stato parziale)

- Per ogni piatto dati completi: **NOT TESTED** — PLATE-01 pending; nessun dato reale.
- Consuntivo aggregato e piatti non eseguiti: **PARTIAL** — struttura pronta; manca inventario completo e generazione del consuntivo.
- Artefatto versionato: **PASS sul branch**, merge e ulteriori evidenze ancora da verificare.

Dipendenza di chiusura: RTARS-32, raccolta log effettivi e superamento DoD.
