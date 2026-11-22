# Inventario attrezzature e materiali — RTARS-13

**Issue:** [RTARS-13](https://niccolopiazzi01.atlassian.net/browse/RTARS-13)  
**Ultimo aggiornamento:** 2026-11-22  
**Ambito:** strumenti di lavoro, software e consumabili usati per stampa FDM, assemblaggio e diagnosi di RIG-TARS.  
**BOM dei componenti del robot:** [RTARS-9](../hardware/bom/README.md) (mantenuta separata per evitare duplicazioni).

## Criteri di lettura

- **DISPONIBILE — dichiarato:** possesso esplicitamente confermato dall'utente; caratteristiche/quantità ignote non vengono dedotte.
- **DOCUMENTATO — storico:** possesso o acquisto riportato in precedenti conversazioni; disponibilità attuale o quantità residua da verificare.
- **DA VERIFICARE:** non selezionato nella ricognizione oppure assenza di conferma; **non** equivale a mancante.
- **MANCANTE:** dichiarato esplicitamente assente nella ricognizione attuale. Nessun elemento è classificato così senza conferma.
- **NON APPLICABILE:** utilità non ancora stabilita rispetto a una fase operativa.

Gli ID sono stabili. Non considerare l'elenco un ordine d'acquisto. L'utente dichiara di possedere assortimenti completi di misure e forme degli utensili manuali: non occorre inventariare singolarmente le misure. La compatibilità si verifica comunque durante l'uso, evitando forzature.

## 1. Attrezzatura fisica

| ID | Categoria | Attrezzo | Stato | Quantità / note | Uso previsto |
| --- | --- | --- | --- | --- | --- |
| TOOL-001 | Assemblaggio | Cacciaviti a croce di precisione | DISPONIBILE — dichiarato | Assortimento completo di misure dichiarato | Viti con impronta a croce |
| TOOL-002 | Assemblaggio | Pinzette di precisione | DISPONIBILE — dichiarato | Forme e misure disponibili dichiarate | Piccole parti e connettori |
| TOOL-003 | Assemblaggio | Tronchesine | DISPONIBILE — dichiarato | Modello da verificare | Taglio fascette/filo, con cautela |
| TOOL-004 | Assemblaggio | Chiavi esagonali / brugole | DISPONIBILE — dichiarato | Assortimento completo dichiarato; non dedurre uso su viti del kit | Eventuali elementi esagonali |
| TOOL-005 | Misura | Calibro digitale | DISPONIBILE — dichiarato | Disponibilità confermata; caratteristiche metrologiche non essenziali a questo inventario | Quote di stampe e accoppiamenti |
| TOOL-006 | Elettronica | Multimetro digitale | DISPONIBILE — dichiarato | Modello da verificare | Verifiche elettriche a circuito disalimentato, ove applicabile |
| TOOL-007 | Elettronica | Saldatore a stagno | DISPONIBILE — dichiarato | Temperatura/punte da verificare | Eventuali lavorazioni autorizzate |
| TOOL-008 | Elettronica | Stagno e flussante | DISPONIBILE — dichiarato | Lega, diametro e quantità da verificare | Saldature, se necessarie |
| TOOL-009 | Elettronica | Pinze spelafili | DISPONIBILE — dichiarato | Sezioni compatibili da verificare | Preparazione cavi, se necessaria |
| TOOL-010 | Stampa FDM | Spatola per rimozione stampe | DISPONIBILE — dichiarato | Modello da verificare | Rimozione pezzi a piatto freddo |
| TOOL-011 | Finitura | Carta abrasiva / lime | DISPONIBILE — dichiarato | Grane e geometrie da verificare | Rifinitura pezzi |
| TOOL-012 | Stampa FDM | Essiccatore per filamenti | DISPONIBILE — dichiarato | Disponibilità confermata; parametri operativi da leggere sul modello prima dell'uso | Gestione filamenti umidi |
| TOOL-013 | Finitura | Colla per plastica | DISPONIBILE — dichiarato | Tipo chimico e compatibilità PLA da verificare | Incollaggi solo dove previsti |
| TOOL-014 | Elettronica | Alimentatore da banco | DA VERIFICARE | Non selezionato; non dichiarato mancante | Eventuale diagnosi |
| TOOL-015 | Finitura | Utensile per sbavatura | DA VERIFICARE | Non selezionato; lime già disponibili come possibile alternativa | Bordi delle stampe |
| TOOL-016 | Laboratorio | Pinza generica | DOCUMENTATO — storico | Segnalata nel progetto Stampa 3D; verificare disponibilità attuale | Presa e manipolazione |
| TOOL-017 | Laboratorio | Bilancia | DOCUMENTATO — storico | Modello/risoluzione da verificare | Misurazione massa consumabili/pezzi |
| TOOL-018 | Laboratorio | Cutter | DOCUMENTATO — storico | Modello da verificare | Piccoli tagli, con protezioni adeguate |
| TOOL-019 | Laboratorio | Trapano | DA VERIFICARE | Segnalato assente nell'agosto 2026, non ricontrollato oggi | Solo eventuali lavorazioni meccaniche |

### Alternative e assenze

| Oggetto | Alternativa o mitigazione | Stato della valutazione |
| --- | --- | --- |
| Utensile per sbavatura | Lime/carta abrasiva già disponibili, se geometria e tolleranze lo consentono | Alternativa disponibile per finitura ordinaria; necessità di attrezzo dedicato non dimostrata |
| Alimentatore da banco | Nessuna alternativa validata | Necessità da stabilire; **non** sostituire con alimentazioni improvvisate |
| Trapano | Nessuna alternativa validata | Necessità da stabilire sui modelli ufficiali |
| Utensili a croce | Assortimento di misure/formati dichiarato completo | Nessun acquisto richiesto; scegliere la punta corretta durante l'assemblaggio |

## 2. Stampante e ambiente

| ID | Risorsa | Stato | Specifiche documentate / limiti |
| --- | --- | --- | --- |
| EQUIP-001 | ELEGOO Neptune 4 **Standard** | DISPONIBILE — dichiarato | FDM, volume nominale 225 × 225 × 265 mm; ugello stock brass 0,4 mm storico; sostituito con acciaio temprato 0,4 mm (dichiarazione operatore 2026-11-22, RTARS-29) |
| EQUIP-002 | Ventilazione stampante | DOCUMENTATO — storico | Gruppo ausiliario posteriore a quattro ventole descritto; funzionalità corrente non testata in questa task |
| EQUIP-003 | Controllo stampante via LAN | DOCUMENTATO — storico | Klipper ELEGOO / Fluidd / Moonraker riportati come configurazione; versione e connettività attuali da verificare |
| EQUIP-004 | Ambiente di stampa | DOCUMENTATO — storico | Misurazione indicativa ~25 °C e 50% UR in precedente conversazione, **non** valore attuale |

La Neptune 4 Standard è distinta da Pro, Plus e Max. I dati di volume/ugello sono specifiche documentate e non costituiscono nuova ispezione hardware.

## 3. Filamenti e consumabili di stampa

L'utente dichiara in data 2026-11-22 **oltre 800 g di filamento residuo per ciascuna delle cinque varianti elencate**. Sono quantità dichiarate, non pesate in questa task. I prezzi sono storici, non correnti.

| ID | Materiale | Colore | Formato / diametro | Stato | Evidenza e note |
| --- | --- | --- | --- | --- | --- |
| MAT-001 | ELEGOO Rapid PLA+ | Black | 1,75 mm; residuo >800 g (dichiarato) | DISPONIBILE — dichiarato | Materiale effettivamente usato nei test Neptune 4, T1-M01 |
| MAT-002 | ELEGOO PLA Pro | Burgundy Red | Residuo >800 g (dichiarato); diametro non rilevato | DISPONIBILE — dichiarato | Acquisto dichiarato 2026-08-28, €14,08 |
| MAT-003 | ELEGOO PLA Matte | Sakura Pink | Residuo >800 g (dichiarato); diametro non rilevato | DISPONIBILE — dichiarato | Acquisto dichiarato 2026-08-28, €14,90 |
| MAT-004 | ELEGOO PLA Metallic | Metal Bronze **(scelto per RIG-TARS)** | Residuo >800 g (dichiarato); diametro non rilevato | DISPONIBILE — dichiarato | Acquisto dichiarato 2026-08-28, €15,73; *metallic* è denominazione commerciale, non prova di caricamento metallico abrasivo |
| MAT-005 | ELEGOO Rapid PLA Plus | White | Residuo >800 g (dichiarato); diametro non rilevato | DISPONIBILE — dichiarato | Acquisto dichiarato 2026-08-28, €13,25 |
| MAT-006 | Alcool isopropilico (IPA) | — | Concentrazione ignota | DA VERIFICARE | Non selezionato; non dichiarato mancante |
| MAT-007 | Frenafiletti aggiuntivo | — | Tipo ignoto | DA VERIFICARE | Distinto da eventuale frenafiletti preapplicato a viti del kit |
| MAT-008 | Ulteriori filamenti PETG / TPU / ASA / ABS / Nylon | — | — | DA VERIFICARE | Discussioni/raccomandazioni pregresse **non** equivalgono ad acquisto o possesso |

**Totale storico degli acquisti MAT-002–MAT-005:** €57,96 (quattro acquisti dichiarati, non quattro bobine necessariamente ancora disponibili). Non sommare il prezzo di MAT-001 perché qui non è documentato in modo univoco.

**Vincolo di processo:** l'utente ha segnalato in precedenza filamento con popping/sintomi di umidità. La disponibilità di un essiccatore non dimostra che il filamento sia asciutto: verificare condizioni prima delle stampe prolungate.

## 4. Software e toolchain

| ID | Risorsa | Stato | Versione / note |
| --- | --- | --- | --- |
| SW-001 | OrcaSlicer | DOCUMENTATO — storico | 2.8.2 riportato nell'ambiente Debian |
| SW-002 | Bambu Studio | DOCUMENTATO — storico | Usato nel progetto Stampa 3D; versione attuale non rilevata |
| SW-003 | Klipper ELEGOO | DOCUMENTATO — storico | Firmware/controllo Neptune 4; build corrente non rilevata |
| SW-004 | Fluidd e Moonraker | DOCUMENTATO — storico | Interfaccia/API Neptune 4; versioni correnti non rilevate |
| SW-005 | ESP-IDF | DOCUMENTATO — storico | 5.5.3, installazione/verifica riportata nel progetto RTARS; nuova verifica non eseguita qui |
| SW-006 | CMake, Ninja, Xtensa toolchain e OpenOCD | DOCUMENTATO — storico | Presenza riportata durante controllo ESP-IDF; non si attribuiscono versioni non verificate |
| SW-007 | Git/GitHub | DISPONIBILE — operativo | Repository pianic2/personal-rig-tars, gestione versionata |
| SW-008 | Jira RTARS | DISPONIBILE — operativo | Tracciamento lavori e collegamenti a evidenze |

## 5. Separazione dall'inventario dei componenti RIG-TARS

Il kit acquistato è il **RIG Serie Robots: TARS** di Luwu Dynamics, variante maker senza parti plastiche stampate. Componenti elettronici, attuatori, minuteria e quantità della confezione appartengono alla [BOM RTARS-9](../hardware/bom/README.md), non a questo inventario degli strumenti.

La classificazione delle viti del kit deve rimanere aderente alle ultime ispezioni/fotografie RTARS-9: **non** dedurre teste esagonali o dadi da descrizioni precedenti discordanti. Le brugole possedute non indicano che siano necessarie per il kit.

## 6. Verifiche aperte e criteri di completamento

- [x] Strumenti selezionati e dichiarati disponibili riportati individualmente.
- [x] Materiali di stampa recuperati da evidenze storiche con nomi/varianti documentati.
- [x] Elementi non selezionati conservati come **DA VERIFICARE**, non marcati mancanti.
- [x] Alternative/assenze non dimostrate esplicitate; nessuna compatibilità non testata dichiarata valida.
- [x] Quantità residue registrate come dichiarazione dell'utente (>800 g per ciascuna delle cinque varianti); diametro delle varianti non rilevate e condizioni del filamento restano controlli operativi prima della stampa, non blocchi dell'inventario.
- [x] Essiccatore registrato come disponibile; modello e parametri conformi ai produttori saranno verificati prima di un ciclo concreto, senza bloccare questa task documentale.
- [x] Assortimento completo di misure/formati degli utensili dichiarato dall'utente; scelta della punta corretta demandata all'assemblaggio.
- [x] Alimentatore da banco e trapano mantenuti DA VERIFICARE come dotazioni **non necessarie per chiudere l'inventario**; necessità operativa futura valutata quando emerge. Lime/carta abrasiva già disponibili per finitura ordinaria.
- [x] Le attrezzature note solo da storico rimangono esplicitamente classificate DOCUMENTATO — storico; la loro disponibilità non viene promossa senza conferma, come previsto dall'AC di inventariazione.

### Provenienza e revisione

- **Ricognizione diretta:** conferme dell'utente del 2026-11-22 (13 voci selezionate; assortimenti completi di utensili; cinque varianti di filamento con residuo >800 g ciascuna; Metal Bronze scelto per RIG-TARS).
- **Progetto Stampa 3D:** dichiarazioni e acquisti registrati tra agosto e novembre 2026; alcune informazioni sono storiche e richiedono verifica fisica corrente.
- **RTARS-9:** fonte canonica per BOM e minuteria del robot.
- **Nessuna evidenza fotografica aggiuntiva** esaminata per questa revisione.

**Esito RTARS-13:** inventario documentale completo rispetto agli AC («attrezzature e materiali elencati; assenze e alternative registrate»). Le verifiche d'uso, l'adeguatezza della stampa e le necessità future restano controlli di fase; non sono prerequisiti per censire gli strumenti. **Filamento selezionato:** ELEGOO PLA Metallic Metal Bronze, scelta dell'utente, non ancora validata con stampa di prova.
