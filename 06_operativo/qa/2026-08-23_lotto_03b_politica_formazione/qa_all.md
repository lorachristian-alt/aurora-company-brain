# Suite QA delle note — report unico

- Data: 2026-08-23
- Perimetro: **lotto** (lotto `lotto_03b_politica_formazione`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 43 AVVISI** · esito **GIALLO**

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
| `workspace\` | 13 |
| `sources\` | 1 |
| **totale** | **386** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **372** note.*

| `type` | Note |
|---|---|
| `atomica` | 270 |
| `concetto` | 5 |
| `conflitto` | 53 |
| `entita` | 23 |
| `hub` | 14 |
| `index` | 11 |
| `sessione` | 10 |

---
## qa_frontmatter (perimetro: lotto, 43 note)

- ERRORI: **0**
- AVVISI: **26**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-cinque-righe-di-perimetro-incerto-nel-registro.md` |  | frontmatter | summary di 295 caratteri (tetto 250) |
| `fatto-cinque-righe-di-perimetro-incerto-nel-registro.md` |  | frontmatter | corpo di 338 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-diciassette-titoli-scaduti-al-18-05.md` |  | frontmatter | summary di 306 caratteri (tetto 250) |
| `fatto-diciassette-titoli-scaduti-al-18-05.md` |  | frontmatter | summary contiene piu' di una frase |
| `fatto-due-sessioni-formative-programmate-per-il-09-06.md` |  | frontmatter | summary di 281 caratteri (tetto 250) |
| `fatto-formazione-allergeni-registrata-biennale.md` |  | frontmatter | summary di 255 caratteri (tetto 250) |
| `fatto-mani-addetto-farcitura-non-conforme.md` |  | frontmatter | corpo di 302 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-politica-cultura-sicurezza-alimentare.md` |  | frontmatter | summary di 301 caratteri (tetto 250) |
| `fatto-politica-food-defense-e-food-fraud.md` |  | frontmatter | summary di 313 caratteri (tetto 250) |
| `fatto-registro-formazione-intestazione-ripetuta.md` |  | frontmatter | summary di 260 caratteri (tetto 250) |
| `fatto-squadra-emergenza-antincendio-in-scadenza.md` |  | frontmatter | summary di 314 caratteri (tetto 250) |
| `fatto-squadra-emergenza-antincendio-in-scadenza.md` |  | frontmatter | corpo di 301 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso.md` |  | frontmatter | summary di 333 caratteri (tetto 250) |
| `fatto-validita-haccp-da-procedura-non-in-archivio.md` |  | frontmatter | summary di 304 caratteri (tetto 250) |
| `fatto-validita-haccp-da-procedura-non-in-archivio.md` |  | frontmatter | corpo di 340 parole: fra 301 e 350, si motiva o si spezza |
| `questione-cinquanta-o-cinquantadue-persone.md` |  | frontmatter | summary di 273 caratteri (tetto 250) |
| `questione-evidenze-del-02-04-nove-o-cinque.md` |  | frontmatter | summary di 273 caratteri (tetto 250) |
| `questione-ore-formazione-due-valori-per-il-2025.md` |  | frontmatter | summary di 361 caratteri (tetto 250) |
| `questione-ore-formazione-due-valori-per-il-2025.md` |  | frontmatter | summary contiene piu' di una frase |
| `questione-sessioni-allergeni-2026-non-a-registro.md` |  | frontmatter | summary di 251 caratteri (tetto 250) |
| `questione-tre-o-quattro-neoassunti-senza-formazione.md` |  | frontmatter | corpo di 338 parole: fra 301 e 350, si motiva o si spezza |
| `doc-politica-qualita-2026.md` |  | frontmatter | corpo di 304 parole: fra 301 e 350, si motiva o si spezza |
| `entita-federica-sartori.md` |  | frontmatter | summary di 255 caratteri (tetto 250) |
| `kpi-enti-formatori-e-corsi.md` |  | frontmatter | summary di 293 caratteri (tetto 250) |
| `kpi-obiettivi-politica-2026.md` |  | frontmatter | summary di 300 caratteri (tetto 250) |
| `kpi-obiettivi-politica-2026.md` |  | frontmatter | summary contiene piu' di una frase |


## qa_link_integrity (perimetro: lotto, 386 note nel vault)

- ERRORI: **0**
- AVVISI: **15**

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
| `sessione-s4-lotto-03b.md` |  | link | dichiara l'hub [[area-risorse-umane]] come proprio in related, ma quell'hub non la elenca nel corpo |


## qa_provenance (perimetro: lotto, 43 note)

- ERRORI: **0**
- AVVISI: **2**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-tre-o-quattro-neoassunti-senza-formazione.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 43 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-produzione.md` | hub | aperto | 1 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 3 |
| `doc-politica-qualita-2026.md` | atomica | risolto | 1 |
| `fatto-chiusura-nc-documentale-e-il-richiamo.md` | atomica | risolto | 1 |
| `fatto-formazione-2025-sotto-obiettivo.md` | atomica | aperto | 1 |
| `fatto-mani-addetto-farcitura-non-conforme.md` | atomica | risolto | 1 |
| `fatto-politica-cultura-sicurezza-alimentare.md` | atomica | risolto | 2 |
| `fatto-politica-firmata-il-15-01.md` | atomica | risolto | 1 |
| `fatto-politica-food-defense-e-food-fraud.md` | atomica | risolto | 1 |
| `fatto-politica-otto-impegni-e-il-nono-ritirato.md` | atomica | risolto | 1 |
| `fatto-riserva-su-nc1-efficacia-da-verificare.md` | atomica | risolto | 2 |
| `kpi-indicatori-2025-consuntivo.md` | atomica | risolto | 1 |
| `kpi-obiettivi-politica-2026.md` | atomica | risolto | 1 |
| `questione-evidenze-del-02-04-nove-o-cinque.md` | atomica | aperto | 2 |
| `questione-ore-formazione-due-valori-per-il-2025.md` | conflitto | aperto | 2 |
| `questione-tre-o-quattro-neoassunti-senza-formazione.md` | atomica | aperto | 4 |

### risorse-umane

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-risorse-umane.md` | hub | aperto | 2 |
| `doc-scadenzario-formazione-2026.md` | atomica | risolto | 2 |
| `entita-federica-sartori.md` | entita | aperto | 2 |
| `fatto-cinque-righe-di-perimetro-incerto-nel-registro.md` | atomica | aperto | 1 |
| `fatto-diciassette-titoli-scaduti-al-18-05.md` | atomica | risolto | 1 |
| `fatto-due-sessioni-formative-programmate-per-il-09-06.md` | atomica | aperto | 1 |
| `fatto-formazione-allergeni-registrata-biennale.md` | atomica | risolto | 2 |
| `fatto-in-scadenza-cinque-o-sei.md` | atomica | risolto | 1 |
| `fatto-registro-formazione-intestazione-ripetuta.md` | atomica | risolto | 1 |
| `fatto-squadra-emergenza-antincendio-in-scadenza.md` | atomica | aperto | 1 |
| `fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso.md` | atomica | aperto | 1 |
| `fatto-validita-haccp-da-procedura-non-in-archivio.md` | atomica | aperto | 2 |
| `kpi-enti-formatori-e-corsi.md` | atomica | risolto | 1 |
| `kpi-formazione-stati-al-18-05.md` | atomica | risolto | 1 |
| `questione-cinquanta-o-cinquantadue-persone.md` | conflitto | aperto | 3 |
| `questione-sessioni-allergeni-2026-non-a-registro.md` | conflitto | aperto | 2 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `politica_qualita_e_sicurezza_alimentare_2026.docx` | fatto-politica-cultura-sicurezza-alimentare, fatto-politica-firmata-il-15-01, fatto-politica-food-defense-e-food-fraud, fatto-politica-otto-impegni-e-il-nono-ritirato, questione-cinquanta-o-cinquantadue-persone, questione-ore-formazione-due-valori-per-il-2025, doc-politica-qualita-2026, entita-federica-sartori, kpi-obiettivi-politica-2026 |
| `registro_presenze_corsi_HACCP_scaduti.csv` | area-risorse-umane, fatto-cinque-righe-di-perimetro-incerto-nel-registro, fatto-diciassette-titoli-scaduti-al-18-05, fatto-due-sessioni-formative-programmate-per-il-09-06, fatto-formazione-allergeni-registrata-biennale, fatto-in-scadenza-cinque-o-sei, fatto-registro-formazione-intestazione-ripetuta, fatto-squadra-emergenza-antincendio-in-scadenza, fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso, fatto-validita-haccp-da-procedura-non-in-archivio, questione-cinquanta-o-cinquantadue-persone, questione-sessioni-allergeni-2026-non-a-registro, questione-tre-o-quattro-neoassunti-senza-formazione, doc-scadenzario-formazione-2026, entita-federica-sartori, kpi-enti-formatori-e-corsi, kpi-formazione-stati-al-18-05 |