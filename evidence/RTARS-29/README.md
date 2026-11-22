# RTARS-29 — Ispezione stampante e materiali (2026-11-22)

Issue: https://niccolopiazzi01.atlassian.net/browse/RTARS-29
Fonte: runbook compilato dall'operatore il 2026-11-22. Le osservazioni fisiche sono dichiarazioni dell'operatore, non prove strumentali indipendenti.

## Configurazione dichiarata
- Stampante: ELEGOO Neptune 4 Standard (non Bambu Lab).
- Ugello: diametro 0,4 mm; materiale ottone, dichiarato.
- Materiale: ELEGOO PLA Metallic, colore Metal Bronze, diametro dichiarato 1,75 mm.
- Slicer: Bambu Studio versione dichiarata 2.8.2.61 (versione pubblicata ufficialmente, ma non verificata sull'installazione mediante export/screenshot).
- Preset stampante: dichiarato corretto per Neptune 4 Standard 0,4 mm, nome/parametri non acquisiti.
- Preset filamento: **NON VERIFICATO** (nome non fornito).
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
| Preset filamento | NOT TESTED | nome 'Non verificato' |
| Temperature rispetto a scheda prodotto | PASS documentale sui setpoint dichiarati | 210/205 °C, bed 60 °C |
| Compatibilità start/end G-code | PASS dichiarativo / PARZIALE | stampe pregresse riuscite, nessun contenuto G-code revisionato |
| Criticità identificate | PASS | preset filamento mancante; raccomandazione ugello; tracciabilità limitata |

## Rischi e decisione
- **OPEN G29-01**: acquisire nome/esportazione del preset filamento ed eventuali override; evitare di dichiarare validata una configurazione anonima.
- **OPEN G29-02**: valutare usura ugello in ottone rispetto alla raccomandazione di acciaio temprato del produttore; non dedurre abrasività certa dal nome commerciale. Documentare rischio e mitigazione o sostituire ugello dopo valutazione.
- **OPEN G29-03**: verifica oggettiva delle configurazioni macchina, start/end G-code e delle evidenze di asciuttezza, dove richieste per dichiarare compatibilità completa.

**Decisione:** NON READY FOR DONE. I risultati dichiarativi sono registrati, le temperature sono compatibili con i limiti del materiale, ma un dato di configurazione obbligatorio è assente e il rischio ugello deve essere valutato. Nessuna stampa eseguita da questa attività; nessuna evidenza indipendente inventata.

Regola: https://github.com/pianic2/personal-rig-tars/blob/main/docs/process/DEFINITION_OF_DONE.md
