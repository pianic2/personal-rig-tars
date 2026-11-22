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
