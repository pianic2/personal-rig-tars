# RTARS-30 — Due preset di processo CANDIDATI da importare

## Provenienza e integrità
L'utente ha fornito `Process presets.zip` (SHA-256 `26f41f13772589bdeb85dbb3520e3a09d85a93c722a14ac493b4700f354d13ae`). Sono stati generati due JSON nativi derivati dai preset di processo utente, distribuiti temporaneamente come allegato privato in chat `RTARS-30-BambuStudio-Preset-CANDIDATI.zip` (SHA-256 `c9319301e111e8733a35fe460bce21c2f845ba192b307ce1a03ec63359fd10db`). **L'allegato ZIP non è ancora parte della PR o del repository**: questa pagina versione la ricetta riproducibile e gli SHA dei due JSON.

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
- **NOT TESTED:** preset macchina corretto e relativo G-code, preset filamento ELEGOO PLA Metallic Metal Bronze; al momento lo screenshot usa Generic PLA.
- **NOT TESTED:** slicing dei quattro piatti con i due profili dedicati, verifica orientamenti/supporti e fit test.

Per RTARS-30 **non** basta il test di parsing JSON, né lo screenshot di vecchio HL-18 QUALITY. Non creare G-code da lanciare sulla macchina fino alla verifica del vero preset Neptune 4 Standard con ugello 0,4, della temperatura/ventilazione del PLA Metallic e delle istruzioni di avvio/fine Klipper. Non pubblicare modelli e derivati MakerWorld.
