# RTARS-30 — Evidenza anteprima Bambu Studio QUALITY (2026-11-22)

**Origine:** foto fornita dall'utente in chat, SHA-256 `ab3a74239d7851b0c0368ca87cac6341a91418363b3e3d34f898e65c1bc33166`. Foto originale **non pubblicata** nel repository (privacy e licenza MakerWorld).

## Dati leggibili sullo schermo
- Applicazione: Bambu Studio (interfaccia Preview).
- Printer selection: **Elegoo Neptune 4** (testo visibile; modello Standard noto da dichiarazione/inventario, non identificabile indipendentemente da questa foto).
- Process: **HL-18 QUALITY 0.20mm** per Elegoo Neptune 4 (nome visibile; non uno dei due nuovi profili `RTARS-AESTHETIC` / `RTARS-FUNCTIONAL`).
- Filament selection: **Generic PLA**, NON preset specifico ELEGOO PLA Metallic Bronze. La bobina fisica dichiarata rimane ELEGOO PLA Metallic Metal Bronze, senza prova di calibrazione del preset generico.
- Ugello da 0,4 mm: dichiarazione dell'utente e denominazione dei preset preesistenti; non è confermata indipendentemente dalla foto.
- Filament Model, slot 1: **87.04 m**, **259.61 g**.
- Cost visualizzato: **5.49** (valuta non mostrata).
- Tempo previsto per piatto: PLATE-01 **1h50m**, PLATE-02 **3h45m**, PLATE-03 **7h59m**, PLATE-04 **9h45m**.
- Totale visualizzato: **23h19m**, coerente con la somma dei quattro valori arrotondati.
- Massa stimata è aggregata del modello; nessuna ripartizione per piatto o quantità reale consumata/scartata verificabile.
- Area centrale mostra il riepilogo, **non geometrie/toolpath/ispezione visibile**: non consente di convalidare orientamenti, supporti, warning o integrità del G-code.

## Confronto con il precedente RTARS-34
| Metrica | Baseline precedente | QUALITY screenshot | Scarto osservato |
|---|---:|---:|---:|
| Tempo | 12h03m14s (somma piatti), riepilogo 12h03m | 23h19m (minuti visualizzati) | +11h15m46s rispetto alla somma precedente; precisione solo ai minuti per nuova evidenza |
| Model filament length | 90.48 m | 87.04 m | −3.44 m |
| Model mass | 269.85 g | 259.61 g | −10.24 g |
| Cost displayed | 5.63 | 5.49 | −0.14 (valuta non specificata) |

**Non sostituire il vecchio run**: non abbiamo prova che siano identici modelli, orientamenti, temperatura, impostazioni complete, versione slicer o definizioni di materiale. Queste stime non attestano prove di stampa fisica.

## Gate RTARS-30
- PASS: selezione `Elegoo Neptune 4`, `Generic PLA`, `HL-18 QUALITY 0.20mm` e quattro stime di piatto osservate.
- NOT TESTED: identificazione/verifica parametrica del preset macchina (start/end G-code, volume, firmware e ugello); preset reale ELEGOO Metallic Bronze; esportazione di due processi RTARS-AESTHETIC/FUNCTIONAL; per parte orientamento e supporti; simulazione degli effettivi due preset dedicati; fit test RTARS-31.
- Divieto: dichiarare che i quattro piatti hanno superato i test dei profili TARS, o avviare RTARS-32 basandosi su questa sola foto.

**Azione minima successiva:** il filamento selezionato deve essere verificato per Elegoo PLA Metallic Bronze; due preset dedicati da materializzare ed esportare. Poi rieseguire lo slicing e produrre un riepilogo per ciascun profilo senza pubblicare la geometria licenziata.
