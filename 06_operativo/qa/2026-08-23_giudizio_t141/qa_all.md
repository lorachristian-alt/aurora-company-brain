# Suite QA delle note — report unico

- Data: 2026-08-23
- Perimetro: **lotto** (lotto `giudizio_t141`) — **perimetro di manutenzione: 0 grezzi, 3 note** (E35)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 0 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro manutenzione (0 grezzi, 3 note) · **0 ERRORI, 17 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 2 |
| `areas\` | 212 |
| `projects\` | 8 |
| `docs\` | 36 |
| `entities\` | 30 |
| `concepts\` | 6 |
| `data\` | 38 |
| `outputs\` | 1 |
| `code\` | 16 |
| `workspace\` | 12 |
| `sources\` | 1 |
| **totale** | **362** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **349** note.*

| `type` | Note |
|---|---|
| `atomica` | 252 |
| `concetto` | 5 |
| `conflitto` | 50 |
| `entita` | 22 |
| `hub` | 13 |
| `index` | 11 |
| `sessione` | 9 |

---
## qa_frontmatter (perimetro: lotto, 14 note)

- ERRORI: **0**
- AVVISI: **3**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-due-nc-interne-sul-proprio-ritardo.md` |  | frontmatter | corpo di 308 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-evidenze-audit-oltre-termine.md` |  | frontmatter | corpo di 348 parole: fra 301 e 350, si motiva o si spezza |
| `questione-vendor-rating-2025-c-e-o-non-c-e.md` |  | frontmatter | summary di 262 caratteri (tetto 250) |


## qa_link_integrity (perimetro: lotto, 362 note nel vault)

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


## qa_provenance (perimetro: lotto, 14 note)

- ERRORI: **0**
- AVVISI: **0**


## qa_copertura (perimetro: lotto, 14 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `fatto-due-nc-interne-sul-proprio-ritardo.md` | atomica | risolto | 1 |
| `fatto-evidenze-audit-oltre-termine.md` | atomica | aperto | 4 |
| `questione-vendor-rating-2025-c-e-o-non-c-e.md` | atomica | aperto | 2 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|