# Scripts

Script riproducibili per sviluppo e validazione. Documentare prerequisiti, parametri ed effetti collaterali.

- `validate_rtars18.py`: preflight dry-run per il firmware TARS Global, fissato a `rig_tars_rl` `456e3ee95ccbe94deae9484568719e8686b4b68b`. Uso, modalità build/probe/flash, conferma richiesta e privacy: [procedura RTARS-18](../docs/firmware/AUTOMATED_VALIDATION.md). Flash e probe sono opt-in; la scrittura richiede porta rilevata, preflight superato, lock dipendenze e frase di conferma.
