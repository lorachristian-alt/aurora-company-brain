# Suite QA delle note — report unico

- Data: 2026-08-18
- Perimetro: **vault**
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 1 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro vault · **135 ERRORI, 64 AVVISI** · esito **ROSSO**

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
## qa_frontmatter (perimetro: vault, 106 note)

- ERRORI: **0**
- AVVISI: **21**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-avvertenza-costruttore-guarnizioni-non-originali.md` |  | frontmatter | corpo di 315 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-decisione-proseguire-valvola-08-05.md` |  | frontmatter | corpo di 335 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-fermo-pkm-450-l26130.md` |  | frontmatter | corpo di 330 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-guarnizione-pkm-450-manutenzione-scaduta.md` |  | frontmatter | corpo di 332 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-muffe-l26128-45-giorni.md` |  | frontmatter | corpo di 319 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-102-origine-interna.md` |  | frontmatter | summary di 258 caratteri (tetto 250) |
| `fatto-nc-102-origine-interna.md` |  | frontmatter | corpo di 324 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-piano-produzione-sett19-21.md` |  | frontmatter | corpo di 331 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-repliche-shelf-life-l26130-divergenti.md` |  | frontmatter | corpo di 331 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-riepilogo-datalogger-inaffidabile.md` |  | frontmatter | corpo di 314 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-risalita-termica-post-riavvio-l26130.md` |  | frontmatter | corpo di 326 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-verifiche-ccp3-turno-l26130.md` |  | frontmatter | corpo di 311 parole: fra 301 e 350, si motiva o si spezza |
| `doc-limite-o2-residuo-af-sn-0450.md` |  | frontmatter | summary contiene piu' di una frase |
| `doc-scheda-tecnica-af-sn-0450.md` |  | frontmatter | summary contiene piu' di una frase |
| `kpi-manutenzioni-arretrate-2026.md` |  | frontmatter | corpo di 344 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-shelf-life-af-sn-0450.md` |  | frontmatter | corpo di 338 parole: fra 301 e 350, si motiva o si spezza |
| `script-genera-llms-txt.md` |  | frontmatter | corpo di 303 parole: fra 301 e 350, si motiva o si spezza |
| `script-qa-copertura.md` |  | frontmatter | corpo di 315 parole: fra 301 e 350, si motiva o si spezza |
| `script-qa-frontmatter.md` |  | frontmatter | corpo di 322 parole: fra 301 e 350, si motiva o si spezza |
| `script-qa-link-integrity.md` |  | frontmatter | corpo di 341 parole: fra 301 e 350, si motiva o si spezza |
| `script-qa-provenance.md` |  | frontmatter | corpo di 345 parole: fra 301 e 350, si motiva o si spezza |


## qa_link_integrity (perimetro: vault, 106 note nel vault)

- ERRORI: **0**
- AVVISI: **1**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `sessione-s4-lotto-1a.md` |  | link | dichiara l'hub [[macchina-linea-1]] come proprio in related, ma quell'hub non la elenca nel corpo |


## qa_provenance (perimetro: vault, 106 note)

- ERRORI: **0**
- AVVISI: **42**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `area-logistica.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-giro-di-vite-seconde-firme-ccp3.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-repliche-shelf-life-l26130-divergenti.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
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
| `questione-codice-allarme-pkm-450.md` |  | provenance | codice senza riscontro in nessuna fonte citata: «E-214» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:07» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «15:09:02» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | fonte immagine 'IMG-20260510-WA0007.jpg': riscontro visivo, da chiudere a mano |
| `questione-codice-allarme-pkm-450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-codice-ricambio-valvola-pkm-450.md` |  | provenance | la fonte 'scheda_manutenzione_ordinaria_forni_industrial.csv' non aggancia nessuna affermazione della nota: rumore nel payload |
| `questione-durata-deviazione-ccp2-l26130.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-tassello-inox-non-passato.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «Verifica di fine turno (capoturno)» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «dalle 15 alle 18.45 linea ferma per rottura valvola azoto. verifiche n» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «18:50» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «19:55» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | fonte immagine 'MOD-QA-07_10-05-26_L1_T2_scansione.jpg': riscontro visivo, da chiudere a mano |
| `fatto-misura-frammento-rec-2026-011.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |
| `questione-misura-frammento-strumentale.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |
| `doc-ccp2-limite-critico.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `entita-elena-marchetti.md` |  | provenance | la fonte 'MOD-QA-31_reclamo_REC-2026-011.pdf' non aggancia nessuna affermazione della nota: rumore nel payload |
| `entita-ivano-dal-maso.md` |  | provenance | la fonte 'R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml' non aggancia nessuna affermazione della nota: rumore nel payload |
| `concetto-atmosfera-protettiva.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `concetto-fefo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `concetto-shelf-life.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `kpi-shelf-life-af-sn-0450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-limite-o2-residuo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-scarti-riavvio-l26130.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: vault, 106 note)

- ERRORI: **135**
- AVVISI: **0**

### Errori

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `(copertura)` |  | copertura | il grezzo 'AUA_autorizzazione_unica_ambientale_scarichi.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'CPI_certificato_prevenzione_incendi_VVF.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'CV_Tommaso_Refosco_2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Circolare_INPS_aliquote_contributive_2026.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Comunicazione_aumento_listino_farine_indicizzazione.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Conferma_incarico_audit_rinnovo_2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Conferma_ordine_Tosano_promo_sottocosto_settimane_19_21.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'DDT_Euroglass_Boccacci_Vetro_N99201.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'DDT_MOLINO_VENETO_Farina_0_N48392_OCR_SPORCO.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'DVR_estratto_valutazione_rischi_2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Fattura_TosanoCerea_2026_0188_copia_cortesia.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Fatture_Elettroniche_SDI_Inbound_Q2.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Fwd_Fwd_Fwd_ATTENZIONE_richiamo_prodotto_concorrente_RASFF.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Fwd_newsletter_confindustria_marzo.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Fwd_preventivo_tunnel_surgelazione_Criotech_rev2.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'IO-05_istruzione_operativa_lavaggio_CIP.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'IT03984710230_00188.xml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'IT03984710230_00215.xml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'IT03984710230_00215.xml.p7m' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Listino_MolinoVeneto_giu2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Newsletter_Fiere_alimentari_2026_NON_LEGGERE.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Nuova cartella di lavoro.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Ordine_Tosano_2026_PRM_118_119_120.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'PRO-QA-08_gestione_reclami_cliente_rev2.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Prospetto_straordinari_gen-apr_2026.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'R_candidatura_spontanea_tecnologo_alimentare.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'R_sollecito_pagamento_fattura_scaduta_Oleificio.eml' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'SKM_C224e26050408520.jpg' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo '_QUESTO_ARCHIVIO_E_SIMULATO.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'accordo_quadro_private_label_Tosano_2026_firmato.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'anagrafica_articoli_export_gestionale.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'analisi_acque_reflue_autocontrollo_2026.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'analisi_marginalita_per_referenza_2026.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'analisi_scostamenti_costo_materie_prime.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'analisi_sell_out_Tosano_marzo_aprile2026.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'appunti_tecnologo_quaderno_prove_pilota_OCR.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'assicurazione_polizza_RCT_RCO_quietanza_2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'bilancio_esercizio_2025_deposito_CCIAA.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'bolla_ingresso_azoto_alimentare_Nordgas_OCR.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'bolletta_VenetaEnergia_maggio2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'bozza_presentazione_nuova_linea_snack_CDA.pptx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'brief_agenzia_packaging_restyling_snack.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'budget_2026_vs_consuntivo_per_linea.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'calcolo_CapEx_linea3_bakery_nuova.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'capitolato_tecnico_fornitura_imballaggi_plastici.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'comunicazione_chiusura_estiva_2026.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'consumi_energetici_forni_kwh_maggio26.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'contestazione_logistica_Tosano_ritardo_Cerea.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'contestazione_sindacale_straordinari_Tosano.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'contratto_fornitura_MolinoVeneto_2026_firmato.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'contratto_manutenzione_impianto_frigo_TS01.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'corso_inglese_aziendale_proposta.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'cruscotto_KPI_qualita_2026.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'doc 2 (1).pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'elenco_attrezzature_taratura_strumenti_2026.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'elenco_chiavi_e_accessi.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'elenco_interni_telefonici.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'email_HR_dimissioni_operai_linea2.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'estratto_conto_unicredit_maggio26.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'estratto_registro_carico_scarico_MOCA.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'fattura_antivirus_licenze_2026.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'formazione_allergeni_operatori_2026.pptx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'img20260428_09241055.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'iscritti_cena_aziendale_dicembre.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'job_description_responsabile_produzione.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'libro_unico_lavoro_estratto_maggio2026.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'lista_contatti_buyer_GDO_nordest.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'listino prezzi GDO v2 VECCHIO non usare.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'listino_prezzi_canale_GDO_fresco_v3.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'log_allarmi_cella_frigo_surgelati_aprile.log' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'log_lavaggio_CIP_linea1_maggio.log' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'log_timbrature_fabbrica_maggio_settimana2.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'mail_fornitore_ingrediente_nuovo_paprika_specifiche.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'mail_titolare_Aurora_visione_aziendale_5anni.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'manutenzione_fotocopiatrice_contratto_copie.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'menu_mensa_aprile_maggio.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'modulo richiesta ferie VUOTO da stampare.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'noleggio_distributori_automatici_contratto.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'nota_commercialista_credito_imposta_beni_strumentali.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'nota_infortunio_INAIL_operaio_linea3.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'nota_spese_trasferte_Zampieri_aprile.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'notifica_ATS_ispezione_programmata_igiene.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'ordine cancelleria marzo.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'ordine_DPI_scarpe_antinfortunistiche.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'ordini_acquisto_materie_prime_aperti_giugno.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'organigramma_aziendale_aggiornato_marzo26.pptx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'panel_test_assaggio_interno_cornetto_premium.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'piano_autocontrollo_acqua_potabile_analisi.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'piano_turni_apprendisti_tecnologi_food.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'politica_qualita_e_sicurezza_alimentare_2026.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'polizza_RC_prodotto_rinnovo_2026_OCR.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'prenotazioni_sala_riunioni_maggio.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'presentazione_commerciale_Aurora_GDO_2026.pptx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'preventivo_Criotech_tunnel_CR-SP180_rev2.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'preventivo_software_ERP_CSB_System_vs_SAP.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'preventivo_tinteggiatura_uffici_NON_ACCETTATO.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'previsionale cassa giugno-agosto DEF (2).xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'previsionale_cassa_giugno_agosto2026.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'procedura_ritiro_prodotto_CRISI_GDO.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'proiezione_ARR_contratti_GDO_2026_2027.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'registro_carico_scarico_rifiuti_estratto_2026.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'registro_estintori_scadenze.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'registro_presenze_corsi_HACCP_scaduti.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'registro_tamponi_superfici_listeria_salmonella.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'reperibilita_gennaio_febbraio_2026.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'report_costi_fissi_OpEx_manutenzioni.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'reso_pallet_EPAL_conteggio_Tosano.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'ricetta_base_esperimento_snack_salato_v12.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'richiesta_campionatura_fiera_Cibus_2026.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'scadenzario_effetti_RIBA_giugno26.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'scheda_allergeni_matrice_cross_contamination.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'scheda_sicurezza_detergente_acido_lavaggio_CIP.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'scheda_tecnica_farina_tipo_0_MolinoVeneto.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'segnalazione_guasto_cancello_carraio.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'segnalazione_qualita_cliente_privato_corpo_estraneo.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'tariffe_vettori_terzi_trasporto_fresco_2026.csv' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'vendor_rating_fornitori_2026.xlsx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'verbale_CDA_approvazione_investimento_tunnel.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'verbale_assemblea_condominio_capannone.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'verbale_incontro_Mario_Rossi_Buyer_Tosano_05_05.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'verbale_riesame_direzione_SGQ_2026.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'verbale_scale_up_industriale_cornetto_premium.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'verifica_periodica_impianto_terra_DPR462.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'visura_camerale_ordinaria_AuroraFoodGroup.pdf' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo 'volantino_convenzione_palestra.txt' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | il grezzo '~$ttera_risposta_Tosano_reclamo_BOZZA_v3.docx' non compare in `fonti` di nessuna nota |
| `(copertura)` |  | copertura | l'area 'amministrazione' non ha il suo hub area-amministrazione in areas\ |
| `(copertura)` |  | copertura | l'area 'ricerca-sviluppo' non ha il suo hub area-ricerca-sviluppo in areas\ |
| `(copertura)` |  | copertura | l'area 'risorse-umane' non ha il suo hub area-risorse-umane in areas\ |
| `(copertura)` |  | copertura | l'area 'sicurezza-ambiente' non ha il suo hub area-sicurezza-ambiente in areas\ |


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
| `area-commerciale.md` | hub | risolto | 1 |
| `bozza-lettera-tosano-reclamo.md` | atomica | aperto | 1 |
| `entita-tosano-cerea.md` | entita | risolto | 2 |
| `fatto-richiesta-relazione-48-ore.md` | atomica | risolto | 1 |
| `prodotto-af-sn-0450.md` | entita | risolto | 4 |

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
| `fatto-riparazione-guarnizione-non-originale.md` | atomica | risolto | 3 |
| `fatto-valvola-modulante-pt-104-revisione-rimandata.md` | atomica | aperto | 2 |
| `kpi-manutenzioni-arretrate-2026.md` | atomica | aperto | 1 |
| `macchina-pkm-450.md` | entita | risolto | 2 |
| `questione-arrivo-officina-fermo-pkm-450.md` | conflitto | aperto | 2 |
| `questione-codice-allarme-pkm-450.md` | conflitto | aperto | 3 |
| `questione-codice-ricambio-valvola-pkm-450.md` | conflitto | aperto | 4 |
| `questione-materiale-guarnizione-pkm-450.md` | conflitto | aperto | 6 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-produzione.md` | hub | aperto | 1 |
| `entita-ionut-popescu.md` | entita | risolto | 3 |
| `fatto-operatori-ccp3-linea1-maggio.md` | atomica | aperto | 3 |
| `fatto-piano-produzione-sett19-21.md` | atomica | risolto | 1 |
| `fatto-quaderno-capoturno-linea1.md` | atomica | risolto | 1 |
| `kpi-oee-l26130-l1-t2.md` | atomica | risolto | 2 |
| `kpi-produzione-0450-linea1-maggio.md` | atomica | risolto | 2 |
| `macchina-ft-01.md` | entita | risolto | 3 |
| `macchina-linea-1.md` | hub | aperto | 3 |
| `questione-linea1-domenica-10-05-fuori-piano.md` | conflitto | aperto | 3 |
| `questione-pezzi-prodotti-l26130.md` | conflitto | aperto | 3 |
| `questione-scarti-riavvio-l26130.md` | conflitto | aperto | 2 |
| `questione-velocita-nominali-linee.md` | conflitto | aperto | 3 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 1 |
| `doc-ccp2-limite-critico.md` | atomica | risolto | 1 |
| `doc-limite-o2-residuo-af-sn-0450.md` | atomica | risolto | 1 |
| `doc-manuale-haccp.md` | atomica | risolto | 2 |
| `doc-mod-qa-07.md` | atomica | risolto | 2 |
| `doc-scheda-tecnica-af-sn-0450.md` | atomica | risolto | 1 |
| `entita-elena-marchetti.md` | entita | risolto | 5 |
| `fatto-blocco-cautelativo-lotti.md` | atomica | risolto | 5 |
| `fatto-convalida-md-1800-scaduta.md` | atomica | aperto | 1 |
| `fatto-deviazione-ccp2-l26130.md` | atomica | risolto | 4 |
| `fatto-esito-laboratorio-frammento.md` | atomica | risolto | 2 |
| `fatto-giro-di-vite-seconde-firme-ccp3.md` | atomica | risolto | 2 |
| `fatto-ispezione-ats-carrello-ricambi.md` | atomica | risolto | 1 |
| `fatto-microperdite-saldatura-l26130.md` | atomica | risolto | 1 |
| `fatto-misura-frammento-rec-2026-011.md` | atomica | risolto | 2 |
| `fatto-muffe-l26128-45-giorni.md` | atomica | aperto | 3 |
| `fatto-nc-102-origine-interna.md` | atomica | risolto | 2 |
| `fatto-operatore-senza-formazione-haccp-l26130.md` | atomica | risolto | 1 |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` | atomica | aperto | 1 |
| `fatto-registro-cartaceo-mod-qa-12.md` | atomica | risolto | 3 |
| `fatto-repliche-shelf-life-l26130-divergenti.md` | atomica | aperto | 1 |
| `fatto-riepilogo-datalogger-inaffidabile.md` | atomica | aperto | 1 |
| `fatto-risalita-termica-post-riavvio-l26130.md` | atomica | aperto | 1 |
| `fatto-sonde-pt-104-in-taratura.md` | atomica | risolto | 1 |
| `fatto-verifiche-ccp3-turno-l26130.md` | atomica | risolto | 3 |
| `kpi-mass-balance-l26130.md` | atomica | aperto | 1 |
| `kpi-seconde-firme-ccp3-maggio.md` | atomica | risolto | 1 |
| `kpi-shelf-life-af-sn-0450.md` | atomica | aperto | 1 |
| `lotto-l26130.md` | hub | aperto | 2 |
| `macchina-md-3200.md` | entita | risolto | 3 |
| `macchina-pt-104.md` | entita | risolto | 2 |
| `progetto-gestione-reclamo-rec-2026-011.md` | hub | attivo | 2 |
| `questione-aw-umidita-af-sn-0450.md` | conflitto | aperto | 3 |
| `questione-data-apertura-rec-2026-011.md` | conflitto | aperto | 3 |
| `questione-durata-deviazione-ccp2-l26130.md` | conflitto | aperto | 2 |
| `questione-limite-o2-residuo.md` | conflitto | aperto | 4 |
| `questione-misura-frammento-strumentale.md` | conflitto | aperto | 2 |
| `questione-tassello-inox-non-passato.md` | conflitto | aperto | 2 |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` | conflitto | aperto | 3 |
| `script-genera-llms-txt.md` | atomica | risolto | 0 |
| `script-qa-all.md` | atomica | risolto | 0 |
| `script-qa-copertura.md` | atomica | risolto | 0 |
| `script-qa-frontmatter.md` | atomica | risolto | 0 |
| `script-qa-link-integrity.md` | atomica | risolto | 0 |
| `script-qa-provenance.md` | atomica | risolto | 0 |
| `sessione-s4-lotto-1a.md` | sessione | — | 0 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `AUA_autorizzazione_unica_ambientale_scarichi.pdf` | **nessuna** |
| `CPI_certificato_prevenzione_incendi_VVF.pdf` | **nessuna** |
| `CV_Tommaso_Refosco_2026.pdf` | **nessuna** |
| `Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` | **nessuna** |
| `Circolare_INPS_aliquote_contributive_2026.txt` | **nessuna** |
| `Comunicazione_aumento_listino_farine_indicizzazione.eml` | **nessuna** |
| `Conferma_incarico_audit_rinnovo_2026.pdf` | **nessuna** |
| `Conferma_ordine_Tosano_promo_sottocosto_settimane_19_21.eml` | **nessuna** |
| `Convocazione_riunione_direzione_12_05.eml` | questione-data-riunione-direzione |
| `DDT_Euroglass_Boccacci_Vetro_N99201.txt` | **nessuna** |
| `DDT_MOLINO_VENETO_Farina_0_N48392_OCR_SPORCO.txt` | **nessuna** |
| `DVR_estratto_valutazione_rischi_2026.pdf` | **nessuna** |
| `DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf` | **nessuna** |
| `Fattura_TosanoCerea_2026_0188_copia_cortesia.pdf` | **nessuna** |
| `Fatture_Elettroniche_SDI_Inbound_Q2.txt` | **nessuna** |
| `Fwd_Fwd_Fwd_ATTENZIONE_richiamo_prodotto_concorrente_RASFF.eml` | **nessuna** |
| `Fwd_newsletter_confindustria_marzo.txt` | **nessuna** |
| `Fwd_preventivo_tunnel_surgelazione_Criotech_rev2.eml` | **nessuna** |
| `IMG-20260510-WA0007.jpg` | questione-codice-allarme-pkm-450 |
| `IMG_20260514_152241_frammento_REC-2026-011.jpg` | fatto-misura-frammento-rec-2026-011, questione-misura-frammento-strumentale |
| `IO-05_istruzione_operativa_lavaggio_CIP.docx` | **nessuna** |
| `IT03984710230_00188.xml` | **nessuna** |
| `IT03984710230_00215.xml` | **nessuna** |
| `IT03984710230_00215.xml.p7m` | **nessuna** |
| `I_Fwd_Richiesta_relazione_48_ore_Tosano.eml` | area-commerciale, fatto-blocco-cautelativo-lotti, fatto-richiesta-relazione-48-ore, entita-tosano-cerea, prodotto-af-sn-0450 |
| `Listino_MolinoVeneto_giu2026.pdf` | **nessuna** |
| `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` | fatto-verifiche-ccp3-turno-l26130, questione-verifiche-ccp3-10-05-tre-versioni |
| `MOD-QA-31_reclamo_REC-2026-011.pdf` | fatto-avvertenza-costruttore-guarnizioni-non-originali, fatto-verifiche-ccp3-turno-l26130, fatto-blocco-cautelativo-lotti, fatto-misura-frammento-rec-2026-011, progetto-gestione-reclamo-rec-2026-011, questione-data-apertura-rec-2026-011, entita-elena-marchetti, prodotto-af-sn-0450 |
| `Newsletter_Fiere_alimentari_2026_NON_LEGGERE.eml` | **nessuna** |
| `Nuova cartella di lavoro.xlsx` | **nessuna** |
| `Ordine_Tosano_2026_PRM_118_119_120.pdf` | **nessuna** |
| `PRO-QA-08_gestione_reclami_cliente_rev2.docx` | **nessuna** |
| `Prospetto_straordinari_gen-apr_2026.xlsx` | **nessuna** |
| `RE_RE_URGENTE_reclamo_corpo_estraneo_lotto_L26130.eml` | fatto-blocco-cautelativo-lotti, progetto-gestione-reclamo-rec-2026-011, questione-data-apertura-rec-2026-011, entita-elena-marchetti |
| `R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml` | **nessuna** |
| `R_candidatura_spontanea_tecnologo_alimentare.eml` | **nessuna** |
| `R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml` | fatto-riparazione-guarnizione-non-originale, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-ivano-dal-maso, macchina-pkm-450 |
| `R_sollecito_pagamento_fattura_scaduta_Oleificio.eml` | **nessuna** |
| `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` | fatto-avvertenza-costruttore-guarnizioni-non-originali, fatto-nc-102-origine-interna, questione-materiale-guarnizione-pkm-450, fatto-esito-laboratorio-frammento, questione-misura-frammento-strumentale, questione-aw-umidita-af-sn-0450 |
| `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt` | **nessuna** |
| `SKM_C224e26050408520.jpg` | **nessuna** |
| `SKM_C224e26051412340.pdf` | lotto-mv26-0429a |
| `Scansione_20260518_0003.pdf` | fatto-esito-laboratorio-frammento |
| `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf` | doc-limite-o2-residuo-af-sn-0450, doc-mod-qa-07, doc-scheda-tecnica-af-sn-0450, macchina-ft-01, macchina-linea-1, macchina-md-3200, prodotto-af-sn-0450, concetto-atmosfera-protettiva, concetto-ccp, concetto-shelf-life, questione-aw-umidita-af-sn-0450, questione-limite-o2-residuo |
| `Verbale_ispezione_ATS_09_06_2026.pdf` | fatto-ispezione-ats-carrello-ricambi, doc-manuale-haccp, entita-elena-marchetti |
| `_QUESTO_ARCHIVIO_E_SIMULATO.txt` | **nessuna** |
| `accordo_quadro_private_label_Tosano_2026_firmato.txt` | **nessuna** |
| `anagrafica_articoli_export_gestionale.xlsx` | **nessuna** |
| `analisi_acque_reflue_autocontrollo_2026.xlsx` | **nessuna** |
| `analisi_marginalita_per_referenza_2026.xlsx` | **nessuna** |
| `analisi_scostamenti_costo_materie_prime.xlsx` | **nessuna** |
| `analisi_sell_out_Tosano_marzo_aprile2026.csv` | **nessuna** |
| `appunti_capoturno_quaderno_linea1_OCR.txt` | fatto-decisione-proseguire-valvola-08-05, fatto-fermo-forno-ft-01-05-05, fatto-fermo-pkm-450-l26130, fatto-giro-di-vite-seconde-firme-ccp3, fatto-muffe-l26128-45-giorni, fatto-operatore-senza-formazione-haccp-l26130, fatto-operatori-ccp3-linea1-maggio, fatto-prodotto-non-segregato-deviazione-ccp2, fatto-quaderno-capoturno-linea1, fatto-valvola-modulante-pt-104-revisione-rimandata, questione-arrivo-officina-fermo-pkm-450, questione-linea1-domenica-10-05-fuori-piano, questione-tassello-inox-non-passato, questione-verifiche-ccp3-10-05-tre-versioni, entita-ionut-popescu, macchina-ft-01, macchina-linea-1, kpi-produzione-0450-linea1-maggio, questione-limite-o2-residuo, questione-pezzi-prodotti-l26130 |
| `appunti_tecnologo_quaderno_prove_pilota_OCR.txt` | **nessuna** |
| `assicurazione_polizza_RCT_RCO_quietanza_2026.pdf` | **nessuna** |
| `bilancio_esercizio_2025_deposito_CCIAA.pdf` | **nessuna** |
| `bolla_ingresso_azoto_alimentare_Nordgas_OCR.txt` | **nessuna** |
| `bolletta_VenetaEnergia_maggio2026.pdf` | **nessuna** |
| `bozza_presentazione_nuova_linea_snack_CDA.pptx` | **nessuna** |
| `brief_agenzia_packaging_restyling_snack.docx` | **nessuna** |
| `budget_2026_vs_consuntivo_per_linea.xlsx` | **nessuna** |
| `calcolo_CapEx_linea3_bakery_nuova.csv` | **nessuna** |
| `calcolo_sfrido_efficienza_OEE_linea_bakery.csv` | area-produzione, fatto-fermo-pkm-450-l26130, kpi-oee-l26130-l1-t2, questione-pezzi-prodotti-l26130, questione-scarti-riavvio-l26130, questione-velocita-nominali-linee |
| `capitolato_tecnico_fornitura_imballaggi_plastici.txt` | **nessuna** |
| `certificato_analisi_lotto_farina_MV26_0429A.pdf` | questione-consegna-farina-mv26-0429a, questione-tmc-farina-mv26-0429a, lotto-mv26-0429a |
| `checklist_metal_detector_manuale_operaio.txt` | fatto-allarme-acustico-md-3200-basso, fatto-giro-di-vite-seconde-firme-ccp3, fatto-muffe-l26128-45-giorni, fatto-operatori-ccp3-linea1-maggio, questione-linea1-domenica-10-05-fuori-piano, questione-tassello-inox-non-passato, questione-verifiche-ccp3-10-05-tre-versioni, doc-mod-qa-07, entita-ionut-popescu, macchina-md-3200, concetto-ccp, kpi-produzione-0450-linea1-maggio, kpi-seconde-firme-ccp3-maggio, questione-velocita-nominali-linee |
| `comunicazione_chiusura_estiva_2026.txt` | **nessuna** |
| `consumi_energetici_forni_kwh_maggio26.csv` | **nessuna** |
| `contestazione_logistica_Tosano_ritardo_Cerea.txt` | **nessuna** |
| `contestazione_sindacale_straordinari_Tosano.txt` | **nessuna** |
| `contratto_fornitura_MolinoVeneto_2026_firmato.pdf` | **nessuna** |
| `contratto_manutenzione_impianto_frigo_TS01.docx` | **nessuna** |
| `corso_inglese_aziendale_proposta.txt` | **nessuna** |
| `cruscotto_KPI_qualita_2026.xlsx` | **nessuna** |
| `doc 2 (1).pdf` | **nessuna** |
| `elenco_attrezzature_taratura_strumenti_2026.csv` | **nessuna** |
| `elenco_chiavi_e_accessi.txt` | **nessuna** |
| `elenco_interni_telefonici.txt` | **nessuna** |
| `email_HR_dimissioni_operai_linea2.txt` | **nessuna** |
| `estratto_conto_unicredit_maggio26.csv` | **nessuna** |
| `estratto_registro_carico_scarico_MOCA.xlsx` | **nessuna** |
| `fattura_antivirus_licenze_2026.txt` | **nessuna** |
| `formazione_allergeni_operatori_2026.pptx` | **nessuna** |
| `img20260428_09241055.txt` | **nessuna** |
| `inventario_magazzino_scadenze_FEFO_maggio.csv` | area-logistica, questione-consegna-farina-mv26-0429a, questione-tmc-farina-mv26-0429a, lotto-mv26-0429a, concetto-fefo |
| `iscritti_cena_aziendale_dicembre.csv` | **nessuna** |
| `job_description_responsabile_produzione.docx` | **nessuna** |
| `lettera_risposta_Tosano_reclamo_BOZZA_v3.docx` | bozza-lettera-tosano-reclamo |
| `libro_unico_lavoro_estratto_maggio2026.xlsx` | **nessuna** |
| `lista_contatti_buyer_GDO_nordest.csv` | **nessuna** |
| `listino prezzi GDO v2 VECCHIO non usare.csv` | **nessuna** |
| `listino_prezzi_canale_GDO_fresco_v3.csv` | **nessuna** |
| `log_allarmi_cella_frigo_surgelati_aprile.log` | **nessuna** |
| `log_lavaggio_CIP_linea1_maggio.log` | **nessuna** |
| `log_temperature_pastorizzatore_linea1_10_05_26.log` | fatto-deviazione-ccp2-l26130, fatto-riepilogo-datalogger-inaffidabile, fatto-risalita-termica-post-riavvio-l26130, questione-durata-deviazione-ccp2-l26130, macchina-pt-104 |
| `log_timbrature_fabbrica_maggio_settimana2.csv` | **nessuna** |
| `mail_fornitore_ingrediente_nuovo_paprika_specifiche.txt` | **nessuna** |
| `mail_titolare_Aurora_visione_aziendale_5anni.txt` | **nessuna** |
| `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` | area-qualita, fatto-deviazione-ccp2-l26130, fatto-registro-cartaceo-mod-qa-12, fatto-verifiche-ccp3-turno-l26130, doc-ccp2-limite-critico, doc-manuale-haccp, entita-elena-marchetti, lotto-l26130, macchina-pt-104 |
| `manuale_uso_manutenzione_PKM450_estratto.pdf` | fatto-avvertenza-costruttore-guarnizioni-non-originali, fatto-guarnizione-pkm-450-manutenzione-scaduta, fatto-ricambi-fuori-area-produzione-manuale-pkm, questione-codice-allarme-pkm-450, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-pakmatic, concetto-atmosfera-protettiva |
| `manutenzione_fotocopiatrice_contratto_copie.csv` | **nessuna** |
| `menu_mensa_aprile_maggio.txt` | **nessuna** |
| `modulo richiesta ferie VUOTO da stampare.txt` | **nessuna** |
| `noleggio_distributori_automatici_contratto.txt` | **nessuna** |
| `non_conformita_interne_registro_2026.csv` | fatto-decisione-proseguire-valvola-08-05, fatto-deviazione-ccp2-l26130, fatto-fermo-pkm-450-l26130, fatto-nc-102-origine-interna, fatto-registro-cartaceo-mod-qa-12, fatto-riparazione-guarnizione-non-originale, questione-durata-deviazione-ccp2-l26130, entita-ivano-dal-maso, concetto-fefo, questione-limite-o2-residuo |
| `nota_commercialista_credito_imposta_beni_strumentali.docx` | **nessuna** |
| `nota_infortunio_INAIL_operaio_linea3.txt` | **nessuna** |
| `nota_spese_trasferte_Zampieri_aprile.csv` | **nessuna** |
| `notifica_ATS_ispezione_programmata_igiene.txt` | **nessuna** |
| `ordine cancelleria marzo.txt` | **nessuna** |
| `ordine_DPI_scarpe_antinfortunistiche.csv` | **nessuna** |
| `ordini_acquisto_materie_prime_aperti_giugno.csv` | **nessuna** |
| `organigramma_aziendale_aggiornato_marzo26.pptx` | **nessuna** |
| `panel_test_assaggio_interno_cornetto_premium.csv` | **nessuna** |
| `piano_autocontrollo_acqua_potabile_analisi.csv` | **nessuna** |
| `piano_produzione_settimanale_sett19_21.xlsx` | fatto-operatori-ccp3-linea1-maggio, fatto-piano-produzione-sett19-21, questione-linea1-domenica-10-05-fuori-piano, macchina-linea-1, questione-velocita-nominali-linee |
| `piano_turni_apprendisti_tecnologi_food.txt` | **nessuna** |
| `politica_qualita_e_sicurezza_alimentare_2026.docx` | **nessuna** |
| `polizza_RC_prodotto_rinnovo_2026_OCR.txt` | **nessuna** |
| `prenotazioni_sala_riunioni_maggio.csv` | **nessuna** |
| `presentazione_commerciale_Aurora_GDO_2026.pptx` | **nessuna** |
| `preventivo_Criotech_tunnel_CR-SP180_rev2.pdf` | **nessuna** |
| `preventivo_software_ERP_CSB_System_vs_SAP.txt` | **nessuna** |
| `preventivo_tinteggiatura_uffici_NON_ACCETTATO.txt` | **nessuna** |
| `previsionale cassa giugno-agosto DEF (2).xlsx` | **nessuna** |
| `previsionale_cassa_giugno_agosto2026.xlsx` | **nessuna** |
| `procedura_ritiro_prodotto_CRISI_GDO.txt` | **nessuna** |
| `proiezione_ARR_contratti_GDO_2026_2027.csv` | **nessuna** |
| `registro_carico_scarico_rifiuti_estratto_2026.pdf` | **nessuna** |
| `registro_estintori_scadenze.csv` | **nessuna** |
| `registro_presenze_corsi_HACCP_scaduti.csv` | **nessuna** |
| `registro_tamponi_superfici_listeria_salmonella.csv` | **nessuna** |
| `reperibilita_gennaio_febbraio_2026.csv` | **nessuna** |
| `report_costi_fissi_OpEx_manutenzioni.txt` | **nessuna** |
| `report_fermo_macchina_confezionatrice_MAP.txt` | area-manutenzione, fatto-decisione-proseguire-valvola-08-05, fatto-fermo-pkm-450-l26130, fatto-guarnizione-pkm-450-manutenzione-scaduta, fatto-riparazione-guarnizione-non-originale, questione-arrivo-officina-fermo-pkm-450, questione-codice-allarme-pkm-450, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-elena-marchetti, entita-ivano-dal-maso, macchina-pkm-450, kpi-oee-l26130-l1-t2, questione-scarti-riavvio-l26130 |
| `reso_pallet_EPAL_conteggio_Tosano.txt` | **nessuna** |
| `ricetta_base_esperimento_snack_salato_v12.txt` | **nessuna** |
| `richiesta_campionatura_fiera_Cibus_2026.csv` | **nessuna** |
| `scadenzario_effetti_RIBA_giugno26.csv` | **nessuna** |
| `scheda_allergeni_matrice_cross_contamination.docx` | **nessuna** |
| `scheda_manutenzione_ordinaria_forni_industrial.csv` | fatto-convalida-md-1800-scaduta, fatto-fermo-forno-ft-01-05-05, fatto-guarnizione-pkm-450-manutenzione-scaduta, fatto-manutenzioni-rimandate-per-promo, fatto-ricambi-fuori-area-produzione-manuale-pkm, fatto-riepilogo-manutenzione-non-quadra, fatto-sonde-pt-104-in-taratura, fatto-valvola-modulante-pt-104-revisione-rimandata, questione-codice-ricambio-valvola-pkm-450, questione-materiale-guarnizione-pkm-450, entita-pakmatic, macchina-ft-01, macchina-md-3200, kpi-manutenzioni-arretrate-2026 |
| `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt` | **nessuna** |
| `scheda_tecnica_farina_tipo_0_MolinoVeneto.txt` | **nessuna** |
| `segnalazione_guasto_cancello_carraio.txt` | **nessuna** |
| `segnalazione_qualita_cliente_privato_corpo_estraneo.txt` | **nessuna** |
| `tariffe_vettori_terzi_trasporto_fresco_2026.csv` | **nessuna** |
| `test_shelf_life_accelerata_confezione_MAP_snack.csv` | fatto-microperdite-saldatura-l26130, fatto-muffe-l26128-45-giorni, fatto-repliche-shelf-life-l26130-divergenti, concetto-shelf-life, kpi-shelf-life-af-sn-0450, questione-aw-umidita-af-sn-0450, questione-limite-o2-residuo |
| `tracciabilita_lotti_massbalance_L26130.xlsx` | questione-consegna-farina-mv26-0429a, questione-tmc-farina-mv26-0429a, fatto-blocco-cautelativo-lotti, entita-tosano-cerea, lotto-l26130, lotto-mv26-0429a, prodotto-af-sn-0450, kpi-mass-balance-l26130, questione-pezzi-prodotti-l26130 |
| `trascrizione_riunione_direzione_12_05_2026.txt` | area-direzione, fatto-deviazione-ccp2-l26130, fatto-registro-cartaceo-mod-qa-12, fatto-riunione-direzione-reclamo-l26130, questione-data-riunione-direzione, questione-materiale-guarnizione-pkm-450, fatto-blocco-cautelativo-lotti, questione-data-apertura-rec-2026-011, entita-ionut-popescu |
| `vendor_rating_fornitori_2026.xlsx` | **nessuna** |
| `verbale_CDA_approvazione_investimento_tunnel.docx` | **nessuna** |
| `verbale_assemblea_condominio_capannone.txt` | **nessuna** |
| `verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt` | **nessuna** |
| `verbale_incontro_Mario_Rossi_Buyer_Tosano_05_05.txt` | **nessuna** |
| `verbale_riesame_direzione_SGQ_2026.txt` | **nessuna** |
| `verbale_scale_up_industriale_cornetto_premium.txt` | **nessuna** |
| `verifica_periodica_impianto_terra_DPR462.pdf` | **nessuna** |
| `visura_camerale_ordinaria_AuroraFoodGroup.pdf` | **nessuna** |
| `volantino_convenzione_palestra.txt` | **nessuna** |
| `~$ttera_risposta_Tosano_reclamo_BOZZA_v3.docx` | **nessuna** |