# Suite QA delle note — report unico

- Data: 2026-08-17
- Perimetro: **lotto** (lotto `l26130`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 0 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 33 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 24 |
| `projects\` | 8 |
| `docs\` | 3 |
| `entities\` | 9 |
| `concepts\` | 2 |
| `data\` | 5 |
| `outputs\` | 1 |
| `code\` | 7 |
| `workspace\` | 2 |
| `sources\` | 1 |
| **totale** | **63** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **60** note.*

| `type` | Note |
|---|---|
| `atomica` | 25 |
| `concetto` | 1 |
| `conflitto` | 11 |
| `entita` | 7 |
| `hub` | 8 |
| `index` | 11 |

---
## qa_frontmatter (perimetro: lotto, 57 note)

- ERRORI: **0**
- AVVISI: **4**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-nc-102-origine-interna.md` |  | frontmatter | summary di 258 caratteri (tetto 250) |
| `fatto-nc-102-origine-interna.md` |  | frontmatter | corpo di 324 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-riepilogo-datalogger-inaffidabile.md` |  | frontmatter | corpo di 314 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-risalita-termica-post-riavvio-l26130.md` |  | frontmatter | corpo di 326 parole: fra 301 e 350, si motiva o si spezza |


## qa_link_integrity (perimetro: lotto, 63 note nel vault)

- ERRORI: **0**
- AVVISI: **0**


## qa_provenance (perimetro: lotto, 57 note)

- ERRORI: **0**
- AVVISI: **29**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `area-logistica.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
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
| `questione-codice-allarme-pkm-450.md` |  | provenance | codice senza riscontro in nessuna fonte citata: «E-214» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | codice senza riscontro in nessuna fonte citata: «E-214» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:07» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:09:02» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | fonte immagine 'IMG-20260510-WA0007.jpg': riscontro visivo, da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-codice-ricambio-valvola-pkm-450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-durata-deviazione-ccp2-l26130.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-materiale-guarnizione-pkm-450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-misura-frammento-rec-2026-011.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |
| `questione-misura-frammento-strumentale.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |
| `doc-ccp2-limite-critico.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `entita-elena-marchetti.md` |  | provenance | la fonte 'MOD-QA-31_reclamo_REC-2026-011.pdf' non aggancia nessuna affermazione della nota: rumore nel payload |
| `entita-ivano-dal-maso.md` |  | provenance | la fonte 'R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml' non aggancia nessuna affermazione della nota: rumore nel payload |
| `concetto-fefo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-scarti-riavvio-l26130.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 57 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### commerciale

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-commerciale.md` | hub | risolto | 1 |
| `bozza-lettera-tosano-reclamo.md` | atomica | aperto | 1 |
| `entita-tosano-cerea.md` | entita | risolto | 2 |
| `fatto-richiesta-relazione-48-ore.md` | atomica | risolto | 1 |
| `prodotto-af-sn-0450.md` | entita | risolto | 3 |

### direzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-direzione.md` | hub | aperto | 1 |
| `fatto-riunione-direzione-reclamo-l26130.md` | atomica | risolto | 1 |
| `questione-data-riunione-direzione.md` | conflitto | aperto | 2 |

### logistica

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-logistica.md` | hub | aperto | 1 |
| `concetto-fefo.md` | concetto | risolto | 2 |
| `lotto-mv26-0429a.md` | entita | risolto | 4 |
| `questione-consegna-farina-mv26-0429a.md` | conflitto | aperto | 3 |
| `questione-tmc-farina-mv26-0429a.md` | conflitto | aperto | 3 |

### manutenzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-manutenzione.md` | hub | aperto | 1 |
| `entita-ivano-dal-maso.md` | entita | risolto | 3 |
| `fatto-fermo-pkm-450-l26130.md` | atomica | risolto | 3 |
| `fatto-riparazione-guarnizione-non-originale.md` | atomica | risolto | 3 |
| `macchina-pkm-450.md` | entita | risolto | 2 |
| `questione-codice-allarme-pkm-450.md` | conflitto | aperto | 2 |
| `questione-codice-ricambio-valvola-pkm-450.md` | conflitto | aperto | 2 |
| `questione-materiale-guarnizione-pkm-450.md` | conflitto | aperto | 4 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-produzione.md` | hub | aperto | 1 |
| `kpi-oee-l26130-l1-t2.md` | atomica | risolto | 2 |
| `questione-pezzi-prodotti-l26130.md` | conflitto | aperto | 2 |
| `questione-scarti-riavvio-l26130.md` | conflitto | aperto | 2 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 1 |
| `doc-ccp2-limite-critico.md` | atomica | risolto | 1 |
| `doc-manuale-haccp.md` | atomica | risolto | 2 |
| `entita-elena-marchetti.md` | entita | risolto | 5 |
| `fatto-blocco-cautelativo-lotti.md` | atomica | risolto | 5 |
| `fatto-deviazione-ccp2-l26130.md` | atomica | risolto | 4 |
| `fatto-esito-laboratorio-frammento.md` | atomica | risolto | 2 |
| `fatto-ispezione-ats-carrello-ricambi.md` | atomica | risolto | 1 |
| `fatto-misura-frammento-rec-2026-011.md` | atomica | risolto | 2 |
| `fatto-nc-102-origine-interna.md` | atomica | risolto | 2 |
| `fatto-registro-cartaceo-mod-qa-12.md` | atomica | risolto | 3 |
| `fatto-riepilogo-datalogger-inaffidabile.md` | atomica | aperto | 1 |
| `fatto-risalita-termica-post-riavvio-l26130.md` | atomica | aperto | 1 |
| `fatto-verifiche-ccp3-turno-l26130.md` | atomica | risolto | 3 |
| `kpi-mass-balance-l26130.md` | atomica | aperto | 1 |
| `lotto-l26130.md` | hub | aperto | 2 |
| `macchina-pt-104.md` | entita | risolto | 2 |
| `progetto-gestione-reclamo-rec-2026-011.md` | hub | attivo | 2 |
| `questione-data-apertura-rec-2026-011.md` | conflitto | aperto | 3 |
| `questione-durata-deviazione-ccp2-l26130.md` | conflitto | aperto | 2 |
| `questione-misura-frammento-strumentale.md` | conflitto | aperto | 2 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `Convocazione_riunione_direzione_12_05.eml` | questione-data-riunione-direzione |
| `IMG-20260510-WA0007.jpg` | questione-codice-allarme-pkm-450 |
| `IMG_20260514_152241_frammento_REC-2026-011.jpg` | fatto-misura-frammento-rec-2026-011, questione-misura-frammento-strumentale |
| `I_Fwd_Richiesta_relazione_48_ore_Tosano.eml` | area-commerciale, fatto-blocco-cautelativo-lotti, fatto-richiesta-relazione-48-ore, entita-tosano-cerea, prodotto-af-sn-0450 |
| `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` | fatto-verifiche-ccp3-turno-l26130 |
| `MOD-QA-31_reclamo_REC-2026-011.pdf` | fatto-verifiche-ccp3-turno-l26130, fatto-blocco-cautelativo-lotti, fatto-misura-frammento-rec-2026-011, progetto-gestione-reclamo-rec-2026-011, questione-data-apertura-rec-2026-011, entita-elena-marchetti, prodotto-af-sn-0450 |
| `RE_RE_URGENTE_reclamo_corpo_estraneo_lotto_L26130.eml` | fatto-blocco-cautelativo-lotti, progetto-gestione-reclamo-rec-2026-011, questione-data-apertura-rec-2026-011, entita-elena-marchetti |
| `R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml` | fatto-riparazione-guarnizione-non-originale, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-ivano-dal-maso, macchina-pkm-450 |
| `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` | fatto-nc-102-origine-interna, questione-materiale-guarnizione-pkm-450, fatto-esito-laboratorio-frammento, questione-misura-frammento-strumentale |
| `SKM_C224e26051412340.pdf` | lotto-mv26-0429a |
| `Scansione_20260518_0003.pdf` | fatto-esito-laboratorio-frammento |
| `Verbale_ispezione_ATS_09_06_2026.pdf` | fatto-ispezione-ats-carrello-ricambi, doc-manuale-haccp, entita-elena-marchetti |
| `calcolo_sfrido_efficienza_OEE_linea_bakery.csv` | area-produzione, fatto-fermo-pkm-450-l26130, kpi-oee-l26130-l1-t2, questione-pezzi-prodotti-l26130, questione-scarti-riavvio-l26130 |
| `certificato_analisi_lotto_farina_MV26_0429A.pdf` | questione-consegna-farina-mv26-0429a, questione-tmc-farina-mv26-0429a, lotto-mv26-0429a |
| `inventario_magazzino_scadenze_FEFO_maggio.csv` | area-logistica, questione-consegna-farina-mv26-0429a, questione-tmc-farina-mv26-0429a, lotto-mv26-0429a, concetto-fefo |
| `lettera_risposta_Tosano_reclamo_BOZZA_v3.docx` | bozza-lettera-tosano-reclamo |
| `log_temperature_pastorizzatore_linea1_10_05_26.log` | fatto-deviazione-ccp2-l26130, fatto-riepilogo-datalogger-inaffidabile, fatto-risalita-termica-post-riavvio-l26130, questione-durata-deviazione-ccp2-l26130, macchina-pt-104 |
| `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` | area-qualita, fatto-deviazione-ccp2-l26130, fatto-registro-cartaceo-mod-qa-12, fatto-verifiche-ccp3-turno-l26130, doc-ccp2-limite-critico, doc-manuale-haccp, entita-elena-marchetti, lotto-l26130, macchina-pt-104 |
| `non_conformita_interne_registro_2026.csv` | fatto-deviazione-ccp2-l26130, fatto-fermo-pkm-450-l26130, fatto-nc-102-origine-interna, fatto-registro-cartaceo-mod-qa-12, fatto-riparazione-guarnizione-non-originale, questione-durata-deviazione-ccp2-l26130, entita-ivano-dal-maso, concetto-fefo |
| `report_fermo_macchina_confezionatrice_MAP.txt` | area-manutenzione, fatto-fermo-pkm-450-l26130, fatto-riparazione-guarnizione-non-originale, questione-codice-allarme-pkm-450, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-elena-marchetti, entita-ivano-dal-maso, macchina-pkm-450, kpi-oee-l26130-l1-t2, questione-scarti-riavvio-l26130 |
| `tracciabilita_lotti_massbalance_L26130.xlsx` | questione-consegna-farina-mv26-0429a, questione-tmc-farina-mv26-0429a, fatto-blocco-cautelativo-lotti, entita-tosano-cerea, lotto-l26130, lotto-mv26-0429a, prodotto-af-sn-0450, kpi-mass-balance-l26130, questione-pezzi-prodotti-l26130 |
| `trascrizione_riunione_direzione_12_05_2026.txt` | area-direzione, fatto-deviazione-ccp2-l26130, fatto-registro-cartaceo-mod-qa-12, fatto-riunione-direzione-reclamo-l26130, questione-data-riunione-direzione, questione-materiale-guarnizione-pkm-450, fatto-blocco-cautelativo-lotti, questione-data-apertura-rec-2026-011 |