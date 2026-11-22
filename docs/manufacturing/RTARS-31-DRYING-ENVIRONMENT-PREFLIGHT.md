# RTARS-31 — Lotto pilota di tre pezzi: condizioni filamento e ambiente (2026-11-22)

## Provenienza e limiti
Le misure riportate di seguito sono **dichiarazioni dell'operatore**, non misure eseguite dall'autore del documento. La lettura del sensore interno dell'essiccatore esprime **umidità relativa dell'aria nella camera**, non percentuale di acqua nel filamento. Nessun log storico della temperatura, certificazione del sensore o massa pre/post essiccazione è stato fornito. Non si attesta un'essiccazione perfetta o qualificazione materiale completa.

| Campo | Valore | Tipo di evidenza |
|---|---:|---|
| Materiale | ELEGOO PLA Metallic Metal Bronze | Identificazione già documentata in RTARS-29 |
| Essiccazione filamento | **4 ore** | Dichiarazione operatore |
| Setpoint essiccazione | **45 °C** | Dichiarazione operatore; stabilità/lettura termica non dimostrata |
| Umidità relativa nella camera di essiccazione, al momento della lettura | **15% RH** | Dichiarazione operatore |
| Umidità relativa dell'aria nella stanza di stampa | **65% RH** | Dichiarazione operatore |
| Temperatura ambiente stanza di stampa | **25 °C** | Dichiarazione operatore |
| Tipo/modello essiccatore e supervisione | **Non comunicati** | Non inferire |
| Peso e contenuto d'acqua reale del filamento | **Non misurati** | NOT TESTED |
| Tempo tra estrazione dalla camera e inizio stampa | **Non comunicato** | NOT TESTED |

### Valutazione tecnica
- Il valore **15% RH** è coerente con una camera d'aria molto asciutta al momento della lettura, ma **non prova** che la bobina intera abbia raggiunto l'equilibrio igrometrico: l'essiccazione dipende da durata, temperatura reale, massa/geometria bobina e circolazione d'aria.
- **65% RH, 25 °C** in stanza descrivono un ambiente relativamente umido rispetto alla camera di essiccazione. Minimizzare l'esposizione all'aria tra essiccazione e utilizzo; preferire alimentazione diretta dal drybox se sicura e compatibile con il percorso filamento, oppure trasferire subito la bobina e mantenere asciutto il residuo.
- La termocamera del dryer e la camera di stampa non sono la stessa cosa; non confondere i due numeri. Non impostare «moisture = 15%» su alcun record del materiale.
- RTARS-30 è chiusa su `main` (PR #28 merged), due preset nativi versionati. G-code target `3_parts.gcode` SHA-256 `32fec82a5f94c0d36b87587c2e853acb7f2462dc7703ec7e0fd6e9e1563a99fa`. **Non allegarlo**: contains MakerWorld-licensed derived geometry.
- Slicer estimate: **2h32m12s**, **20.59 g**, three parts; values not actual print results. Profile `RTARS-FUNCTIONAL CANDIDATE 0.20mm`, Generic PLA @Elegoo; nozzle 210°C first layer/205°C subsequent; bed 60°C. Machine `ELEGOO Neptune 4 Standard`, 0.4 mm hardened steel per RTARS-29 declaration.

## Gate pre-stampa (da verificare localmente)
1. La bobina è utilizzata da un drybox adatto o trasferita alla stampante con minima esposizione all'aria umida. La gestione della bobina non ostacola trascinamento o estrusione.
2. Piatto e ugello puliti, superficie corretta, livello/Z-offset e homing verificati, piatto libero da impedimenti/morsetti sul percorso. Condizione meccanica e ventole normali.
3. Il file caricato sulla macchina è quello del lotto di tre parti (hash locale confrontato se disponibile); stampante identifica e carica il G-code corretto per Klipper/Neptune 4 Standard.
4. L'operatore **presidia** home, purge e primo layer: nessuna collisione, distacco o estrusione anomala. Arrestare in caso di errore. Nessuna stampa notturna non supervisionata.
5. Registrare `started_at` e stato del primo layer; poi durata effettiva, esito di ogni pezzo, eventuali difetti (stringing, bolle, popping, adesione, qualità supporti), masse/scarti se misurabili.
6. Dopo raffreddamento, misurare quote funzionali **nominali dal modello locale** e reali con calibro, registrare differenze per parte e fit senza forzature. Non inventare quote, tolleranze o risultati.

## Matrice stato
| Gate | Stato |
|---|---|
| Precedente profilo RTARS-30 versionato e Preview lotto 3 pezzi | PASS (evidenze RTARS-30) |
| Essiccazione dichiarata e misure RH/ambiente acquisite | PASS (dichiarazioni operatore, senza certificazione sensori) |
| Filamento pienamente asciutto a livello materiale | NOT TESTED |
| Preflight macchina immediatamente prima della stampa (5 controlli della checklist operatore) | PASS — attestazione operatore 2026-11-22; non misura strumentale indipendente |
| Avvio, primo layer e stampa effettiva | NOT TESTED |
| Misure, fotografie, fit test e correzioni tracciate | NOT TESTED |
| Jira RTARS-31 Done | NON AUTORIZZATO |

Nessuna stampa viene dichiarata avviata o completata in questa evidenza.

## Attestazione preflight acquisita — 2026-11-22

L'operatore ha dichiarato **PASS** per tutti e cinque i controlli della checklist interattiva del lotto da tre pezzi:
1. Piatto pulito, libero da ostacoli e correttamente livellato.
2. Ugello e percorso filamento senza impedimenti.
3. G-code corretto per Neptune 4 Standard e lotto tre pezzi.
4. Setpoint confermati: 210/205 °C ugello, 60 °C piano.
5. Possibilità di presidiare homing, spurgo e primo layer.

**Ambito esatto dell'attestazione:** checklist completata prima dell'avvio. L'operatore scrive «Procedo ad avviare», non conferma che la macchina sia già partita. Conseguentemente `started_at`, G-code eseguito, homing effettivo, purge e primo layer restano **NOT TESTED**. Il controllo n. 5 riguarda disponibilità alla supervisione, non avvenuta supervisione.

Prossima fonte: [protocollo primo layer](RTARS-31-FIRST-LAYER-RUNBOOK.md).
