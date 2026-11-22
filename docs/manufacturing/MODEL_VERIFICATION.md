# RTARS-27 — Verifica statica dei modelli 3D

**Esito complessivo: NOT TESTED per autenticità ufficiale/revisione e licenza.** Inventario e controlli sul file locale sono riproducibili; non dimostrano che l'archivio sia l'allegato del profilo MakerWorld indicato.

## Input e provenienza

- Percorso locale: `assets/3d/upstream/RIG-TARS_+Open-Source+Desktop+Sci-Fi+Robot.zip` (escluso dal versionamento).
- Provenienza dichiarata: profilo MakerWorld #3318467 / profilo 3767953, ma il collegamento fra questo ZIP e la pubblicazione **non è dimostrato** da metadati o confronto del download.
- SHA-256 archivio: `73f824fa02f36a52d28e1931989fcd17b53dbbba5dd7d9e73a874f45c8ca7fa9`.
- Contenuto: `armV3.3mf`, 2,481,283 byte; SHA-256 `42912423fb2d91076ccc4721f9568fff6115fe686e7e3e51ca7572c15b5bc7c7`.
- Il manifest registra hash, dimensioni e percorso di tutti i 40 membri del 3MF. Non contiene geometrie.

## Risultati

| Controllo | Esito | Evidenza / limite |
| --- | --- | --- |
| Archivio ZIP e CRC | **PASS** | `zipfile.testzip()` non trova errori; singolo membro. |
| Apertura struttura 3MF / XML | **PASS** | `[Content_Types].xml`, relazioni e `3D/3dmodel.model` leggibili. |
| Unità dichiarate | **PASS** | `millimeter` nel modello 3MF; non è una misura fisica indipendente. |
| Oggetti / istanze / piatti | **PASS** | 16 risorse-oggetto e 16 istanze, distribuite su 3 piatti secondo i metadati Bambu. Nomi e conteggi sono nel manifest. |
| Mesh | **PASS** | 13 file di mesh, 13 hash mesh distinti; 13/13 senza indici invalidi, triangoli degeneri o triangoli ripetuti. |
| Watertight / manifold | **PASS** | Per tutte le 13 mesh ogni spigolo non orientato è condiviso da esattamente 2 triangoli. È un controllo topologico per indice vertice; non certifica orientamento, autointersezioni, tolleranze o stampabilità. |
| Duplicati esatti | **FAIL — anomalia** | Tre risorse senza mesh (`3D/Objects/object_27.model`, `object_28.model`, `object_29.model`) hanno lo stesso SHA-256 `c44b2a6f09e7c89be1c6b1d8d0e5e8bb9b3cb28daff94452eb73ddbeee46b232`. Non sono duplicati di geometria; potrebbero essere contenitori vuoti/metadati, da chiarire con il titolare. |
| Altri formati CAD nell'upstream | **N/A** | L'unico file esterno è uno ZIP con un 3MF. Nessun STL, STEP, SLDASM, OBJ o altro CAD separato è presente. Il 3MF contiene nomi `*.STEP` nei metadati, non file STEP sorgente. |
| Nome, revisione e autenticità MakerWorld | **NOT TESTED** | La pagina MakerWorld non è leggibile dalla sessione; il nome locale `armV3.3mf` e i metadati interni non provano che sia l'asset ufficiale né la revisione corrente. |
| Compatibilità meccanica / kit reale | **NOT TESTED** | Nessuna prova dimensionale comparativa, stampa o assemblaggio; l'analisi statica non dimostra compatibilità. |
| Licenza specifica dei modelli | **NOT TESTED** | La licenza deve essere verificata sulla pagina originale o con il titolare. Il riferimento di terza parte a “MakerWorld Exclusive License” non è una conferma primaria. Nessun modello originale o derivato è versionato. |

## Confronto con le fonti TARS

- La BOM ufficiale TARS V1.0 dichiara `tars.SLDASM`, `tars.STEP` e `tarsV3.3mf` come fonti per la propria distinta, e riferisce **17 componenti strutturali in 13 tipi**.
- La guida ufficiale alla stampa consultata per questa verifica descrive invece i progetti `tarsv4普通打印.3mf` e `tarsv4.3mf` (Bambu Studio 02.08.02.61). La tabella leggibile contiene 12 righe di tipo, per 14 unità sommando le quantità visualizzate; il testo/immagini della stessa guida parlano di 4 piatti e 14 pezzi. Questo conteggio documentale non coincide con i 17 pezzi/13 tipi dichiarati dalla BOM V1.0 e va chiarito senza sostituire una fonte all'altra.
- L'archivio locale è denominato `armV3.3mf`, dichiara Bambu Studio 02.07.01.57 e contiene 16 istanze su 3 piatti, 13 etichette di parte con quantità totale 16. Questi dati **non** attestano che `armV3` sia una revisione di `tarsV3`, `tarsV4`, il progetto MakerWorld o l'assieme `tars.SLDASM`/`tars.STEP`.
- RTARS-9 contiene l'inventario del kit e le discrepanze hardware/minuteria; non fornisce evidenza che l'archivio corrente sia il CAD della revisione fisica acquistata.

## Comandi riproducibili

Con Python 3.11+ (solo libreria standard; nessuna dipendenza runtime aggiunta):

```sh
python3 -m unittest scripts/test_verify_3d_models.py -v
python3 scripts/verify_3d_models.py \
  --upstream assets/3d/upstream \
  --extract-dir /tmp/rtars27-extract \
  --manifest docs/manufacturing/MODEL_MANIFEST.json
python3 scripts/verify_3d_models.py \
  --upstream assets/3d/upstream \
  --extract-dir /tmp/rtars27-check \
  --manifest docs/manufacturing/MODEL_MANIFEST.json \
  --check-manifest
```

Lo script rifiuta percorsi assoluti e traversal, symlink negli archivi, CRC non valido e membri superiori al limite configurato; estrae solo sotto la directory di lavoro richiesta e non scrive mai in `assets/3d/upstream`. Il manifest è JSON ordinato e senza data/ambiente, quindi la rigenerazione è deterministica a input invariato. Data ed ambiente effettivi sono registrati in [verification-environment.md](verification-environment.md).

## Azioni necessarie per chiudere i gap

1. Ottenere dalla pagina originale MakerWorld il download del profilo #3767953, la revisione e la licenza visibile; conservarne gli hash senza committare i modelli.
2. Chiedere al titolare se `armV3.3mf` sia ufficiale, quale sia il rapporto con `tarsV3`/`tarsV4`, e perché il pacchetto contenga tre oggetti vuoti duplicati.
3. Chiarire la differenza documentale 17/13 (BOM) contro 14 pezzi indicati nella guida e 16 istanze presenti nel file locale.
4. Associare il file alla revisione del kit acquisita in RTARS-9 e, se appropriato, eseguire confronti CAD e prova di montaggio controllata prima di dichiarare compatibilità.
