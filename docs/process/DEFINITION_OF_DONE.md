# Definition of Done (DoD)

**Progetto:** RIG-TARS · **Task di riferimento:** [RTARS-12](https://niccolopiazzi01.atlassian.net/browse/RTARS-12) · **Stato:** approvata

Una issue Jira può essere dichiarata **Done** soltanto quando tutti i criteri applicabili sono soddisfatti. Il superamento della DoD **non equivale** a una certificazione del robot o delle sue caratteristiche hardware.

## Checklist

- [ ] Tutti gli Acceptance Criteria (AC) sono soddisfatti e supportati da evidenze consultabili o riproducibili.
- [ ] Codice, documenti e altri artefatti previsti sono versionati nel repository, **se applicabile**.
- [ ] Documentazione tecnica, interfacce, istruzioni di configurazione e riferimenti interessati sono aggiornati, **se applicabile**.
- [ ] Test e ispezioni pertinenti sono stati eseguiti e ne sono registrati esiti, errori e limitazioni, **se applicabile**.
- [ ] Non rimangono difetti bloccanti né rischi di sicurezza inaccettabili nell'ambito consegnato.
- [ ] Limitazioni residue, rischi non bloccanti accettati e attività successive sono documentati e tracciati in Jira.
- [ ] Le modifiche al repository hanno superato i controlli pertinenti e sono state revisionate e integrate nel branch di destinazione, **se applicabile**.
- [ ] Jira riporta i collegamenti a commit, PR, documenti o altre evidenze pertinenti e descrive il risultato consegnato.
- [ ] Per attività hardware che coinvolgono alimentazione, cablaggio o movimentazione, i controlli applicabili della [checklist di sicurezza](HARDWARE_SAFETY.md) sono superati e documentati.

## Classificazione delle verifiche

| Esito | Significato | Impatto sulla DoD |
| --- | --- | --- |
| **PASS** | Verifica eseguita con risultato positivo ed evidenza adeguata. | Criterio soddisfatto. |
| **FAIL** | Verifica eseguita con risultato negativo. | Blocca Done se il controllo è obbligatorio; eventuali difetti non bloccanti devono essere valutati e tracciati. |
| **NOT TESTED** | Verifica pertinente ma non eseguita, oppure senza evidenza sufficiente. | Non vale come PASS; se obbligatoria, blocca Done. |
| **N/A** | Verifica non pertinente per il perimetro della issue, con motivazione registrata. | Non blocca Done. |

Le evidenze possono essere link a test, commit, PR, log, fotografie, misurazioni o verbali di ispezione. Devono dimostrare il criterio dichiarato: un semplice collegamento senza riscontro non è sufficiente.

Una task successiva **non sostituisce** il soddisfacimento di un AC obbligatorio e non giustifica un rischio di sicurezza irrisolto.

## Procedura di chiusura

1. Verificare gli AC applicabili.
2. Eseguire test e checklist pertinenti; registrare gli esiti.
3. Aggiornare la documentazione e collegare le evidenze in Jira.
4. Revisionare e integrare nel branch di destinazione le modifiche al repository, quando previste.
5. Impostare Done in Jira soltanto dopo il superamento dei controlli obbligatori.

Il livello delle verifiche deve essere proporzionato al perimetro e ai rischi effettivi dell'attività.
