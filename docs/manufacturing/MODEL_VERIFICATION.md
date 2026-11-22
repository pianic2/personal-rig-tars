# RTARS-27 — Inventario e verifica dei modelli 3D

## Sintesi degli esiti

L'archivio locale è stato inventariato e il suo 3MF è stato analizzato senza modificare gli upstream. Package, grafo e mesh analizzati risultano `PASS` per i controlli statici implementati. La provenienza è attestata dal proprietario; la verifica indipendente della pagina, la licenza e la corrispondenza di revisione restano `NOT TESTED`. Il confronto documentale rileva quantità differenti e non prova compatibilità meccanica.

Il manifest riproducibile è [MODEL_MANIFEST.json](MODEL_MANIFEST.json). Non include geometrie. Le verifiche puntuali e le azioni residue sono in [MODEL_DISCREPANCIES.md](MODEL_DISCREPANCIES.md).

## Sorgente, hash e distinzione delle evidenze

| Elemento | Evidenza | SHA-256 | Provenienza/stato |
| --- | --- | --- | --- |
| ZIP locale `RIG-TARS_+Open-Source+Desktop+Sci-Fi+Robot.zip` | Archivio originale, escluso da Git | `73f824fa02f36a52d28e1931989fcd17b53dbbba5dd7d9e73a874f45c8ca7fa9` | Il proprietario attesta il download dal modello MakerWorld #3318467 / profilo 3767953. Nessun confronto indipendente con un download dalla pagina. |
| `armV3.3mf` | 2.481.283 byte; unico file esterno nell'archivio | `42912423fb2d91076ccc4721f9568fff6115fe686e7e3e51ca7572c15b5bc7c7` | Metadata locali: BambuStudio 02.07.01.57; Creation/ModificationDate 2026-09-02; `Designer` e `License` vuoti; `DesignerUserId=1510856505`. Valori dichiarati dal file, non verificati con il publisher. |

L'autore visualizzato nella pagina, data originale di pubblicazione e cronologia/versione del profilo non sono stati verificati: accesso diretto alla pagina MakerWorld bloccato da Cloudflare (HTTP 403). Il proprietario attesta la provenienza del download, non l'identità dell'autore o la revisione pubblicata. Un indice terzo che attribuisce “MakerWorld Exclusive License” non costituisce evidenza primaria. La licenza dei modelli è `NOT TESTED`; nessun modello o derivato è ridistribuito.

## Inventario del 3MF

- 40 membri ZIP interni, ciascuno con percorso, dimensione e SHA-256 nel manifest; l'archivio contiene un solo file esterno, il progetto `armV3.3mf`.
- 16 oggetti nel modello principale e 29 oggetti complessivi nei model-part XML; 13 oggetti mesh e 16 contenitori con componenti lungo il grafo raggiungibile.
- 16 elementi build, tutti stampabili, 16 istanze foglia mesh su tre piatti; 13 model parts contengono oggetti mesh e i 13 hash di file XML completi sono distinti. Questo è un confronto byte-per-byte dei file XML, non un hash canonico delle sole geometrie. Le istanze riutilizzano legittimamente gli stessi oggetti: `arm.STEP` due istanze e `舵机盖.STEP` tre istanze. Percorsi, ID, riferimenti, trasformazioni di ogni componente/build, catene trasformazione, bounding box trasformate e metadati modello sono nel manifest.
- I tre file `3D/Objects/object_27.model`, `object_28.model`, `object_29.model` sono XML validi ma contengono risorse e build vuote. Nessun oggetto, mesh, componente o build li referenzia. Le relazioni li menzionano, ma non sono usati dal grafo stampabile. Il loro hash identico è conseguenza dei contenuti vuoti ripetuti; non sono né mesh duplicate né contenitori con geometrie. Discrepanza D3D-04 risolta `PASS` senza alterare i file.
- Unità: `millimeter` dichiarata nel modello principale e in tutti i 17 model parts, esplicita in ogni caso. È un dato 3MF, non una misura fisica indipendente. Il manifest distingue unità dichiarate e unità effettive (il default della specifica è millimeter quando l'attributo manca), registra la conversione tra model parts e riporta bounding box istanza in mm.
- Tutti i 13 payload mesh sono leggibili; indici vertici validi; 0 triangoli degeneri e 0 facce ripetute per payload. Ogni edge non orientato costruito sugli indici dei vertici ricorre esattamente due volte (watertight/manifold secondo questo test). Il controllo non salda vertici coincidenti e non certifica orientamento, autointersezioni, precisione, slicing o stampabilità.
- Nessuna riparazione geometrica. Gli archivi e i payload CAD non sono estratti in repository né modificati. SHA duplicati sono riportati come informazione, mai usati da soli per fallire un modello.

### Matrice parte-per-parte: locale contro guida ufficiale V4

Le quantità locali sono conteggi delle istanze di build stampabili etichettate nel progetto. La funzione è riportata solo quando il nome corrisponde esattamente a un'etichetta della guida; in altri casi la traduzione è letterale e la funzione/corrispondenza resta non verificabile. La guida elenca 12 righe e 14 unità.

| Nome locale originale | Traduzione letterale | Funzione/mapping documentale | Locale | Guida V4 ufficiale | Esito confronto |
| --- | --- | --- | ---: | --- | --- |
| `arm.STEP` | braccio | Nessuna riga con questo nome; ruolo non determinabile dal solo label | 2 | — | Nessuna corrispondenza dimostrata |
| `R arm_shell.STEP` | guscio braccio destro (label) | Nessuna riga nominale corrispondente | 1 | — | Nessuna corrispondenza dimostrata |
| `arm_shell.STEP` | guscio braccio | Nessuna riga nominale corrispondente | 1 | — | Nessuna corrispondenza dimostrata |
| `body_shell.STEP` | guscio corpo | Nessuna riga nominale corrispondente | 1 | — | Nessuna corrispondenza dimostrata |
| `主体.STEP` | corpo principale | Main Body: nome inglese corrispondente | 1 | Main Body ×1 | Nome e quantità coincidono; identità geometrica non verificata |
| `屏幕贴胶底壳.STEP` | guscio inferiore adesivo schermo | Screen Adhesive Bottom Shell: nome corrispondente | 1 | Screen Adhesive Bottom Shell ×1 | Nome e quantità coincidono; identità geometrica non verificata |
| `摄像头盖板.STEP` | copertura camera | Camera Cover: nome corrispondente | 1 | Camera Cover ×1 | Nome e quantità coincidono; identità geometrica non verificata |
| `摇杆.STEP` | joystick | Joystick | 1 | Joystick ×1 | Nome e quantità coincidono; identità geometrica non verificata |
| `支架.STEP` | supporto/staffa | Nessuna riga nominale corrispondente; funzione non determinabile | 1 | — | Nessuna corrispondenza dimostrata |
| `电路板支架小.STEP` | piccolo supporto scheda elettronica | Nessuna riga nominale corrispondente | 1 | — | Nessuna corrispondenza dimostrata |
| `电路板支架小L.STEP` | piccolo supporto scheda elettronica L | Nessuna riga nominale corrispondente | 1 | — | Nessuna corrispondenza dimostrata |
| `舵机盖.STEP` | copertura servo | Servo Cover: nome corrispondente | 3 | Servo Cover ×1 | Quantità discordante (3 vs 1) |
| `舵臂.STEP` | braccio servo | Servo Arm | 1 | Servo Arm ×1 | Nome e quantità coincidono; identità geometrica non verificata |

La matrice non assegna parti locali a Shoulder Outer Shell, Shoulder Inner Shell, Screen Shell, Upper/Lower Servo Clamp o Switch Cover: nomi e metadata non sono sufficienti a dimostrare l'equivalenza. Cinque nomi guida coincidono con nome e quantità locale; il nome Servo Cover coincide ma la quantità no. La guida V4 documenta inoltre Shoulder Outer Shell ×2, Shoulder Inner Shell ×2, Screen Shell ×1, Upper Servo Clamp ×1, Lower Servo Clamp ×1 e Switch Cover ×1, non identificati nominalmente nell'archivio locale.

### Confronto con BOM V1.0, guida e RTARS-9

| Fonte/revisione | Nomenclatura e quantità documentate | Confronto con locale |
| --- | --- | --- |
| BOM ufficiale TARS V1.0 | Indica `tars.SLDASM`, `tars.STEP`, `tarsV3.3mf`; 17 strutture stampate / 13 tipi, con ulteriori elementi come pulsante. La pagina BOM accessibile non espone in testo la distinta strutturale parte-per-parte. | Totale 17/13 contro 16/13 locale. Nomi specifici non riconciliabili dal testo della BOM. |
| Guida ufficiale stampa (aggiornata 2026-10-19) | Progetti `tarsv4普通打印.3mf` e `tarsv4.3mf`, Bambu Studio 02.08.02.61; tabella 12 nomi / 14 unità. | Quattro etichette corrispondono per nome e quantità; `Servo Cover` ha quantità 1 in guida vs 3 locale. Totali 14/12 vs 16/13. |
| Archivio MakerWorld attestato dal proprietario | Nome locale `armV3.3mf`; app Bambu Studio 02.07.01.57; 16 istanze / 13 label. | Download attribuito al profilo dal proprietario; non prova che `armV3` equivalga a `tarsV3`, `tarsV4`, `tars.STEP` o `tars.SLDASM`. Nessun file alternativo disponibile per confronto mesh/CAD. |
| Inventario hardware RTARS-9 | Inventario hardware/minuteria e note sulla revisione del kit; nessun elenco parte-per-parte dei pezzi stampati con versione CAD. | Riconciliazione del kit stampato `N/A` per mancanza di inventario pertinente. Compatibilità fisica `NOT TESTED`. |

Le differenze di nome/versione e i totali differenti sono dimostrati come discrepanze documentali, non come differenze geometriche. Non è stata inventata alcuna equivalenza tra revisioni. La matrice completa gli stati in `MODEL_DISCREPANCIES.md` (D3D-01…08).

## Verificatore, riproducibilità e limiti

`scripts/verify_3d_models.py` usa solo la libreria standard Python. Analizza ZIP, 3MF stand-alone e 3MF contenuti in archivi; per 3MF ispeziona relazioni OPC/3MF, oggetti, componenti, riferimenti cross-part, ID, cicli, build, istanze e trasformazioni; valida triangoli, coordinate e incidenza degli edge e registra anche oggetti non raggiungibili. Rifiuta nomi assoluti/traversal, symlink e percorsi ZIP duplicati, CRC errati e superamento dei limiti predefiniti (10.000 membri, 256 MiB per membro, 512 MiB espansi complessivi, 128 MiB per XML, profondità del grafo 512). L'estrazione è confinata a una directory separata dall'upstream. Errori di input diventano `FAIL` con exit code non-zero; nessun risultato parziale è spacciato per successo.

Per le trasformazioni si applica la serializzazione 3MF Core: 12 valori per le prime tre colonne della matrice affine. Le istanze compongono trasformazione di build e componenti, convertendo le coordinate tra unità dichiarate nei diversi model parts prima di riportare i bounds in mm. Vedi [specifica 3MF Core v1.3](https://3mf.io/spec/core-v1-3-0/). Nessuna libreria proprietaria o dipendenza aggiunta. Nessuna geometria autonoma STL/STEP/IGES è decodificata; formati non-3MF sono solo identificati/hashati.

Comandi riproducibili (Python 3.11+):

```sh
python3 -m unittest discover -s scripts -p 'test*.py' -v
python3 -m py_compile scripts/verify_3d_models.py scripts/test_verify_3d_models.py
python3 scripts/verify_3d_models.py --upstream assets/3d/upstream \
  --extract-dir /tmp/rtars27-extract --manifest docs/manufacturing/MODEL_MANIFEST.json
python3 scripts/verify_3d_models.py --upstream assets/3d/upstream \
  --extract-dir /tmp/rtars27-check --manifest docs/manufacturing/MODEL_MANIFEST.json \
  --check-manifest
```

Test sintetici coprono SHA-256, traversal/assoluti, ZIP corrotto, CRC/path non sicuri, duplicati, symlink, limiti ZIP bomb, estrazione, determinismo, mesh malformate, unità, oggetti non referenziati, relazioni/referenze mancanti, cicli intra- e cross-part, contenitori senza mesh proprie, build/istanze multiple e trasformazioni composte. Esiti ed ambiente effettivi sono registrati in [verification-environment.md](verification-environment.md).

## Licenza e distribuzione

La pagina primaria MakerWorld non ha fornito contenuto verificabile in questa esecuzione. Il campo licenza nei metadata 3MF è vuoto. Una licenza del firmware non determina i diritti sul CAD. La licenza è `NOT TESTED`; gli originali e i derivati restano esclusi da Git, non redistribuiti. Per verificarla serve consultare la pagina MakerWorld accessibile o ottenere autorizzazione esplicita riferita a questi file.
