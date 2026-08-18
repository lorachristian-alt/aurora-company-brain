# Suite QA delle note — report unico

- Data: 2026-08-18
- Perimetro: **lotto** (lotto `1a`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 0 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 30 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 48 |
| `projects\` | 8 |
| `docs\` | 6 |
| `entities\` | 14 |
| `concepts\` | 5 |
| `data\` | 12 |
| `outputs\` | 1 |
| `code\` | 7 |
| `workspace\` | 3 |
| `sources\` | 1 |
| **totale** | **106** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **102** note.*

| `type` | Note |
|---|---|
| `atomica` | 52 |
| `concetto` | 4 |
| `conflitto` | 18 |
| `entita` | 11 |
| `hub` | 9 |
| `index` | 11 |
| `sessione` | 1 |

---
## qa_frontmatter (perimetro: lotto, 59 note)

- ERRORI: **0**
- AVVISI: **9**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-avvertenza-costruttore-guarnizioni-non-originali.md` |  | frontmatter | corpo di 315 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-decisione-proseguire-valvola-08-05.md` |  | frontmatter | corpo di 335 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-fermo-pkm-450-l26130.md` |  | frontmatter | corpo di 330 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-guarnizione-pkm-450-manutenzione-scaduta.md` |  | frontmatter | corpo di 332 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-muffe-l26128-45-giorni.md` |  | frontmatter | corpo di 319 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-piano-produzione-sett19-21.md` |  | frontmatter | corpo di 331 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-repliche-shelf-life-l26130-divergenti.md` |  | frontmatter | corpo di 331 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-manutenzioni-arretrate-2026.md` |  | frontmatter | corpo di 344 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-shelf-life-af-sn-0450.md` |  | frontmatter | corpo di 338 parole: fra 301 e 350, si motiva o si spezza |


## qa_link_integrity (perimetro: lotto, 106 note nel vault)

- ERRORI: **0**
- AVVISI: **0**


## qa_provenance (perimetro: lotto, 59 note)

- ERRORI: **0**
- AVVISI: **21**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-giro-di-vite-seconde-firme-ccp3.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-repliche-shelf-life-l26130-divergenti.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-codice-allarme-pkm-450.md` |  | provenance | codice senza riscontro in nessuna fonte citata: «E-214» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | codice senza riscontro in nessuna fonte citata: «E-214» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | codice senza riscontro in nessuna fonte citata: «E-214» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:07» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:09:02» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | fonte immagine 'IMG-20260510-WA0007.jpg': riscontro visivo, da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-tassello-inox-non-passato.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «Verifica di fine turno (capoturno)» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «dalle 15 alle 18.45 linea ferma per rottura valvola azoto. verifiche n» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «18:50» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «19:55» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | fonte immagine 'MOD-QA-07_10-05-26_L1_T2_scansione.jpg': riscontro visivo, da chiudere a mano |
| `doc-scheda-tecnica-af-sn-0450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `concetto-atmosfera-protettiva.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `concetto-shelf-life.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `kpi-shelf-life-af-sn-0450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-limite-o2-residuo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 59 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### (senza area)

| Nota | type | stato | fonti |
|---|---|---|---|
| `concetto-atmosfera-protettiva.md` | concetto | risolto | 2 |
| `concetto-ccp.md` | concetto | risolto | 2 |
| `concetto-shelf-life.md` | concetto | risolto | 2 |

### commerciale

| Nota | type | stato | fonti |
|---|---|---|---|
| `prodotto-af-sn-0450.md` | entita | risolto | 4 |

### manutenzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `entita-pakmatic.md` | entita | risolto | 2 |
| `fatto-allarme-acustico-md-3200-basso.md` | atomica | risolto | 1 |
| `fatto-avvertenza-costruttore-guarnizioni-non-originali.md` | atomica | risolto | 3 |
| `fatto-decisione-proseguire-valvola-08-05.md` | atomica | risolto | 3 |
| `fatto-fermo-forno-ft-01-05-05.md` | atomica | risolto | 2 |
| `fatto-fermo-pkm-450-l26130.md` | atomica | risolto | 4 |
| `fatto-guarnizione-pkm-450-manutenzione-scaduta.md` | atomica | risolto | 3 |
| `fatto-manutenzioni-rimandate-per-promo.md` | atomica | aperto | 1 |
| `fatto-ricambi-fuori-area-produzione-manuale-pkm.md` | atomica | risolto | 2 |
| `fatto-riepilogo-manutenzione-non-quadra.md` | atomica | aperto | 1 |
| `fatto-valvola-modulante-pt-104-revisione-rimandata.md` | atomica | aperto | 2 |
| `kpi-manutenzioni-arretrate-2026.md` | atomica | aperto | 1 |
| `questione-arrivo-officina-fermo-pkm-450.md` | conflitto | aperto | 2 |
| `questione-codice-allarme-pkm-450.md` | conflitto | aperto | 3 |
| `questione-codice-ricambio-valvola-pkm-450.md` | conflitto | aperto | 4 |
| `questione-materiale-guarnizione-pkm-450.md` | conflitto | aperto | 6 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `entita-ionut-popescu.md` | entita | risolto | 3 |
| `fatto-operatori-ccp3-linea1-maggio.md` | atomica | aperto | 3 |
| `fatto-piano-produzione-sett19-21.md` | atomica | risolto | 1 |
| `fatto-quaderno-capoturno-linea1.md` | atomica | risolto | 1 |
| `kpi-produzione-0450-linea1-maggio.md` | atomica | risolto | 2 |
| `macchina-ft-01.md` | entita | risolto | 3 |
| `macchina-linea-1.md` | hub | aperto | 3 |
| `questione-linea1-domenica-10-05-fuori-piano.md` | conflitto | aperto | 3 |
| `questione-pezzi-prodotti-l26130.md` | conflitto | aperto | 3 |
| `questione-velocita-nominali-linee.md` | conflitto | aperto | 3 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `doc-limite-o2-residuo-af-sn-0450.md` | atomica | risolto | 1 |
| `doc-mod-qa-07.md` | atomica | risolto | 2 |
| `doc-scheda-tecnica-af-sn-0450.md` | atomica | risolto | 1 |
| `fatto-convalida-md-1800-scaduta.md` | atomica | aperto | 1 |
| `fatto-giro-di-vite-seconde-firme-ccp3.md` | atomica | risolto | 2 |
| `fatto-microperdite-saldatura-l26130.md` | atomica | risolto | 1 |
| `fatto-muffe-l26128-45-giorni.md` | atomica | aperto | 3 |
| `fatto-operatore-senza-formazione-haccp-l26130.md` | atomica | risolto | 1 |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` | atomica | aperto | 1 |
| `fatto-repliche-shelf-life-l26130-divergenti.md` | atomica | aperto | 1 |
| `fatto-sonde-pt-104-in-taratura.md` | atomica | risolto | 1 |
| `kpi-seconde-firme-ccp3-maggio.md` | atomica | risolto | 1 |
| `kpi-shelf-life-af-sn-0450.md` | atomica | aperto | 1 |
| `macchina-md-3200.md` | entita | risolto | 3 |
| `questione-aw-umidita-af-sn-0450.md` | conflitto | aperto | 3 |
| `questione-limite-o2-residuo.md` | conflitto | aperto | 4 |
| `questione-tassello-inox-non-passato.md` | conflitto | aperto | 2 |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` | conflitto | aperto | 3 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf` | doc-limite-o2-residuo-af-sn-0450, doc-mod-qa-07, doc-scheda-tecnica-af-sn-0450, macchina-ft-01, macchina-linea-1, macchina-md-3200, prodotto-af-sn-0450, concetto-atmosfera-protettiva, concetto-ccp, concetto-shelf-life, questione-aw-umidita-af-sn-0450, questione-limite-o2-residuo |
| `appunti_capoturno_quaderno_linea1_OCR.txt` | fatto-decisione-proseguire-valvola-08-05, fatto-fermo-forno-ft-01-05-05, fatto-fermo-pkm-450-l26130, fatto-giro-di-vite-seconde-firme-ccp3, fatto-muffe-l26128-45-giorni, fatto-operatore-senza-formazione-haccp-l26130, fatto-operatori-ccp3-linea1-maggio, fatto-prodotto-non-segregato-deviazione-ccp2, fatto-quaderno-capoturno-linea1, fatto-valvola-modulante-pt-104-revisione-rimandata, questione-arrivo-officina-fermo-pkm-450, questione-linea1-domenica-10-05-fuori-piano, questione-tassello-inox-non-passato, questione-verifiche-ccp3-10-05-tre-versioni, entita-ionut-popescu, macchina-ft-01, macchina-linea-1, kpi-produzione-0450-linea1-maggio, questione-limite-o2-residuo, questione-pezzi-prodotti-l26130 |
| `checklist_metal_detector_manuale_operaio.txt` | fatto-allarme-acustico-md-3200-basso, fatto-giro-di-vite-seconde-firme-ccp3, fatto-muffe-l26128-45-giorni, fatto-operatori-ccp3-linea1-maggio, questione-linea1-domenica-10-05-fuori-piano, questione-tassello-inox-non-passato, questione-verifiche-ccp3-10-05-tre-versioni, doc-mod-qa-07, entita-ionut-popescu, macchina-md-3200, concetto-ccp, kpi-produzione-0450-linea1-maggio, kpi-seconde-firme-ccp3-maggio, questione-velocita-nominali-linee |
| `manuale_uso_manutenzione_PKM450_estratto.pdf` | fatto-avvertenza-costruttore-guarnizioni-non-originali, fatto-guarnizione-pkm-450-manutenzione-scaduta, fatto-ricambi-fuori-area-produzione-manuale-pkm, questione-codice-allarme-pkm-450, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-pakmatic, concetto-atmosfera-protettiva |
| `piano_produzione_settimanale_sett19_21.xlsx` | fatto-operatori-ccp3-linea1-maggio, fatto-piano-produzione-sett19-21, questione-linea1-domenica-10-05-fuori-piano, macchina-linea-1, questione-velocita-nominali-linee |
| `scheda_manutenzione_ordinaria_forni_industrial.csv` | fatto-convalida-md-1800-scaduta, fatto-fermo-forno-ft-01-05-05, fatto-guarnizione-pkm-450-manutenzione-scaduta, fatto-manutenzioni-rimandate-per-promo, fatto-ricambi-fuori-area-produzione-manuale-pkm, fatto-riepilogo-manutenzione-non-quadra, fatto-sonde-pt-104-in-taratura, fatto-valvola-modulante-pt-104-revisione-rimandata, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-pakmatic, macchina-ft-01, macchina-md-3200, kpi-manutenzioni-arretrate-2026 |
| `test_shelf_life_accelerata_confezione_MAP_snack.csv` | fatto-microperdite-saldatura-l26130, fatto-muffe-l26128-45-giorni, fatto-repliche-shelf-life-l26130-divergenti, concetto-shelf-life, kpi-shelf-life-af-sn-0450, questione-aw-umidita-af-sn-0450, questione-limite-o2-residuo |