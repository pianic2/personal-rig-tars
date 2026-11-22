---
title: "RIG-TARS — Catalogo delle fonti ufficiali"
issue: "RTARS-10"
document_type: "llm-source-index"
language: "it"
verified_on: "2026-11-22"
source_policy: "primary-sources-only"
---

# RIG-TARS — indice della documentazione ufficiale

> **Scopo:** punto d'ingresso per LLM, agenti e sviluppatori. Questo file **indirizza alle fonti**, non sostituisce manuali, disegni, codice o prove hardware. Non è una distinta base né una procedura di cablaggio.
>
> **Task:** [RTARS-10](https://niccolopiazzi01.atlassian.net/browse/RTARS-10) · **Ultima ricognizione:** 2026-11-22 · **Lingua indice:** italiano (fonti EN/ZH).
>
> **Priorità:** (1) revisione effettiva del robot + firmware in uso; (2) sorgente/release **specifico TARS**; (3) manuale TARS corrispondente; (4) firmware multiprodotto RIG-Omni; (5) documentazione del framework/periferica. In caso di conflitto, **non fondere** due procedure.

## Legenda e regole di utilizzo

- **V** = URL e contenuto identificati su una fonte del produttore (o sulla documentazione ufficiale del fornitore del framework) al 2026-11-22. Non significa che siano stati testati su un robot fisico.
- **R** = riferimento ufficiale a un artefatto, **non** prova che l'artefatto scaricabile/revisione hardware sia stato verificato.
- **GAP** = link/file/specifica per TARS non dimostrati. Non trasformare un riferimento in una specifica approvata.
- **Dinamica** = pagina Wiki o branch `main` che può cambiare; usare data e revisione del momento della consultazione.
- **Snapshot** = URL GitHub con SHA fissato; preferibile per citare un'implementazione in un report riproducibile.
- La versione scritta nel file `version.txt` è una **versione del sorgente**, non prova che esista una release binaria con quel numero.
- Ogni conclusione dell'LLM deve distinguere **fatto documentato**, **deduzione**, **verifica sperimentale** e **dato mancante**, riportando almeno URL + versione/SHA + percorso/sezione.
- Non presumere che una scheda o disegno RIG-Puppy, Hover o Arm sia intercambiabile con TARS. Prima di un collegamento elettrico servono pinout e revisione reali della scheda.

## Baseline verificata

| Aspetto | Evidenza / versione al 2026-11-22 | Fonte |
| --- | --- | --- |
| Piattaforma | ESP32-S3; display TARS 320×240; 3 servocomandi bus SCS009 | [Wiki TARS](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_overview), [RIG-Omni README](https://github.com/LuwuDynamics/rig_omni/blob/main/README.md) |
| Firmware TARS dedicato | `LuwuDynamics/rig_tars_rl`, `main` = `456e3ee95ccbe94deae9484568719e8686b4b68b`; `main/boards/tars/version.txt` = **3.8.1** | [Snapshot](https://github.com/LuwuDynamics/rig_tars_rl/tree/456e3ee95ccbe94deae9484568719e8686b4b68b), [version.txt](https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/main/boards/tars/version.txt) |
| Release binaria TARS | **v3.8.1**, pubblicata **2026-11-11**; archivi separati `cn` e `gb` | [Release ufficiale](https://github.com/LuwuDynamics/rig_tars_rl/releases/tag/v3.8.1) |
| Firmware multiprodotto | `LuwuDynamics/rig_omni`, `main` = `c2b42cd73ef65f5cd2a158d6949f0273869454dc`; TARS `version.txt` = **3.8.0** | [Snapshot](https://github.com/LuwuDynamics/rig_omni/tree/c2b42cd73ef65f5cd2a158d6949f0273869454dc), [version.txt](https://github.com/LuwuDynamics/rig_omni/blob/c2b42cd73ef65f5cd2a158d6949f0273869454dc/main/boards/tars/version.txt) |
| Toolchain documentata | **ESP-IDF 5.5.3** per TARS; eventuali versioni più recenti richiedono validazione separata | [README TARS](https://github.com/LuwuDynamics/rig_tars_rl/blob/main/README.md), [Espressif docs 5.5.3](https://docs.espressif.com/projects/esp-idf/en/v5.5.3/esp32s3/) |
| Materiale meccanico citato | BOM cinese **V1.0**; sorgenti nominati `tars.SLDASM`, `tars.STEP` e profilo di stampa `tarsV3.3mf`. Disponibilità/download e compatibilità con il kit **non accertati** | [BOM ufficiale TARS](https://wiki.xgorobot.com/kb/pet-tars/cmtvbmd1m00051zasro6ju2aa), [Stampa 3D](https://wiki.xgorobot.com/kb/pet-tars/ce6c7c0540e8ab67a56cbbe5f) |

**Distinzione essenziale tra firmware:** `rig_tars_rl` non è semplicemente un alias di `rig_omni`. Il primo documenta recupero cadute con PPO, mantenimento heading via IMU, simulazione MuJoCo, 21 azioni, versione 3.8.1 e specifici flussi di reset/calibrazione. Il secondo è la base multiprodotto 3.8.0 della documentazione internazionale precedente. **Non mischiare comandi, configurazioni, pacchetti firmware, gestione touch o calibrazione senza identificare la variante in esecuzione.**

## Indice per argomento

### A. Sorgenti, release, compilazione e diagnostica

| ID | Fonte ufficiale | Versione / stato | Quando consultarla |
| --- | --- | --- | --- |
| **FW-01** | [README — rig_tars_rl](https://github.com/LuwuDynamics/rig_tars_rl/blob/main/README.md) | **V**, TARS 3.8.1, EN; dinamica | **Prima scelta** per firmware dedicato TARS, funzioni, build, flash e diagnosi |
| **FW-02** | [README_CN — rig_tars_rl](https://github.com/LuwuDynamics/rig_tars_rl/blob/main/README_CN.md) | **V**, TARS 3.8.1, ZH; dinamica | Conferma dei flussi regionali CN/Global e terminologia originale |
| **FW-03** | [Release TARS v3.8.1](https://github.com/LuwuDynamics/rig_tars_rl/releases/tag/v3.8.1) | **V**, 2026-11-11; versione fissata | Release note e pacchetti ufficiali `rig-tars-3.8.1-cn.zip` / `rig-tars-3.8.1-gb.zip` |
| **FW-04** | [Sorgente TARS 3.8.1 (snapshot)](https://github.com/LuwuDynamics/rig_tars_rl/tree/456e3ee95ccbe94deae9484568719e8686b4b68b/main/boards/tars) | **V**, SHA `456e3ee95ccbe94deae9484568719e8686b4b68b` | Comportamento effettivo di board, motori, movimento, calibrazione e UI |
| **FW-05** | [Tool seriali TARS](https://github.com/LuwuDynamics/rig_tars_rl/blob/main/tools/tars_log/README.md) | **V**, 3.8.1; dinamica | Build/flash assistiti, interrogazione ID servo, tensione bus, stati ed errori |
| **FW-06** | [RIG-TARS training e simulazione](https://github.com/LuwuDynamics/rig_tars_rl/blob/main/tars_rl/README.md) | **V**, 3.8.1; dinamica | MuJoCo, modello MJCF, calibrazione servo, PPO, checkpoint, esportazione pesi |
| **FW-07** | [Documentazione embedded del repository TARS](https://github.com/LuwuDynamics/rig_tars_rl/tree/main/docs/content) | **V**, dinamica | Architettura, hardware, MCP, display, audio, reti, API, sviluppo e troubleshooting; **controllare codice/revisione** |
| **FW-08** | [README — RIG-Omni multiprodotto (snapshot)](https://github.com/LuwuDynamics/rig_omni/blob/c2b42cd73ef65f5cd2a158d6949f0273869454dc/README.md) | **V**, TARS nel sorgente = 3.8.0, EN | Architettura multiprodotto, Kconfig, moduli condivisi; non assumere parità con FW-01 |
| **FW-09** | [Sorgente TARS 3.8.0 (snapshot RIG-Omni)](https://github.com/LuwuDynamics/rig_omni/tree/c2b42cd73ef65f5cd2a158d6949f0273869454dc/main/boards/tars) | **V**, SHA `c2b42cd73ef65f5cd2a158d6949f0273869454dc` | Confrontare firmware precedente e modifiche compatibilità |
| **FW-10** | [ESP-IDF Programming Guide — ESP32-S3 v5.5.3](https://docs.espressif.com/projects/esp-idf/en/v5.5.3/esp32s3/) | **V**, versione SDK fissa, Espressif | Toolchain, periferiche, flash, debug, FreeRTOS; non sostituisce il pinout del robot |
| **FW-11** | [TARS — Development (Wiki EN)](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_develop) | **V**, Wiki dinamica, EN | Esercizi, setup e navigazione sorgenti; esempi principalmente RIG-Omni: ricontrollare con FW-01 |
| **FW-12** | [TARS — 二次开发 (Wiki ZH)](https://wiki.xgorobot.com/kb/pet-tars/cmtwvlwmm003k12zs8zkaq5j7) | **V**, Wiki dinamica, ZH | Guida sviluppo cinese che rimanda esplicitamente a `rig_tars_rl` |
| **FW-13** | [Versions and source notes](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_versions) | **V**, Wiki dinamica, EN | Distinguere versione sorgente, release pubblicata e pacchetto da flash |
| **FW-14** | [Luwu Tools — web flasher](https://tools.xgorobot.com/) | **V**, servizio dinamico | Accesso al flasher; scegliere **modello e lingua/regione** con attenzione |
| **FW-15** | [Firmware installation and recovery](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_firmware) | **V**, Wiki dinamica, EN | Flusso generale di flashing e recupero, requisiti USB |
| **FW-16** | [Development environment and build](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_development) | **V**, Wiki dinamica, EN | Installazione e build di riferimento; per 3.8.1 dare precedenza a FW-01 |

**Mappa per leggere il codice:** nel repository **effettivamente selezionato** partire da `main/boards/tars/tars_board.cc` (inizializzazione/MCP), `board_config.h` (pin e display), `robot.cc` (zeri, calibrazione), `robot_action.cc` (movimenti), `motor.cc` e `main/boards/common/motors/` (bus), `tars_display.cc` (terminale), `main/mcp_server.cc` (tool). Per l'RL leggere `tars_rl/model/` e `tars_rl/README.md`. **Verificare sempre l'esistenza dei percorsi nel commit indicato**, senza dedurre che due repository contengano identici file.

### B. Hardware, montaggio, calibrazione e uso

| ID | Fonte ufficiale | Versione / stato | Quando consultarla |
| --- | --- | --- | --- |
| **HW-01** | [RIG-TARS — Overview](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_overview) | **V**, Wiki dinamica, EN | Specifiche generali, ESP32-S3, display, interfacce, configurazione base |
| **HW-02** | [RIG-TARS — Kit assembly](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly) | **V**, Wiki dinamica, EN | **Percorso di riferimento**: test elettronica → flash ufficiale → montaggio → calibrazione; contiene video/immagini |
| **HW-03** | [RIG-TARS — Quick start](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_start) | **V**, Wiki dinamica, EN | Primo avvio, associazione, calibrazione e troubleshooting iniziale |
| **HW-04** | [RIG-TARS — Everyday use](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_daily) | **V**, Wiki dinamica, EN | Controlli fisici, telemetria, agenti, modalità conversazione/telecomando |
| **HW-05** | [RIG-TARS — Troubleshooting](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_faq) | **V**, Wiki dinamica, EN | Diagnosi TARS specifica, calibrazione e recovery |
| **HW-06** | [TARS — Terminal display](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_terminal) | **V**, Wiki dinamica, EN | ST, BAT, V, M1–M3, IMU, log animato, honesty/humor |
| **HW-07** | [RIG-TARS — BOM, fase 1 (中文)](https://wiki.xgorobot.com/kb/pet-tars/cmtvbmd1m00051zasro6ju2aa) | **V**, **documento V1.0**, ZH | Parti elettroniche, SCS009 ×3, viteria, quantità dichiarate, origine CAD; **non** sostituisce verifica RTARS-9 |
| **HW-08** | [RIG-TARS — stampa 3D, fase 2 (中文)](https://wiki.xgorobot.com/kb/pet-tars/ce6c7c0540e8ab67a56cbbe5f) | **V**, profilo citato `tarsV3.3mf`, ZH | Nomi/quantità dei pezzi, parametri Bambu Studio e layout quattro piatti |
| **HW-09** | [RIG-TARS — FAQ (中文)](https://wiki.xgorobot.com/kb/pet-tars/c4870babda29d9f453541d023) | **V**, Wiki dinamica, ZH | Verifiche su stampa, viteria e uso in edizione cinese |
| **HW-10** | [LuwuDynamics — pagina prodotto TARS](https://shop.xgorobot.com/products/rig-tars-fully-open-source-3d-printed-programmable-ai-companion-robot-maker-diy-kit) | **V**, catalogo dinamico | Identificazione commerciale kit/variante, **non** specifica elettrica certificata |

**Attenzione alla revisione:** il manuale inglese di primo avvio indica esplicitamente che la documentazione pubblica non specifica una sequenza pin-per-pin completa né una mappa verificata degli ID di ogni giunto. Le immagini di test preassemblaggio non sono lo schema di cablaggio completo. Evitare di attivare motori finché assemblaggio, alimentazione, IDs e procedura di calibrazione non corrispondono all'hardware posseduto.

### C. CAD, modelli 3D e schemi elettrici

| ID | Fonte | Versione / stato | Limitazione |
| --- | --- | --- | --- |
| **CAD-01** | [Guida ufficiale stampa TARS](https://wiki.xgorobot.com/kb/pet-tars/ce6c7c0540e8ab67a56cbbe5f) | **V**, `tarsV3.3mf` citato, Bambu Studio 02.07.01.57 | **Guida verificata**, **download 3MF non verificato** |
| **CAD-02** | [Guida BOM TARS](https://wiki.xgorobot.com/kb/pet-tars/cmtvbmd1m00051zasro6ju2aa) | **V**, V1.0; cita `tars.SLDASM` / `tars.STEP` | L'esistenza dei nomi in una guida **non prova** disponibilità pubblica dei sorgenti CAD |
| **CAD-03** | [Directory MakerWorld LuwuDynamics](https://makerworld.com/en/@LuwuDynamics) | **R**, profilo segnalato dalla Wiki ufficiale | Non è stato verificato un **singolo modello TARS** proveniente da questo profilo né la revisione, la licenza o il suo contenuto |
| **CAD-04** | [RIG Series Design Files — risorse comuni](https://wiki.xgorobot.com/kb/common-resources-en/dc036a811b7b5b80ebb8cef0f) | **V**, Wiki dinamica | La pagina dichiara applicabilità **Puppy / Hover / Arm**, **non TARS**; non usarla come attestazione di STL/STEP TARS |
| **CAD-05** | [RIG Series Driver Board Schematic](https://wiki.xgorobot.com/kb/common-resources-en/e83d2b6f9491257670d2b05d2) | **V**, schemi **v2026.09.22** | Sono dichiarati per **Puppy** e **Hover+Arm**; **nessuno schema TARS** dimostrato |
| **CAD-06** | [Modello MuJoCo nel repository TARS](https://github.com/LuwuDynamics/rig_tars_rl/tree/main/tars_rl/model) | **V**, sorgente simulazione 3.8.1 | MJCF/mesh per simulazione: **non** assumere che siano STL per fabbricazione o disegni esecutivi |

Il catalogo **non** attribuisce a LuwuDynamics modelli ospitati da account terzi. Prima di scaricare, stampare o redistribuire STL/3MF verificare **autore, revisione, contenuti e licenza** della pagina MakerWorld del singolo modello. La licenza Apache-2.0 del firmware **non concede automaticamente** diritti identici sulle parti 3D.

### D. Risorse di piattaforma / rinvii

| ID | Fonte ufficiale | Versione / stato | Uso |
| --- | --- | --- | --- |
| **GEN-01** | [RIG Series — documentation hub](https://wiki.xgorobot.com/kb/the-rig-series-robot) | **V**, Wiki dinamica | Elenco dei manuali EN e relativi percorsi TARS |
| **GEN-02** | [Downloads and resources](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_downloads) | **V**, Wiki dinamica | Punto di ingresso a flashing, app, sorgenti e risorse meccaniche |
| **GEN-03** | [Common Resource Library](https://wiki.xgorobot.com/kb/common-resources-en) | **V**, Wiki dinamica | Risorse trasversali con **ambito di applicazione da controllare** |
| **GEN-04** | [Shared troubleshooting](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_troubleshooting) | **V**, Wiki dinamica | Problemi comuni alla serie, subordinati a HW-05 |
| **GEN-05** | [Display, sound and resource management](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_resources) | **V**, Wiki dinamica | Risorse display/audio; TARS usa layout distinto |
| **GEN-06** | [TARS — versione cinese / indice](https://wiki.xgorobot.com/kb/pet-tars) | **R**, indice per navigazione | Individuare eventuali nuove fasi di assemblaggio cinese e le revisioni più recenti |

## Instradamento per agenti LLM

Per domande dell'utente, usare **prima** l'ID indicato; approfondire solo se serve.

| Domanda / parole chiave | Aprire prima | Poi, se necessario |
| --- | --- | --- |
| versione, binary, update, region, download | FW-01 → FW-03 → FW-04 | FW-08 → FW-13 |
| compilazione, toolchain, sdkconfig, ESP-IDF | FW-01 → FW-10 → FW-05 | FW-11 / FW-16 |
| collegamenti, pin, cablaggio, servo ID | HW-02 → HW-03 → FW-04 | HW-07; **GAP** per schema TARS |
| distinta base, quantità, viteria | HW-07 → HW-08 | RTARS-9 nel repo, quando disponibile |
| STL, STEP, stampa, slicing, geometrie | CAD-01 → CAD-02 → CAD-03 | CAD-06 soltanto per simulazione |
| boot, pairing, Wi-Fi, reset, touch | FW-01 → HW-03 → HW-05 | HW-04; verificare variante firmware |
| display, status, honesty/humor | HW-06 → FW-04 | HW-04 |
| servo, gait, recovery, heading, IMU | FW-01 → FW-04 → FW-06 | FW-05 |
| voce, LLM, MCP, integrazioni | FW-01 → FW-07 → FW-04 | HW-04 |
| errore di compilazione, seriale, flash | FW-05 → FW-01 → HW-05 | FW-10 |
| differenze vecchio/nuovo firmware | FW-01 → FW-08 | confrontare entrambi gli SHA |

**Procedura obbligatoria di recupero:**

1. Identificare **modello + revisione hardware + firmware installato + regione**. Se sconosciuti, marcare i risultati come condizionali.
2. Selezionare la categoria/ID. Accedere alla **fonte originale**, non inferire dettagli soltanto da questa tabella.
3. Per codice/configurazione, leggere file reali alla versione/SHA selezionati; per Wiki dinamica registrare data di accesso.
4. Prima di proporre azioni fisiche, incrociare manuale, schema **TARS-specifico** e osservazione del kit; se manca una prova, fermarsi.
5. Riportare nell'output: `source_id`, URL, versione/SHA, sezioni/righe esaminate, eventuali contraddizioni e dati non verificati.
6. **Mai** interpretare `main` come stabile nel tempo, né dedurre che il firmware attivo coincida con l'ultima release online.

Esempio di richiesta per un altro agente:

~~~text
Consulta docs/references/OFFICIAL_SOURCES_INDEX.md. Risolvi prima la
versione reale del firmware e la revisione hardware; scegli gli ID
delle fonti pertinenti; apri le fonti primarie e restituisci per ogni
affermazione URL, source_id, versione/SHA e stato di verifica.
Non usare schemi Puppy/Hover/Arm per TARS e non inventare pin/servo ID.
~~~

## Gap e conflitti da mantenere visibili

| ID | Gap / conflitto | Conseguenza e criterio di chiusura |
| --- | --- | --- |
| **G-01** | Modello MakerWorld **specifico TARS**, provenienza, revisione, checksum e licenza **non verificati** | La guida CAD è indicizzata, ma non va dichiarato completato il requisito di un **download di modello 3D TARS verificato** senza identificare e aprire l'asset originale |
| **G-02** | Schemi elettrici in GEN-03/CAD-05 escludono TARS; assente pinout approvato per la revisione reale | Ottenere disegno elettrico/BOM kit del produttore e confermare codice scheda e revisione, senza riutilizzare lo schema di altri modelli |
| **G-03** | Wiki EN costruita attorno a `rig_omni` 3.8.0; README dedicato TARS e Wiki ZH trattano `rig_tars_rl` 3.8.1 | Applicare sempre la documentazione della **variante realmente in uso**; non fondere procedure touch, reset, calibrazione e flash |
| **G-04** | Wiki BOM/print cita file `tars.STEP`, `tars.SLDASM`, `tarsV3.3mf` ma non è stato verificato un URL di download dei singoli file | Acquisire manifest ufficiale e controllare compatibilità dimensionale/revisione prima di stampe o CAD |
| **G-05** | Versioni dei manuali dinamici spesso non esplicite | `verified_on` = data della ricognizione, **non** versione della pagina. Registrare aggiornamento e checksum al prossimo riesame |
| **G-06** | Nessuna prova di build/flash e funzionamento su un robot reale in questa task | La verifica dell'URL **non** soddisfa test di integrazione hardware; mantenere separata dai gate delle task successive |

## Manutenzione del catalogo

- Aggiornare `verified_on` solo dopo aver ripetuto la verifica delle fonti interessate; quando cambia `main`, archiviare il vecchio SHA nelle note/PR.
- Non aggiornare automaticamente il baseline SDK al rilascio di una versione più recente: fare prima un test dedicato di build e compatibilità.
- Aggiungere una riga per ogni nuova fonte con ID stabile, URL **diretto**, lingua, versione/revisione, grado di verifica e utilità.
- Per cambiamenti di comportamento (reset, motori, pin, alimentazione), aprire un issue di verifica e mantenere la vecchia evidenza tracciabile.
- Preferire **link** e piccole annotazioni anziché copiare manuali, file 3D, PDF o contenuti soggetti a licenze distinte.

**Limite della ricognizione:** sono stati verificati contenuti/documenti delle fonti citate, file e release GitHub; **non** è stato effettuato download o audit dei binari, della meccanica e della licenza dei modelli 3D, né alcuna prova fisica sul kit.
