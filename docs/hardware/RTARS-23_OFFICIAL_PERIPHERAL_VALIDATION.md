# RTARS-23 — Come collaudare display, touch e IMU

> **Guida pratica per il kit RIG-TARS.** Segui i passaggi dall'alto verso il basso. Alla fine compila il piccolo verbale.
>
> **Situazione attuale:** procedura preparata, **test non ancora eseguiti**. Questa pagina non dichiara che l'hardware funzioni già.
>
> [Task Jira RTARS-23](https://niccolopiazzi01.atlassian.net/browse/RTARS-23)

## Che cosa dobbiamo verificare?

Dobbiamo rispondere a tre domande:

1. **Display:** si accende e mostra immagini corrette?
2. **Touch:** quando tocchiamo il sensore, il firmware riconosce il comando?
3. **IMU:** il sensore di movimento restituisce dati che cambiano quando cambia l'orientamento?

Per ciascuna domanda servono **un risultato (PASS / FAIL / NON TESTATO) e una prova** (foto o log). Non serve produrre decine di screenshot.

## Prima di cominciare — 5 minuti di controlli

**Materiale:** kit RIG-TARS, alimentazione prevista dal produttore per questa revisione, cavo USB dati se richiesto, computer e telefono per una foto.

**Fai questi controlli con tutte le alimentazioni scollegate:**

- [ ] Nessun cavo visibilmente rovinato o con rame esposto.
- [ ] Tutti i connettori sono nelle posizioni e nell'orientamento mostrati nella [guida ufficiale di assemblaggio](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly), **per la revisione del tuo kit**.
- [ ] Tensione, polarità e modalità di alimentazione sono state verificate per la scheda reale. Se non lo sono, **fermati e non accendere**.
- [ ] Il kit è appoggiato su un piano stabile; non ci sono parti che potrebbero muoversi o tirare i cavi.
- [ ] Il **boot del firmware** è già stato verificato e documentato. Rilevare il chip USB CH343 o la flash da 16 MB **non basta** a dimostrare il boot.
- [ ] Sai come spegnere subito la scheda in caso di anomalia.

**Se una casella obbligatoria non è verificabile, non proseguire.** Non spostare connettori sotto tensione. Se noti calore anomalo, fumo, odori sospetti o movimenti inattesi, interrompi la prova.

La guida ufficiale prevede un controllo dell'elettronica *prima* dell'assemblaggio completo. Per le connessioni, guarda le immagini originali del produttore: non abbiamo riprodotto uno schema dei pin perché non è stata confermata la revisione della scheda.

---

## Prova 1 — Display

**Obiettivo:** dimostrare che il display funziona, non soltanto che riceve corrente.

1. Dopo aver superato i controlli iniziali, collega e accendi il kit **seguendo il test elettronico nella guida ufficiale**.
2. Guarda che cosa appare sullo schermo.
3. Controlla se il contenuto è leggibile, stabile e senza righe o artefatti anomali.
4. Scatta **una foto** della schermata. Nascondi eventuali QR di pairing o identificatori personali.
5. Scrivi il risultato nel verbale in fondo.

**PASS** = lo schermo mostra contenuto leggibile e stabile.  
**FAIL** = resta nero, mostra soltanto retroilluminazione, presenta errori o anomalie.  
**NON TESTATO** = non hai potuto eseguire la prova in sicurezza.

**Se non funziona:** spegni, scollega ogni alimentazione (USB compresa) e solo dopo verifica il connettore e la configurazione del firmware. Non cambiare pin a tentativi.

---

## Prova 2 — Sensore touch

**Attenzione:** qui si intende il **sensore touch esterno** del kit; non presumere che il display sia touchscreen.

1. Identifica il sensore touch nella configurazione ufficiale.
2. Verifica che il firmware si trovi in una schermata o modalità nella quale il touch è previsto e **non provoca movimenti**.
3. Tocca brevemente il sensore.
4. Osserva se cambia qualcosa sul display o se viene registrato un evento nel log seriale.
5. Se la modalità è sicura e la risposta è chiara, ripeti altre due volte.

**PASS** = ogni tocco di prova produce la risposta prevista e osservabile.  
**FAIL** = la modalità di test è disponibile ma i tocchi non vengono riconosciuti.  
**NON TESTATO** = non è disponibile una modalità sicura o non possiamo capire se il tocco è stato rilevato.

**Importante:** se appare una schermata di calibrazione meccanica (`CALIB`), **non confermare gli zeri sul kit non assemblato** soltanto per sbloccare il test. Nella guida ufficiale il touch viene anche usato durante la calibrazione successiva all'assemblaggio; questo non equivale a un test indipendente del sensore.

**Prova da conservare:** un breve video, oppure un log che mostri gli eventi touch.

---

## Prova 3 — IMU (sensore di movimento)

L'IMU rileva l'orientamento e l'accelerazione. Il terminale ufficiale può mostrare lo stato `OFF`, `CAL` o `OK`, oltre a dati come `R/P/Y` e `AX/AY/AZ`.

1. Controlla se il display o il log seriale mostrano **lo stato dell'IMU e i valori misurati**.
2. Con il kit fermo e in sicurezza, registra una prima lettura.
3. **Solo se il movimento della scheda è sicuro e non attiva i servomotori**, cambia leggermente il suo orientamento, senza tendere i cavi.
4. Registra una seconda lettura e controlla se cambia in modo plausibile.
5. Riporta la scheda a riposo e annota il comportamento.

**PASS** = il sensore risulta operativo e le letture cambiano coerentemente con la prova.  
**FAIL** = il sensore dovrebbe funzionare nella modalità verificata, ma produce errori o dati incoerenti.  
**NON TESTATO** = non sono disponibili letture affidabili o non è sicuro muovere la scheda.

Non è sufficiente vedere la parola “IMU” sul display: servono **valori reali**. Non inventiamo soglie numeriche o comandi non riportati nella documentazione.

**Prova da conservare:** log o foto con almeno due letture (prima e dopo), indicazione dell'orientamento e ora della prova.

---

## Alla fine — Spegnimento

1. Spegni il kit tramite la procedura prevista.
2. Scollega **tutte** le fonti di alimentazione, USB inclusa.
3. Solo a questo punto puoi intervenire sui connettori, se necessario.
4. Compila il verbale qui sotto.

## Verbale da compilare

Puoi copiare e incollare questo blocco nella chat quando avrai eseguito i test. Io lo userò per preparare le evidenze da versionare su GitHub.

```text
RTARS-23 — RISULTATI COLLAUDO
Data e ora:
Revisione della scheda (se leggibile):
Firmware/versione e regione:
Alimentazione usata:
Boot già verificato? (sì/no + riferimento):
Alimentazione e cablaggio verificati? (sì/no + riferimento):

DISPLAY: PASS / FAIL / NON TESTATO
Che cosa compare sullo schermo?
Foto disponibile? sì/no

TOUCH: PASS / FAIL / NON TESTATO
Che cosa succede quando tocco il sensore?
Log o video disponibile? sì/no

IMU: PASS / FAIL / NON TESTATO
Stato IMU:
Lettura a riposo:
Lettura dopo variazione di orientamento:
Log o foto disponibile? sì/no

Spegnimento completato? sì/no
Anomalie riscontrate:
```

**Regola per chiudere Jira:** display, touch e IMU devono avere ciascuno un PASS comprovato; devono risultare soddisfatti anche i prerequisiti di sicurezza e la [Definition of Done](../process/DEFINITION_OF_DONE.md). In caso contrario RTARS-23 resta aperta. Un test non effettuato non diventa PASS per presunzione.

---

## Documentazione ufficiale utilizzata

Questa procedura è una **guida pratica originale** basata sulle fonti del produttore, consultate il **22 novembre 2026**. Non sostituisce i suoi diagrammi di cablaggio, le istruzioni di alimentazione o gli aggiornamenti firmware.

| Fonte | A cosa serve |
|---|---|
| [RIG-TARS — Guida di assemblaggio](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly) | Configurazione dell'elettronica, prova preassemblaggio e spegnimento |
| [RIG-TARS — Primo avvio](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_start) | Avvio e calibrazione |
| [RIG-TARS — Problemi comuni](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_faq) | Diagnosi display e problemi hardware |
| [RIG-TARS — Display terminale](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_terminal) | Stati IMU e telemetria mostrata |
| [RIG-TARS — Sviluppo](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_develop) | Firmware e strumenti di sviluppo |

### Cosa viene dal produttore e cosa abbiamo definito noi?

**Dal produttore:** sequenza di prova elettronica preliminare, riferimenti al firmware ufficiale, utilizzo del touch in calibrazione, interfaccia terminale e campi di telemetria IMU.

**Criteri del progetto RTARS:** documentare una prova separata per ciascuna periferica, ripetere il touch quando possibile, confrontare le letture IMU prima/dopo, registrare PASS/FAIL/NON TESTATO. Questi criteri non sono una certificazione prestazionale del produttore.

**Limite ancora aperto:** non è stata verificata, per la scheda fisica in uso, una modalità diagnostica indipendente e sicura per tutti e tre i componenti. Se manca, il relativo test resta **NON TESTATO** anziché aggirare firmware o safety gate.

Per i controlli obbligatori prima di alimentare, consulta anche [Sicurezza hardware](../process/HARDWARE_SAFETY.md) e [Definition of Ready](../process/DEFINITION_OF_READY.md).
