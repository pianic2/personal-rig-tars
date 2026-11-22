# RTARS-14 — Verifica toolchain ESP-IDF 5.5.3

- **Data:** 2026-11-22, Europe/Rome
- **Ambiente:** Debian 13, Linux x86_64, kernel 6.12.94+deb13-amd64
- **Ambito:** toolchain di sviluppo ESP32-S3 (non compilazione/flash)
- **Esito:** PASS — 3/3 Acceptance Criteria soddisfatti
- **Origine:** output di terminale fornito dall'operatore, anonimizzato

## AC1 — Versione ESP-IDF

```text
$ idf.py --version
ESP-IDF v5.5.3
```

**PASS.** Versione richiesta verificata.

## AC2 — Tool ESP32-S3 installati

```text
$ idf.py --list-targets
esp32
esp32s2
esp32c3
esp32s3
esp32c2
esp32c6
esp32h2
esp32p4
esp32c5
esp32c61

$ xtensa-esp-elf-gcc --version
xtensa-esp-elf-gcc (crosstool-NG esp-14.2.0_20251107) 14.2.0

$ python "$IDF_PATH/tools/idf_tools.py" check
xtensa-esp-elf-gdb: 16.3_20250913 (PATH e tools directory)
xtensa-esp-elf: esp-14.2.0_20251107 (PATH e tools directory)
riscv32-esp-elf: esp-14.2.0_20251107 (PATH e tools directory)
esp32ulp-elf: 2.38_20240113 (PATH e tools directory)
cmake: 3.31.6 (PATH)
openocd-esp32: v0.12.0-esp32-20251215 (PATH e tools directory)
ninja: 1.12.1 (PATH e tools directory)
esp-rom-elfs: 20241011 (tools directory; non nel PATH)
esp-clang: non nel PATH
esp-clang-libs: non nel PATH
qemu-xtensa: non nel PATH
```

**PASS.** Target `esp32s3` elencato e toolchain Xtensa GCC/GDB presente. Le voci opzionali non individuate nel PATH non costituiscono di per sé un fallimento degli AC.

## AC3 — Ambiente attivabile

```text
$ echo "$IDF_PATH"
<ESP_IDF_INSTALL_DIR>

$ python --version
Python 3.13.5

$ cmake --version
cmake version 3.31.6

$ ninja --version
1.12.1
```

**PASS.** `IDF_PATH` valorizzata, `idf.py` e tool richiesti invocabili nell'ambiente attivato.

## Limiti

Non risultano testati compilazione del firmware upstream, flashing o hardware reale. Le attività sono fuori scope per gli AC di RTARS-14. `idf_tools.py check` verifica il rilevamento dei tool e non sostituisce una build.

## Anonimizzazione

Rimossi hostname, nome utente e percorso home assoluto; `IDF_PATH` è riportato come placeholder. Conservati versione OS/kernel, architettura, strumenti, versioni e risultati tecnici. Nessun identificatore hardware univoco o indirizzo IP viene pubblicato.
