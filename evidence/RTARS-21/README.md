# RTARS-21 — Verifica passiva polarità, alimentazione e cablaggio

- Data: 2026-11-22
- Jira: https://niccolopiazzi01.atlassian.net/browse/RTARS-21
- Scheda: RIG-Board, marcatura `26/6/2025` (revisione hardware precisa non attestata)
- Metodo: osservazioni e misure **dichiarate dall'operatore**, riuso delle evidenze fotografiche già versionate, ispezione con alimentazioni scollegate
- Perimetro: verifica **passiva** e tracciamento delle incognite; **non** collaudo sotto tensione né autorizzazione ad alimentare o ricaricare

## Evidenze esistenti — non duplicate

- [RTARS-20: fotografie fronte/retro e inventario connettori](../RTARS-20/README.md), incluse [foto lato connettori](../RTARS-20/pcb-connectors-side.webp) e [foto lato ESP32](../RTARS-20/pcb-esp32-side.webp)
- [RTARS-9: ispezione PCB e polarità serigrafata](../hardware/RTARS-9/pcb-inspection-2026-11-22.md)
- [RTARS-9: discrepanze D08/D09](../../docs/hardware/bom/source-verification-2026-11-22.md)
- [Checklist sicurezza](../../docs/process/HARDWARE_SAFETY.md)
- [Indice fonti ufficiali](../../docs/references/OFFICIAL_SOURCES_INDEX.md)

## Registro delle verifiche

| ID | Evidenza | Esito / limite |
| --- | --- | --- |
| PRE-01 | Operatore dichiara batteria e USB scollegate durante le misure passive | PASS dichiarativo per setup scollegato |
| PRE-02 | WOWGO XL830L in diodo/continuità: puntali uniti, display 0 e buzzer | PASS, preflight strumento |
| PRE-03 | WOWGO XL830L su DCV 20: fra BAT+ e BAT− della PCB, display 0 V | PASS per la sola misura fra quei contatti; non prova che ogni nodo sia privo di energia |
| G01 | Interruttore/pulsante **separato** a due terminali, con terminali maschio/femmina; premuto = contatto chiuso e buzzer, rilasciato = contatto aperto e niente buzzer | PASS, come riferito dall'operatore; non prova la portata elettrica del contatto |
| G02 | Percorso dichiarato: batteria → interruttore separato → RIG-Board. Operatore conferma corrispondenza con il percorso descritto. Connettore a innesto meccanico obbligato | PARTIAL: disposizione dichiarata, non prova pin-by-pin del circuito completo |
| G03 | Cavi rosso/nero; secondo operatore cablaggio rosso-rosso e nero-nero, innesto meccanicamente obbligato. PCB con serigrafia + verso interruttore PCB e − verso USB-C (RTARS-9) | PARTIAL: corrispondenza dei colori e impossibilità meccanica d'inversione sull'innesto dichiarate; nessuna continuità end-to-end su ogni conduttore |
| G04 | Batteria scollegata misurata a 8,10 V DC con WOWGO XL830L su DCV 20, puntali rispettivamente ai fili rosso e nero | PASS per lettura tensione; NOT TESTED per chimica, configurazione celle, limiti, protezioni |
| G05 | L'operatore dichiara batteria e PCB compatibili perché fornite nel kit | NOT VERIFIED come specifica elettrica della revisione: la dichiarazione non sostituisce scheda tecnica, tensioni limite e pinout |
| G06 | Connettori censiti nelle foto RTARS-20: BAT 2 pin, USB-C, tre connettori servo 3 pin, due FPC/FFC, SPK 2 pin, altri piccoli connettori | PASS per inventario visivo; pinout non leggibili/non documentati mantenuti UNKNOWN, nessun pin assegnato per supposizione |
| G07 | Verbale, fonti e safety gate registrati in questo file | PASS per la documentazione della verifica passiva |

**Nota terminologica:** l'interruttore esterno a pulsante del percorso alimentazione è distinto dall'elemento interruttore visibile sulla PCB in RTARS-20. Non è dimostrato che entrambi abbiano la stessa funzione.

## Mappa dei collegamenti verificati e non verificati

| Origine | Destinazione | Prova disponibile | Stato |
| --- | --- | --- | --- |
| Batteria: filo rosso | Cablaggio rosso, tramite connettore a innesto obbligato | Dichiarazione operatore + lettura 8,10 V ai fili | PARTIAL |
| Batteria: filo nero | Cablaggio nero, tramite connettore a innesto obbligato | Dichiarazione operatore + lettura 8,10 V ai fili | PARTIAL |
| Interruttore esterno, 2 terminali | Apertura/chiusura contatto quando rilasciato/premuto | Prova continuità dichiarata | PASS per il contatto isolato |
| Uscita cablaggio intermedio | Ingresso batteria RIG-Board | Percorso dichiarato; polarità serigrafata su PCB; non verificato punto-punto | PARTIAL |
| RIG-Board BAT− | Secondo riferimento GND indipendente | Nessun pad GND attendibile individuato | NOT TESTED; nessuna connessione presunta |
| Servo / display / camera / speaker | Rispettive periferiche | Solo inventario visivo per RTARS-21; mancano per alcuni pinout specifici | UNKNOWN per pin non attestati |

## Safety gate secondo HARDWARE_SAFETY.md

- **Alimentazione: NOT TESTED come abilitazione a energizzare.** Misurate tensione batteria e assenza di tensione fra i due contatti BAT sulla PCB; mancano dati certi di pacco, protezioni, requisiti di tensione e revisione PCB. **Non collegare né caricare la batteria fino a verifica di questi requisiti.**
- **Cablaggio: PARTIAL.** Integrità macroscopica visiva documentata da RTARS-20, interruttore testato in continuità, accoppiamento meccanico e colori dichiarati. Il tracciamento elettrico end-to-end non è stato misurato. Non dichiarare `PASS` per il cablaggio completo.
- **Movimentazione: N/A.** Nessuna movimentazione prevista nel perimetro di questa ispezione passiva.
- **Continuità BAT− → GND: NOT TESTED.** Non identificato un secondo punto massa affidabile.
- **Identificazione revisione e specifiche: NOT VERIFIED.** La marcatura `26/6/2025` non determina la revisione certificata; vedere D08/D09 in RTARS-9.

## Conclusione / limiti di accettazione

Consegna della **mappa descrittiva e delle verifiche passive effettivamente dichiarate**; nessuna modifica hardware e nessuna accensione effettuata per questa task. La documentazione è completa *come rapporto di ispezione con limitazioni*, ma **non costituisce superamento di tutti i safety gate prima dell'alimentazione**. Ulteriori controlli critici dovranno essere dimostrati prima di alimentare il robot. Ogni eventuale chiusura amministrativa dell'issue deve conservare questi blocchi espliciti: non trasformare `NOT TESTED` in `PASS`.


## Verifica aggiuntiva di fonti del produttore (2026-11-22)

Fonti pubbliche consultate:
- [RIG-TARS, guida di assemblaggio Luwu](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly): descrive il cablaggio di prova del kit e il montaggio TARS; non fornisce da sola la certificazione del pinout del pacco fisico consegnato.
- [SLM6800, pagina del produttore SOLA](https://www.slm-ic.com/show-27-9-1.html) e [scheda prodotto LCSC](https://www.lcsc.com/product-detail/dc-dc-converters_sola-ic-slm6800_C388594.html): identificano il componente come caricatore boost per *due celle Li-ion*, alimentato da ingresso 5 V; la scheda prodotto indica 8,4 V di uscita del circuito di carica. **Queste caratteristiche si riferiscono all'IC, non provano da sole configurazione, protezioni e compatibilità del pacco con l'intera PCB.**
- [RIG-TARS, uso quotidiano Luwu](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_daily): indica di utilizzare il sistema di ricarica fornito, senza sostituire le specifiche del singolo pacco/revisione.

La lettura reale **8,10 V** è *coerente*, non diagnostica, con un pacco Li-ion 2S la cui tensione massima tipica è 8,4 V. La combinazione di kit fornito dal produttore, connettori a innesto vincolato e IC caricatore appropriato costituisce una **plausibilità favorevole**, non una validazione di sicurezza del sistema nel suo complesso.

**Risoluzione amministrativa dei gap:** G01 PASS come osservazione dell'operatore; G02 e G03 PARZIALI per mapping e corrispondenza dei colori/innesti; G04 PASS per la sola lettura 8,10 V ma specifiche pacco non dimostrate; G05 plausibilità supportata dall'IC, compatibilità della specifica revisione NON VERIFIED; G06 inventario visivo disponibile; G07 rapporto completato. Non assegnare PASS a dati ignoti. In base a DEFINITION_OF_DONE.md, RTARS-21 non può essere posta in Fatto finché gli AC critici di sicurezza rimangono aperti. Nessuna ulteriore domanda all'operatore.

## Riscontro definitivo della guida ufficiale TARS — 2026-11-22

La [guida di assemblaggio TARS](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly), sez. 1 «Pre-assembly power-on test: connection reference», pubblica una **foto specifica del collegamento di prova** dell'elettronica del kit e prescrive di utilizzare i componenti forniti con alimentazione scollegata, rispettando posizione e orientamento dei connettori. Questa è una fonte ufficiale aggiuntiva che supporta l'architettura della connessione; **non equivale a una prova di continuità del cablaggio ricevuto**. La pagina raccomanda inoltre di seguire disegni della propria revisione.

La [guida rapida TARS](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_start) dichiara espressamente che la documentazione pubblica non presenta una sequenza completa di cablaggio pin-per-pin o un diagramma verificato degli ID servo per ogni giunto. La [panoramica ufficiale](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_overview) chiarisce che le forniture possono appartenere a revisioni differenti.

**Decisione evidence-first:** G02/G03 ottengono un nuovo riferimento del produttore per la disposizione funzionale, ma rimangono parziali per i pin individuali e la continuità complessiva. G04/G05 ottengono coerenza con il circuito di carica 2S da 8,4 V e batteria misurata 8,10 V; **non** si può certificare il pacco fisico né la compatibilità della revisione PCB senza attestazione, schema o prova adeguata. G01 è PASS; G06 è PASS nel perimetro inventario visivo; G07 è completo come verbale. La dichiarazione di «tutti i gap chiusi» sarebbe contraria ai dati e alla DoD.

**Restrizione operativa invariata:** non alimentare/ricaricare o dichiarare superato il safety gate elettrico sulla sola base di compatibilità dei connettori, colore dei fili o tensione a vuoto.

## Audit fonte primaria: schema applicativo SLM6800 (2026-11-22)

**Fonte primaria tecnica:** [SLM6800 datasheet, versione 1.0, pagina stampata 10/11, figura 5](https://atta.szlcsc.com/upload/public/pdf/source/20250528/77EB65359B52EB0DFA816FE7B9514242.pdf). La figura descrive il circuito applicativo di **ricarica boost per due celle Li-ion**, con **VIN = 5 V** (ingresso del caricatore) e terminali batteria **BAT+** e **BAT− (GND)**. Il riferimento a 5 V **non** va interpretato come tensione nominale del pacco: sono reti diverse. La serigrafia BAT+/BAT− sulla RIG-Board è coerente per denominazione, ma **non è provato** che la PCB replichi integralmente la figura applicativa.

**Fonte ufficiale TARS:** [guida assemblaggio, §1](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly) (ultimo aggiornamento dichiarato 29 settembre 2026): richiede cablaggio secondo lo schema/foto specifico del kit e con alimentazione scollegata; non descrive nella pagina una netlist della scheda posseduta. [Quick start, §2](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_start) dichiara che manca una sequenza pin-by-pin completa pubblica per ogni revisione.

### Matrice gap: risolvibilità documentale

| Gap | Risolto dalla documentazione? | Evidenza e confine |
| --- | --- | --- |
| G01 | Sì: **PASS strumentale dichiarato dall'operatore** | Continuità ON/OFF realmente riferita; non richiede ulteriore fonte |
| G02 | **Parziale** | Schema/foto TARS conferma architettura prevista, non connessioni elettriche reali punto-punto |
| G03 | **Parziale** | Marcature BAT+/BAT− e innesto vincolato dichiarato; non è una misura della continuità end-to-end |
| G04 | **Parziale** | Datasheet IC dimostra che il caricatore è progettato per 2S; 8,10 V misurati sono coerenti, ma non identificano composizione/protezioni pacco |
| G05 | **Parziale** | Fonte ufficiale kit + datasheet IC sostengono compatibilità prevista dal progetto; non certificano limiti della specifica PCB e del pacco |
| G06 | **PASS inventario visivo**, non pinout di ogni periferica | RTARS-20 e foto del produttore |
| G07 | **PASS documentazione** | Questo verbale, riscontri e limiti registrati |

**Decisione:** nessuna ulteriore inferenza può sostituire le prove mancanti. Per DoD e HARDWARE_SAFETY, l'alimentazione e il cablaggio completo **non** possono ricevere PASS e l'issue non deve essere chiusa come validazione completa. La pubblicazione di questo audit non costituisce autorizzazione all'accensione.

## Ultimi risultati del runbook — 2026-11-22 (prevalgono sulle tabelle precedenti)

**Provenienza:** risultati forniti direttamente dall'operatore dopo l'esecuzione del runbook G02/G03. Le letture sono **dichiarate dall'operatore**, non raccolte da un sistema automatico. Il test riguarda il **solo cablaggio passivo isolato**, con batteria e RIG-Board scollegate, come prescritto dal runbook.

| Gate/test | Risultato riportato | Valutazione |
| --- | --- | --- |
| G02R — continuità conduttore rosso | **Presente** | PASS per percorso rosso testato |
| G02N — continuità conduttore nero | **Presente** | PASS per percorso nero testato |
| G02S — pulsante | **Premuto chiude / rilasciato apre** | PASS |
| G03OFF — continuità rosso ↔ nero con pulsante rilasciato | **Nessuna continuità** | PASS per assenza di corto rilevabile fra conduttori |
| G03ON — continuità rosso ↔ nero con pulsante premuto | **Nessuna continuità** | PASS per assenza di corto rilevabile fra conduttori |
| Anomalie osservate | **Nessuna** | Nessuna anomalia dichiarata |
| G04 — documentazione specifiche batteria | **Non disponibili** | NOT VERIFIED: tensione 8,10 V già misurata, ma configurazione/protezioni/limiti pacco non accertati |
| G05 — documentazione di compatibilità batteria/PCB della revisione | **Non disponibile** | NOT VERIFIED: confronto delle specifiche critiche non possibile |

### Valutazione finale dei gate

- **G01: PASS** — prova del pulsante come dichiarata dall'operatore.
- **G02: PASS per continuità del cablaggio isolato e funzionamento interruttore.** Rimane non attribuita una netlist completa della PCB.
- **G03: PASS per i test di isolamento fra conduttori nel cablaggio passivo e corrispondenza visiva del cablaggio dichiarata.** Non è una prova di compatibilità degli ingressi della PCB.
- **G04: NOT VERIFIED**, documentazione del pacco effettivo non disponibile.
- **G05: NOT VERIFIED**, documentazione di compatibilità della revisione effettiva PCB/pacco non disponibile.
- **G06: PASS per inventario visivo**, senza attribuzione di pinout sconosciuti.
- **G07: PASS per registrazione delle evidenze e verbale.**

**Esito della DoD:** le prove passive G02/G03 precedentemente mancanti sono adesso documentate con esito positivo. **Non** sono stati risolti i requisiti critici di alimentazione G04 e G05. `HARDWARE_SAFETY.md` richiede specifiche compatibili verificate per la revisione reale; di conseguenza **RTARS-21 non può essere portata a Fatto secondo la DoD vigente**. La documentazione è pronta e integrabile, ma **non autorizza** a collegare, alimentare o ricaricare la batteria.

## Decisione di accettazione dei gap e chiusura del perimetro passivo — 2026-11-22

**Decisione esplicita del responsabile del progetto:** «segnali come gap accettati. e chiudi la task», riferita ai gap G04/G05 con specifiche non disponibili.

La presente decisione **accetta il differimento**, **non** la validità tecnica né la sicurezza dei requisiti sconosciuti. I criteri di RTARS-21 hanno per perimetro l'ispezione passiva di polarità, cablaggio e mappa dei connettori con alimentazioni scollegate: le evidenze G01–G03, G06 sono disponibili; G07 è il verbale versionato. Il testo originario dell'issue specifica: «La presenza di un valore di tensione non verificato blocca l'alimentazione, non la sola ispezione». Non si trasforma pertanto un esito NOT VERIFIED in PASS.

| Gap accettato | Stato tecnico reale | Accettazione limitata | Tracciamento del requisito prima dell'alimentazione |
| --- | --- | --- | --- |
| **G04** — specifiche batteria del pacco fisico (chimica, numero di celle, limiti, protezioni) | **NOT VERIFIED**; sola tensione misurata 8,10 V | **ACCEPTED FOR PASSIVE INSPECTION ONLY** | [RTARS-46](https://niccolopiazzi01.atlassian.net/browse/RTARS-46) |
| **G05** — requisiti della specifica revisione PCB e compatibilità completa col pacco | **NOT VERIFIED**; coerenza con SLM6800/kit non sufficiente | **ACCEPTED FOR PASSIVE INSPECTION ONLY** | [RTARS-46](https://niccolopiazzi01.atlassian.net/browse/RTARS-46) |

**Decisione DoD riferita a RTARS-21:** mappa visiva con foto già versionate, prove passive di continuità e assenza cortocircuiti con esito positivo, polarità e percorso dei fili documentati, controlli di sicurezza **eseguiti e registrati** per la sola ispezione disalimentata. La task può essere conclusa **come ispezione passiva**, con limiti espliciti, senza pretendere un collaudo funzionale o di sicurezza dell'alimentazione. La successiva operazione di collegare/ricaricare/accendere il pacco **rimane bloccata** dalla task RTARS-46; il suo gate **non** viene superato da questa chiusura.

L'accettazione non modifica né disapplica `docs/process/HARDWARE_SAFETY.md`. La classificazione del safety gate **alimentazione = NOT TESTED / NOT VERIFIED** persiste fino al completamento di RTARS-46.
