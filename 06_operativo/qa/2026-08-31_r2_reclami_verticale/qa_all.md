# Suite QA delle note — report unico

- Data: 2026-08-31
- Perimetro: **lotto** (lotto `r2_reclami_verticale`) — **perimetro di manutenzione: 0 grezzi, 102 note** (E35)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro manutenzione (0 grezzi, 102 note) · **0 ERRORI, 116 AVVISI** · esito **GIALLO**

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
## qa_frontmatter (perimetro: lotto, 113 note)

- ERRORI: **0**
- AVVISI: **50**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-avvertenza-costruttore-guarnizioni-non-originali.md` |  | frontmatter | corpo di 315 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-ccp3-non-in-causa-sul-frammento.md` |  | frontmatter | summary di 260 caratteri (tetto 250) |
| `fatto-ccp3-non-in-causa-sul-frammento.md` |  | frontmatter | corpo di 322 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-convalida-md-1800-scaduta.md` |  | frontmatter | corpo di 320 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-convalida-md-1800-scaduta.md` |  | frontmatter | dichiara un'assenza con la formula di E3 ma non rimanda a un artefatto di ricerca in 06_operativo\ricerche_assenza\ (E43) — debito anteriore a E43, da sanare a fine corsa |
| `fatto-decisione-proseguire-valvola-08-05.md` |  | frontmatter | corpo di 350 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-due-segnalazioni-rendono-il-ritiro-non-rimandabile.md` |  | frontmatter | summary di 297 caratteri (tetto 250) |
| `fatto-due-segnalazioni-rendono-il-ritiro-non-rimandabile.md` |  | frontmatter | corpo di 329 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-fermo-forno-ft-01-05-05.md` |  | frontmatter | corpo di 343 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-frammento-non-e-film-map.md` |  | frontmatter | summary di 264 caratteri (tetto 250) |
| `fatto-ispezione-ats-carrello-ricambi.md` |  | frontmatter | corpo di 344 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` |  | frontmatter | summary di 262 caratteri (tetto 250) |
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` |  | frontmatter | summary contiene piu' di una frase |
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` |  | frontmatter | corpo di 329 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-la-documentazione-visionata-non-copre-l-elenco-richiesto.md` |  | frontmatter | summary di 280 caratteri (tetto 250) |
| `fatto-microperdite-saldatura-l26130.md` |  | frontmatter | corpo di 328 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-102-origine-interna.md` |  | frontmatter | summary di 258 caratteri (tetto 250) |
| `fatto-nc-102-origine-interna.md` |  | frontmatter | corpo di 324 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-cip-2026.md` |  | frontmatter | corpo di 349 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nessuna-nc-per-allarmi-cf-02.md` |  | frontmatter | corpo di 343 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-operatore-senza-formazione-haccp-l26130.md` |  | frontmatter | corpo di 332 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-operatore-senza-formazione-haccp-l26130.md` |  | frontmatter | dichiara un'assenza sull'archivio FUORI dalla formula di attestazione di E3, in `corpo` («nota mette quindi in fila due cose che nessun altro documento dell'archivio tiene insieme»), e non rimanda a nessun artefatto di ricerca in 06_operativo\ricerche_assenza\: si riscrive con la formula e la ricerca lascia il suo artefatto, oppure si restringe il perimetro (E3, E43) — debito anteriore al riconoscitore della classe `assenza`, da sanare a fine corsa |
| `fatto-perimetro-stimato-del-ritiro.md` |  | frontmatter | corpo di 315 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-politica-cultura-sicurezza-alimentare.md` |  | frontmatter | summary di 301 caratteri (tetto 250) |
| `fatto-pro-qa-14-copia-controllata-02.md` |  | frontmatter | summary di 258 caratteri (tetto 250) |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` |  | frontmatter | corpo di 348 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` |  | frontmatter | dichiara un'assenza con la formula di E3 ma non rimanda a un artefatto di ricerca in 06_operativo\ricerche_assenza\ (E43) — debito anteriore a E43, da sanare a fine corsa |
| `fatto-rework-linea-1-sospeso.md` |  | frontmatter | summary di 288 caratteri (tetto 250) |
| `fatto-sopralluogo-interno-del-27-maggio-quattro-punti-critici.md` |  | frontmatter | summary di 311 caratteri (tetto 250) |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | frontmatter | corpo di 311 parole: fra 301 e 350, si motiva o si spezza |
| `questione-carrello-ricambi-dichiarato-rimosso.md` |  | frontmatter | summary di 305 caratteri (tetto 250) |
| `questione-consegna-farina-mv26-0429a.md` |  | frontmatter | dichiara un'assenza sull'archivio FUORI dalla formula di attestazione di E3, in `corpo` («Le letture possibili sono almeno due, e **nessun documento dell'archivio dice quale sia»), e non rimanda a nessun artefatto di ricerca in 06_operativo\ricerche_assenza\: si riscrive con la formula e la ricerca lascia il suo artefatto, oppure si restringe il perimetro (E3, E43) — debito anteriore al riconoscitore della classe `assenza`, da sanare a fine corsa |
| `questione-materiale-guarnizione-pkm-450.md` |  | frontmatter | dichiara un'assenza con la formula di E3 ma non rimanda a un artefatto di ricerca in 06_operativo\ricerche_assenza\ (E43) — debito anteriore a E43, da sanare a fine corsa |
| `fatto-blocco-cautelativo-lotti.md` |  | frontmatter | corpo di 335 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-misura-frammento-rec-2026-011.md` |  | frontmatter | corpo di 326 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-richiesta-relazione-48-ore.md` |  | frontmatter | corpo di 345 parole: fra 301 e 350, si motiva o si spezza |
| `progetto-controllo-ufficiale-ats-2026.md` |  | frontmatter | summary di 261 caratteri (tetto 250) |
| `progetto-gestione-reclamo-rec-2026-011.md` |  | frontmatter | summary di 254 caratteri (tetto 250) |
| `questione-data-apertura-rec-2026-011.md` |  | frontmatter | dichiara un'assenza sull'archivio FUORI dalla formula di attestazione di E3, in `corpo` («dell'evento anziché quella della registrazione** — ma nessun documento dell'archivio lo»), e non rimanda a nessun artefatto di ricerca in 06_operativo\ricerche_assenza\: si riscrive con la formula e la ricerca lascia il suo artefatto, oppure si restringe il perimetro (E3, E43) — debito anteriore al riconoscitore della classe `assenza`, da sanare a fine corsa |
| `doc-documentazione-richiesta-dall-ats.md` |  | frontmatter | summary di 262 caratteri (tetto 250) |
| `doc-riesame-post-crisi.md` |  | frontmatter | summary di 257 caratteri (tetto 250) |
| `doc-verifiche-immediate-reclamo.md` |  | frontmatter | summary di 263 caratteri (tetto 250) |
| `kpi-mass-balance-l26130.md` |  | frontmatter | corpo di 332 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-mass-balance-l26130.md` |  | frontmatter | dichiara un'assenza sull'archivio FUORI dalla formula di attestazione di E3, in `corpo` («**Nessun documento dell'archivio conferma l'ipotesi.**»), e non rimanda a nessun artefatto di ricerca in 06_operativo\ricerche_assenza\: si riscrive con la formula e la ricerca lascia il suo artefatto, oppure si restringe il perimetro (E3, E43) — debito anteriore al riconoscitore della classe `assenza`, da sanare a fine corsa |
| `kpi-obiettivi-politica-2026.md` |  | frontmatter | summary di 300 caratteri (tetto 250) |
| `kpi-obiettivi-politica-2026.md` |  | frontmatter | summary contiene piu' di una frase |
| `kpi-pareto-cause-nc-2026.md` |  | frontmatter | corpo di 328 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-registro-reclami-2026.md` |  | frontmatter | corpo di 324 parole: fra 301 e 350, si motiva o si spezza |
| `questione-pezzi-prodotti-l26130.md` |  | frontmatter | dichiara un'assenza sull'archivio FUORI dalla formula di attestazione di E3, in `corpo` («**Nessun documento in archivio dichiara il perimetro dell'uno o dell'altro**»), e non rimanda a nessun artefatto di ricerca in 06_operativo\ricerche_assenza\: si riscrive con la formula e la ricerca lascia il suo artefatto, oppure si restringe il perimetro (E3, E43) — debito anteriore al riconoscitore della classe `assenza`, da sanare a fine corsa |
| `questione-un-richiamo-in-classe-2.md` |  | frontmatter | summary di 263 caratteri (tetto 250) |


## qa_link_integrity (perimetro: lotto, 507 note nel vault)

- ERRORI: **0**
- AVVISI: **31**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-classe-2-provvisoria-sul-frammento.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `fatto-procedura-applicata-al-caso-di-maggio.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `fatto-promemoria-di-aggiornare-la-procedura.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `doc-classi-di-gravita-della-crisi.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `doc-flusso-della-crisi-sei-fasi.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `doc-modulistica-e-dossier-di-crisi.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `doc-riesame-post-crisi.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `doc-riferimenti-pro-qa-14.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `concetto-ritiro-e-richiamo.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `questione-un-richiamo-in-classe-2.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
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


## qa_provenance (perimetro: lotto, 113 note)

- ERRORI: **0**
- AVVISI: **35**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-cruscotto-colonne-mai-calcolate.md` |  | provenance | la fonte 'cruscotto_KPI_qualita_2026.xlsx' non aggancia nessuna affermazione della nota: rumore nel payload |
| `fatto-decisione-erp-rimandata.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-due-dei-tre-rilievi-e-il-sopralluogo-interno.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-due-segnalazioni-rendono-il-ritiro-non-rimandabile.md` |  | provenance | la fonte 'PRO-QA-08_gestione_reclami_cliente_rev2.docx' non aggancia nessuna affermazione della nota: rumore nel payload |
| `fatto-fermo-forno-ft-01-05-05.md` |  | provenance | data senza riscontro in nessuna fonte citata: «05/05/2026» (nell'intestazione: `title`/`summary`) — debito anteriore alla superficie dell'intestazione (23/08/2026), da sanare a fine corsa |
| `fatto-fermo-forno-ft-01-05-05.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:20» (nell'intestazione: `title`/`summary`) — debito anteriore alla superficie dell'intestazione (23/08/2026), da sanare a fine corsa |
| `fatto-giro-di-vite-seconde-firme-ccp3.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-operatore-senza-formazione-haccp-l26130.md` |  | provenance | data senza riscontro in nessuna fonte citata: «10/05/2026» (nell'intestazione: `title`/`summary`) — debito anteriore alla superficie dell'intestazione (23/08/2026), da sanare a fine corsa |
| `fatto-pro-qa-14-copia-controllata-02.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-quaderno-capoturno-linea1.md` |  | provenance | data senza riscontro in nessuna fonte citata: «12/05/2026» (nell'intestazione: `title`/`summary`) — debito anteriore alla superficie dell'intestazione (23/08/2026), da sanare a fine corsa |
| `fatto-quaderno-capoturno-linea1.md` |  | provenance | numero senza riscontro in nessuna fonte citata: «2026» (nell'intestazione: `title`/`summary`) — debito anteriore alla superficie dell'intestazione (23/08/2026), da sanare a fine corsa |
| `fatto-test-rintracciabilita-audit-2h50.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «dalle 15 alle 18.45 linea ferma per rottura valvola azoto,
verifiche n» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «Verifica di fine turno (capoturno)» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «14:05» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «18:50» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «19:55» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «21:00» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «22:00» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:00» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «16:00» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «17:00» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «19:55» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | provenance | fonte immagine 'MOD-QA-07_10-05-26_L1_T2_scansione.jpg': riscontro visivo, da chiudere a mano |
| `questione-posizione-md-3200-in-linea.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-misura-frammento-rec-2026-011.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |
| `fatto-richiesta-relazione-48-ore.md` |  | provenance | data senza riscontro in nessuna fonte citata: «14/05/2026» (nell'intestazione: `title`/`summary`) — debito anteriore alla superficie dell'intestazione (23/08/2026), da sanare a fine corsa |
| `questione-misura-frammento-strumentale.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «di dimensione
stimata dalla foto 7-9 mm» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-misura-frammento-strumentale.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |
| `doc-documentazione-richiesta-dall-ats.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-gestione-reclami-haccp.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-riesame-post-crisi.md` |  | provenance | la fonte 'procedura_ritiro_prodotto_CRISI_GDO.txt' non aggancia nessuna affermazione della nota: rumore nel payload |
| `doc-verifiche-immediate-reclamo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `concetto-fefo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 113 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### commerciale

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-commerciale.md` | hub | risolto | 1 |
| `entita-tosano-cerea.md` | entita | risolto | 2 |
| `fatto-richiesta-relazione-48-ore.md` | atomica | risolto | 2 |
| `prodotto-af-sn-0450.md` | entita | risolto | 5 |

### direzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-direzione.md` | hub | aperto | 1 |
| `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente.md` | atomica | risolto | 3 |
| `fatto-riunione-direzione-reclamo-l26130.md` | atomica | risolto | 1 |
| `questione-data-riunione-direzione.md` | conflitto | aperto | 2 |

### logistica

| Nota | type | stato | fonti |
|---|---|---|---|
| `concetto-fefo.md` | concetto | risolto | 2 |
| `lotto-mv26-0429a.md` | entita | risolto | 5 |
| `questione-azoto-quantita-e-livello-06-05.md` | conflitto | aperto | 3 |
| `questione-codici-lotto-azoto-06-05.md` | conflitto | aperto | 3 |
| `questione-consegna-farina-mv26-0429a.md` | conflitto | aperto | 3 |
| `questione-tmc-farina-mv26-0429a.md` | conflitto | aperto | 4 |

### manutenzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-manutenzione.md` | hub | aperto | 1 |
| `entita-ivano-dal-maso.md` | entita | risolto | 4 |
| `fatto-avvertenza-costruttore-guarnizioni-non-originali.md` | atomica | risolto | 3 |
| `fatto-decisione-proseguire-valvola-08-05.md` | atomica | risolto | 4 |
| `fatto-fermo-forno-ft-01-05-05.md` | atomica | risolto | 3 |
| `fatto-preventivo-potenza-630-kw-tunnel.md` | atomica | aperto | 1 |
| `fatto-riparazione-guarnizione-non-originale.md` | atomica | risolto | 3 |
| `questione-materiale-guarnizione-pkm-450.md` | conflitto | aperto | 6 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `fatto-quaderno-capoturno-linea1.md` | atomica | risolto | 1 |
| `questione-pezzi-prodotti-l26130.md` | conflitto | aperto | 3 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 3 |
| `concetto-ritiro-e-richiamo.md` | concetto | risolto | 1 |
| `doc-classi-di-gravita-della-crisi.md` | atomica | risolto | 1 |
| `doc-conferma-incarico-audit-rinnovo-2026.md` | atomica | risolto | 1 |
| `doc-cruscotto-kpi-2026.md` | atomica | aperto | 2 |
| `doc-documentazione-richiesta-dall-ats.md` | atomica | risolto | 1 |
| `doc-flusso-della-crisi-sei-fasi.md` | atomica | risolto | 1 |
| `doc-gestione-deviazioni-haccp.md` | atomica | risolto | 1 |
| `doc-gestione-reclami-haccp.md` | atomica | risolto | 1 |
| `doc-limite-o2-residuo-af-sn-0450.md` | atomica | risolto | 1 |
| `doc-modulistica-e-dossier-di-crisi.md` | atomica | risolto | 1 |
| `doc-regole-rework.md` | atomica | risolto | 1 |
| `doc-riesame-direzione-2026.md` | atomica | risolto | 1 |
| `doc-riesame-post-crisi.md` | atomica | risolto | 1 |
| `doc-riferimenti-pro-qa-08.md` | atomica | risolto | 1 |
| `doc-riferimenti-pro-qa-14.md` | atomica | risolto | 1 |
| `doc-validazione-pulizia-allergeni.md` | atomica | risolto | 1 |
| `doc-verifiche-immediate-reclamo.md` | atomica | risolto | 2 |
| `entita-analytica-veneta.md` | entita | risolto | 3 |
| `entita-elena-marchetti.md` | entita | risolto | 5 |
| `fatto-aurora-classificata-a-rischio-medio-alto.md` | atomica | risolto | 1 |
| `fatto-blocco-cautelativo-lotti.md` | atomica | risolto | 6 |
| `fatto-ccp3-non-in-causa-sul-frammento.md` | atomica | risolto | 3 |
| `fatto-classe-2-provvisoria-sul-frammento.md` | atomica | risolto | 1 |
| `fatto-condizioni-uso-marchio-brcgs.md` | atomica | risolto | 1 |
| `fatto-convalida-md-1800-scaduta.md` | atomica | aperto | 3 |
| `fatto-cruscotto-colonne-mai-calcolate.md` | atomica | aperto | 1 |
| `fatto-decisione-erp-rimandata.md` | atomica | aperto | 1 |
| `fatto-due-dei-tre-rilievi-e-il-sopralluogo-interno.md` | atomica | risolto | 3 |
| `fatto-due-segnalazioni-rendono-il-ritiro-non-rimandabile.md` | atomica | risolto | 2 |
| `fatto-form-sito-senza-lotto-obbligatorio.md` | atomica | aperto | 1 |
| `fatto-frammento-non-e-film-map.md` | atomica | risolto | 1 |
| `fatto-giro-di-vite-seconde-firme-ccp3.md` | atomica | risolto | 3 |
| `fatto-il-nesso-col-reclamo-escluso-dalla-qualita.md` | atomica | risolto | 2 |
| `fatto-ispezione-ats-carrello-ricambi.md` | atomica | risolto | 1 |
| `fatto-la-documentazione-visionata-non-copre-l-elenco-richiesto.md` | atomica | risolto | 2 |
| `fatto-maggio-fuori-scala.md` | atomica | risolto | 1 |
| `fatto-microperdite-saldatura-l26130.md` | atomica | risolto | 2 |
| `fatto-misura-frammento-rec-2026-011.md` | atomica | risolto | 3 |
| `fatto-modulo-nc-acqua-riconciliato.md` | atomica | risolto | 3 |
| `fatto-nc-102-origine-interna.md` | atomica | risolto | 2 |
| `fatto-nc-cip-2026.md` | atomica | risolto | 3 |
| `fatto-nessuna-nc-per-allarmi-cf-02.md` | atomica | aperto | 3 |
| `fatto-operatore-senza-formazione-haccp-l26130.md` | atomica | risolto | 2 |
| `fatto-perimetro-stimato-del-ritiro.md` | atomica | risolto | 1 |
| `fatto-politica-cultura-sicurezza-alimentare.md` | atomica | risolto | 2 |
| `fatto-politica-otto-impegni-e-il-nono-ritirato.md` | atomica | risolto | 1 |
| `fatto-porta-cella-cf-02-aperta-38-minuti.md` | atomica | aperto | 2 |
| `fatto-pro-qa-14-copia-controllata-02.md` | atomica | risolto | 1 |
| `fatto-procedura-applicata-al-caso-di-maggio.md` | atomica | risolto | 1 |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` | atomica | aperto | 2 |
| `fatto-promemoria-di-aggiornare-la-procedura.md` | atomica | risolto | 1 |
| `fatto-rework-linea-1-sospeso.md` | atomica | aperto | 1 |
| `fatto-semilavorati-senza-identificazione-in-cella.md` | atomica | risolto | 1 |
| `fatto-sopralluogo-interno-del-27-maggio-quattro-punti-critici.md` | atomica | risolto | 3 |
| `fatto-test-rintracciabilita-audit-2h50.md` | atomica | risolto | 3 |
| `fatto-verifiche-ccp3-turno-l26130.md` | atomica | risolto | 3 |
| `kpi-indicatori-2025-consuntivo.md` | atomica | risolto | 1 |
| `kpi-indicatori-mensili-2026.md` | atomica | risolto | 1 |
| `kpi-mass-balance-l26130.md` | atomica | aperto | 2 |
| `kpi-obiettivi-2026-avanzamento.md` | atomica | risolto | 1 |
| `kpi-obiettivi-politica-2026.md` | atomica | risolto | 1 |
| `kpi-pareto-cause-nc-2026.md` | atomica | aperto | 2 |
| `kpi-reclami-2025.md` | atomica | risolto | 2 |
| `kpi-registro-reclami-2026.md` | atomica | aperto | 3 |
| `kpi-seconde-firme-ccp3-maggio.md` | atomica | risolto | 2 |
| `lotto-l26130.md` | hub | aperto | 2 |
| `macchina-md-3200.md` | entita | risolto | 6 |
| `progetto-controllo-ufficiale-ats-2026.md` | hub | attivo | 2 |
| `progetto-gestione-reclamo-rec-2026-011.md` | hub | attivo | 2 |
| `questione-aw-umidita-af-sn-0450.md` | conflitto | aperto | 3 |
| `questione-carrello-ricambi-dichiarato-rimosso.md` | conflitto | aperto | 8 |
| `questione-cruscotto-e-obiettivi-non-si-mappano.md` | conflitto | aperto | 2 |
| `questione-data-apertura-rec-2026-011.md` | conflitto | aperto | 5 |
| `questione-misura-frammento-strumentale.md` | conflitto | aperto | 3 |
| `questione-posizione-md-3200-in-linea.md` | conflitto | aperto | 4 |
| `questione-referenza-del-secondo-reclamo.md` | conflitto | aperto | 2 |
| `questione-un-richiamo-in-classe-2.md` | conflitto | aperto | 2 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|