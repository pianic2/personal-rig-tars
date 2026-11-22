# RTARS-30 / RTARS-31 — Audit del G-code di 3 parti (2026-11-22)

## Provenienza
File `3_parts.gcode` ricevuto dall'utente in chat. SHA-256 **`32fec82a5f94c0d36b87587c2e853acb7f2462dc7703ec7e0fd6e9e1563a99fa`**; dimensione 5,595,421 byte; 219,663 linee (line-break count). **Il G-code non è pubblicato:** include percorsi, coordinate, identificativi originali e potenzialmente contenuto geometrico soggetto a licenza MakerWorld. L'audit contiene esclusivamente dati di configurazione e misure aggregate.

## Dati estratti direttamente dai commenti e dal blocco macchina
| Campo | Evidenza |
|---|---|
| Slicer | BambuStudio `02.08.02.61` |
| Printer | `Elegoo Neptune 4` / `Elegoo Neptune 4 0.4 nozzle`; nome Standard dichiarato dall'operatore in RTARS-29 |
| Firmware flavor | Klipper |
| Nozzle | `0.4`, `hardened_steel` nei metadati |
| Process realmente impiegato | `RTARS-FUNCTIONAL CANDIDATE 0.20mm @Elegoo Neptune4 0.4 nozzle` |
| Filament | `Generic PLA @Elegoo`, PLA 1.75 mm; Metallic Bronze è il materiale reale dichiarato, non una calibrazione specifica |
| Layer | 0.20 mm standard, 0.12 mm iniziale; **129** layer; Z massimo 19.72 mm |
| Tempo stimato | **2h32m12s** (slicer, NON misura reale) |
| Massa e lunghezza stimate | **20.59 g**, **6903.65 mm** (slicer, NON consumo misurato) |
| Oggetti | **3** distinti nel G-code, rispettivamente una staffa/supporto, una base posteriore dello schermo e una copertura servo (identificazione semantica tradotta dai nomi originali, non accoppiamenti fisici validati) |
| Speed/accel | Outer 35 mm/s; inner 45 mm/s; default acceleration 700 mm/s², outer acceleration 400 mm/s² |
| Walls/infill | 3 loops, 25% gyroid |
| Bed/nozzle setpoint | Bed 60°C, nozzle initial 210°C e altri 205°C, entro le fasce documentali ELEGOO 35–65°C / 190–230°C |
| Supports | `enable_support=1`, `normal(auto)`, threshold 30°, top/bottom Z distance 0.2 mm, interface top layers 3; FEATURE Support 50, Support interface 9, Support transition 5 |
| Altre FEATURES osservate | Floating vertical shell 113; Bridge 49; Overhang wall 39; questi marker **non sono errori certificati** |
| Start/end | `M190`, `M109`, `G28`, spurgo in avvio; `G91`/ritrazione e park finale X10 Y220, spegnimento `M104 S0`, `M140 S0`, `M106 S0` e `M84 X Y E` |

**Nota unità del filamento:** il campo header `total filament volume [cm^3] : 16605.23` è incoerente con massa 20.59 g e densità 1.24 g/cm³: il valore numerico corrisponde approssimativamente a mm³, non cm³. Non usarlo come volume in cm³.

## Cosa dimostra
- **PASS statico**: sono **tre oggetti** nello stesso file, Bambu Studio ha effettivamente prodotto uno slicing col profilo FUNCTIONAL importato, metadati di stampante/filamento coerenti con RTARS-29, supporti generati.
- **PASS documentale**: setpoint di temperatura nei limiti pubblicati dal produttore del filamento.
- **NOT TESTED**: esecuzione reale sulla macchina, accoppiamenti geometrici, dimensioni, velocità effettive, verifica di tutti i percorsi in sistema di coordinate macchina, assenza di interferenze con morsetti/supporti del letto, posizioni esatte dei supporti rispetto alle superfici critiche.
- **NOT TESTED**: un'anteprima Preview con orientamento e supporti motivati per ciascuna parte; l'esistenza del G-code non certifica la qualità dell'orientamento.

## Conclusione per Jira
Questo è un **PASS sostanziale del gate «slicing effettivo con RTARS-FUNCTIONAL» per tre pezzi** e costituisce un dataset valido di partenza per RTARS-31. Non dimostra il requisito RTARS-30 «profili nativi **esportati e versionati**» (attualmente solo ricetta/generatore e digest, i due file JSON completi non sono nel repository) e non copre ancora motivazioni di orientamento/supporto per le altre parti. La DoD richiede tutti gli AC, dunque RTARS-30 **non è ancora READY TO MERGE / Done**.

Non usare G-code, immagini o derivati geometrici nel repository pubblico.
