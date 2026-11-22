# RTARS-9 — Verifica incrociata delle discrepanze (22 novembre 2026)

## Scopo della revisione

È stata svolta una ricognizione delle **9 discrepanze OPEN** dopo l'audit v0.4 del kit RIG-TARS. Obiettivo: cercare fonti ufficiali per classificare con accuratezza ogni difformità e distinguere quanto sia **risolvibile per documentazione** da quanto esiga **conferma del venditore / ispezione fisica / validazione hardware**.

**Non è stata eseguita alcuna prova elettrica, ricarica, flashing o assemblaggio.** Non si è ricevuta una packing list SKU-specifica né un documento del produttore che identifichi la revisione del kit consegnato. Il mero confronto con una *BOM di replica* non autorizza a qualificare la confezione commerciale come incompleta.

## Livelli di evidenza

- **E1 — Fotografia e conteggio proprietario:** vedi `../../../evidence/hardware/RTARS-9/owner-inventory-2026-11-22.md`, incluse rettifiche cronologiche.
- **E2 — LuwuDynamics, distinta per replicare il robot:** https://wiki.xgorobot.com/kb/pet-tars/cmtvbmd1m00051zasro6ju2aa . È una BOM costruita a partire dal montaggio tars.SLDASM / tars.STEP / tarsV3.3mf. Non fornisce una lista certificata del contenuto dell'ordine.
- **E3 — LuwuDynamics, FAQ TARS (viti):** https://wiki.xgorobot.com/kb/pet-tars/c4870babda29d9f453541d023 . Conferma M2×6 `60` e le altre tipologie di viti della distinta tecnica.
- **E4 — LuwuDynamics, overview/firmware:** https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_overview e https://github.com/LuwuDynamics/rig_omni . Per TARS indicano display `ST7789V2` 320×240 e 3 servomotori `SCS009`.
- **E5 — LuwuDynamics, assemblaggio e manuale:** https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly e https://www.xgorobot.com/manual-tars.html . Indicano di rispettare revisione, disegni e orientamento dei connettori; descrivono il processo di alimentazione/ricarica ma **non** identificano tensione e capacità del pacco consegnato.
- **E6 — LuwuDynamics, schemi condivisi:** https://wiki.xgorobot.com/kb/common-resources-en/e83d2b6f9491257670d2 . La pagina dichiara applicabilità a **Puppy, Hover e Arm**: **non** costituisce uno schema certificato della RIG-Board TARS acquistata.
- **E7 — Variante commerciale riferita dal proprietario:** https://shop.xgorobot.com/products/rig-tars-fully-open-source-3d-printed-programmable-ai-companion-robot-maker-diy-kit . La pagina identifica la famiglia di prodotto, ma non prova la packing list del singolo kit consegnato.

## Audit per ogni discrepanza OPEN

| ID | Fatti accertati dalle fonti | Cosa è ancora da dimostrare | Esito |
| --- | --- | --- | --- |
| **D01** | FAQ e tabella viti indicano **60** M2×6; la denominazione originale dice **52**; l'utente ne ha contate **55** | Quante ne richieda la revisione fisica e quante siano garantite con lo SKU | **OPEN** · quantità effettiva insufficienza non dimostrata |
| **D02** | BOM replica = `ST7789P3`; documentazione TARS + firmware = `ST7789V2` 320×240; flat fisico = `FCP-HD240239C12-V1` | Driver montato nel display consegnato e inizializzazione corretta | **OPEN** · incoerenza documentale certa, driver hardware ignoto |
| **D04** | BOM replica = **3** M2×4 a brugola pretrattate **per fissaggio servo**; utente = **0** a brugola | Se il kit aggiornato preveda M2×4 Phillips o sia stata omessa la minuteria necessaria | **OPEN** · montaggio servo non validato |
| **D05** | BOM replica = **2 gruppi** “hex lock screw”, specifica M2×10 e descrizione che cita anche M2×4 esagonali, per **collegamenti meccanici**; utente = 0 M2×10 | Composizione del gruppo, standard esatto e fasteners del collegamento nel kit corrente | **OPEN** · descrizione gruppo da chiarire |
| **D06** | BOM replica = **2** M3×10 a croce testa tonda per **piattaforma hardware**; utente = 0 M3×10, **1** M3×8 piatta a croce | Geometria dei supporti e vite prevista dalla revisione commerciale | **OPEN** · sostituzione non autorizzata |
| **D07** | BOM replica = **2** dadi autobloccanti M3 per **piattaforma hardware**; utente = 0 M3 e **1** dado M2 | Se M3 siano necessari o rimossi nella revisione, e conferma di ciascun punto di fissaggio | **OPEN** · M2 ≠ M3 |
| **D08** | Batteria del kit fisico senza marcature; il manuale TARS descrive carica/LED ma non garantisce **V, mAh, chimica, BMS, pinout/polarità** del singolo pacco | Identificazione tramite scheda tecnica e cablaggio del produttore | **OPEN — SAFETY BLOCKER**, non collegare né caricare |
| **D09** | Marcatura PCB `RIG-Board 26/6/2025`, nessuna rev. dichiarata; servo non marcati; distinta/firmware dichiarano 3 SCS009; schemi pubblici comuni **non includono** TARS | Revisione concreta, connettori e servo effettivi | **OPEN** · non attribuire per somiglianza |
| **D13** | La BOM replica prevede una spugna isolante sagomabile per **ammortizzazione e isolamento**; utente ne dichiara 0 | Inclusione nello SKU, posizione e proprietà minime del materiale (se richiesto) | **OPEN** · la funzione isolante non va improvvisata |

### Riscontri aggiuntivi

1. La FAQ ufficiale risolve **la sola ambiguità documentale 52/60** a favore di un **riferimento di 60**, ma **non** dimostra che i 55 pezzi ricevuti siano sufficienti. Pertanto D01 resta aperta e la BOM non va riscritta con la quantità 55 come riferimento ufficiale.
2. L'overview e il firmware confermano **quale configurazione software è pubblicamente prevista** per il TARS (`ST7789V2`, `SCS009`), **non** quale chip e quali servo privi di marcature siano fisicamente nel kit. D02 e D09 restano aperte a livello di identificazione fisica.
3. La distinta pubblica elenca una **funzione per ogni fissaggio**: Type-C (F002), servo (F003), collegamenti (F004), piattaforma (F005/F006). L'assenza di componenti **non va colmata usando viti simili** senza confronto con disegno e revisione.
4. Il modello **RIG-Hover/Puppy** ha documentazione elettrica/batteria distinta: **non trasferire valori 2S, mAh o schemi** a TARS in assenza di attestazione.
5. La fonte specifica sull'assemblaggio ordina di seguire i **disegni per la propria revisione**; la pagina pubblica non offre una lista per vite esatta della confezione acquistata, né una sequenza pin-by-pin attestata per il PCB fisico.

## Gate tecnico prima dell'assemblaggio

**P0 — Sicurezza elettrica:** D08 + D09 (alimentazione e pinout del PCB); D02 prima di provare a gestire display/firmware. Nessun test sotto tensione con batteria sconosciuta. Usare solo documentazione di collegamento specifica per revisione/hardware effettivi.

**P1 — Meccanica:** D04, D05, D06, D07, D13; misurare o ottenere dal produttore specifiche di testa, lunghezza e sede dei fissaggi della revisione. Non combinare i pezzi del kit con una BOM di replica di revisione incerta.

**P2 — Quantità:** D01; dopo conferma del fabbisogno effettivo, accertare se 55 M2×6 consentono montaggio completo **con margine**.

## Risoluzione operativa: una sola richiesta al produttore

È stato preparato il file [supplier-clarifications-2026-11-22.md](supplier-clarifications-2026-11-22.md) con richiesta **inglese e cinese** a LuwuDynamics di:
- packing list **dello SKU commerciale e del batch/revisione PCB RIG-Board 26/6/2025**;
- videomanuale/tabella delle viti effettivamente previste ai punti di fissaggio;
- scheda batteria e pinout senza assunzioni;
- identificazione del display, tre servo, revisione PCB e necessità della spugna.

Il documento è **pronto per l'invio, non inviato**. Non esiste una risposta ufficiale; finché non arriva, i 9 ID restano `OPEN` nel registro. Quando arriverà, collegare la risposta come nuova evidenza, riclassificare ciascun ID e aggiornare la BOM **senza modificare retroattivamente il conteggio fisico**.

## Conclusione

**Verifica documentale completata, risoluzione fisica non certificabile.** Risultano 4 discrepanze inventariali `RESOLVED` già in v0.4 e **9 rimangono `OPEN`**. La task Jira RTARS-9 resta `Fatto` per il suo scopo originale (censimento e annotazione delle differenze), ma non costituisce autorizzazione a iniziare l'assemblaggio o l'alimentazione.

