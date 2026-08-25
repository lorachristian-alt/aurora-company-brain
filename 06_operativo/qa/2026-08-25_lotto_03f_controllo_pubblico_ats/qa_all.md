# Suite QA delle note — report unico

- Data: 2026-08-25
- Perimetro: **lotto** (lotto `lotto_03f_controllo_pubblico_ats`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 44 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 2 |
| `areas\` | 285 |
| `projects\` | 18 |
| `docs\` | 71 |
| `entities\` | 34 |
| `concepts\` | 7 |
| `data\` | 56 |
| `outputs\` | 1 |
| `code\` | 16 |
| `workspace\` | 16 |
| `sources\` | 1 |
| **totale** | **507** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **490** note.*

| `type` | Note |
|---|---|
| `atomica` | 363 |
| `concetto` | 6 |
| `conflitto` | 73 |
| `entita` | 26 |
| `hub` | 15 |
| `index` | 11 |
| `sessione` | 13 |

---
## qa_frontmatter (perimetro: lotto, 53 note)

- ERRORI: **0**
- AVVISI: **18**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-dodici-capitoli-annunciati-undici-elencati.md` |  | frontmatter | summary contiene piu' di una frase |
| `fatto-il-preavviso-non-preclude-il-controllo-senza-preavviso.md` |  | frontmatter | summary contiene piu' di una frase |
| `fatto-ispezione-ats-carrello-ricambi.md` |  | frontmatter | corpo di 344 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` |  | frontmatter | summary di 262 caratteri (tetto 250) |
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` |  | frontmatter | summary contiene piu' di una frase |
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` |  | frontmatter | corpo di 329 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-la-documentazione-visionata-non-copre-l-elenco-richiesto.md` |  | frontmatter | summary di 280 caratteri (tetto 250) |
| `fatto-sopralluogo-interno-del-27-maggio-quattro-punti-critici.md` |  | frontmatter | summary di 311 caratteri (tetto 250) |
| `questione-carrello-ricambi-dichiarato-rimosso.md` |  | frontmatter | summary di 305 caratteri (tetto 250) |
| `questione-i-moduli-ccp-rivisti-prima-del-controllo.md` |  | frontmatter | summary di 279 caratteri (tetto 250) |
| `questione-ultima-potabilita-completa-2023-o-2026.md` |  | frontmatter | summary di 262 caratteri (tetto 250) |
| `progetto-controllo-ufficiale-ats-2026.md` |  | frontmatter | summary di 261 caratteri (tetto 250) |
| `doc-documentazione-richiesta-dall-ats.md` |  | frontmatter | summary di 262 caratteri (tetto 250) |
| `doc-piano-autocontrollo-acqua.md` |  | frontmatter | summary di 259 caratteri (tetto 250) |
| `doc-piano-autocontrollo-acqua.md` |  | frontmatter | corpo di 340 parole: fra 301 e 350, si motiva o si spezza |
| `doc-sanzioni-prospettate-dal-preavviso.md` |  | frontmatter | summary di 252 caratteri (tetto 250) |
| `entita-paola-segattini.md` |  | frontmatter | summary contiene piu' di una frase |
| `entita-ulss-9-scaligera.md` |  | frontmatter | summary di 252 caratteri (tetto 250) |


## qa_link_integrity (perimetro: lotto, 507 note nel vault)

- ERRORI: **0**
- AVVISI: **21**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-due-segnalazioni-rendono-il-ritiro-non-rimandabile.md` |  | link | dichiara l'hub [[area-direzione]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-il-turno-3-non-e-nel-mass-balance.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-maggio-fuori-scala.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-rework-linea-1-sospeso.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `questione-composizione-lavaggio-completo.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-classe-2-provvisoria-sul-frammento.md` |  | link | dichiara l'hub [[progetto-gestione-reclamo-rec-2026-011]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-perimetro-del-blocco-dal-riavvio.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `fatto-procedura-applicata-al-caso-di-maggio.md` |  | link | dichiara l'hub [[progetto-gestione-reclamo-rec-2026-011]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `doc-chiusura-di-un-reclamo.md` |  | link | dichiara l'hub [[progetto-gestione-reclamo-rec-2026-011]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `doc-tipi-lavaggio-allergeni.md` |  | link | dichiara l'hub [[macchina-cip-01]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-costo-non-qualita-due-totali.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-indicatori-2025-consuntivo.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-indicatori-mensili-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-obiettivi-2026-avanzamento.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-pareto-cause-nc-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-reclami-2025.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-registro-reclami-2026.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-tamponi-per-zona-2026.md` |  | link | dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `kpi-vendor-rating-2025.md` |  | link | dichiara l'hub [[area-logistica]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `questione-perimetro-del-blocco-e-mass-balance.md` |  | link | dichiara l'hub [[lotto-l26130]] come proprio in related, ma quell'hub non la elenca nel corpo |
| `sessione-s4-lotto-03b.md` |  | link | dichiara l'hub [[area-risorse-umane]] come proprio in related, ma quell'hub non la elenca nel corpo |


## qa_provenance (perimetro: lotto, 53 note)

- ERRORI: **0**
- AVVISI: **5**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-due-dei-tre-rilievi-e-il-sopralluogo-interno.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-documentazione-richiesta-dall-ats.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-obblighi-dell-osa-durante-il-controllo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-preavviso-ispezione-ats.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-sanzioni-prospettate-dal-preavviso.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 53 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### direzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` | atomica | risolto | 3 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 3 |
| `doc-documentazione-richiesta-dall-ats.md` | atomica | risolto | 1 |
| `doc-obblighi-dell-osa-durante-il-controllo.md` | atomica | risolto | 2 |
| `doc-piano-autocontrollo-acqua.md` | atomica | risolto | 2 |
| `doc-preavviso-ispezione-ats.md` | atomica | risolto | 1 |
| `doc-sanzioni-prospettate-dal-preavviso.md` | atomica | risolto | 2 |
| `entita-chiara-vicentini.md` | entita | risolto | 4 |
| `entita-paola-segattini.md` | entita | risolto | 2 |
| `entita-ulss-9-scaligera.md` | entita | risolto | 3 |
| `fatto-armadietto-spogliatoi-rotto-da-marzo.md` | atomica | risolto | 3 |
| `fatto-aurora-classificata-a-rischio-medio-alto.md` | atomica | risolto | 1 |
| `fatto-bancali-di-imballi-dietro-la-linea-3.md` | atomica | risolto | 1 |
| `fatto-doc-del-film-map-in-scadenza-a-giugno.md` | atomica | risolto | 2 |
| `fatto-dodici-capitoli-annunciati-undici-elencati.md` | atomica | risolto | 1 |
| `fatto-due-dei-tre-rilievi-e-il-sopralluogo-interno.md` | atomica | risolto | 3 |
| `fatto-il-carrello-ricambi-ancora-a-bordo-linea-il-25-maggio.md` | atomica | risolto | 2 |
| `fatto-il-controllo-copre-sei-dei-dodici-capitoli-annunciati.md` | atomica | risolto | 2 |
| `fatto-il-nesso-col-reclamo-escluso-dalla-qualita.md` | atomica | risolto | 2 |
| `fatto-il-preavviso-non-preclude-il-controllo-senza-preavviso.md` | atomica | risolto | 1 |
| `fatto-il-titolare-promette-i-lavori-alla-chiusura-estiva.md` | atomica | risolto | 1 |
| `fatto-io-05-affissa-in-revisione-superata.md` | atomica | risolto | 4 |
| `fatto-ispezione-ats-carrello-ricambi.md` | atomica | risolto | 1 |
| `fatto-la-documentazione-visionata-non-copre-l-elenco-richiesto.md` | atomica | risolto | 2 |
| `fatto-la-lista-dei-preparativi-e-dichiarata-incompleta.md` | atomica | risolto | 1 |
| `fatto-la-pec-girata-alla-qualita-in-trentasei-minuti.md` | atomica | risolto | 1 |
| `fatto-planimetria-esche-senza-le-tre-postazioni-di-via-palu.md` | atomica | risolto | 3 |
| `fatto-pre-verifica-simulata-prima-del-controllo.md` | atomica | risolto | 3 |
| `fatto-quindici-giorni-fra-preavviso-e-ispezione.md` | atomica | risolto | 1 |
| `fatto-rapporto-di-verifica-md-3200-solo-via-mail.md` | atomica | risolto | 2 |
| `fatto-riunione-di-preparazione-il-mattino-dopo.md` | atomica | risolto | 1 |
| `fatto-sopralluogo-interno-del-27-maggio-quattro-punti-critici.md` | atomica | risolto | 3 |
| `kpi-controllo-interno-acqua-il-giorno-dell-ispezione.md` | atomica | risolto | 2 |
| `progetto-controllo-ufficiale-ats-2026.md` | hub | attivo | 2 |
| `questione-carrello-ricambi-dichiarato-rimosso.md` | conflitto | aperto | 8 |
| `questione-due-protocolli-per-lo-stesso-preavviso.md` | conflitto | aperto | 2 |
| `questione-i-moduli-ccp-rivisti-prima-del-controllo.md` | conflitto | aperto | 6 |
| `questione-il-legale-rappresentante-arriva-a-sopralluogo-iniziato.md` | conflitto | aperto | 2 |
| `questione-la-stima-e-il-preventivo.md` | conflitto | aperto | 3 |
| `questione-ultima-potabilita-completa-2023-o-2026.md` | conflitto | aperto | 3 |

### risorse-umane

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-risorse-umane.md` | hub | aperto | 2 |
| `questione-due-attestati-mancanti-o-due-assenti-al-corso.md` | conflitto | aperto | 3 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `notifica_ATS_ispezione_programmata_igiene.txt` | fatto-armadietto-spogliatoi-rotto-da-marzo, fatto-aurora-classificata-a-rischio-medio-alto, fatto-bancali-di-imballi-dietro-la-linea-3, fatto-doc-del-film-map-in-scadenza-a-giugno, fatto-dodici-capitoli-annunciati-undici-elencati, fatto-due-dei-tre-rilievi-e-il-sopralluogo-interno, fatto-il-carrello-ricambi-ancora-a-bordo-linea-il-25-maggio, fatto-il-controllo-copre-sei-dei-dodici-capitoli-annunciati, fatto-il-nesso-col-reclamo-escluso-dalla-qualita, fatto-il-preavviso-non-preclude-il-controllo-senza-preavviso, fatto-io-05-affissa-in-revisione-superata, fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente, fatto-la-documentazione-visionata-non-copre-l-elenco-richiesto, fatto-la-lista-dei-preparativi-e-dichiarata-incompleta, fatto-la-pec-girata-alla-qualita-in-trentasei-minuti, fatto-planimetria-esche-senza-le-tre-postazioni-di-via-palu, fatto-pre-verifica-simulata-prima-del-controllo, fatto-quindici-giorni-fra-preavviso-e-ispezione, fatto-rapporto-di-verifica-md-3200-solo-via-mail, fatto-riunione-di-preparazione-il-mattino-dopo, fatto-sopralluogo-interno-del-27-maggio-quattro-punti-critici, questione-carrello-ricambi-dichiarato-rimosso, questione-due-attestati-mancanti-o-due-assenti-al-corso, questione-due-protocolli-per-lo-stesso-preavviso, questione-i-moduli-ccp-rivisti-prima-del-controllo, questione-il-legale-rappresentante-arriva-a-sopralluogo-iniziato, questione-ultima-potabilita-completa-2023-o-2026, progetto-controllo-ufficiale-ats-2026, doc-documentazione-richiesta-dall-ats, doc-obblighi-dell-osa-durante-il-controllo, doc-preavviso-ispezione-ats, doc-sanzioni-prospettate-dal-preavviso, entita-chiara-vicentini, entita-paola-segattini, entita-ulss-9-scaligera |