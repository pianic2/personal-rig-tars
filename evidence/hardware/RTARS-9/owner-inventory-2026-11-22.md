# RTARS-9 — Rilievo manuale dichiarato dal proprietario

Data raccolta: **2026-11-22**  
Origine: risposte fornite direttamente nella conversazione dedicata a RTARS-9.  
Natura: **attestazione testuale del proprietario**, non misurazione indipendente dell'assistente. Nessuna prova di revisione o compatibilità tecnica è implicita nelle risposte.

## Identità prodotto e revisione

**Q1 — Qual è esattamente la variante del kit acquistato?**  
Link: https://shop.xgorobot.com/products/rig-tars-fully-open-source-3d-printed-programmable-ai-companion-robot-maker-diy-kit  
Dicitura riferita: `RIG Serie Robots: TARS`.

**Q2 — Sulla confezione/manuale/etichetta compare una versione o numero di lotto?**  
Risposta: «No non compare».

## Elettronica

**Q3 — Quali codici e revisioni sulla scheda?**  
Risposta: `RIG-Board 26/6/2025`. Non è stata riportata una dicitura esplicita di revisione.

**Q4 — Modello sui tre servomotori?**  
Risposta: «Non ha nessuna etichetta o incisione». Modello `SCS009` **non verificato**.

**Q5 — Codice sul display o sul flex?**  
Risposta: `FCP-HD240239C12-V1`. Controller grafico non accertato.

**Q6 — Codice flat fotocamera?**  
Risposta: `HBVCAM-2526 V11`. Sensore effettivo non accertato.

**Q7 — Altoparlante marcato 3514 o altro?**  
Risposta: «No».

**Q8 — Dati elettrici batteria?**  
Risposta: «Nessuno». Nessun parametro elettrico deducibile dalla risposta.

**Q9 — Piccolo circuito antistatico è sensore touch?**  
Risposta: «Si».

## Quantità, accessori e integrità

**Q10 — Numero squadrette servo?**  
Risposta: `3`.

**Q11 — Conteggio per ciascuna delle sei tipologie etichettate nella foto** (tipologia e numero testuali riferiti):

| Etichetta / tipologia | Quantità dichiarata |
| --- | ---: |
| M2×6 autofilettante a croce | **55** |
| M2×4 testa tonda a croce per macchina | **4** |
| M2×4 autofilettante a croce | **4** |
| M2×5 testa piatta a croce per macchina | **2** |
| M3×8 testa piatta a croce per macchina | **1** |
| Dadi esagonali M2 di bloccaggio | **1** |

**Q12 — Sono presenti anche M2×10, M3×10 e dadi autobloccanti M3?**  
Risposta: «no» — quantità osservata `0` per ciascuna di queste **tre** categorie.

**Q13 — Quanti cablaggi distinti, che connettori?**  
Risposta: «la proluga c'e; 3 cavi neri da 3 caveti ciascuno con incastri».  
Interpretazione minimale: 1 prolunga dichiarata presente + 3 cavi neri, ognuno con 3 conduttori e connettori a incastro. **Non** è nota la destinazione dei cavi né è stato esplicitamente identificato il cavo interruttore.

**Q14 — Presenza spugna o isolante morbido?**  
Risposta: «no».

**Q15 — Due contrappesi 20 g ciascuno?**  
Risposta: «si 20g». Due contrappesi presenti; 20 g/unità confermati verbalmente, senza indicazione del metodo di misura.

**Q16 — Danni o componenti apparentemente rotti?**  
Risposta: «no». **Non** equivale a un collaudo funzionale o all'assenza dimostrata di difetti nascosti.

## Regole di utilizzo delle dichiarazioni

1. Il file registra il contenuto delle risposte, che hanno consentito di riempire il CSV. Gli scostamenti dalla distinta V1.0 rimangono nel registro `discrepancies.csv`.
2. Codici `V1`, `V11` e la data `26/6/2025` **non** dimostrano da soli una revisione certificata dell'hardware.
3. Le tre quantità ancora non riconciliate sono `E008` (cavo interruttore), `F002` e `F003` (fissaggi di tipo differente, non equiparabili per sola taglia nominale).
4. L'assenza di M2×10, M3×10, dadi M3 e spugna è **accertata come dichiarazione sull'inventario ricevuto**, ma non determina automaticamente che il venditore abbia sbagliato a confezionare il kit.
5. L'originale della fotografia non è archiviato qui; vedere il manifest per il digest.


## Rettifica successiva del proprietario (22 novembre 2026)

Testo originale: «nella foto lo vedi in basso a sinistra e non ha buste. le viti m2 sono di due categorie distinte svasate autofilettanti e a brugola con frenafiletti».

- Il cavo descritto è il **cavo interruttore E008**, visibile sciolto senza bustina nella zona inferiore sinistra della foto; la voce originaria A008 si riferisce allo **stesso** cavo, non a un'unità aggiuntiva.
- Le due categorie di viti M2×4 vengono specificate dal proprietario come **svasate autofilettanti (F002)** e **a brugola con frenafiletti (F003)**. Sono state ricondotte ai due gruppi già contati in Q11 (**4 + 4**, non altre 8 viti).
- La fonte fotografica riporta tuttavia le etichette `M2*4圆头十字机丝` (testa tonda a croce per macchina) e `M2*4十字自攻螺丝` (autofilettante a croce), diverse dalla nuova classificazione fisica. La differenza rimane **OPEN in D03/D04**, senza sostituire l'una all'altra come fatto certo. Verificare materialmente prima dell'assemblaggio.
- Non modificare retroattivamente le risposte Q1–Q16: questa nota documenta la revisione successiva.
