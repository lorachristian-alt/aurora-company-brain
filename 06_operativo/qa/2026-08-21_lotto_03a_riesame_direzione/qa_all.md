# Suite QA delle note — report unico

- Data: 2026-08-21
- Perimetro: **lotto** (lotto `lotto_03a_riesame_direzione`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 23 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 178 |
| `projects\` | 8 |
| `docs\` | 34 |
| `entities\` | 27 |
| `concepts\` | 6 |
| `data\` | 37 |
| `outputs\` | 1 |
| `code\` | 16 |
| `workspace\` | 10 |
| `sources\` | 1 |
| **totale** | **319** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **308** note.*

| `type` | Note |
|---|---|
| `atomica` | 214 |
| `concetto` | 5 |
| `conflitto` | 47 |
| `entita` | 22 |
| `hub` | 13 |
| `index` | 11 |
| `sessione` | 7 |

---
## qa_frontmatter (perimetro: lotto, 50 note)

- ERRORI: **0**
- AVVISI: **6**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-riesame-straordinario-e-facolta-rsgq.md` |  | frontmatter | summary di 253 caratteri (tetto 250) |
| `fatto-risorse-adeguate-con-riserva.md` |  | frontmatter | summary di 294 caratteri (tetto 250) |
| `fatto-sistema-adeguato-con-riserve.md` |  | frontmatter | summary di 279 caratteri (tetto 250) |
| `fatto-straordinari-oltre-limite-linea2.md` |  | frontmatter | summary di 284 caratteri (tetto 250) |
| `doc-azioni-deliberate-riesame-2026.md` |  | frontmatter | summary di 254 caratteri (tetto 250) |
| `kpi-obiettivi-2026-avanzamento.md` |  | frontmatter | summary di 261 caratteri (tetto 250) |


## qa_link_integrity (perimetro: lotto, 319 note nel vault)

- ERRORI: **0**
- AVVISI: **13**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-maggio-fuori-scala.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-rework-linea-1-sospeso.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `questione-composizione-lavaggio-completo.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `doc-tipi-lavaggio-allergeni.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `entita-chiara-vicentini.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-indicatori-2025-consuntivo.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-indicatori-mensili-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-obiettivi-2026-avanzamento.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-pareto-cause-nc-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-reclami-2025.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-registro-reclami-2026.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-tamponi-per-zona-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-vendor-rating-2025.md` |  | link | dichiara l'hub [[area-logistica]] come proprio in related, ma quell'hub non la elenca nel corpo |


## qa_provenance (perimetro: lotto, 50 note)

- ERRORI: **0**
- AVVISI: **4**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-ccp-stato-al-riesame-2026.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-cruscotto-colonne-mai-calcolate.md` |  | provenance | la fonte 'cruscotto_KPI_qualita_2026.xlsx' non aggancia nessuna affermazione della nota: rumore nel payload |
| `fatto-decisione-erp-rimandata.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-due-nc-minori-audit-2026.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 50 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 1 |
| `doc-azioni-deliberate-riesame-2026.md` | atomica | aperto | 2 |
| `doc-cruscotto-kpi-2026.md` | atomica | aperto | 1 |
| `doc-riesame-direzione-2026.md` | atomica | risolto | 1 |
| `fatto-audit-cliente-tosano-novembre.md` | atomica | risolto | 1 |
| `fatto-audit-csqa-febbraio-2026-esito.md` | atomica | risolto | 1 |
| `fatto-audit-interni-2025-nove-su-dieci.md` | atomica | risolto | 1 |
| `fatto-azioni-riesame-2025-non-tutte-chiuse.md` | atomica | risolto | 1 |
| `fatto-ccp-stato-al-riesame-2026.md` | atomica | risolto | 1 |
| `fatto-costo-non-qualita-2025-parziale.md` | atomica | aperto | 1 |
| `fatto-cruscotto-colonne-mai-calcolate.md` | atomica | aperto | 1 |
| `fatto-decisione-erp-rimandata.md` | atomica | aperto | 1 |
| `fatto-digitalizzazione-archivio-rinviata.md` | atomica | aperto | 1 |
| `fatto-due-nc-minori-audit-2026.md` | atomica | risolto | 1 |
| `fatto-evidenze-audit-oltre-termine.md` | atomica | aperto | 1 |
| `fatto-formazione-2025-sotto-obiettivo.md` | atomica | aperto | 1 |
| `fatto-investimento-tunnel-confermato.md` | atomica | risolto | 1 |
| `fatto-listeria-canalina-linea3-al-riesame.md` | atomica | aperto | 1 |
| `fatto-maggio-fuori-scala.md` | atomica | risolto | 1 |
| `fatto-mock-recall-marzo-2026.md` | atomica | aperto | 1 |
| `fatto-ore-formazione-crollate.md` | atomica | aperto | 2 |
| `fatto-politica-riconfermata-senza-modifiche.md` | atomica | aperto | 1 |
| `fatto-revisione-modulistica-ccp.md` | atomica | risolto | 1 |
| `fatto-riesame-straordinario-e-facolta-rsgq.md` | atomica | aperto | 1 |
| `fatto-risorse-adeguate-con-riserva.md` | atomica | aperto | 1 |
| `fatto-sei-nc-aperte-oltre-sessanta-giorni.md` | atomica | risolto | 1 |
| `fatto-sistema-adeguato-con-riserve.md` | atomica | risolto | 1 |
| `fatto-straordinari-oltre-limite-linea2.md` | atomica | aperto | 1 |
| `fatto-tarature-92-percento-al-riesame.md` | atomica | risolto | 1 |
| `fatto-turnover-linea2-e-domeniche.md` | atomica | aperto | 1 |
| `kpi-indicatori-2025-consuntivo.md` | atomica | risolto | 1 |
| `kpi-indicatori-mensili-2026.md` | atomica | risolto | 1 |
| `kpi-obiettivi-2026-avanzamento.md` | atomica | risolto | 1 |
| `kpi-pareto-cause-nc-2026.md` | atomica | aperto | 2 |
| `kpi-reclami-2025.md` | atomica | risolto | 1 |
| `kpi-registro-reclami-2026.md` | atomica | aperto | 2 |
| `kpi-tamponi-per-zona-2026.md` | atomica | aperto | 2 |
| `kpi-vendor-rating-2025.md` | atomica | risolto | 1 |
| `questione-nc-interne-registrate-su-mod-qa-31.md` | conflitto | aperto | 3 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `cruscotto_KPI_qualita_2026.xlsx` | fatto-cruscotto-colonne-mai-calcolate, fatto-maggio-fuori-scala, fatto-ore-formazione-crollate, doc-cruscotto-kpi-2026, kpi-indicatori-mensili-2026, kpi-pareto-cause-nc-2026, kpi-registro-reclami-2026, kpi-tamponi-per-zona-2026 |
| `verbale_riesame_direzione_SGQ_2026.txt` | fatto-audit-cliente-tosano-novembre, fatto-audit-csqa-febbraio-2026-esito, fatto-audit-interni-2025-nove-su-dieci, fatto-azioni-riesame-2025-non-tutte-chiuse, fatto-ccp-stato-al-riesame-2026, fatto-costo-non-qualita-2025-parziale, fatto-decisione-erp-rimandata, fatto-digitalizzazione-archivio-rinviata, fatto-due-nc-minori-audit-2026, fatto-evidenze-audit-oltre-termine, fatto-formazione-2025-sotto-obiettivo, fatto-investimento-tunnel-confermato, fatto-listeria-canalina-linea3-al-riesame, fatto-mock-recall-marzo-2026, fatto-ore-formazione-crollate, fatto-politica-riconfermata-senza-modifiche, fatto-revisione-modulistica-ccp, fatto-riesame-straordinario-e-facolta-rsgq, fatto-risorse-adeguate-con-riserva, fatto-sei-nc-aperte-oltre-sessanta-giorni, fatto-sistema-adeguato-con-riserve, fatto-straordinari-oltre-limite-linea2, fatto-tarature-92-percento-al-riesame, fatto-turnover-linea2-e-domeniche, questione-nc-interne-registrate-su-mod-qa-31, doc-azioni-deliberate-riesame-2026, doc-riesame-direzione-2026, kpi-indicatori-2025-consuntivo, kpi-obiettivi-2026-avanzamento, kpi-pareto-cause-nc-2026, kpi-reclami-2025, kpi-registro-reclami-2026, kpi-vendor-rating-2025 |