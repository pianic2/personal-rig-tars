# RTARS-29 — Ispezione stampante e materiali (2026-11-22)

Issue: https://niccolopiazzi01.atlassian.net/browse/RTARS-29
Fonte: runbook compilato dall'operatore il 2026-11-22. Le osservazioni fisiche sono dichiarazioni dell'operatore, non prove strumentali indipendenti.

## Configurazione dichiarata
- Stampante: ELEGOO Neptune 4 Standard (non Bambu Lab).
- Ugello: diametro 0,4 mm; materiale ottone, dichiarato.
- Materiale: ELEGOO PLA Metallic, colore Metal Bronze, diametro dichiarato 1,75 mm.
- Slicer: Bambu Studio versione dichiarata 2.8.2.61 (versione pubblicata ufficialmente, ma non verificata sull'installazione mediante export/screenshot).
- Preset stampante: dichiarato corretto per Neptune 4 Standard 0,4 mm, nome/parametri non acquisiti.
- Preset processo: **QUALITY** (nome dichiarato dall'operatore, senza export o parametri del preset).
- Preset filamento selezionato: **Generic PLA**, dichiarato dall'operatore; preset generico, non specifico per ELEGOO PLA Metallic Metal Bronze. Parametri completi/override non ispezionati: **compatibilità NON VERIFICATA**.
- Hotend: 210 °C primo layer, 205 °C successivi; piano: 60 °C tutti i layer.
- Stampante: ispezione visiva PASS dichiarata; bobina integra PASS dichiarata; asciuttezza dichiarata documentata ma metodo/data del controllo non forniti.
- Compatibilità start/end G-code: PASS dichiarato, contenuto non ispezionato.
- Esperienza: operatore riferisce diverse stampe riuscite con la configurazione, senza log, file o quantità disponibili.

## Verifica delle specifiche ufficiali
- ELEGOO PLA Metallic: temperatura ugello 190–230 °C, letto 35–65 °C. I setpoint dichiarati sono entro i due intervalli.
  Fonte: https://www.elegoo.com/products/pla-metal-filament-1-75-mm-colored-1-kg
- Produttore indica come ugello raccomandato acciaio temprato >=0,4 mm per il PLA Metallic. L'ugello dichiarato è in ottone: **differenza rispetto alla raccomandazione**, rischio di usura da valutare, non prova di guasto.
- Release ufficiale Bambu Studio 2.8.2.61: https://github.com/bambulab/BambuStudio/releases

## Matrice AC
| Gate | Esito | Evidenza / gap |
| --- | --- | --- |
| Identificazione modello reale e diametro ugello | PASS dichiarativo | Neptune 4 Standard, 0,4 mm |
| Materiale ugello | PASS dichiarativo | ottone; raccomandazione acciaio temprato non rispettata |
| Stato macchina | PASS dichiarativo | ispezione operatore, nessun difetto segnalato |
| Identità e stato bobina | PASS dichiarativo / PARZIALE | PLA Metallic Metal Bronze, 1,75 mm, bobina integra; asciuttezza riferita ma prova non allegata |
| Slicer, versione | PASS dichiarativo | versione 2.8.2.61, non acquisito screenshot o log |
| Preset stampante | PASS dichiarativo / PARZIALE | confermato come corretto, nome e file non acquisiti |
| Preset processo | PASS dichiarativo | nome QUALITY; impostazioni non esportate |
| Nome preset filamento | PASS dichiarativo | Generic PLA selezionato; distinto dal processo QUALITY |
| Adeguatezza preset al PLA Metallic | NOT TESTED | parametri/override Generic PLA non esportati né revisionati |
| Temperature rispetto a scheda prodotto | PASS documentale sui setpoint dichiarati | 210/205 °C, bed 60 °C |
| Compatibilità start/end G-code | PASS dichiarativo / PARZIALE | stampe pregresse riuscite, nessun contenuto G-code revisionato |
| Criticità identificate | PASS | preset filamento mancante; raccomandazione ugello; tracciabilità limitata |

## Rischi e decisione
- **OPEN G29-01 (ridotto)**: nome del preset acquisito (`Generic PLA`); acquisire impostazioni/override, confrontarle con ELEGOO PLA Metallic e non assumere che un preset PLA generico sia qualificato per il materiale effettivo.
- **OPEN G29-02**: valutare usura ugello in ottone rispetto alla raccomandazione di acciaio temprato del produttore; non dedurre abrasività certa dal nome commerciale. Documentare rischio e mitigazione o sostituire ugello dopo valutazione.
- **OPEN G29-03**: verifica oggettiva delle configurazioni macchina, start/end G-code e delle evidenze di asciuttezza, dove richieste per dichiarare compatibilità completa.

**Decisione:** NON READY FOR DONE. I risultati dichiarativi sono registrati, le temperature sono compatibili con i limiti del materiale, ma un dato di configurazione obbligatorio è assente e il rischio ugello deve essere valutato. Nessuna stampa eseguita da questa attività; nessuna evidenza indipendente inventata.

Regola: https://github.com/pianic2/personal-rig-tars/blob/main/docs/process/DEFINITION_OF_DONE.md

## Evidenza aggiuntiva — schermate Filament Manager (2026-11-22)

L'operatore ha fornito due fotografie dell'interfaccia Bambu Studio, schede **Filament** e **Cooling** del preset visualizzato **Generic PLA @Elegoo**. Le fotografie sono state esaminate in conversazione; non sono state copiate nel repository. Questa trascrizione anonimizzata non attribuisce alle immagini verifiche che non mostrano.

### Valori visibili in Filament
- Type: PLA; diameter 1,75 mm; pressure advance: checkbox non selezionata; velocity adaptation factor: 1; softening temperature: 60 °C.
- Recommended nozzle temperature: min 205 °C, max 210 °C (intervallo configurato nel preset, **non** limiti ufficiali del produttore).
- Smooth PEI/High Temp plate: 60 °C initial layer, 60 °C other layers.
- Nozzle: 210 °C initial layer, 205 °C other layers.
- Prime volume visualizzato: filament change 45 mm³, hotend change 60 mm³.

### Valori visibili in Cooling
- Initial layer fan: primi 1 layer a 0%.
- Min fan speed threshold: 100% a layer time 100 s; max threshold: 100% a layer time 8 s.
- Keep fan always on: enabled; slow printing down for better layer cooling: enabled; force cooling for overhangs and bridges: enabled.
- Auxiliary fan: primi 1 layer a 0%; configurazione di ramp-up visualizzata fino al 70%. L'effettiva presenza/attivazione fisica della ventola ausiliaria e l'effetto dell'impostazione sulla Neptune 4 non sono dimostrati dalla schermata.
- La scheda Setting Overrides non è stata fornita, né sono disponibili l'export completo del preset, i parametri start/end G-code o una prova di stampa riproducibile.

### Rivalutazione
- **G29-01 identità e parametri visibili**: PASS per i campi leggibili delle due schermate; compatibilità globale del preset Generic PLA per il materiale effettivo **PARTIAL / NON VERIFICATA** (Cooling, impostazioni avanzate e override non integralmente revisionati).
- **G29-02** raccomandazione ugello acciaio temprato vs ottone: ancora da valutare; non è evidenza di usura effettiva.
- **G29-03** compatibilità G-code e asciuttezza: rimangono evidenze dichiarative.
- **DoD**: ancora non completamente superata; non effettuare merge/chiusura sulla base di queste due immagini.
