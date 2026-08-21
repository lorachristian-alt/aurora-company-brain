# Suite QA delle note — report unico

- Data: 2026-08-21
- Perimetro: **lotto** (lotto `lotto_02b_bis_allergeni`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 25 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 151 |
| `projects\` | 8 |
| `docs\` | 31 |
| `entities\` | 27 |
| `concepts\` | 6 |
| `data\` | 29 |
| `outputs\` | 1 |
| `code\` | 16 |
| `workspace\` | 10 |
| `sources\` | 1 |
| **totale** | **281** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **270** note.*

| `type` | Note |
|---|---|
| `atomica` | 177 |
| `concetto` | 5 |
| `conflitto` | 46 |
| `entita` | 22 |
| `hub` | 13 |
| `index` | 11 |
| `sessione` | 7 |

---
## qa_frontmatter (perimetro: lotto, 52 note)

- ERRORI: **0**
- AVVISI: **13**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-passaggi-barrati-scheda-allergeni.md` |  | frontmatter | corpo di 328 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-pc-sesamo-condizionato-al-prototipo.md` |  | frontmatter | summary di 269 caratteri (tetto 250) |
| `fatto-programma-p2-ogni-giorno.md` |  | frontmatter | corpo di 343 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-referenze-fuori-scheda-horeca.md` |  | frontmatter | summary contiene piu' di una frase |
| `fatto-rework-linea-1-sospeso.md` |  | frontmatter | summary di 288 caratteri (tetto 250) |
| `fatto-scheda-allergeni-modifiche-non-accettate.md` |  | frontmatter | corpo di 336 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-sessioni-formazione-allergeni-2026.md` |  | frontmatter | summary di 255 caratteri (tetto 250) |
| `fatto-turno-notte-senza-formazione.md` |  | frontmatter | summary contiene piu' di una frase |
| `doc-criteri-accettazione-cip.md` |  | frontmatter | summary di 286 caratteri (tetto 250) |
| `doc-criteri-accettazione-cip.md` |  | frontmatter | corpo di 322 parole: fra 301 e 350, si motiva o si spezza |
| `doc-programmi-cip-per-linea.md` |  | frontmatter | summary di 253 caratteri (tetto 250) |
| `doc-sequenze-produzione-allergeni.md` |  | frontmatter | summary di 272 caratteri (tetto 250) |
| `doc-stoccaggio-segregato-allergeni.md` |  | frontmatter | summary di 271 caratteri (tetto 250) |


## qa_link_integrity (perimetro: lotto, 281 note nel vault)

- ERRORI: **0**
- AVVISI: **5**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-programma-p2-ogni-giorno.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `fatto-rework-linea-1-sospeso.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `questione-composizione-lavaggio-completo.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `doc-tipi-lavaggio-allergeni.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `entita-chiara-vicentini.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |


## qa_provenance (perimetro: lotto, 52 note)

- ERRORI: **0**
- AVVISI: **7**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `area-logistica.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-composizione-lavaggio-completo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-tamponi-allergeni-non-registrati.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-programmi-cip-per-linea.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-responsabilita-allergeni.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-scheda-tecnica-af-sn-0450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-stoccaggio-segregato-allergeni.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 52 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### logistica

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-logistica.md` | hub | aperto | 1 |
| `doc-stoccaggio-segregato-allergeni.md` | atomica | risolto | 1 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 1 |
| `doc-criteri-accettazione-cip.md` | atomica | risolto | 1 |
| `doc-etichettatura-precauzionale.md` | atomica | risolto | 1 |
| `doc-formazione-allergeni-2026.md` | atomica | risolto | 2 |
| `doc-manuale-haccp.md` | atomica | risolto | 2 |
| `doc-matrice-allergeni-referenze.md` | atomica | risolto | 1 |
| `doc-programmi-cip-per-linea.md` | atomica | risolto | 1 |
| `doc-regole-rework.md` | atomica | risolto | 1 |
| `doc-responsabilita-allergeni.md` | atomica | risolto | 1 |
| `doc-scheda-tecnica-af-sn-0450.md` | atomica | risolto | 1 |
| `doc-sequenze-produzione-allergeni.md` | atomica | risolto | 1 |
| `doc-tipi-lavaggio-allergeni.md` | atomica | risolto | 1 |
| `doc-validazione-pulizia-allergeni.md` | atomica | risolto | 1 |
| `entita-chiara-vicentini.md` | entita | risolto | 3 |
| `fatto-cartello-bacheca-2024-senza-sesamo.md` | atomica | aperto | 2 |
| `fatto-deroga-sequenza-l2-cancellata.md` | atomica | risolto | 2 |
| `fatto-firma-registro-formazione-all-ingresso.md` | atomica | risolto | 1 |
| `fatto-latte-riclassificato-af-sn-0450.md` | atomica | risolto | 1 |
| `fatto-passaggi-barrati-scheda-allergeni.md` | atomica | aperto | 1 |
| `fatto-pc-sesamo-condizionato-al-prototipo.md` | atomica | aperto | 1 |
| `fatto-programma-p2-ogni-giorno.md` | atomica | risolto | 2 |
| `fatto-proteina-latte-prima-del-bio.md` | atomica | aperto | 1 |
| `fatto-quasi-incidente-sequenza-novembre.md` | atomica | aperto | 1 |
| `fatto-referenze-fuori-scheda-horeca.md` | atomica | aperto | 1 |
| `fatto-rework-linea-1-sospeso.md` | atomica | aperto | 1 |
| `fatto-saletta-pilota-sesamo-segregato.md` | atomica | risolto | 1 |
| `fatto-scheda-allergeni-modifiche-non-accettate.md` | atomica | aperto | 1 |
| `fatto-sessioni-formazione-allergeni-2026.md` | atomica | risolto | 2 |
| `fatto-turno-notte-senza-formazione.md` | atomica | aperto | 1 |
| `fatto-validazione-pulizia-da-ripetere.md` | atomica | aperto | 1 |
| `prodotto-af-sn-0470.md` | entita | risolto | 2 |
| `questione-arachidi-solfiti-aula-e-matrice.md` | conflitto | aperto | 2 |
| `questione-composizione-lavaggio-completo.md` | conflitto | aperto | 3 |
| `questione-frequenza-tamponi-prescritta-e-reale.md` | conflitto | aperto | 2 |
| `questione-nc-lavaggi-sul-modulo-reclami.md` | conflitto | aperto | 5 |
| `questione-precauzionale-af-sn-0450-soia.md` | conflitto | aperto | 2 |
| `questione-proteine-test-manuale-e-scheda.md` | conflitto | aperto | 2 |
| `questione-rework-congelamento-slide-e-scheda.md` | conflitto | aperto | 2 |
| `questione-tamponi-allergeni-non-registrati.md` | conflitto | aperto | 3 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `formazione_allergeni_operatori_2026.pptx` | fatto-cartello-bacheca-2024-senza-sesamo, fatto-firma-registro-formazione-all-ingresso, fatto-quasi-incidente-sequenza-novembre, fatto-sessioni-formazione-allergeni-2026, fatto-turno-notte-senza-formazione, questione-arachidi-solfiti-aula-e-matrice, questione-rework-congelamento-slide-e-scheda, questione-tamponi-allergeni-non-registrati, doc-formazione-allergeni-2026, entita-chiara-vicentini, prodotto-af-sn-0470 |
| `scheda_allergeni_matrice_cross_contamination.docx` | fatto-cartello-bacheca-2024-senza-sesamo, fatto-deroga-sequenza-l2-cancellata, fatto-latte-riclassificato-af-sn-0450, fatto-passaggi-barrati-scheda-allergeni, fatto-pc-sesamo-condizionato-al-prototipo, fatto-proteina-latte-prima-del-bio, fatto-referenze-fuori-scheda-horeca, fatto-rework-linea-1-sospeso, fatto-saletta-pilota-sesamo-segregato, fatto-scheda-allergeni-modifiche-non-accettate, fatto-sessioni-formazione-allergeni-2026, fatto-validazione-pulizia-da-ripetere, questione-arachidi-solfiti-aula-e-matrice, questione-composizione-lavaggio-completo, questione-nc-lavaggi-sul-modulo-reclami, questione-precauzionale-af-sn-0450-soia, questione-proteine-test-manuale-e-scheda, questione-rework-congelamento-slide-e-scheda, questione-tamponi-allergeni-non-registrati, doc-etichettatura-precauzionale, doc-formazione-allergeni-2026, doc-matrice-allergeni-referenze, doc-regole-rework, doc-responsabilita-allergeni, doc-sequenze-produzione-allergeni, doc-stoccaggio-segregato-allergeni, doc-tipi-lavaggio-allergeni, doc-validazione-pulizia-allergeni, entita-chiara-vicentini, prodotto-af-sn-0470 |