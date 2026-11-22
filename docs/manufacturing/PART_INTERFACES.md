# RTARS-28 — Interfacce, criticità e verifiche delle parti 3D

**Jira:** https://niccolopiazzi01.atlassian.net/browse/RTARS-28  
**Fonte canonica:** [MODEL_VERIFICATION.md](MODEL_VERIFICATION.md), [MODEL_MANIFEST.json](MODEL_MANIFEST.json), [MODEL_DISCREPANCIES.md](MODEL_DISCREPANCIES.md).  
**Inventario classificato:** [PART_CLASSIFICATION.csv](PART_CLASSIFICATION.csv).  
**Baseline:** archivio locale MakerWorld dichiarato dal proprietario, `armV3.3mf`, SHA-256 `42912423fb2d91076ccc4721f9568fff6115fe686e7e3e51ca7572c15b5bc7c7`.

## Perimetro e natura dell'evidenza

Questa è una classificazione basata sull'inventario verificato in RTARS-27, con un controllo locale di corrispondenza del file sorgente per RTARS-28. Il file disponibile in `/tmp/rtars27-extract/armV3.3mf` ha SHA-256 `42912423fb2d91076ccc4721f9568fff6115fe686e7e3e51ca7572c15b5bc7c7`, uguale al digest atteso nel manifest. Il file è rimasto fuori dal repository. I riferimenti `3D/Objects/...model#<id>` e gli ID build riportati nel CSV collegano ciascuna etichetta agli oggetti mesh/istanze del manifest, senza coordinate.

**Esito della verifica geometrica RTARS-28: NOT TESTED per la localizzazione delle superfici specifiche.** È stata confermata la presenza/riferibilità delle 13 mesh e la verifica topologica statica preesistente di RTARS-27 (mesh leggibili, indici validi, nessun triangolo degenere/ripetuto e ogni edge-index condiviso da due triangoli). Questi controlli non identificano quali facce siano piani di appoggio, fori, sedi, incastri, guide, interfacce mobili o superfici di fissaggio. Non è stata completata una ispezione faccia-per-faccia delle mesh; pertanto non viene registrata alcuna superficie specifica come osservata e nessuna coppia come mate verificato. Le descrizioni di `candidate_interfaces_not_verified` restano ipotesi basate sui nomi e sul ruolo provvisorio.

## Scala di priorità (priorità del controllo, non certificazione di rischio)

- **P0**: parti che, *se la funzione ipotizzata è confermata*, partecipano a struttura portante o movimento; controllare prima dell'uso.
- **P1**: custodie, staffe e alloggiamenti con possibili contatti, fissaggi o vincoli di ingombro.
- **P2**: superfici dimostrate esclusivamente decorative; **nessuna parte è assegnata P2** sulla base dei soli nomi, perché non si può escludere una funzione di accoppiamento.

P0: `arm.STEP` (2), `主体.STEP` (1), `摇杆.STEP` (1), `舵臂.STEP` (1).  
P1: gli altri 9 tipi (11 istanze).  
**Totale:** 13 tipi / 16 istanze; ogni riga ha priorità e piano di verifica.

## Registro delle interfacce candidate e stato dell'evidenza

| Gruppo | Parti | Interfaccia ipotizzata — non osservata sulla mesh in RTARS-28 | Verifica necessaria |
| --- | --- | --- | --- |
| Braccia e articolazioni | P01, P02, P03, P13 | Braccio/gusci, possibile giunto con servo | Identificare mate reali e assi; verificare spazio di rotazione, fissaggi e contatti |
| Corpo | P04, P05, P09 | Guscio/corpo/staffa | Identificare bordi di appoggio e sedi; valutare chiusura e fissaggi |
| Elettronica | P06, P07, P10, P11 | Display, camera, PCB | Confrontare sedi, aperture e forature con componenti effettivi; verificare vie cavi e assenza di compressione |
| Comando | P08 | Eventuale perno/guide joystick | Stabilire natura dell'attuatore e controllare escursione, giochi e interferenze |
| Servo | P12 (3), P13 | Gusci servo e interfaccia braccio-horn | Confrontare sagoma dei 3 servo e horn fisici; distinguere posizione delle 3 istanze |

**Avvertenza:** ogni riga sopra è una ipotesi da verificare; non è una caratteristica geometrica osservata. Il CSV assegna riferimenti mesh e build instance stabili per rendere ripetibile la successiva ispezione senza pubblicare geometria. La disposizione delle istanze sul piatto non prova alcuna relazione di assemblaggio. Una mesh statica, da sola, non dimostra cinematica, compatibilità con hardware esterno o un mate tra due parti.

## Registro per parte — evidenza RTARS-28

| ID | Riferimento mesh (`MODEL_MANIFEST.json`) | Osservazioni geometriche localizzate | Accoppiamenti ipotizzati | Mate verificati |
| --- | --- | --- | --- | --- |
| P01 | `object_5.model#1`; build `2`, `13` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Gusci/attuatori, da etichetta | Nessuno |
| P02 | `object_16.model#9`; build `10` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Chiusura/fissaggio con braccio, da etichetta | Nessuno |
| P03 | `object_17.model#11`; build `12` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Chiusura/fissaggio con braccio, da etichetta | Nessuno |
| P04 | `object_26.model#16`; build `17` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Guscio/corpo, da etichetta | Nessuno |
| P05 | `object_39.model#28`; build `29` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Sedi/supporti/gusci, da etichetta | Nessuno |
| P06 | `object_38.model#26`; build `27` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Adesivo/display, da etichetta | Nessuno |
| P07 | `object_31.model#18`; build `19` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Copertura/apertura camera, da etichetta | Nessuno |
| P08 | `object_12.model#3`; build `4` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Perno/guide/escursione, da etichetta | Nessuno |
| P09 | `object_35.model#20`; build `21` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Sostegno/fissaggio, funzione ignota | Nessuno |
| P10 | `object_36.model#22`; build `23` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Supporto PCB, da etichetta | Nessuno |
| P11 | `object_37.model#24`; build `25` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Supporto PCB, da etichetta | Nessuno |
| P12 | `object_14.model#5`; build `6`, `14`, `15` | Una mesh referenziata da tre istanze; nessuna superficie interna/esterna localizzata | Copertura/sede servo, da etichetta | Nessuno |
| P13 | `object_15.model#7`; build `8` | Nessuna faccia/interfaccia localizzata; integrità mesh solo come in RTARS-27 | Servo horn/albero, da etichetta | Nessuno |

**Interpretazione rigorosa:** “integrità mesh” è un risultato topologico del controllo RTARS-27, non una descrizione funzionale della forma. Questo registro non attribuisce fori, sedi o piani specifici a parti in assenza di ispezione sufficiente.

## Politica dimensionale e tolleranze

- **Tolleranze ufficiali note per singola interfaccia: nessuna attestata dalle fonti acquisite.** Non inserire ±mm, clearance, compensazione XY o filettature sulla base di ipotesi.
- Bounding box, unità millimetriche dichiarate e trasformazioni delle mesh in `MODEL_MANIFEST.json` descrivono l'asset digitale, non quote nominali con tolleranze di fabbricazione.
- Se in seguito si dispone di specifiche dimensionali per la revisione corretta, registrare valore, unità, fonte, revisione e metodo di verifica.
- Se manca una specifica, lo stato rimane `NOT TESTED / tolerance unspecified` e le verifiche previste restano prescrizioni di lavoro futuro, non PASS.
- Evitare interventi irreversibili (alesatura, colla, rettifica di fori/giunti, sostituzioni viti) prima dell'identificazione del pezzo e della compatibilità con hardware effettivo.

## Verifiche successive (fuori dall'AC di classificazione)

1. Aprire il **file locale originale** nel visualizzatore/slicer autorizzato; associare gli ID a un'esplorazione visuale e individuare le superfici effettive. Non pubblicare screenshot contenenti geometria se la licenza lo vieta.
2. Confrontare le interfacce individuate con PCB, display, servo, horn e minuteria della [BOM RTARS-9](../hardware/bom/README.md); i dati del kit hanno gap documentali e le viti non vanno considerate intercambiabili.
3. Verificare orientamento e supporti nel profilo di stampa dedicato (RTARS-30); effettuare prove dimensionali/accoppiamenti soltanto nelle task di stampa/montaggio, registrando esiti oggettivi.
4. Se un accoppiamento è incompatibile, tracciare la discrepanza sulla revisione corretta prima di modificare un modello.

## Gate e risultato

| Gate | Evidenza | Esito |
| --- | --- | --- |
| G01 | 13 tipi, 16 istanze da RTARS-27, trascritti nel CSV | PASS documentale |
| G02 | Una classificazione provvisoria e motivazione per ognuno dei 13 tipi | PASS documentale |
| G03 | Riferimento mesh per ciascuna parte e descrizione di superfici osservate | **NOT TESTED** — riferimenti mesh disponibili, ma superfici specifiche non localizzate |
| G04 | Ogni tipo dispone di priorità e controllo successivo | PASS documentale |
| G05 | Nessuna tolleranza fittizia, modifica CAD o asset ridistribuito | PASS per questi documenti |
| G06 | Versionamento/PR integrata di questa revisione | PASS — [PR #23](https://github.com/pianic2/personal-rig-tars/pull/23), squash `c6ab6ae6eb24a6335bd8353fd54813f9fa2bfaff` |
| G07 | AC di localizzazione superfici, DoD e link Jira | **AC non soddisfatto** — localizzazione `NOT TESTED`; evidenze registrate su [RTARS-28](https://niccolopiazzi01.atlassian.net/browse/RTARS-28), stato In Progress |

**Decisione di ambito:** l'AC richiede superfici di accoppiamento e verifiche previste; RTARS-28 ha completato classificazione e piano di verifica, ma la localizzazione delle effettive superfici sulla mesh non è dimostrata. L'AC resta quindi **parzialmente soddisfatto** e il gate geometrico `NOT TESTED`; non dichiarare Done finché l'ispezione per tutte le 13 tipologie non registra caratteristiche osservate con riferimento mesh stabile. Non dedurre contatti dalla sola disposizione sul piatto. Nessuna stampa, misura dimensionale o prova di montaggio è inclusa.

## Licenza

Il testo della MakerWorld Exclusive License fornito dal proprietario limita la pubblicazione di modelli e derivati. Questi file contengono soltanto nomi, quantità, classificazioni e istruzioni originali scritte per il progetto; **nessuna geometria, asset 3MF/STL, mesh o derivato CAD** è committato. La provenienza e i limiti di verifica della licenza sono registrati in RTARS-27.
