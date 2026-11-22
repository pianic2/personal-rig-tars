# RTARS-9 — BOM e riconciliazione kit fisico

**Baseline:** `v0.3-owner-reconciliation` · 2026-11-22  
**Issue Jira:** https://niccolopiazzi01.atlassian.net/browse/RTARS-9  
**PR:** https://github.com/pianic2/personal-rig-tars/pull/1  
**Esito:** inventario quantitativo compilato secondo dichiarazioni del proprietario; classificazioni fisiche non sempre concordi con le etichette. Nessun collaudo elettrico o meccanico. **Non è un collaudo elettrico, meccanico o funzionale.**

## Identità e fonti (non confondere il modello con la revisione)

- **Prodotto indicato dal proprietario:** RIG Series Robots: TARS (testo riportato nell'ordine: `RIG Serie Robots: TARS`).
- **Pagina di acquisto fornita:** https://shop.xgorobot.com/products/rig-tars-fully-open-source-3d-printed-programmable-ai-companion-robot-maker-diy-kit
- **Revisione di confezione / lotto:** nessuna marcatura di revisione o lotto dichiarata dal proprietario.
- **PCB fisicamente consegnata:** marcatura testuale `RIG-Board 26/6/2025`. **La data non è una revisione hardware e non equivale automaticamente a `RIG-Board0722`.**
- **BOM di costruzione di riferimento:** https://wiki.xgorobot.com/kb/pet-tars/cmtvbmd1m00051zasro6ju2aa — `LuwuDynamics Products BOM V1.0 · TARS`. La versione V1.0 è **del documento**, NON del kit fisico.
- **Assemblaggio:** https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly
- **Firmware upstream:** https://github.com/LuwuDynamics/rig_omni
- **Fonte primaria del contenuto ricevuto:** foto zenitale del kit del 2026-11-22 ([manifest e hash](../../../evidence/hardware/RTARS-9/MANIFEST.md)) + [verifica fisica riferita dal proprietario](../../../evidence/hardware/RTARS-9/owner-inventory-2026-11-22.md) con risposte Q1–Q16 e rettifica successiva riportata in appendice.

La pagina commerciale identifica il prodotto ma non costituisce, da sola, una distinta di confezionamento verificata della variante effettivamente spedita. Le differenze rispetto alla BOM V1.0 sono **scostamenti rispetto al riferimento di costruzione**, non automaticamente errori di fornitura.

## Artefatti e semantica

- [rig-tars-bom.csv](rig-tars-bom.csv): 25 voci, 17 `OFFICIAL` (distinta V1.0) + 8 `OBSERVED_EXTRA` (evidenze fotografiche non riconciliate con certezza).
- [discrepancies.csv](discrepancies.csv): 13 registrazioni storiche, **3 RESOLVED** (`D10`, `D11`, `D12`) e **10 OPEN**, inclusa `D13` sulla spugna assente.
- `qty_expected`: quantità della BOM pubblica V1.0; **non** quantità garantita nella confezione.
- `qty_observed`: conteggio visto direttamente in foto oppure confermato dall'utente in Q1–Q16; il campo `evidence_source` indica la base. Un numero `0` significa *assenza riferita dal proprietario rispetto alla voce di riferimento*.
- `packages_observed`: confezioni visibili, mai numero di viti. Le tre tipologie scritte sulla bustina mista sono associate alla **stessa bustina**.
- `observed_marking`: marcatura trascritta letteralmente, non prova automatica del driver, del produttore o di una revisione.
- `revision_verified`: vuoto se nessuna revisione hardware attestata in modo inequivocabile; il suffisso `-V1` del display e `V11` della camera **restano nel codice grezzo**.
- `evidence_source`: `USER_Qn` (risposta dichiarativa alla domanda n), `PHOTO` (foto) o `PHOTO_LABEL` (etichetta della foto).
- `status`: classifica osservazioni e limitazioni, non esito di test funzionali.
- `ABSENT_VS_REFERENCE` / `SPEC_NOT_RECONCILED`: non equivale automaticamente a non conformità contrattuale; per stabilirla servono la packing list della variante e/o istruzioni di assemblaggio aggiornate.

**Non sommare automaticamente** le righe `OBSERVED_EXTRA` e `OFFICIAL`: `A008` e `E008` indicano lo stesso cavo interruttore (identificato dal proprietario), diverso dalla prolunga `E005`. Le denominazioni delle due tipologie M2×4 riferite dal proprietario non coincidono con le etichette fotografate A003/A004: il conflitto rimane aperto prima dell'assemblaggio, e tali voci non vanno conteggiate due volte.

## Rilevazioni nuove confermate dal proprietario

| Componente | Evidenza attuale | Limite |
| --- | --- | --- |
| Scheda | 1, marcatura `RIG-Board 26/6/2025` | Revisione e corrispondenza esatta a RIG-Board0722 sconosciute |
| Display | 1, `FCP-HD240239C12-V1` | Controller ST7789P3/ST7789V2 non confermato |
| Fotocamera | 1, `HBVCAM-2526 V11` | Sensore ottico preciso non confermato |
| Servomotori | 3 senza marcature | Non si può attestare SCS009 |
| Altoparlante | 1 senza marcature | Non si può attestare 3514 |
| Sensore touch | 1 confermato dal proprietario | Modello non riportato |
| Batteria | 1 senza marcature | Tensione, chimica, capacità, polarità, protezione ignote |
| Squadrette servo | 3 | Originalità/modello non dimostrati |
| Contrappesi | 2 da 20 g ciascuno secondo proprietario | Composizione non misurata |
| Prolunga | 1 presente (E005) | Lunghezza e pinout non accertati; non coincide con E008/A008 |
| Cablaggi neri | 3 pezzi, 3 conduttori per pezzo, connettori a incastro | Destinazione e pinout non accertati |
| Spugna isolante | 0 riportata | Confrontare con variante commerciale/manuale |
| Integrità | Nessun danno visibile riferito dal proprietario | Nessun test elettrico/di movimento |

### Minuteria: tabella comparativa senza equivalenze arbitrarie

| Voce | Qtà nel riferimento V1.0 | Conteggio riferito del kit | Esito |
| --- | ---: | ---: | --- |
| M2×6 autofilettanti a croce | 60 (52 nella descrizione) | **55** | Discrepanza quantitativa aperta |
| M2×4 svasate autofilettanti | 2 | **4 riferite dal proprietario** | Etichetta della bustina indica testa tonda a croce per macchina: D03 OPEN fino a verifica della geometria |
| M2×4 a brugola con frenafiletti | 3 | **4 riferite dal proprietario** | Etichetta della bustina indica autofilettanti a croce: D04 OPEN fino a verifica dell'impronta |
| M2×10 / gruppo esagonale | 2 | **0** | Assente rispetto al riferimento |
| M3×10 a croce | 2 | **0** | È presente **1 M3×8 testa piatta**, non equivalente |
| Dadi autobloccanti M3 | 2 | **0** | È presente **1 dado M2**, non equivalente |
| M2×5 testa piatta a croce | Non censite nella tabella core | **2** | Accessorio osservato |

Il conteggio delle M2×6 è **55**, non 60 e non 52. Non sovrascrivere il dato osservato per farlo combaciare con la fonte.

## Gap risolti e gap che rimangono

**Risolti a livello di rilievo inventariale:**

- **D10:** contati 3 servo horn e tutte e sei le tipologie di minuteria effettivamente elencate nelle buste; verificata come **assente** la spugna. Il divario rispetto al riferimento rimane tracciato altrove, in particolare `D13`.
- **D11:** cavo interruttore E008 identificato dal proprietario come cavo nero libero nella zona inferiore sinistra della foto; A008 e la stessa unità. Pinout e lunghezze restano controlli successivi.
- **D12:** marcatura del flat camera leggibile `HBVCAM-2526 V11`; la chiusura non attesta il chip del sensore camera.

**Restano OPEN:** `D01`–`D09`, `D13` (10). Principali questioni: quantità 55/60/52; driver display; fissaggi non riconciliati; M2×10, M3×10, dadi M3 non presenti; batteria non marcata; modello servo/PCB revision sconosciuti; identificazione cavo interruttore; spugna assente. Consultare [discrepancies.csv](discrepancies.csv) per causa e prossima verifica.

## Audit degli Acceptance Criteria di RTARS-9

| Acceptance criterion | Stato | Evidenza |
| --- | --- | --- |
| Inventario con nome e riferimento di ogni componente individuato | PASS | CSV: 25 righe, ID unici, fonte e marcature |
| Quantità fisiche registrate per ogni componente | PASS come dichiarazioni | `qty_observed` valorizzato in **25/25** voci; A003/A004/A008 sono alias storici, non scorte aggiuntive |
| Revisione registrata *se disponibile* | PASS come registrazione negativa | Nessuna revisione del kit dichiarata; i codici presenti sono registrati senza dedurre numeri di revisione |
| Stato registrato per ogni voce | PASS | Colonna `status` piena |
| Differenze annotate con evidenze | PASS | 13 discrepanze: 3 risolte e 10 aperte; quelle aperte restano vincoli espliciti per assemblaggio/validazione |
| Evidenza fotografica permanentemente versionata | **PARZIALE** | Solo hash nel repo, immagine originale ancora non archiviata |

**Decisione:** i criteri originali di RTARS-9 (nome, quantità, revisione se disponibile, stato, differenze annotate) risultano soddisfatti come inventario dichiarativo e tracciato. La task può passare a **Fatto**; PR soggetta a review senza merge automatico. I conflitti di classificazione D03/D04 e i rischi hardware restano documentati e vanno verificati prima dell'assemblaggio.

## Sicurezza e limiti del controllo

- La batteria **non ha marcature**: non caricare, collegare o usare per test sotto tensione finché non siano noti specifiche, polarità e procedure del produttore.
- `M3×8` non si sostituisce a `M3×10`; i dadi `M2` non sostituiscono `M3`; non iniziare montaggio in assenza di corrispondenza con il manuale della revisione usata.
- I 17 pezzi stampati del robot (13 categorie in distinta) sono fuori dallo scope del kit di elettronica e appartengono all'Epic E04.
- La fotografia originale è stata condivisa nella conversazione; il repository contiene il suo manifest con SHA-256, **non** il file binario. Il nuovo documento di ispezione è una dichiarazione del proprietario, non una fotografia delle marcature.


## Rettifica v0.3 — ultime quantità e fonte del conflitto

Il proprietario identifica il cavo interruttore sciolto, senza bustina, visibile in basso a sinistra: **E008=1**, mentre **A008 è la stessa unità** e non va sommata. Il primo e il secondo gruppo M2×4, già contati in Q11, vengono classificati dal proprietario rispettivamente come **svasate autofilettanti F002=4** e **a brugola con frenafiletti F003=4**. La fotografia delle bustine ha etichette *differenti* e rimane una fonte valida: **D03 e D04 restano OPEN** fino alla verifica della geometria/impronta. La loro apertura non impedisce il censimento dichiarativo, ma impedisce di usare la BOM come distinta di montaggio senza verifica. Con queste correzioni, `qty_observed` è compilata in tutte le 25 righe; alcune righe sono alias e non vanno sommate tra loro.

**D11 RESOLVED** per identificazione inventariale. Non sono stati verificati pinout, qualità delle viti, chimica/polarità batteria o modello dei servomotori. L'originale della foto resta fuori dal repository e il suo hash è nel manifest: quest'ultimo non è equivalente a un archivio fotografico persistente.
