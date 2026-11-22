# Checklist di sicurezza hardware

**Progetto:** RIG-TARS · **Task di riferimento:** [RTARS-12](https://niccolopiazzi01.atlassian.net/browse/RTARS-12) · **Stato:** approvata

Usare i controlli pertinenti **prima della prima accensione e dopo modifiche ad alimentazione, cablaggio, attuatori o assemblaggio meccanico**. Questa checklist supporta le ispezioni del progetto: **non sostituisce** le istruzioni verificate del produttore, una valutazione elettrica qualificata o una certificazione di prodotto.

**Regola di arresto:** se un controllo obbligatorio fallisce, una specifica critica resta incerta o compare un comportamento anomalo, interrompere la prova, disconnettere l'alimentazione quando è possibile farlo in sicurezza e registrare il problema. Non riprendere finché la condizione non è stata risolta.

## 1. Alimentazione — prima di fornire energia

- [ ] Tensione prevista e polarità sono verificate sulle specifiche della **revisione reale della scheda**; non si assumono valori validi per altre varianti.
- [ ] Alimentatore, connettori e cavi hanno caratteristiche adeguate al carico collegato, secondo specifiche verificate.
- [ ] Non sono presenti cortocircuiti evidenti, isolamento danneggiato, conduttori esposti o oggetti conduttivi liberi.
- [ ] Le modifiche ai collegamenti sono state effettuate **ad alimentazione scollegata**, gestendo in sicurezza eventuale energia residua.
- [ ] Il sistema di disconnessione dell'alimentazione è noto, accessibile e utilizzabile tempestivamente in caso di anomalia.
- [ ] Le verifiche strumentali di tensione e polarità sono registrate prima del collegamento di elettronica sensibile, **quando applicabile**.

## 2. Cablaggio — prima dell'alimentazione o del movimento

- [ ] Pinout, orientamento dei cavi e posizione dei connettori corrispondono alla **revisione hardware effettiva**.
- [ ] I connettori sono inseriti correttamente; non sono presenti cavi o giunzioni visibilmente danneggiati o instabili.
- [ ] I cavi non possono entrare nella corsa degli attuatori né essere schiacciati, trascinati o abrasi durante la prova.
- [ ] Eventuali conduttori esposti o connessioni provvisorie sono protetti e fissati in modo adeguato.
- [ ] Collegamenti di massa e alimentazione sono stati verificati rispetto allo schema elettrico applicabile, **quando disponibile**; la mancanza dello schema non autorizza collegamenti basati su supposizioni.

## 3. Movimentazione — prima e durante la prova

- [ ] Il robot è collocato su una superficie stabile, in un'area libera da persone, animali e oggetti fragili.
- [ ] Il primo movimento avviene mediante una sequenza controllata, con limiti prudenti **solo se supportati e verificati** per hardware e firmware utilizzati; non si inventano limiti di sicurezza.
- [ ] Non sono presenti interferenze meccaniche evidenti, fissaggi allentati o cavi intrappolati lungo la corsa prevista.
- [ ] È disponibile una procedura di arresto o disconnessione immediata, verificata senza introdurre rischi aggiuntivi.
- [ ] Un operatore sorveglia continuamente la prima accensione e le prove iniziali di movimento.
- [ ] In presenza di rumori anomali, surriscaldamento, fumo, movimento imprevisto o perdita di controllo, la prova viene interrotta immediatamente.

## Verbale di verifica

Compilare un verbale in Jira o in un documento di evidenza collegato alla issue. Assegnare **un esito distinto a ciascuna categoria applicabile**.

| Campo | Valore |
| --- | --- |
| Issue Jira | RTARS-… |
| Data e operatore | … |
| Scheda e revisione hardware | … / non verificata |
| Versione firmware / commit | … / N/A motivato |
| Fonti del produttore consultate | … |
| Alimentazione | PASS / FAIL / NOT TESTED / N/A (motivo) |
| Cablaggio | PASS / FAIL / NOT TESTED / N/A (motivo) |
| Movimentazione | PASS / FAIL / NOT TESTED / N/A (motivo) |
| Evidenze per ciascuna categoria | Link a fotografie, misure, log o note di prova |
| Anomalie, rischi e attività successive | … |

Gli esiti seguono le definizioni della [DoD](DEFINITION_OF_DONE.md). **PASS** richiede che tutti i controlli applicabili della categoria siano superati. Un controllo pertinente non eseguito è **NOT TESTED**, non **N/A**. Se un dato critico è sconosciuto, bloccare la prova interessata e riportarlo nel verbale.

## Limiti e tracciabilità delle fonti

Questa checklist **non** stabilisce soglie numeriche di tensione o corrente, dimensionamento dei fusibili, velocità o coppie degli attuatori. Tali parametri richiedono fonti autorevoli riferite alla configurazione installata e/o misure validate. Consultare l'[indice delle fonti ufficiali](../references/OFFICIAL_SOURCES_INDEX.md); contrassegnare le specifiche mancanti o contraddittorie come **non verificate**. Non effettuare prove rischiose allo scopo di colmare lacune documentali.
