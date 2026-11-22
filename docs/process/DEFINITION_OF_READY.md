# Definition of Ready (DoR)

**Progetto:** RIG-TARS · **Task di riferimento:** [RTARS-12](https://niccolopiazzi01.atlassian.net/browse/RTARS-12) · **Stato:** approvata

Una issue Jira è **Ready** quando è possibile iniziare il lavoro senza dover indovinare obiettivo, perimetro, prerequisiti o criteri di successo. Questa verifica si applica **prima di iniziare** un'attività, non prima di crearla nel backlog.

## Checklist

- [ ] Obiettivo, perimetro e risultato atteso sono espliciti.
- [ ] Gli Acceptance Criteria (AC) sono osservabili e verificabili.
- [ ] Dipendenze, impedimenti e prerequisiti sono identificati; quelli indispensabili per iniziare in sicurezza sono risolti.
- [ ] Fonti, specifiche e riferimenti necessari sono collegati, oppure le lacune informative sono dichiarate con un piano di verifica.
- [ ] Strumenti, hardware, accessi e ambiente necessari sono disponibili, **se applicabile**.
- [ ] Rischi noti e vincoli di sicurezza sono identificati, **se applicabile**.
- [ ] È possibile valutare oggettivamente il completamento tramite gli AC e la [Definition of Done](DEFINITION_OF_DONE.md).

## Regole operative

1. Verificare i criteri pertinenti prima di avviare la issue. Registrare in Jira gli eventuali prerequisiti, impedimenti ed esiti **N/A**, con una breve motivazione; non è necessario duplicare l'intera checklist in ogni issue.
2. Nelle attività di ricerca (*discovery*) sono ammesse incognite: la issue deve specificare le domande da risolvere e le evidenze o decisioni da produrre. Le incognite non bloccano lo stato Ready, salvo impediscano un lavoro sicuro o rendano il perimetro indefinito.
3. Una issue che non soddisfa la DoR resta da chiarire o nel backlog: non deve essere avviata come se fosse pronta.
4. Un'attività hardware con prerequisiti critici non verificati per alimentazione, cablaggio o movimentazione **non è Ready**. Consultare la [checklist di sicurezza hardware](HARDWARE_SAFETY.md).
5. Jira è la fonte di riferimento per perimetro, stato e AC; il repository conserva regole di progetto, artefatti tecnici ed evidenze versionate.
