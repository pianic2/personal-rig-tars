# RTARS-27 — Discrepanze e verifiche aperte

| ID | Tema | Evidenza disponibile | Stato | Evidenza/azione necessaria |
| --- | --- | --- | --- | --- |
| D3D-01 | Provenienza | Upstream locale contiene `armV3.3mf`; MakerWorld #3318467 / profilo 3767953 non direttamente accessibile. | **NOT TESTED** | Scaricare dal profilo e confrontare hash del file originale; conferma del titolare se il download non è accessibile. |
| D3D-02 | Revisione e nome file | Archivio locale: armV3, Bambu Studio 02.07.01.57, creazione 2026-09-02. Guida ufficiale ora nomina tarsV4; BOM V1.0 nomina tarsV3. | **FAIL — mismatch documentale** | Il titolare deve spiegare la relazione tra varianti; nessuna equivalenza presunta. |
| D3D-03 | Quantità | BOM V1.0: 17 pezzi / 13 tipi. Guida stampa: 14 pezzi secondo testo/layout, tabella con 12 tipi e 14 unità. File locale: 16 istanze / 13 nomi. | **FAIL — discrepanza** | Distinta e profilo riferiti alla medesima revisione del progetto, oppure chiarimento ufficiale delle varianti. |
| D3D-04 | Oggetti duplicati | Tre risorse mesh-less 3MF con hash identico. 13 mesh geometriche invece sono tutte distinte a livello di file. | **FAIL — anomalia** | Ispezione/esportazione dal software CAD ufficiale o chiarimento del produttore. |
| D3D-05 | Confronto RTARS-9 | RTARS-9 documenta parti fisiche/minuteria e gap della revisione del kit, senza identificare il modello locale come CAD di quella revisione. | **NOT TESTED** | Identificazione del kit/profilo e mapping parte-per-parte supportati da disegno o misura. |
| D3D-06 | Licenza | Licenza MakerWorld non verificata sulla fonte originale; il firmware ha licenze distinte. | **NOT TESTED** | Registrare testo/licenza direttamente dalla pagina del modello o autorizzazione esplicita del titolare. |
| D3D-07 | Compatibilità fisica | Nessuna prova di stampa o assemblaggio eseguita. | **NOT TESTED** | Validazione dimensionale rispetto ai componenti e alla revisione del kit; prova fisica controllata. |

Non è stata applicata alcuna correzione automatica. ZIP, 3MF e geometrie originali non sono inclusi nel commit; le esclusioni `.gitignore` proteggono `assets/3d/upstream/`.
