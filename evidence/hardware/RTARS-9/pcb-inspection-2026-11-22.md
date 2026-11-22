# RTARS-9 — Ispezione fotografica RIG-Board: due lati PCB

**Data:** 2026-11-22  
**Provenienza:** due immagini caricate dall'utente nel dialogo. Sono fotografie del PCB realmente ricevuto, **non** uno schema elettrico né test di misura. La versione binaria **non è archiviata in GitHub**; sono conservati nome, impronte SHA-256 e riscontri visuali.

## Evidenze originali

| File caricato | Byte reali (magic) | Dimensioni | SHA-256 |
| --- | --- | --- | --- |
| `1000166688.heic` | JPEG/JFIF, non HEIC | 1230 × 1536 | `0ae97dd27bdc69e4a7a6a20f81e795ecad26f2469c66f7ba975d1ac90b7e41a4` |
| `1000166689.heic` | JPEG/JFIF, non HEIC | 1311 × 1536 | `47f9bdd20a756436578f8ca92717174e1e3fd40198d8ea522006372b2d38cc15` |

Il primo file è il **retro** della PCB (ESP32 e antenna); il secondo è il **lato connettori** (servo, SPK, flat, USB-C e circuiti alimentazione).

## Identificazione diretta dalle foto

| Caratteristica | Evidenza ottica | Confidence / limiti |
| --- | --- | --- |
| Carrier PCB | Serigrafia `RIG-Board` e `26/6/25` sul retro | Alta lettura; **non prova codice di revisione** |
| Modulo Espressif | Schermatura marcata `ESP32-S3-WROOM-1` e `MCN16R8` | Alta lettura; la denominazione di variante `N16R8` è associata da Espressif a **16 MB Flash + 8 MB PSRAM**. Non equivale alla revisione PCB |
| Charger / power management | IC frontalmente marcato `SLM6800`, linea successiva `2310`; vicino a induttore `2R2` | Alta lettura della sigla. La scheda tecnica ufficiale SOLA descrive il SLM6800 come caricatore a conversione boost **per due celle Li-ion**; non dimostra la chimica, configurazione o tensione effettiva del pacco batteria incluso |
| Connettori servo | Tre connettori a tre contatti sull'orlo superiore; sul retro etichette `Servo` visibili | Numerosità e funzione di famiglia supportate; assegnazioni pin V/GND/segnale e ID effettivi non accertate |
| Speaker | Connettore piccolo a due contatti con scritta `SPK` | Funzione leggibile |
| Flex | Due connettori FPC larghi, misura diversa | Sono connessioni fisiche; il pinout e l'associazione a display/camera non dimostrati dall'immagine PCB isolata |
| USB | Porta USB-C sul lato inferiore a destra | Visibile |
| Switch | Componente meccanico sul bordo inferiore a sinistra del connettore batteria | Visibile; funzione elettrica non certificata |
| Altro circuito | Marcatura `117-3.3` | Leggibile, ma **non identificare come circuito specifico o pinout senza datasheet** |

## Polarità serigrafata presso il connettore della batteria

**Orientamento obbligatorio per interpretare la frase sinistra/destra:** PCB con il **lato dei componenti e dei connettori verso l'osservatore**, i **tre servo socket in alto**, e la **porta USB-C in basso a destra**.

Nell'orientamento sopra:
- il **connettore bianco a due contatti sul bordo inferiore**, fra l'interruttore e USB-C, mostra **`+` sul pin vicino all'interruttore di accensione/spegnimento**;
- e **`−` (GND) sul pin vicino alla porta USB-C**.

Questa formulazione usa **riferimenti fisici stabili** e prevale sulle descrizioni «sinistro»/«destro», che dipendono dall'orientamento. La disposizione è confermata anche dal proprietario nel messaggio successivo alle fotografie: «pin terra e vicino alla porta usb-c mentre il pin positivo e vicino al bottone di accendimento/spengimento». Non dimostra la corrispondenza dei fili del plug della batteria.

Queste sono **serigrafie** presenti sulla PCB, non una misurazione strumentale. La direzione può invertirsi osservando il plug della batteria dall'altro lato o dal lato cavi. Non ricavare la posizione di rosso/nero dall'aspetto dei connettori o dalla loro compatibilità meccanica. Identificare il pinout del plug batteria **nel medesimo sistema di riferimento** con schema ufficiale e controllo competente prima di inserire il connettore.

## D08 — Stato verificabile

**FATTO NUOVO:** polarità nominale dei due pin marcata su PCB e charger chip `SLM6800` identificato.

**ANCORA SCONOSCIUTI:** numero di celle del pacco fisico, V nominale e massima, capacità, chimica dichiarata dal produttore, BMS/protezioni, indicazione polarità/ordine fili *del plug batteria*, comportamento di ricarica sul PCB specifico e revisione del PCB. Il chip SLM6800 supporta un sistema 2-cell Li-ion, ma **non è prova** che il pacco blu senza scritte sia quello giusto o che il suo connettore sia cablato correttamente.

**Stato:** `OPEN`. Nessuna autorizzazione ad alimentare o ricaricare la batteria o a collegare un alimentatore a un pin di alimentazione non verificato.

## D09 — Stato verificabile

**FATTO NUOVO:** il modulo Espressif **ESP32-S3-WROOM-1 / MCN16R8** è leggibile sul retro. Per la sua variante N16R8 Espressif pubblica 16 MB Flash + 8 MB PSRAM.

**ANCORA SCONOSCIUTI:** numero di revisione **carrier PCB RIG-Board**, numero di modello dei tre servomotori senza etichetta, protocollo e pinout servo, collegamento reale delle funzioni della board.

**Stato:** `OPEN` per la parte non verificata. La presenza del modulo è da considerare identificata a livello hardware.

## Fonti tecniche dei componenti (non della board RIG-TARS)

- Espressif, **ESP32-S3-WROOM-1**, moduli e datasheet: https://www.espressif.com/en/products/modules/esp32-s3-wroom-1-wroom-1u
- SOLA Microelectronics, **SLM6800 Two-Cell Boost Mode Li-Ion Battery Charger**: https://www.slm-ic.com/en/show-27-9-1.html

**Nota metodologica:** il datasheet di un componente montato sulla PCB non sostituisce lo schema elettrico della carrier e non certifica il circuito completo, il tipo di batteria o i vincoli operativi dell'intero robot.

