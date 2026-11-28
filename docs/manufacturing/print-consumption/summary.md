# RTARS-34 — Consuntivo provvisorio (2026-11-22)

> **Non è un consuntivo di stampe eseguite.** Valori di slicing comunicati dall'utente e trascritti da screenshot; nessun consumo effettivo attestato.

## Nuovo run QUALITY da screenshot RTARS-30 (2026-11-22)

- **Non sovrascrive il run precedente**, conservato per audit in `summary_slicing_estimate`.
- Screenshot: Elegoo Neptune 4, processo HL-18 QUALITY 0.20 mm, filamento selezionato **Generic PLA** (non preset esplicitamente calibrato per Elegoo Metallic Bronze).
- Stima tempo 4 piatti **23h19m**: PLATE-01 1h50m, PLATE-02 3h45m, PLATE-03 7h59m, PLATE-04 9h45m.
- Filamento modello **87.04 m / 259.61 g** (aggregato, non consumo reale); costo visualizzato **5.49**, valuta non visibile.
- Differenza osservata dal run precedente: tempo +11h15m46s (precisione nuova ai minuti), massa modello −10.24 g, lunghezza modello −3.44 m; non prova parità di impostazioni, modelli o supporti.
- Nessuna prova di esecuzione fisica, misura di scarto o idoneità del G-code. Evidenza testuale: [evidence/slicer-summary-quality-2026-11-22.md](evidence/slicer-summary-quality-2026-11-22.md).

## Inventario di slicing osservato (run precedente)

| ID | Durata stimata | Massa per piatto | Scarti per piatto | Stato stampa fisica |
| --- | ---: | ---: | ---: | --- |
| PLATE-01 | 00:59:14 | 24.5 g (precedente dichiarazione, non corroborata dalla foto) | 0.12 g (precedente dichiarazione, categoria ignota) | pending (dichiarato) |
| PLATE-02 | 02:14:00 | n/d | n/d | non confermato |
| PLATE-03 | 04:01:00 | n/d | n/d | non confermato |
| PLATE-04 | 04:49:00 | n/d | n/d | non confermato |
| **Totale durate singoli piatti** | **12:03:14** | **non sommabile per-piatto** | **non sommabile per-piatto** | **0 stampe documentate** |

## Totali aggregati mostrati dallo slicer

- **4 piatti nel riepilogo** (non necessariamente l'intero inventario RTARS-32).
- **Tempo visualizzato:** 12h3m (somma tempi singoli: 12h3m14s).
- **Filamento modello:** 90.48 m.
- **Massa modello aggregata:** 269.85 g; non sostituisce massa di filamento effettivamente consumata, che include eventuali scarti.
- **Costo visualizzato:** 5.63 (valuta non visibile).
- **Materiale (tipo):** sconosciuto.

## Consumi effettivi

Durata effettiva: **n/d**; massa consumata effettiva: **n/d**; scarti effettivi: **n/d**; esito finale: **n/d**. Non trattare `n/d` come zero.

**Copertura stampa fisica:** 0 con log disponibile, 1 dichiarato pending, 3 di stato non confermato. **Copertura stime slicing:** 4 piatti su 4 presenti nello screenshot.

## Fonti e gap

- Dataset: [plates.json](plates.json)
- Trascrizione e SHA-256 dell'immagine originale (foto non caricata nel repository): [evidence/slicer-summary-2026-11-22.md](evidence/slicer-summary-2026-11-22.md)
- Mancano: report/export nativo dello slicer, conferma materiale e profili reali, ripartizione massa/scarti per piatto, stato effettivo delle stampe e inventario definitivo RTARS-32.
