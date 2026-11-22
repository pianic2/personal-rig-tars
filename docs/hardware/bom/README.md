# RTARS-9 — Inventario e riconciliazione BOM RIG-TARS

**Baseline:** `v0.4-owner-correction` (2026-11-22)  
**Jira:** https://niccolopiazzi01.atlassian.net/browse/RTARS-9 — Fatto nel perimetro dell'inventario  
**Pull request:** https://github.com/pianic2/personal-rig-tars/pull/1 — in revisione, non mergiata

## Provenienza e limiti

La BOM distingue:
1. **BOM V1.0 LuwuDynamics** = *distinta tecnica di costruzione* (quantità `qty_expected`), non prova delle quantità garantite nella variante commerciale.
2. **Kit fisico** = fotografia fornita dall'utente e conteggi/identificazioni dichiarati successivamente (`qty_observed`).
3. **Marcature delle confezioni** = testo originale in cinese riportato nel CSV, conservato anche quando differisce dalle dichiarazioni sulle viti.
4. **Verifiche non eseguite** = prove elettriche, compatibilità filettature e viti, revisione elettronica, pinout e batteria.

**Variante acquistata dichiarata:** “RIG Serie Robots: TARS”.  
**Pagina acquisto fornita:** https://shop.xgorobot.com/products/rig-tars-fully-open-source-3d-printed-programmable-ai-companion-robot-maker-diy-kit  
**Distinta tecnica pubblica:** https://wiki.xgorobot.com/kb/pet-tars/cmtvbmd1m00051zasro6ju2aa  
**Assemblaggio:** https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly  
**Upstream firmware:** https://github.com/LuwuDynamics/rig_omni

La revisione complessiva del kit non è indicata sulla confezione. La marcatura PCB `RIG-Board 26/6/2025` è una marcatura/data, **non un numero di revisione dimostrato**.

## Artefatti

- [rig-tars-bom.csv](rig-tars-bom.csv) — 25 righe (17 di riferimento, 8 osservazioni della foto), quantità, stato, marcature e fonte della verifica.
- [discrepancies.csv](discrepancies.csv) — 13 discrepanze storiche, **4 RESOLVED** (D03, D10, D11, D12) e **9 OPEN**.
- [owner-inventory-2026-11-22.md](../../../evidence/hardware/RTARS-9/owner-inventory-2026-11-22.md) — risposte originali Q1–Q16 e **due rettifiche cronologiche**, ultima delle quali prevale sulle precedenti.
- [MANIFEST.md](../../../evidence/hardware/RTARS-9/MANIFEST.md) — metadati e digest SHA-256 della fotografia; la copia originale **non è ancora nel repository**.

### Regole di conteggio

- `qty_expected`: quantità da distinta V1.0, non valore normativo per il kit consegnato.
- `qty_observed`: pezzi visti o dichiarati, oppure 0 se l'utente ne ha esplicitamente dichiarata l'assenza.
- `revision_verified`: vuoto se non esiste prova chiara della revisione; `FCP-HD240239C12-V1` e `HBVCAM-2526 V11` sono codici trascritti, non revisioni automaticamente confermate.
- `evidence_source`: `PHOTO_LABEL`, `PHOTO`, `USER_Qn` oppure `USER_CORRECTION_2026-11-22`.
- **Non sommare gli alias fotografici ai componenti canonici:** `A008=E008` (cavo interruttore); `A004=F002` (gruppo delle quattro viti svasate secondo il proprietario). `A003` è il gruppo distinto di quattro viti a testa tonda, **non** alias F002.
- `F003` è una **specifica della BOM V1.0 non riscontrata fisicamente**: valore osservato 0, non 4.
- La correzione del proprietario sulle viti a croce **non annulla** il dado M2 separato, censito in `A007` e mai esplicitamente ritirato.

## Componenti elettronici e meccanici identificati

| Oggetto | Rilievo del proprietario | Limite |
| --- | --- | --- |
| Scheda principale | 1, `RIG-Board 26/6/2025` | Revisione e equivalenza con RIG-Board0722 sconosciute |
| Display | 1, `FCP-HD240239C12-V1` | Controller ST7789P3 vs ST7789V2 sconosciuto |
| Fotocamera | 1, `HBVCAM-2526 V11` | Sensore ottico non attestato |
| Servo | 3, senza etichette/incisioni | Modello SCS009 non certificabile dalla sola vista |
| Servo horn | 3 | Modello esatto non verificato |
| Altoparlante | 1, senza codice | La sigla 3514 resta solo nella fonte |
| Batteria | 1, senza marcature | Tensione, capacità, chimica, polarità, protezioni non accertate |
| Sensore touch | 1, identificato dal proprietario | Sigla non disponibile |
| Contrappesi | 2, 20 g ciascuno secondo proprietario | Composizione del metallo non misurata |
| Prolunga | 1 | Lunghezza 200 mm non misurata |
| Cavo interruttore | 1, libero senza bustina nella zona inferiore sinistra della foto | `E008=A008`; lunghezza e pinout ignoti |
| Cablaggi neri | 3, con 3 conduttori ciascuno e connettori a incastro | Destinazione/pinout non verificati |
| Spugna isolante | 0 | Assenza rispetto alla fonte tecnica, non necessariamente alla packing list commerciale |

## Minuteria — situazione corretta al 22 novembre 2026

| Categoria | Quantità nel kit, dichiarata | Distinta V1.0 | Note |
| --- | ---: | ---: | --- |
| M2×6 a croce, autofilettanti secondo etichetta | **55** | 60 nella colonna / 52 in descrizione | D01: conflitto nella fonte e scostamento di quantità |
| **M2×4 a croce, testa tonda** | **4** | Non mappabile direttamente | `A003`: etichetta cinese indica testa tonda a croce per macchina, concorde sulla testa |
| **M2×4 a croce, testa svasata** | **4** | F002: 2 svasate autofilettanti | `A004=F002` ai fini dell'inventario; l'etichetta dice autofilettante a croce ma non precisa la testa; filetto da verificare |
| **M2×4 a brugola con frenafiletti** | **0** | F003: 3 | Nessuna vite M2×4 con esagono incassato secondo ultima rettifica del proprietario; D04 OPEN |
| M2×5 testa piatta a croce | **2** | Non riconciliata | `A005`, fonte etichetta |
| M3×8 testa piatta a croce | **1** | F005: 2 M3×10 | Non equivalente a M3×10 (D06) |
| Dado esagonale M2 di bloccaggio | **1** | F006: 2 dadi M3 | È una categoria distinta dalle viti a croce (D07) |
| M2×10 | **0** | F004: 2 | D05 OPEN |
| M3×10 | **0** | F005: 2 | D06 OPEN |
| Dadi autobloccanti M3 | **0** | F006: 2 | D07 OPEN |

**Nota storica fondamentale:** inizialmente le quattro viti M2×4 svasate sono state attribuite per errore alla busta A003, e le quattro viti M2×4 a croce alla categoria “brugola con frenafiletti”. La seconda correzione del proprietario chiarisce: **tutte le M2×4 sono a croce, alcune tonde e alcune svasate, nessuna a brugola**. La classificazione corrente prevale, ma le dichiarazioni originali rimangono archiviate per audit.

### Etichette cinesi — testo, non verifica fisica

| Marcatura della busta | Traduzione tecnica |
| --- | --- |
| `M2*6十字自攻螺丝` | M2×6 autofilettante a croce |
| `M2*4圆头十字机丝` | M2×4 testa tonda a croce per macchina |
| `M2*4十字自攻螺丝` | M2×4 autofilettante a croce (senza specificare testa) |
| `M2*5平头十字机丝` | M2×5 testa piatta a croce per macchina |
| `M3*8平头十字机丝` | M3×8 testa piatta a croce per macchina |
| `M2六角对锁螺母` | Dado esagonale M2 di bloccaggio |

**Testa e impronta della vite non determinano la natura del filetto.** La compatibilità meccanica dei fissaggi è una verifica successiva; non sostituire automaticamente viti o dadi fra specifiche diverse.

## Stato dei gap

**Risolti (4):** D03 (riconciliazione teste tonde/svasate), D10 (conteggi/accessori), D11 (cavo interruttore), D12 (marcatura camera).

**Aperti (9):** D01 (M2×6, 55/60/52), D02 (driver display), D04 (brugola M2×4 non presente), D05 (M2×10 assenti), D06 (M3×10 assenti), D07 (dadi M3 assenti), D08 (batteria senza specifiche), D09 (modello servo e revisione PCB non verificati), D13 (spugna assente).

**Aperto** significa differenza dalla distinta di riferimento o specifica da reperire, **non** dimostrazione che il venditore abbia consegnato un kit incompleto.

## Gate RTARS-9

| AC originale | Esito |
| --- | --- |
| Nome e componenti censiti | PASS: 25 righe, identificatori e fonti |
| Quantità rilevate | PASS nel perimetro dichiarativo: 25/25 campi, alcuni alias da non sommare |
| Revisione registrata se disponibile | PASS: nessuna revisione certificabile; marcature grezze conservate |
| Stato di ogni componente | PASS |
| Differenze annotate | PASS: registro con 13 voci storiche e stato per ciascuna |

**Decisione:** RTARS-9 è `Fatto` come inventario documentale. Restano verifiche prima del montaggio. La fotografia originale è disponibile nella conversazione, con hash registrato, ma **non** come binario nel repo. Nessun merge automatico della PR.

**Sicurezza:** batteria senza parametri noti: non collegare o ricaricare fino a identificazione affidabile. I fissaggi alternativi vanno verificati con la corretta revisione dell'assemblaggio. Nessuna accensione né collaudo eseguito. Le parti stampate appartengono a Epic E04, non sono classificate mancanti dal kit di elettronica.
