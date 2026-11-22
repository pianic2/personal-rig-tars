# RTARS-28 — Interfacce, criticità e verifiche delle parti 3D

**Jira:** https://niccolopiazzi01.atlassian.net/browse/RTARS-28  
**Fonte canonica:** [MODEL_VERIFICATION.md](MODEL_VERIFICATION.md), [MODEL_MANIFEST.json](MODEL_MANIFEST.json), [MODEL_DISCREPANCIES.md](MODEL_DISCREPANCIES.md).  
**Inventario classificato:** [PART_CLASSIFICATION.csv](PART_CLASSIFICATION.csv).  
**Baseline:** archivio locale MakerWorld dichiarato dal proprietario, `armV3.3mf`, SHA-256 `42912423fb2d91076ccc4721f9568fff6115fe686e7e3e51ca7572c15b5bc7c7`.

## Perimetro e natura dell'evidenza

Questa è una **classificazione documentale preliminare**: 13 etichette originali e 16 istanze stampabili, estratte dall'inventario verificato in RTARS-27. I ruoli sono dedotti dalla traduzione letterale dei nomi dei modelli e **non** da una ricostruzione certificata dell'assieme. Non si dichiara di aver ispezionato visivamente i dettagli degli accoppiamenti, misurato geometrie, stampato parti o provato il montaggio. Le interfacce nella colonna `candidate_interfaces_not_verified` del CSV sono **candidati da localizzare** sui modelli reali, non superfici già geometricamente identificate.

RTARS-27 ha già confermato la leggibilità strutturale delle 13 mesh e il grafo delle 16 istanze; questa verifica statica **non equivale** alla validazione delle interfacce. Non si importa la geometria della guida V4 nella baseline V3, né si deduce corrispondenza geometrica tra revisioni. Tre ripetizioni di `舵机盖.STEP` e due di `arm.STEP` sono istanze legittime. Il confronto documentale RTARS-27 resta la fonte per le discrepanze.

## Scala di priorità (priorità del controllo, non certificazione di rischio)

- **P0**: parti che, *se la funzione ipotizzata è confermata*, partecipano a struttura portante o movimento; controllare prima dell'uso.
- **P1**: custodie, staffe e alloggiamenti con possibili contatti, fissaggi o vincoli di ingombro.
- **P2**: superfici dimostrate esclusivamente decorative; **nessuna parte è assegnata P2** sulla base dei soli nomi, perché non si può escludere una funzione di accoppiamento.

P0: `arm.STEP` (2), `主体.STEP` (1), `摇杆.STEP` (1), `舵臂.STEP` (1).  
P1: gli altri 9 tipi (11 istanze).  
**Totale:** 13 tipi / 16 istanze; ogni riga ha priorità e piano di verifica.

## Registro delle interfacce da accertare

| Gruppo | Parti | Interfaccia candidata — non verificata | Controllo successivo |
| --- | --- | --- | --- |
| Braccia e articolazioni | P01, P02, P03, P13 | Braccio/gusci, possibile giunto con servo | Identificare mate reali e assi; verificare spazio di rotazione, fissaggi e contatti |
| Corpo | P04, P05, P09 | Guscio/corpo/staffa | Identificare bordi di appoggio e sedi; valutare chiusura e fissaggi |
| Elettronica | P06, P07, P10, P11 | Display, camera, PCB | Confrontare sedi, aperture e forature con componenti effettivi; verificare vie cavi e assenza di compressione |
| Comando | P08 | Eventuale perno/guide joystick | Stabilire natura dell'attuatore e controllare escursione, giochi e interferenze |
| Servo | P12 (3), P13 | Gusci servo e interfaccia braccio-horn | Confrontare sagoma dei 3 servo e horn fisici; distinguere posizione delle 3 istanze |

**Avvertenza:** un gruppo indica una possibile relazione funzionale, **non** una coppia di mate confermata nel CAD. Il file 3MF documenta la disposizione di stampa, non vincoli di assieme; non permette di identificare automaticamente tutte le superfici accoppiate.

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
| G03 | Candidati di accoppiamento, gruppi d'interfaccia e limiti espliciti | PASS come **piano**; localizzazione geometrica effettiva NOT TESTED |
| G04 | Ogni tipo dispone di priorità e controllo successivo | PASS documentale |
| G05 | Nessuna tolleranza fittizia, modifica CAD o asset ridistribuito | PASS per questi documenti |
| G06 | Versionamento/PR integrata | Da verificare in GitHub |
| G07 | DoD, link Jira e transizione Done | Da verificare in Jira |

**Decisione di ambito:** il criterio Jira richiede elenco parti con criticità, superfici di accoppiamento e verifiche previste. Le superfici sono registrate qui come **candidate, non identificate geometricamente**. Se il criterio viene interpretato come *identificazione reale delle superfici su ciascuna mesh*, questo risultato da solo **non** soddisfa integralmente l'AC; serve un'ispezione geometrica ulteriore. Non convertire `NOT TESTED` in `PASS`.

## Licenza

Il testo della MakerWorld Exclusive License fornito dal proprietario limita la pubblicazione di modelli e derivati. Questi file contengono soltanto nomi, quantità, classificazioni e istruzioni originali scritte per il progetto; **nessuna geometria, asset 3MF/STL, mesh o derivato CAD** è committato. La provenienza e i limiti di verifica della licenza sono registrati in RTARS-27.
