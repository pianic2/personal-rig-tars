# RTARS-20 — Ispezione visiva della RIG-Board e dei componenti elettronici

**Jira:** https://niccolopiazzi01.atlassian.net/browse/RTARS-20  
**Data ispezione/documentazione:** 2026-11-22  
**Metodo:** analisi di due fotografie reali fronte/retro + dichiarazione del proprietario. Nessuna prova elettrica o sotto tensione effettuata nell'ambito di questa verifica.  
**Perimetro:** individuazione visiva di marcature, connettori, possibili danni; non equivale a collaudo funzionale o certificazione elettrica.

## Evidenza fotografica versionata

| Lato | Foto consultabile | Originale fornito nella conversazione | SHA-256 originale | Risoluzione pubblicata |
| --- | --- | --- | --- | --- |
| Lato connettori e circuiti di alimentazione | [pcb-connectors-side.webp](pcb-connectors-side.webp) | `1000166689.heic` (contenuto JPEG, non HEIC) | `47f9bdd20a756436578f8ca92717174e1e3fd40198d8ea522006372b2d38cc15` | 1050 × 1230 |
| Lato modulo ESP32 e antenna | [pcb-esp32-side.webp](pcb-esp32-side.webp) | `1000166688.heic` (contenuto JPEG, non HEIC) | `0ae97dd27bdc69e4a7a6a20f81e795ecad26f2469c66f7ba975d1ac90b7e41a4` | 1050 × 1311 |

Le due immagini sono copie convertite in WebP, ridimensionate e senza metadati fotografici; **non** sono copie bit-per-bit degli originali. Gli SHA-256 delle copie pubblicate sono in [SHA256SUMS](SHA256SUMS). Gli SHA-256 originali coincidono con le foto già censite in [RTARS-9](../hardware/RTARS-9/pcb-inspection-2026-11-22.md), permettendo di confrontare la provenienza senza attribuire due ispezioni indipendenti alla stessa evidenza.

## Identificazione e inventario visivo

| Elemento | Rilievo | Stato |
| --- | --- | --- |
| PCB | Serigrafia `RIG-Board` e `26/6/25` | Identificata la marcatura; revisione esatta **non verificata** |
| Modulo wireless/controller | `ESP32-S3-WROOM-1`, marcatura `MCN16R8` | Identificabile fotograficamente; non prova il funzionamento |
| Porte servo | Tre connettori bianchi a 3 contatti, riferimenti `Servo` sul lato opposto | Censiti; pinout e assegnazione dei singoli servo **non verificati** |
| Connettori FPC/FFC | Due connettori piatti di diversa larghezza | Censiti; segnali e destinazioni non verificati |
| Speaker | Connettore a 2 pin, serigrafia `SPK` | Censito |
| Alimentazione | Connettore bianco a 2 pin sul bordo inferiore, fra interruttore e USB-C | Censito; polarità serigrafata già documentata in RTARS-9, **plug batteria non verificato** |
| USB | Porta USB-C sul bordo inferiore | Presente; nessuna prova della porta |
| Interruttore | Elemento meccanico sul bordo inferiore | Presente; nessuna prova di continuità |
| Altri connettori | Piccoli connettori bianchi nella parte alta/destra del lato componenti | Visibili; funzione non attribuita senza schema verificato |
| Circuiti / marcature | `SLM6800`, `117-3.3`, induttori `2R2`, altre sigle non sempre leggibili | Censite le marcature leggibili; nessuna deduzione sull'alimentazione del pacco consegnato |

La marcatura `26/6/25` **non è una revisione PCB accertata**. La scheda tecnica del singolo IC non certifica l'intero circuito, la batteria o lo schema TARS.

## Integrità e anomalie

| Controllo | Riscontro | Esito nel perimetro |
| --- | --- | --- |
| Fotografie di entrambe le facce | Due foto acquisite, confrontabili con i digest originali e versionate come WebP | **PASS** |
| Danneggiamenti macroscopici a PCB, componenti, piste e connettori | Nessuna lesione, bruciatura o deformazione evidente nelle aree fotografate; la foto non garantisce verifica microscopica | **PASS — solo visivo** |
| Condizione generale degli altri componenti elettronici del kit | Proprietario: «Nessun danno a nessun componente» | **PASS — dichiarazione del proprietario** (non ispezione fotografica individuale) |
| Batteria / precondizione ispezione | Proprietario: «la batteria non l'ho mai inserita»; nessun cavo collegato alle porte nelle fotografie | **PASS** per assenza di batteria inserita dichiarata; alimentazioni pregresse da USB **non attestate** |
| Stabilità fisica dei connettori, saldature, continuità e cortocircuiti | Non verificabili compiutamente dalle fotografie | **NOT TESTED**, fuori dall'accertamento fotografico |
| Prove elettriche, flashing, ricarica e movimento | Non eseguite e non richieste dalla task | **N/A** per l'ispezione fotografica; **non** autorizzate da questo esito |

**Nuove anomalie fisiche evidenti:** nessuna riscontrata nelle foto e nessuna dichiarata dal proprietario. Eventuali riflessi/residui superficiali o giunti non perfettamente distinguibili non vengono automaticamente classificati come danni. In caso di successiva anomalia, aprire o collegare una issue Jira prima di procedere.

## Safety gate / limiti espliciti

- Questo report **non abilita l'accensione**. Restano aperti i dubbi preesistenti di RTARS-9 su batteria senza specifiche, polarità del plug, revisione PCB, pinout e modello servo (D08/D09).
- **Alimentazione:** NOT TESTED come collaudo. Non collegare o ricaricare il pacco finché tensione, composizione, protezioni e corrispondenza del cablaggio non siano verificate sulle specifiche applicabili.
- **Cablaggio:** NOT TESTED: orientamento, serraggio, pinout e continuità saranno verificati nella relativa attività di collegamento.
- **Movimentazione:** N/A: nessun montaggio o test di movimento previsto da RTARS-20.
- Nessuna modifica o saldatura alla PCB eseguita in questa attività.

Riferimenti: [Definition of Done](../../docs/process/DEFINITION_OF_DONE.md), [sicurezza hardware](../../docs/process/HARDWARE_SAFETY.md), [documentazione RTARS-9](../../docs/hardware/bom/README.md), [guida assemblaggio ufficiale](https://wiki.xgorobot.com/kb/the-rig-series-robot/rig_en_tars_assembly).

## Acceptance Criteria (Jira RTARS-20)

- **Foto delle due facce PCB:** PASS — immagini pubblicate nella presente cartella.
- **Connettori ed etichette censiti:** PASS per ciò che è distinguibile sulle fotografie; sigle/pinout ignoti esplicitamente segnalati.
- **Danni censiti:** PASS nel perimetro di ispezione visiva; nessun danno evidente o dichiarato.
- **Anomalie in Jira:** nessuna **nuova anomalia** da aprire in questa ispezione; i rischi e le discrepanze preesistenti restano tracciati in RTARS-9 e non sono chiusi per effetto della presente task.

**Conclusione:** ispezione visiva documentata con esito positivo limitato; **nessun collaudo funzionale/elettrico certificato**.
