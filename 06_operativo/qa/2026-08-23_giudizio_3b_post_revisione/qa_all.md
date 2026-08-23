# Suite QA delle note — report unico

- Data: 2026-08-23
- Perimetro: **lotto** (lotto `giudizio_3b_post_revisione`) — **perimetro di manutenzione: 0 grezzi, 7 note** (E35)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro manutenzione (0 grezzi, 7 note) · **0 ERRORI, 22 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 2 |
| `areas\` | 229 |
| `projects\` | 8 |
| `docs\` | 38 |
| `entities\` | 31 |
| `concepts\` | 6 |
| `data\` | 41 |
| `outputs\` | 1 |
| `code\` | 16 |
| `workspace\` | 12 |
| `sources\` | 1 |
| **totale** | **385** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **372** note.*

| `type` | Note |
|---|---|
| `atomica` | 270 |
| `concetto` | 5 |
| `conflitto` | 53 |
| `entita` | 23 |
| `hub` | 14 |
| `index` | 11 |
| `sessione` | 9 |

---
## qa_frontmatter (perimetro: lotto, 18 note)

- ERRORI: **0**
- AVVISI: **7**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-diciassette-titoli-scaduti-al-18-05.md` |  | frontmatter | summary di 272 caratteri (tetto 250) |
| `fatto-diciassette-titoli-scaduti-al-18-05.md` |  | frontmatter | summary contiene piu' di una frase |
| `fatto-quattro-righe-di-perimetro-incerto-nel-registro.md` |  | frontmatter | summary di 295 caratteri (tetto 250) |
| `fatto-registro-formazione-intestazione-ripetuta.md` |  | frontmatter | summary di 260 caratteri (tetto 250) |
| `fatto-squadra-emergenza-antincendio-in-scadenza.md` |  | frontmatter | summary di 314 caratteri (tetto 250) |
| `fatto-squadra-emergenza-antincendio-in-scadenza.md` |  | frontmatter | corpo di 305 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso.md` |  | frontmatter | summary di 301 caratteri (tetto 250) |


## qa_link_integrity (perimetro: lotto, 385 note nel vault)

- ERRORI: **0**
- AVVISI: **14**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-maggio-fuori-scala.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-rework-linea-1-sospeso.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `questione-composizione-lavaggio-completo.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `doc-tipi-lavaggio-allergeni.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `entita-chiara-vicentini.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-costo-non-qualita-due-totali.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-indicatori-2025-consuntivo.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-indicatori-mensili-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-obiettivi-2026-avanzamento.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-pareto-cause-nc-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-reclami-2025.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-registro-reclami-2026.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-tamponi-per-zona-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-vendor-rating-2025.md` |  | link | dichiara l'hub [[area-logistica]] come proprio in related, ma quell'hub non la elenca nel corpo |


## qa_provenance (perimetro: lotto, 18 note)

- ERRORI: **0**
- AVVISI: **1**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 18 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### risorse-umane

| Nota | type | stato | fonti |
|---|---|---|---|
| `doc-scadenzario-formazione-2026.md` | atomica | risolto | 2 |
| `fatto-diciassette-titoli-scaduti-al-18-05.md` | atomica | risolto | 1 |
| `fatto-quattro-righe-di-perimetro-incerto-nel-registro.md` | atomica | aperto | 1 |
| `fatto-registro-formazione-intestazione-ripetuta.md` | atomica | risolto | 1 |
| `fatto-squadra-emergenza-antincendio-in-scadenza.md` | atomica | aperto | 1 |
| `fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso.md` | atomica | aperto | 1 |
| `kpi-formazione-stati-al-18-05.md` | atomica | risolto | 1 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|