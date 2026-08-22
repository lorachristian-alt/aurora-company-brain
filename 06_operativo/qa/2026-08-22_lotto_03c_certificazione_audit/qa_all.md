# Suite QA delle note — report unico

- Data: 2026-08-22
- Perimetro: **lotto** (lotto `lotto_03c_certificazione_audit`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 1 |
| `qa_link_integrity.py` | 1 |
| `qa_provenance.py` | 1 |
| `qa_copertura.py` | 1 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 36 AVVISI** · esito **GIALLO**

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
## qa_frontmatter (perimetro: lotto, 69 note)

- ERRORI: **0**
- AVVISI: **16**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `self-certificazioni.md` |  | frontmatter | corpo di 345 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-evidenze-audit-oltre-termine.md` |  | frontmatter | corpo di 341 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-impianto-haccp-verificato-in-audit.md` |  | frontmatter | corpo di 312 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-obblighi-registro-f-gas.md` |  | frontmatter | corpo di 329 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-quattro-neoassunti-linea2-senza-formazione-allergeni.md` |  | frontmatter | corpo di 312 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-sistema-adeguato-con-riserve.md` |  | frontmatter | summary di 279 caratteri (tetto 250) |
| `questione-clausola-della-nc1-in-due-versioni.md` |  | frontmatter | summary contiene piu' di una frase |
| `questione-evidenze-del-02-04-nove-o-cinque.md` |  | frontmatter | summary di 273 caratteri (tetto 250) |
| `questione-quando-l-ente-torna-a-verificare.md` |  | frontmatter | summary di 270 caratteri (tetto 250) |
| `questione-validazione-ccp2-mai-confermata.md` |  | frontmatter | corpo di 316 parole: fra 301 e 350, si motiva o si spezza |
| `questione-validazione-ccp2-mai-confermata.md` |  | frontmatter | dichiara un'assenza con la formula di E3 ma non rimanda a un artefatto di ricerca in 06_operativo\ricerche_assenza\ (E43) — debito anteriore a E43, da sanare a fine corsa |
| `questione-vendor-rating-2025-c-e-o-non-c-e.md` |  | frontmatter | summary di 262 caratteri (tetto 250) |
| `doc-mod-qa-07.md` |  | frontmatter | corpo di 350 parole: fra 301 e 350, si motiva o si spezza |
| `doc-sequenze-produzione-allergeni.md` |  | frontmatter | summary di 272 caratteri (tetto 250) |
| `entita-icea.md` |  | frontmatter | summary contiene piu' di una frase |
| `kpi-pareto-cause-nc-2026.md` |  | frontmatter | corpo di 328 parole: fra 301 e 350, si motiva o si spezza |


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


## qa_provenance (perimetro: lotto, 69 note)

- ERRORI: **0**
- AVVISI: **6**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-due-nc-e-cinque-osservazioni.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-due-nc-minori-audit-2026.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-test-rintracciabilita-audit-2h50.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-convalida-md-3200-tre-date.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-tre-o-quattro-neoassunti-senza-formazione.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-ccp2-limite-critico.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 69 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### direzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `questione-data-riunione-direzione.md` | conflitto | aperto | 2 |

### manutenzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `fatto-obblighi-registro-f-gas.md` | atomica | aperto | 2 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `macchina-ft-01.md` | entita | risolto | 3 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 3 |
| `doc-azioni-deliberate-riesame-2026.md` | atomica | aperto | 2 |
| `doc-ccp2-limite-critico.md` | atomica | risolto | 1 |
| `doc-conferma-incarico-audit-rinnovo-2026.md` | atomica | risolto | 1 |
| `doc-manuale-haccp.md` | atomica | risolto | 2 |
| `doc-mod-qa-07.md` | atomica | risolto | 3 |
| `doc-rapporto-audit-csqa-2026.md` | atomica | risolto | 1 |
| `doc-riesame-direzione-2026.md` | atomica | risolto | 1 |
| `doc-sequenze-produzione-allergeni.md` | atomica | risolto | 1 |
| `entita-analytica-veneta.md` | entita | risolto | 3 |
| `entita-csqa-certificazioni.md` | atomica | risolto | 3 |
| `entita-icea.md` | atomica | risolto | 2 |
| `entita-nadia-franceschini.md` | atomica | risolto | 4 |
| `fatto-audit-cliente-tosano-novembre.md` | atomica | risolto | 1 |
| `fatto-audit-csqa-febbraio-2026-esito.md` | atomica | risolto | 3 |
| `fatto-audit-di-rinnovo-giugno-2026.md` | atomica | risolto | 2 |
| `fatto-chi-e-stato-intervistato-in-audit.md` | atomica | risolto | 1 |
| `fatto-chiusura-nc-documentale-e-il-richiamo.md` | atomica | risolto | 1 |
| `fatto-condizioni-uso-marchio-brcgs.md` | atomica | risolto | 1 |
| `fatto-due-nc-e-cinque-osservazioni.md` | atomica | risolto | 2 |
| `fatto-due-nc-interne-sul-proprio-ritardo.md` | atomica | risolto | 1 |
| `fatto-due-nc-minori-audit-2026.md` | atomica | risolto | 2 |
| `fatto-evidenze-audit-oltre-termine.md` | atomica | aperto | 5 |
| `fatto-grade-aa-messo-in-guardia.md` | atomica | risolto | 2 |
| `fatto-impianto-haccp-verificato-in-audit.md` | atomica | risolto | 4 |
| `fatto-nc1-seconde-firme-undici-moduli-su-venti.md` | atomica | risolto | 2 |
| `fatto-nc2-carrello-ricambi-a-bordo-linea.md` | atomica | risolto | 2 |
| `fatto-proteina-latte-prima-del-bio.md` | atomica | aperto | 1 |
| `fatto-quattro-neoassunti-linea2-senza-formazione-allergeni.md` | atomica | risolto | 2 |
| `fatto-referenze-nello-scope-del-certificato.md` | atomica | risolto | 1 |
| `fatto-riserva-su-nc1-efficacia-da-verificare.md` | atomica | risolto | 2 |
| `fatto-rivalidazione-ccp2-non-formalizzata.md` | atomica | risolto | 2 |
| `fatto-scope-certificato-e-quattro-esclusioni.md` | atomica | risolto | 2 |
| `fatto-semilavorati-senza-identificazione-in-cella.md` | atomica | risolto | 1 |
| `fatto-sistema-adeguato-con-riserve.md` | atomica | risolto | 2 |
| `fatto-termometri-tp08-tp11-fuori-dal-registro.md` | atomica | aperto | 3 |
| `fatto-test-rintracciabilita-audit-2h50.md` | atomica | risolto | 3 |
| `fatto-vendor-rating-senza-imballaggi-e-laboratorio.md` | atomica | risolto | 2 |
| `fatto-zanzariera-lacerata-e-porta-officina.md` | atomica | aperto | 2 |
| `kpi-pareto-cause-nc-2026.md` | atomica | aperto | 2 |
| `questione-carrello-ricambi-dichiarato-rimosso.md` | conflitto | aperto | 6 |
| `questione-categorie-e-durata-audit-divergenti.md` | atomica | aperto | 2 |
| `questione-clausola-della-nc1-in-due-versioni.md` | atomica | aperto | 6 |
| `questione-convalida-md-3200-tre-date.md` | atomica | aperto | 4 |
| `questione-data-di-emissione-del-rapporto-di-audit.md` | atomica | aperto | 2 |
| `questione-evidenze-del-02-04-nove-o-cinque.md` | atomica | aperto | 2 |
| `questione-proroga-informale-al-27-03.md` | atomica | aperto | 2 |
| `questione-quando-l-ente-torna-a-verificare.md` | atomica | aperto | 4 |
| `questione-scadenza-certificato-luglio-o-aprile.md` | atomica | aperto | 3 |
| `questione-sette-nc-o-due.md` | atomica | aperto | 2 |
| `questione-tre-o-quattro-neoassunti-senza-formazione.md` | atomica | aperto | 2 |
| `questione-validazione-ccp2-mai-confermata.md` | atomica | risolto | 2 |
| `questione-vendor-rating-2025-c-e-o-non-c-e.md` | atomica | aperto | 2 |
| `self-certificazioni.md` | atomica | risolto | 2 |
| `sessione-s4-lotto-03c.md` | sessione | — | 0 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` | self-certificazioni, area-qualita, fatto-audit-csqa-febbraio-2026-esito, fatto-condizioni-uso-marchio-brcgs, fatto-due-nc-e-cinque-osservazioni, fatto-referenze-nello-scope-del-certificato, fatto-scope-certificato-e-quattro-esclusioni, questione-categorie-e-durata-audit-divergenti, questione-clausola-della-nc1-in-due-versioni, questione-data-di-emissione-del-rapporto-di-audit, questione-quando-l-ente-torna-a-verificare, questione-scadenza-certificato-luglio-o-aprile, questione-sette-nc-o-due, entita-csqa-certificazioni, entita-icea, entita-nadia-franceschini |
| `Conferma_incarico_audit_rinnovo_2026.pdf` | fatto-audit-di-rinnovo-giugno-2026, fatto-riserva-su-nc1-efficacia-da-verificare, questione-quando-l-ente-torna-a-verificare, questione-scadenza-certificato-luglio-o-aprile, doc-conferma-incarico-audit-rinnovo-2026, entita-nadia-franceschini |
| `R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml` | fatto-audit-di-rinnovo-giugno-2026, fatto-evidenze-audit-oltre-termine, fatto-grade-aa-messo-in-guardia, fatto-riserva-su-nc1-efficacia-da-verificare, questione-carrello-ricambi-dichiarato-rimosso, questione-clausola-della-nc1-in-due-versioni, questione-evidenze-del-02-04-nove-o-cinque, questione-proroga-informale-al-27-03, questione-quando-l-ente-torna-a-verificare, questione-scadenza-certificato-luglio-o-aprile, entita-csqa-certificazioni, entita-nadia-franceschini |
| `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt` | self-certificazioni, area-qualita, fatto-audit-csqa-febbraio-2026-esito, fatto-chi-e-stato-intervistato-in-audit, fatto-chiusura-nc-documentale-e-il-richiamo, fatto-due-nc-e-cinque-osservazioni, fatto-due-nc-minori-audit-2026, fatto-evidenze-audit-oltre-termine, fatto-grade-aa-messo-in-guardia, fatto-impianto-haccp-verificato-in-audit, fatto-nc1-seconde-firme-undici-moduli-su-venti, fatto-nc2-carrello-ricambi-a-bordo-linea, fatto-quattro-neoassunti-linea2-senza-formazione-allergeni, fatto-rivalidazione-ccp2-non-formalizzata, fatto-scope-certificato-e-quattro-esclusioni, fatto-semilavorati-senza-identificazione-in-cella, fatto-sistema-adeguato-con-riserve, fatto-termometri-tp08-tp11-fuori-dal-registro, fatto-test-rintracciabilita-audit-2h50, fatto-vendor-rating-senza-imballaggi-e-laboratorio, fatto-zanzariera-lacerata-e-porta-officina, questione-carrello-ricambi-dichiarato-rimosso, questione-categorie-e-durata-audit-divergenti, questione-clausola-della-nc1-in-due-versioni, questione-convalida-md-3200-tre-date, questione-data-di-emissione-del-rapporto-di-audit, questione-evidenze-del-02-04-nove-o-cinque, questione-proroga-informale-al-27-03, questione-quando-l-ente-torna-a-verificare, questione-sette-nc-o-due, questione-tre-o-quattro-neoassunti-senza-formazione, questione-validazione-ccp2-mai-confermata, questione-vendor-rating-2025-c-e-o-non-c-e, doc-rapporto-audit-csqa-2026, entita-csqa-certificazioni, entita-nadia-franceschini |