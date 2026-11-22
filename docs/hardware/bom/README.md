# RTARS-9 — BOM fisica RIG-TARS

**Baseline:** 2026-11-22 / `v0.1-photo-audit`  
**Issue:** https://niccolopiazzi01.atlassian.net/browse/RTARS-9  
**Stato verifica:** PARZIALE; non costituisce un collaudo, non autorizza accensione, non garantisce completezza quantitativa.

## Scopo e fonti

- **Specifica di riferimento:** documentazione LuwuDynamics per RIG-TARS, distinta “LuwuDynamics Products BOM V1.0 · TARS” riassunta nella pagina ufficiale [Fase 1 — acquisti/BOM](https://wiki.xgorobot.com/kb/pet-tars/cmtvbmd1m00051zasro6ju2aa).
- **Documento di assemblaggio:** https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly
- **Firmware TARS:** https://github.com/LuwuDynamics/rig_omni (il firmware menziona ST7789V2 320×240; la distinta hardware menziona ST7789P3).
- **Evidenza fisica:** un'unica foto zenitale del kit caricata dall'utente nella conversazione ChatGPT del 2026-11-22; metadati e SHA-256 in [evidence manifest](../../../evidence/hardware/RTARS-9/MANIFEST.md).

## File

- [rig-tars-bom.csv](rig-tars-bom.csv): inventario e corrispondenze tra voci ufficiali e pezzi osservati.
- [discrepancies.csv](discrepancies.csv): differenze, ambiguità e verifiche richieste.

## Semantica rigorosa dei campi

- `reference_scope = OFFICIAL`: voce nella distinta pubblica di riferimento, **non promessa di contenuto esatto della confezione commerciale acquistata**.
- `reference_scope = OBSERVED_EXTRA`: oggetto/etichetta visibile ma non riconciliato in modo certo con la distinta di riferimento.
- `qty_expected`: quantità dichiarata dalla distinta, non misurata; vuoto quando non presente o non comparabile.
- `qty_observed`: numero esatto soltanto dove il singolo oggetto è distinguibile visivamente (non stime dietro plastica, etichette o sovrapposizioni).
- `packages_observed`: numero delle confezioni visibili, **non** quantità dei pezzi all'interno; una bustina contenente tre tipi di minuteria compare in tre righe, non rappresenta tre bustine differenti.
- `revision_verified`: vuoto quando non accertata da marcatura leggibile o documento del fornitore; l'assenza di revisione non implica rev. 1.
- `NOT_IDENTIFIED`: non distinguibile nella foto, **non** “MISSING”.
- `SPEC_MISMATCH`: la specifica stampata sulla confezione è diversa dalla voce di riferimento; **non** implica difetto del kit commerciale.
- `IDENTIFICATION_PENDING`, `COUNT_UNVERIFIED`, `MODEL_UNVERIFIED`, `SPEC_UNVERIFIED`, `REVISION_UNVERIFIED`, `WEIGHT_UNVERIFIED`: osservazione possibile con caratteristica essenziale non verificata.

Non confrontare automaticamente le righe `OBSERVED_EXTRA` con le `OFFICIAL`: alcuni oggetti fisici possono essere lo stesso elemento descritto da fonti diverse (vedere E005/A008 e il cablaggio). Per prevenire doppio conteggio, nessuna quantità complessiva di cablaggi viene calcolata.

## Cosa la foto prova

Sono distinguibili con ragionevole certezza: 1 PCB principale, 1 display con flat, 1 batteria in involucro blu, 1 fotocamera su flat, 1 speaker, **3 servomotori**, **2 contrappesi**, almeno 1 bustina con squadrette servo, 1 bustina con circuito e fili, varie buste cablaggi e minuteria. Le sigle specifiche della scheda, dei servomotori, del display e della batteria **non sono convalidate**.

Etichette della minuteria trascritte dalla foto:

| Etichetta cinese | Traduzione operativa | Posizione |
| --- | --- | --- |
| M2*6十字自攻螺丝 | Vite M2×6 a croce autofilettante | Alto destra |
| M2*4圆头十字机丝 | Vite M2×4 a croce testa tonda per macchina | Centro destra |
| M2*4十字自攻螺丝 | Vite M2×4 a croce autofilettante | Medio-basso destra |
| M2*5平头十字机丝 | Vite M2×5 testa piatta a croce per macchina | Busta combinata, basso destra |
| M3*8平头十字机丝 | Vite M3×8 testa piatta a croce per macchina | Busta combinata, basso destra |
| M2六角对锁螺母 | Dado esagonale M2 di bloccaggio | Busta combinata, basso destra |

I tre testi della bustina combinata **non permettono di assegnare ogni vite vista alla propria tipologia**. La forma della testa, il filetto, la misura e la compatibilità meccanica non sono verificati con calibro.

## Limiti e distinzioni

1. I 17 pezzi stampati (13 tipologie) **non sono inclusi nell'inventario fisico del kit di elettronica**; saranno gestiti nell'Epic E04. Non classificare “mancanti” le parti da stampare.
2. Il componente batteria compare in foto, ma tensione, chimica, celle, polarità, circuito di protezione e caricatore sono sconosciuti: **non alimentare né caricare prima della verifica fisica e delle istruzioni del produttore**.
3. Il modello specifico `SCS009`, `RIG-Board0722`, `ST7789P3` e il peso unitario di 20 g sono **specifiche delle fonti**, non letture delle marcature degli oggetti fotografati.
4. `M3x8` ≠ `M3x10` e `M2` ≠ `M3`; non correggere la BOM né sostituire i fissaggi senza verifica della revisione effettiva.
5. La revisione generale del kit **non è verificabile dalla foto**. La BOM usa la fonte pubblica V1.0 per il confronto ma non attribuisce “kit revision V1.0” all'hardware consegnato.
6. Il file originale della foto è allegato alla conversazione; in questa versione del repository ne è registrato l'hash, **non la copia binaria**. Il manifest non va interpretato come foto già presente in GitHub.

## Gate rispetto agli Acceptance Criteria RTARS-9

| AC | Esito | Evidenza |
| --- | --- | --- |
| Tutte le voci riconducibili alla distinta ufficiale censite | PASS (con scope esplicito) | rig-tars-bom.csv |
| Nome e quantità per ogni voce; quantità fisiche certe | **PARTIAL** | qty_expected compilata per voci ufficiali; qty_observed lasciata vuota quando il contenuto della bustina è occultato |
| Revisione se disponibile | **PARTIAL** | campo revision_verified vuoto e limiti evidenziati; non si inventa una revisione |
| Stato e differenze annotate | PASS | status per riga e discrepancies.csv |
| Tracciabilità della foto nel repository | **PARTIAL** | hash disponibile; copia binaria non presente |

**Conclusione verificabile:** baseline pronta per revisione, **non ancora Done** sotto un'interpretazione rigorosa degli AC; la fotografia singola non basta per attestare la quantità fisica di tutte le tipologie né la corrispondenza del kit. Non usare questa tabella come distinta di montaggio definitiva.

## Operazioni residue per chiusura vera

Contare separatamente le viti, le squadrette e i cavi; fotografare il retro della PCB, le targhette dei tre servo, il retro display e l'etichetta batteria; identificare spugna e sensore; confrontare la revisione dell'assemblaggio con la minuteria etichettata; conservare la foto originale nel repo o in un archivio permanente con hash verificato. Le verifiche vanno rese osservabili senza accendere il kit.

