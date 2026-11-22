# RTARS-34 — Trascrizione riepilogo slicer (2026-11-22)

**Origine:** fotografia di un riepilogo di slicing, inviata dall'utente nella conversazione RTARS-34. La fotografia originale **non è stata caricata su GitHub**; questo documento è una trascrizione dei valori leggibili, non un export dello slicer né una prova di stampa fisica. Nessuna identità, percorso locale o altro metadato personale è trascritto.

**SHA-256 JPEG originale ricevuto:** `7a71943da07bf84a3ed422f615ed743423e0e6be687137181eac01a324f13616`. L'hash identifica il file ricevuto ma **non ne rende disponibili i byte nel repository**.

## Statistiche visibili sullo schermo

| Campo del riepilogo | Valore visualizzato | Nota |
| --- | --- | --- |
| Filament | 1 | Numero slot, materiale non indicato |
| Model — filament length | 90.48 m | Totale mostrato, non per piatto |
| Model — mass | 269.85 g | Massa del modello aggregata, **non** massa totale effettiva consumata |
| Total cost | 5.63 | Unità monetaria non visibile |
| Plate 1 | 59m14s | 3,554 secondi |
| Plate 2 | 2h14m | 8,040 secondi |
| Plate 3 | 4h1m | 14,460 secondi |
| Plate 4 | 4h49m | 17,340 secondi |
| Total | 12h3m | Visualizzazione del software, apparentemente arrotondata ai minuti |

**Controllo matematico:** 3,554 + 8,040 + 14,460 + 17,340 = 43,394 s = **12h03m14s**. Differenza di 14 s rispetto al totale visualizzato arrotondato ai minuti; nessuna incongruenza significativa dimostrata.

## Riconciliazione PLATE-01

Il wizard precedente dichiarava **63 minuti**, **24.5 g** e **0.12 g scarti**. La fotografia permette di correggere solamente la **durata stimata** di PLATE-01 a **59m14s** (scarto tra le due stime: **3m46s**). La fotografia **non mostra** né i 24.5 g né gli 0.12 g associati a PLATE-01: tali valori restano dichiarazioni precedenti non corroborate dallo screenshot, non devono essere sommati o considerati consuntivi fisici.

## Limitazioni / gap

- Non è visibile l'applicazione/edizione/versione esatta dello slicer, né il profilo macchina per ciascun piatto; "Bambu Studio" è dichiarato dall'utente.
- Il nome del profilo già dichiarato per PLATE-01 contiene `Elegoo Neptune4`: occorre verificare corrispondenza alla stampante effettiva.
- Non sono leggibili materiale (PLA/PETG/altro), costo unitario, distribuzione per piatto della massa, tipo/quantità degli scarti o dati di pesatura.
- La foto non documenta l'esecuzione della stampa; tutti e quattro i piatti restano `pending` ai fini della consuntivazione.
- La fotografia e il progetto/export dello slicer restano da archiviare come evidenze binarie (dopo sanitizzazione e controlli di licenza, se pertinenti).
- La presenza di quattro piatti nel riepilogo **non prova** che siano tutti i piatti previsti per RTARS-32: riconciliare con l'inventario canonico.

## Regole di rendicontazione

I dati del riquadro **Model** sono valori aggregati di slicing; non si devono distribuire proporzionalmente ai singoli piatti senza dati per-piatto. Non sommare la massa scartata a quella consumata senza prima definire cosa includa quest'ultima. Valori effettivi di stampa: attualmente **assenti**.
