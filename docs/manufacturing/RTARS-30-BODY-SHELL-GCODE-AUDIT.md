# RTARS-30 / RTARS-31 — Audit statico G-code `body_shell` (2026-11-22)

**Sorgente privata:** file `body_shell.gcode` ricevuto dall'utente (3,136,621 byte, 121,568 righe), SHA-256 `a9a79772de096e8b95d49a76dea16c5df548bd25ac56695a267a5039aabdff11`. **NON pubblicare il G-code**: include istruzioni geometriche/coordinate e thumbnail derivate da modello soggetto a MakerWorld Exclusive. Questa evidenza contiene solo estratti numerici e conclusioni non geometriche; nessuna mesh, thumbnail o toolpath.

## Verifiche estratte dalla sorgente

| Campo / osservazione | Risultato | Valutazione |
|---|---|---|
| Slicer | `BambuStudio 02.08.02.61` | PASS identificazione |
| Printer | `Elegoo Neptune 4`, preset `Elegoo Neptune 4 0.4 nozzle` | PASS nome del preset nel file, non identificazione hardware indipendente |
| Nozzle | `nozzle_diameter=0.4`, `nozzle_type=hardened_steel` | PASS configurazione; materiale fisico già dichiarato in RTARS-29 |
| Process | `RTARS-FUNCTIONAL CANDIDATE 0.20mm @Elegoo Neptune4 0.4 nozzle` | PASS selezione effettiva del candidato nello slicing |
| Filament | `Generic PLA @Elegoo`, PLA 1.75 mm | PASS identificazione; NON è una qualificazione specifica per ELEGOO PLA Metallic Bronze |
| Layer | 0.20 mm standard / 0.12 mm iniziale, 68 layer, Z max 12.72 mm | PASS parametri realmente presenti |
| Temperature | nozzle 210°C primo/205°C altri, bed 60°C | PASS all'interno dei range ELEGOO Metallic (nozzle 190–230, bed 35–65°C); non prova controllo termico fisico |
| Speed | outer wall 35, inner wall 45, first-layer 18 mm/s | PASS corrispondenza ai parametri FUNCTIONAL |
| Acceleration | default 700 mm/s² | PASS configurazione |
| Walls/infill | 3 loops / gyroid 25% | PASS configurazione |
| Supports | `enable_support=1`, `normal(auto)`, threshold 30°, top Z distance 0.2 mm; FEATURE Support (9), Support interface (3), transition (1) | PASS generazione effettiva di sezioni supporto; collocazione/necessità geometrica NOT TESTED |
| G-code | `gcode_flavor=klipper`, `M83` E relativo, `G28` homing, `M190 S60`, `M109 S210`; start purge and end heater/fan shutdown commands present | PASS presenza/forma dei comandi; compatibilità firmware/limiti reali NON certificata |
| X/Y path bounds | X 5.0–167.5 mm; Y 0.0–220.0 mm nei valori emessi dai `G0/G1` | PASS controllo statico dei valori espressi; il movimento in coordinate relative richiede interpretazione e controllo sul firmware per certificazione |
| Duration | 2h22m03s | SLICER ESTIMATE ONLY |
| Filament | 7284.33 mm / 21.73 g, density 1.24 | SLICER ESTIMATE ONLY, not measured mass |
| Model | 68 layers, max Z 12.72 mm | SLICER ESTIMATE ONLY |
| Printed fit/strength | nessuna evidenza fisica | NOT TESTED |

**Avvertenza su header:** `total filament volume [cm^3] : 17520.86` è internamente incoerente con `21.73 g` a `1.24 g/cm³`. Il numero equivale approssimativamente a 17,520.86 **mm³**, ossia 17.52 cm³; non interpretare il campo come 17,520 cm³. Manteniamo massa/filamento come stime dello slicer, non misure.

## Audit del contenuto macchina
- `machine_start_gcode` nel file: reset feed/flow M220/M221; preriscaldo M104; M190 bed; G90; G28; movimenti di posizionamento; M109 nozzle; G92 E0, linea di spurgo.
- `machine_end_gcode` nel file: retrazione, movimento finale X10 Y220, fan M106 S0, nozzle M104 S0, bed M140 S0 e disable motori X/Y/E.
- Nessun `M600` eseguibile osservato (la stringa compare nella sezione di configurazione). Non sono presenti `G2/G3` eseguibili.
- **Non eseguito** G-code su macchina in questa verifica. L'analisi statica non assicura comportamenti Klipper personalizzati, macro o assenza di collisione, soprattutto durante homing/purge/end.

## Decisione RTARS-31
`body_shell` corrisponde alla tipologia P04 (guscio corpo, priorità P1) della classificazione RTARS-28: appropriato come **smoke test di slicing e processo**, ma **non basta** da solo per validare accoppiamenti critici P0 (P01/P05/P08/P13). Inoltre ha una durata stimata >2h: non è un provino minimo di calibrazione.

**Gate per usare un primo provino in RTARS-31:** (1) preset FUNCTIONAL selezionato e letto nel G-code: PASS; (2) temperature PLA conformi in configurazione: PASS documentale; (3) controllo file statico delle istruzioni essenziali e bounds emessi: PASS limitato; (4) controllo di posizionamento supporti e interfacce sul modello locale: NOT TESTED; (5) print e misure con calibro e foto del fit: NOT TESTED. Per gli accoppiamenti P0 è necessario un provino mirato e misure nominali della specifica interfaccia.

Non avviare produzione definitiva RTARS-32 basandosi sul solo G-code.
