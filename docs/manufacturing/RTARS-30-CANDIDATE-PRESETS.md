# RTARS-30 — Due preset di processo CANDIDATI da importare

## Provenienza e integrità
L'utente ha fornito `Process presets.zip` (SHA-256 `26f41f13772589bdeb85dbb3520e3a09d85a93c722a14ac493b4700f354d13ae`). Sono stati generati due JSON nativi derivati dai preset di processo utente, distribuiti temporaneamente come allegato privato in chat `RTARS-30-BambuStudio-Preset-CANDIDATI.zip` (SHA-256 `c9319301e111e8733a35fe460bce21c2f845ba192b307ce1a03ec63359fd10db`). **Entrambi i JSON nativi sono ora committati nella PR #28** sotto [`docs/manufacturing/presets/`](presets/). Lo ZIP originale resta privato; questa pagina versione la ricetta riproducibile e gli SHA dei due JSON. Il loro Git blob SHA-1 è stato confrontato con i bytes originali dello ZIP e coincide esattamente.

| Preset candidato | Sorgente originale | Campi modificati |
|---|---|---|
| RTARS-AESTHETIC CANDIDATE 0.16mm @Elegoo Neptune4 0.4 nozzle | HL-18 QUALITY 0.20mm @Elegoo Neptune4 0.4 nozzle | `layer_height` `0.2` → `0.16`, `name`, `print_settings_id` |
| RTARS-FUNCTIONAL CANDIDATE 0.20mm @Elegoo Neptune4 0.4 nozzle | PLA_DIAGNOSTIC_CONSERVATIVE 0.20mm @Elegoo Neptune4 0.4 nozzle | Solo `name`, `print_settings_id` |

Tutti gli altri campi restano **identici** ai rispettivi JSON di input: **non** si attribuisce calibrazione, portata, resistenza o precisione ai due processi.

**Digest JSON generati:**
- AESTHETIC SHA-256: `d1de21d70d9146e16a79656243147c75295e3930dd79bdadab5c5b7741c6ece8`
- FUNCTIONAL SHA-256: `3493204d0bd54ac68945e28208d2c294cd1e08be1f99b952b525a0f487c6d38d`

### Riproduzione dal file ZIP originale
1. Estrarre i due file sorgente nominali nell'archivio originario.
2. Caricare i file JSON UTF-8.
3. Per AESTHETIC, impostare `layer_height` a stringa `"0.16"`, modificare `name` e `print_settings_id` al nuovo nome indicato in tabella.
4. Per FUNCTIONAL, modificare solo `name` e `print_settings_id` al nuovo nome.
5. Serializzare i JSON, conservando **tutti gli altri 277/278 campi**, e provare l'import in Bambu Studio in ambiente locale. Il file ZIP consegnato in chat contiene i JSON completi e un manifest per checksum.

## Gate di validazione
- **PASS:** generazione automatizzata e sintattica dei due JSON da file autentici forniti dall'utente.
- **PASS — dichiarazione utente (2026-11-22):** entrambi i JSON candidati importati correttamente in Bambu Studio, senza errori segnalati. Conferma operativa dell'importazione, non verifica indipendente del contenuto dopo l'import.
- **NOT TESTED:** comparazione delle impostazioni effettivamente importate con i JSON (layer, velocità, supporti e override).
- **PASS:** entrambi i JSON nativi sono presenti su GitHub, letti dopo il commit e verificati byte-identici al file distribuito (SHA-256 in tabella sopra e Git blob SHA-1).
- **PASS statico:** file `3_parts.gcode` mostra uso del profilo FUNCTIONAL.
- **PARTIAL:** macchina/G-code in revisione statica, preset Generic PLA @Elegoo documentato in RTARS-29 senza calibrazione Metallic Bronze dedicata.
- **NOT TESTED:** revisione locale motivata degli orientamenti/supporti del lotto (vedi [`RTARS-30-THREE-PART-ORIENTATION-SUPPORT-CHECKLIST.md`](RTARS-30-THREE-PART-ORIENTATION-SUPPORT-CHECKLIST.md)); slicing di entrambi i profili su tutti i quattro piatti non richiesto per il primo lotto di RTARS-31; fit test fisici downstream.

Per RTARS-30 **non** basta il test di parsing JSON, né lo screenshot di vecchio HL-18 QUALITY. Non creare G-code da lanciare sulla macchina fino alla verifica del vero preset Neptune 4 Standard con ugello 0,4, della temperatura/ventilazione del PLA Metallic e delle istruzioni di avvio/fine Klipper. Non pubblicare modelli e derivati MakerWorld.

## Decisione quantitativa 2026-11-22 — profilo da utilizzare per RTARS-31

**SELEZIONE: RTARS-FUNCTIONAL CANDIDATE 0.20mm**, come profilo unico per la prima prova funzionale (NON approvazione della produzione definitiva). La decisione confronta i JSON originali delle due configurazioni importate dall'utente; per evitare otto slicing dei quattro piatti, si richiede **un solo provino funzionale selezionato**, dopo i controlli macchina/materiale.

| Parametro nei JSON | AESTHETIC 0.16 | FUNCTIONAL 0.20 | Valutazione |
|---|---:|---:|---|
| Layer (mm) | 0.16 | 0.20 | Functional 25% più alto, 20% meno layer a parità di altezza Z nominale (non una misura del tempo) |
| Outer wall speed (mm/s) | 50 | 35 | Functional 30% più lento |
| Inner wall speed (mm/s) | 70 | 45 | Functional 35.7% più lento |
| Infill speed (mm/s) | 80 | 55 | Functional 31.25% più lento |
| Acceleration generale (mm/s²) | 1500 | 700 | Functional 53.3% inferiore |
| Accelerazione parete esterna (mm/s²) | 800 | 400 | Functional 50% inferiore |
| Primo layer speed (mm/s) | 30 | 18 | Functional 40% più lento |
| Wall loops | 3 | 3 | parità |
| Infill | 25% | 25% | parità |
| Supports | normal(auto), 30° | normal(auto), 30° | parità, da verificare sulla geometria |

**Interpretazione:** velocità/accelerazioni più conservative riducono il carico dinamico nominale ma non dimostrano precisione dimensionale, adesione o resistenza. La riduzione dei layer è puramente geometrica e non equivale a −20% di tempo. Tempo e massa reali col nuovo preset **sconosciuti**; il run QUALITY 23h19m non è riutilizzabile come previsione FUNCTIONAL.

### Gate di esecuzione
- **PASS:** entrambi i preset importati, secondo dichiarazione utente; decisione quantitativa riproducibile.
- **PARTIAL macchina/materiale:** Neptune 4 Standard/ugello 0,4, flavor Klipper e 210/205/60°C documentati da RTARS-29 e G-code effettivo. Lo start/end G-code è stato ispezionato staticamente; sicurezza esecutiva, verifica supporti per interfacce e calibrazione Generic PLA per Metallic Bronze non certificate. Prima di avviare stampa reale eseguire preflight locale.
- **PASS per Done RTARS-30:** i due profili sono versionati come JSON nativi in `docs/manufacturing/presets/`, con SHA originali verificati; il G-code `3_parts` prova lo slicing FUNCTIONAL.
- **PENDING per Done RTARS-30:** verifica motivata di orientamenti e supporti per le parti su Preview, con verbale di ispezione locale; nessun test fisico viene implicitamente considerato completato.
- **NON autorizzata:** stampa definitiva RTARS-32.
