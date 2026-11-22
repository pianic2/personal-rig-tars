# RTARS-23 — Procedura tracciabile di collaudo display, touch e IMU

**Issue:** [RTARS-23](https://niccolopiazzi01.atlassian.net/browse/RTARS-23)  
**Tipo documento:** procedura originale derivata da fonti ufficiali; NON copia del manuale  
**Consultazione delle fonti:** 2026-11-22  
**Stato delle prove:** NOT TESTED — questo documento non attesta un collaudo già effettuato  
**Ambito:** kit elettronico RIG-TARS, prima del montaggio strutturale; revisioni e cablaggi da identificare fisicamente.

## 1. Fonti e perimetro documentale

| ID | Fonte ufficiale | Sezione rilevante | Ultimo aggiornamento dichiarato dalla fonte |
|---|---|---|---|
| S1 | [RIG-TARS — Kit assembly](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly) | §§1–3, 5: verifica kit, connessione di prova, firmware ufficiale, test e disconnessione | 2026-09-29 |
| S2 | [RIG-TARS — Quick start](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_start) | §§1–2: power-on, stati del display, calibrazione | 2026-09-29 |
| S3 | [RIG-TARS — Troubleshooting](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_faq) | display, movimento, contenuto del report di supporto | 2026-10-08 |
| S4 | [TARS — Terminal display](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_terminal) | lettura display, telemetria e stati IMU | 2026-10-08 |
| S5 | [RIG-TARS — Development](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_develop) | firmware pubblico, ESP32-S3, target TARS, recupero | Da ricontrollare sul sito al momento della prova |

**Fonte di verità:** i collegamenti e le procedure ufficiali pubblicate dal produttore; queste note descrivono i passaggi di verifica del progetto e ne rendono auditabile l'esecuzione. Per fotografie, diagrammi, video e dettagli non riprodotti, consultare direttamente gli originali. Non archiviare immagini/video del produttore nel repository senza autorizzazione.

**Regole interne:** [HARDWARE_SAFETY](../process/HARDWARE_SAFETY.md), [DoR](../process/DEFINITION_OF_READY.md), [DoD](../process/DEFINITION_OF_DONE.md). Questa procedura non prevale su tali gate.

## 2. Riscontri verificati nelle fonti

- **S1:** il produttore richiede un test di accensione dei componenti elettronici prima dell'installazione nella struttura. I componenti vanno connessi con alimentazione scollegata seguendo la fotografia/schema corrispondente al kit. La guida distingue il layout temporaneo di prova dalla posa finale.
- **S1:** il flusso del firmware ufficiale usa USB dati e [Luwu Tools](https://tools.luwudynamics.ai) con modello RIG-TARS, versione rilasciata e regione appropriata. Flashing e successivo riavvio non dimostrano, da soli, che tutte le periferiche funzionino.
- **S1:** dopo il test, spegnere, scollegare tutte le fonti di alimentazione (USB inclusa) e solo allora disconnettere i componenti. La calibrazione meccanica definitiva è successiva al montaggio.
- **S2:** in fase di calibrazione, il sensore touch esterno viene usato per confermare gli zeri **solo con il robot correttamente montato e allineato**. Non usarlo per forzare il superamento del test di elettronica sfusa.
- **S3:** per uno schermo non funzionante, controllare alimentazione e target software; a potenza rimossa, controllare cavo e blocco del connettore. La configurazione TARS usa lo schermo orizzontale ST7789V2, non un display circolare.
- **S4:** terminale orizzontale 320×240; indicazioni IMU `OFF`, `CAL`, `OK`; grandezze `R/P/Y` e `AX/AY/AZ`. L'animazione `FLIGHT LOG` non è un log diagnostico reale.
- **S3/S4:** per anomalie registrare versione hardware/firmware, regione, sequenza riproducibile, messaggio visualizzato e, se possibile, output seriale.

**Limiti della documentazione consultata:** nelle sezioni sopra non è fornito un protocollo autonomo di accettazione touch/IMU con soglie numeriche, né si è verificato un pinout univoco della specifica revisione del kit. Per RTARS-23 i test funzionali sotto sono criteri di verifica del progetto, non specifiche prestazionali dichiarate dal produttore. Prima di alimentare, identificare la revisione reale e verificare il diagramma di connessione ufficiale specifico.

## 3. Gate 0 — Autorizzazione a provare

Registrare ognuna delle seguenti condizioni con evidenza; un esito incerto su cablaggio o alimentazione è **BLOCKED**, non PASS.

1. Boot test completato ed evidenziato (dipendenza RTARS-23); non confondere la sola identificazione del chip USB o della capacità flash con il boot applicativo.
2. Alimentazione e polarità per la revisione fisica confermate mediante fonte attendibile; assenza di corti/danni e presenza di interruttore/disconnessione accessibile.
3. Collegamenti dei componenti, verso e serraggio verificati sulla **foto ufficiale di test pre-assemblaggio S1** e sulla revisione reale; alimentazione assente durante qualsiasi cambio.
4. Elettronica supportata su superficie stabile, lontana da conduttori; nessun cavo in zona di movimento; operatore presente.
5. Firmware, regione, modello e strategia di alimentazione definiti e annotati. Se è necessario flashare: prima verificare target, release e procedura ufficiale; non cancellare/configurare arbitrariamente la flash.
6. Nessuna calibrazione dei servomotori o prova di movimento del meccanismo sciolto per ottenere un PASS.

Riferimenti: S1, S2 e [HARDWARE_SAFETY](../process/HARDWARE_SAFETY.md).

## 4. Procedura controllata

### T01 — Accensione e display

**Fonte:** S1 §§2–3, S2 §2, S3, S4.

1. A Gate 0 superato, alimentare secondo l'arrangiamento documentato per il kit; seguire l'avvio del firmware originale coerente con modello/regione.
2. Osservare avvio, stabilità, immagini e messaggi (incluso eventuale `CALIB`); fotografare lo stato senza esporre codici QR/identificatori personali.
3. Confrontare aspetto/risoluzione con S4; annotare errori, artefatti, riavvii e se il display resta spento.
4. Se il display non parte, interrompere; controllare solo a potenza rimossa le condizioni descritte in S3. Nessun cambio pin o adattamento improvvisato.

**PASS di progetto:** avvio e rendering leggibili e stabili, senza difetti osservabili nella finestra di prova registrata. **Evidenza:** foto anonimizzata + firmware/region + osservazioni. Il solo backlight non è PASS.

### T02 — Sensore touch

**Fonte:** S1 §3, S2 §2, S4 (stati visualizzati). **Estensione di collaudo del progetto:** risposta funzionale al tocco.

1. Identificare il sensore touch esterno effettivamente presente, non supporre che il pannello display sia touchscreen.
2. Con il firmware in uno stato documentato che ammette l'input touch senza richiedere calibrazione meccanica, effettuare un tocco breve e registrare la risposta osservabile (display o output seriale).
3. Ripetere per tre tocchi distinti solo se il comportamento è sicuro, deterministico e non attiva movimenti; registrare aspettativa/risultato per evento.
4. Se è visibile `CALIB` su un robot non assemblato, **non confermare gli zeri**. Classificare il test indipendente come NOT TESTED fino alla disponibilità di una modalità diagnostica sicura documentata; non usare il touch come espediente per aggirare la calibrazione.

**PASS di progetto:** risposta verificabile a input intenzionali in uno stato previsto dal firmware. **Evidenza:** video ridotto o log seriale anonimizzato con eventi e stato. Assenza di risposta interpretabile = FAIL o NOT TESTED secondo la disponibilità della modalità di test.

### T03 — IMU

**Fonte:** S4, S3. **Estensione di collaudo del progetto:** coerenza di lettura sensore.

1. Se il terminale o il monitor seriale mostra telemetria valida, annotare stato IMU (`OFF/CAL/OK`) e letture a riposo (`R/P/Y`, `AX/AY/AZ`) con timestamp.
2. Solo se il kit è in condizioni sicure, l'operatore può variare leggermente l'orientamento della scheda supportata, senza provocare attivazioni e senza mettere in trazione cavi/connettori. Non muovere parti con servi energizzati.
3. Annotare una seconda lettura; verificare se le grandezze pertinenti cambiano coerentemente e tornano in prossimità del valore iniziale quando riportate a riposo. Non inventare tolleranze, frequenze di campionamento né registri I²C.
4. Se lo stato resta `OFF`/`CAL` o la telemetria non è disponibile, non dichiarare PASS solo perché il campo IMU appare sul display: annotare esito e diagnostica necessaria.

**PASS di progetto:** stato operativo confermato e misure osservate, plausibili e sensibili a una variazione controllata. **Evidenza:** log seriale o sequenza fotografica con valori prima/dopo, timestamp e condizioni. Non equivale a calibrazione metrologica.

### T04 — Shutdown

**Fonte:** S1 §3. Arrestare il firmware/spegnere, togliere l'alimentazione e l'USB, quindi eventualmente separare i componenti; annotare eventuali anomalie. Non usare il setup di prova come riferimento per la posizione di calibrazione definitiva.

## 5. Registro di esecuzione (compilare dopo le prove)

| Campo | Riscontro |
|---|---|
| Esecutore e timestamp | NON ACQUISITO |
| Hardware e revisione | NON VERIFICATA |
| Firmware release/commit e regione | NON ACQUISITI |
| Tipo di alimentazione / riferimenti | NON VERIFICATI |
| Gate 0 / boot test | NOT TESTED — evidenza da collegare |
| Gate 0 / alimentazione | NOT TESTED |
| Gate 0 / cablaggio | NOT TESTED |
| T01 display | NOT TESTED |
| T02 touch | NOT TESTED |
| T03 IMU | NOT TESTED |
| T04 shutdown | NOT TESTED |
| Anomalie, rischi e issue collegate | Nessuna evidenza ancora acquisita; non equivale ad assenza di anomalie |

### Evidenze da raccogliere

- `evidence/RTARS-23/<timestamp>-environment.md`: revisione hardware, firmware, regione, fonti, alimentazione, condizioni.
- `evidence/RTARS-23/<timestamp>-display.jpg`: schermata senza identificativi o segreti.
- `evidence/RTARS-23/<timestamp>-touch.log` oppure video redatto/anonimizzato.
- `evidence/RTARS-23/<timestamp>-imu.log`: serie timestampate prima/dopo + contesto.
- `evidence/RTARS-23/<timestamp>-results.md`: esiti distinti, anomalie e link agli artefatti.

I percorsi sono **nomi proposti**, non file già presenti. Prima della pubblicazione rimuovere account, hostname, percorsi personali, seriali identificativi, QR di pairing, SSID, password e token. Conservare nel report le informazioni tecniche necessarie alla riproducibilità.

## 6. Matrice di tracciabilità AC

| AC Jira | Test | Criterio di chiusura | Stato |
|---|---|---|---|
| Display collaudato | T01 | PASS con evidenza | NOT TESTED |
| Touch collaudato | T02 | PASS con evidenza | NOT TESTED |
| IMU collaudata | T03 | PASS con evidenza | NOT TESTED |
| Malfunzionamenti tracciati | Tutti | Report con esiti/incidenti espliciti | NOT TESTED |
| Prerequisiti boot, power, cablaggio | Gate 0 | Evidenze PASS | NOT TESTED |
| Safety / DoD | Gate 0 e T04 | Nessun safety gate obbligatorio irrisolto; evidenze versionate e collegate a Jira | NOT TESTED |

**Regola finale:** non porre RTARS-23 in Done finché Gate 0 e tutti gli AC obbligatori non sono dimostrati. Le letture precedenti del bridge CH343 e della flash da 16 MB non costituiscono prova di display/touch/IMU. Questo documento registra **la procedura pianificata e le fonti consultate**, non un'esecuzione già avvenuta.

## 7. Aggiornamento delle fonti

Prima di una nuova sessione di collaudo, riaprire S1–S4; se contenuti, timestamp o istruzioni cambiano, registrarne la data e aggiornare la procedura tramite PR. Conservare nei commit la storia delle decisioni; i testi/illustrazioni del manuale restano ai rispettivi titolari.
