# Suite QA delle note — report unico

- Data: 2026-08-24
- Perimetro: **lotto** (lotto `giudizio_3d_dedicato2`) — **perimetro di manutenzione: 0 grezzi, 2 note** (E35)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 0 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro manutenzione (0 grezzi, 2 note) · **0 ERRORI, 19 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 2 |
| `areas\` | 251 |
| `projects\` | 8 |
| `docs\` | 52 |
| `entities\` | 32 |
| `concepts\` | 6 |
| `data\` | 49 |
| `outputs\` | 1 |
| `code\` | 16 |
| `workspace\` | 14 |
| `sources\` | 1 |
| **totale** | **432** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **417** note.*

| `type` | Note |
|---|---|
| `atomica` | 306 |
| `concetto` | 5 |
| `conflitto` | 61 |
| `entita` | 24 |
| `hub` | 14 |
| `index` | 11 |
| `sessione` | 11 |

---
## qa_frontmatter (perimetro: lotto, 13 note)

- ERRORI: **0**
- AVVISI: **0**


## qa_link_integrity (perimetro: lotto, 432 note nel vault)

- ERRORI: **0**
- AVVISI: **17**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-due-segnalazioni-rendono-il-ritiro-non-rimandabile.md` |  | link | dichiara l'hub [[area-direzione]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-maggio-fuori-scala.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-rework-linea-1-sospeso.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `questione-composizione-lavaggio-completo.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `doc-chiusura-di-un-reclamo.md` |  | link | dichiara l'hub [[progetto-gestione-reclamo-rec-2026-011]] come proprio in related, ma quell'hub non la elenca nel corpo |
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
| `sessione-s4-lotto-03b.md` |  | link | dichiara l'hub [[area-risorse-umane]] come proprio in related, ma quell'hub non la elenca nel corpo |


## qa_provenance (perimetro: lotto, 13 note)

- ERRORI: **0**
- AVVISI: **2**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `questione-misura-frammento-strumentale.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «di dimensione
stimata dalla foto 7-9 mm» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-misura-frammento-strumentale.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |


## qa_copertura (perimetro: lotto, 13 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `questione-misura-frammento-strumentale.md` | conflitto | aperto | 3 |
| `questione-pro-qa-08-reclami-o-rintracciabilita.md` | conflitto | aperto | 3 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|