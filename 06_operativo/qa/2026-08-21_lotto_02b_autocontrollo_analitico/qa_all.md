# Suite QA delle note — report unico

- Data: 2026-08-21
- Perimetro: **lotto** (lotto `lotto_02b_autocontrollo_analitico`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 0 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 27 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 129 |
| `projects\` | 8 |
| `docs\` | 22 |
| `entities\` | 25 |
| `concepts\` | 6 |
| `data\` | 29 |
| `outputs\` | 1 |
| `code\` | 16 |
| `workspace\` | 9 |
| `sources\` | 1 |
| **totale** | **247** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **237** note.*

| `type` | Note |
|---|---|
| `atomica` | 153 |
| `concetto` | 5 |
| `conflitto` | 39 |
| `entita` | 20 |
| `hub` | 13 |
| `index` | 11 |
| `sessione` | 6 |

---
## qa_frontmatter (perimetro: lotto, 48 note)

- ERRORI: **0**
- AVVISI: **26**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-appunti-in-coda-file-reflue.md` |  | frontmatter | corpo di 301 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-carica-in-salita-linea-1-aprile.md` |  | frontmatter | corpo di 336 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-cip-fuori-criterio.md` |  | frontmatter | summary di 273 caratteri (tetto 250) |
| `fatto-cip-fuori-criterio.md` |  | frontmatter | corpo di 344 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-criterio-conducibilita-cip-superato.md` |  | frontmatter | corpo di 348 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-lettura-mancante-registro-tamponi.md` |  | frontmatter | corpo di 305 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-listeria-scarico-pt-104-aprile.md` |  | frontmatter | corpo di 323 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-medie-non-calcolate-file-reflue.md` |  | frontmatter | corpo di 350 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-26-018-ruote-carrelli-febbraio.md` |  | frontmatter | corpo di 316 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-26-056-ganasce-pkm-450-maggio.md` |  | frontmatter | corpo di 343 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-acq-26-01-ghiaccio-aprile.md` |  | frontmatter | corpo di 341 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-cip-2026.md` |  | frontmatter | corpo di 349 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-superamento-grassi-scarico-marzo.md` |  | frontmatter | corpo di 323 parole: fra 301 e 350, si motiva o si spezza |
| `questione-listeria-24-02-non-nel-registro-tamponi.md` |  | frontmatter | summary contiene piu' di una frase |
| `doc-autocontrollo-scarico-s1.md` |  | frontmatter | corpo di 346 parole: fra 301 e 350, si motiva o si spezza |
| `doc-condizioni-uso-detergente-acido.md` |  | frontmatter | summary di 274 caratteri (tetto 250) |
| `doc-condizioni-uso-detergente-acido.md` |  | frontmatter | corpo di 301 parole: fra 301 e 350, si motiva o si spezza |
| `doc-criteri-accettazione-cip.md` |  | frontmatter | summary di 286 caratteri (tetto 250) |
| `doc-criteri-accettazione-cip.md` |  | frontmatter | corpo di 322 parole: fra 301 e 350, si motiva o si spezza |
| `doc-parametri-fasi-cip.md` |  | frontmatter | corpo di 322 parole: fra 301 e 350, si motiva o si spezza |
| `doc-piano-autocontrollo-acqua.md` |  | frontmatter | summary di 259 caratteri (tetto 250) |
| `doc-piano-autocontrollo-acqua.md` |  | frontmatter | corpo di 340 parole: fra 301 e 350, si motiva o si spezza |
| `doc-piano-tamponi-superfici.md` |  | frontmatter | corpo di 347 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-conducibilita-acqua-per-punto.md` |  | frontmatter | corpo di 322 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-parametri-scarico-s1-2026.md` |  | frontmatter | corpo di 349 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-tamponi-superfici-2026.md` |  | frontmatter | corpo di 344 parole: fra 301 e 350, si motiva o si spezza |


## qa_link_integrity (perimetro: lotto, 247 note nel vault)

- ERRORI: **0**
- AVVISI: **0**


## qa_provenance (perimetro: lotto, 48 note)

- ERRORI: **0**
- AVVISI: **1**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `macchina-cip-01.md` |  | provenance | la fonte 'scheda_sicurezza_detergente_acido_lavaggio_CIP.txt' non aggancia nessuna affermazione della nota: rumore nel payload |


## qa_copertura (perimetro: lotto, 48 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `macchina-linea-1.md` | hub | aperto | 4 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 1 |
| `doc-autocontrollo-scarico-s1.md` | atomica | risolto | 1 |
| `doc-condizioni-uso-detergente-acido.md` | atomica | risolto | 1 |
| `doc-criteri-accettazione-cip.md` | atomica | risolto | 1 |
| `doc-parametri-fasi-cip.md` | atomica | risolto | 1 |
| `doc-piano-autocontrollo-acqua.md` | atomica | risolto | 2 |
| `doc-piano-tamponi-superfici.md` | atomica | risolto | 2 |
| `entita-analytica-veneta.md` | entita | risolto | 3 |
| `fatto-appunti-in-coda-file-reflue.md` | atomica | aperto | 1 |
| `fatto-carica-in-salita-linea-1-aprile.md` | atomica | risolto | 1 |
| `fatto-cip-fuori-criterio.md` | atomica | risolto | 2 |
| `fatto-cloro-residuo-ghiaccio-in-calo.md` | atomica | risolto | 1 |
| `fatto-criterio-conducibilita-cip-superato.md` | atomica | risolto | 3 |
| `fatto-date-in-quattro-grafie-registro-tamponi.md` | atomica | aperto | 1 |
| `fatto-degrassatore-frequenza-trimestrale.md` | atomica | risolto | 1 |
| `fatto-durezza-acqua-addolcita-in-deroga.md` | atomica | risolto | 1 |
| `fatto-lettura-mancante-registro-tamponi.md` | atomica | aperto | 1 |
| `fatto-listeria-scarico-pt-104-aprile.md` | atomica | risolto | 1 |
| `fatto-mani-addetto-farcitura-non-conforme.md` | atomica | risolto | 1 |
| `fatto-medie-non-calcolate-file-reflue.md` | atomica | aperto | 1 |
| `fatto-modulo-nc-acqua-riconciliato.md` | atomica | risolto | 3 |
| `fatto-nc-26-018-ruote-carrelli-febbraio.md` | atomica | risolto | 2 |
| `fatto-nc-26-055-nastro-forno-maggio.md` | atomica | risolto | 2 |
| `fatto-nc-26-056-ganasce-pkm-450-maggio.md` | atomica | risolto | 2 |
| `fatto-nc-acq-26-01-ghiaccio-aprile.md` | atomica | risolto | 1 |
| `fatto-nc-acq-26-02-ferro-spogliatoi-aprile.md` | atomica | risolto | 1 |
| `fatto-nc-cip-2026.md` | atomica | risolto | 3 |
| `fatto-superamento-grassi-scarico-marzo.md` | atomica | risolto | 1 |
| `kpi-conducibilita-acqua-per-punto.md` | atomica | risolto | 1 |
| `kpi-conducibilita-risciacquo-cip-maggio.md` | atomica | risolto | 3 |
| `kpi-parametri-scarico-s1-2026.md` | atomica | risolto | 1 |
| `kpi-tamponi-superfici-2026.md` | atomica | risolto | 1 |
| `macchina-cip-01.md` | hub | aperto | 4 |
| `questione-frequenza-tamponi-prescritta-e-reale.md` | conflitto | aperto | 2 |
| `questione-listeria-24-02-non-nel-registro-tamponi.md` | conflitto | aperto | 2 |
| `script-censimento-formule.md` | atomica | risolto | 0 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `analisi_acque_reflue_autocontrollo_2026.xlsx` | fatto-appunti-in-coda-file-reflue, fatto-degrassatore-frequenza-trimestrale, fatto-medie-non-calcolate-file-reflue, fatto-superamento-grassi-scarico-marzo, doc-autocontrollo-scarico-s1, entita-analytica-veneta, kpi-parametri-scarico-s1-2026 |
| `piano_autocontrollo_acqua_potabile_analisi.csv` | fatto-cloro-residuo-ghiaccio-in-calo, fatto-criterio-conducibilita-cip-superato, fatto-durezza-acqua-addolcita-in-deroga, fatto-modulo-nc-acqua-riconciliato, fatto-nc-acq-26-01-ghiaccio-aprile, fatto-nc-acq-26-02-ferro-spogliatoi-aprile, doc-piano-autocontrollo-acqua, entita-analytica-veneta, kpi-conducibilita-acqua-per-punto, kpi-conducibilita-risciacquo-cip-maggio |
| `registro_tamponi_superfici_listeria_salmonella.csv` | fatto-carica-in-salita-linea-1-aprile, fatto-date-in-quattro-grafie-registro-tamponi, fatto-lettura-mancante-registro-tamponi, fatto-listeria-scarico-pt-104-aprile, fatto-mani-addetto-farcitura-non-conforme, fatto-nc-26-018-ruote-carrelli-febbraio, fatto-nc-26-055-nastro-forno-maggio, fatto-nc-26-056-ganasce-pkm-450-maggio, questione-frequenza-tamponi-prescritta-e-reale, questione-listeria-24-02-non-nel-registro-tamponi, doc-piano-tamponi-superfici, entita-analytica-veneta, kpi-tamponi-superfici-2026 |