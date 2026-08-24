# Ricerca di assenza — `cadenza-trimestrale-haccp`

> **Che cos'è** · L'artefatto che E43 impone a chi dichiara un'assenza: la prova che
> la ricerca su tutto `sources\` è stata **eseguita**, con i termini e il perimetro
> che ha avuto. ⚠️ Non prova che l'assenza sia vera — nessuno script può — prova che
> il gesto è stato fatto.

| | |
|---|---|
| Eseguita il | **24/08/2026 alle 13:15:36** |
| Termini cercati | `trimestral` |
| Perimetro | i **160** file del manifest `manifest_corpus_v1.1.json`, in `sources\` |
| File con testo estraibile | **155** |
| File senza testo estraibile | **5** — elencati sotto |
| Confronto | senza accenti, senza distinzione di maiuscole — **largo apposta** |
| Esito | **TROVATO: 22 occorrenze in 22 file — l'assenza NON si scrive** |

Dichiarata nella nota `questione-riesame-trimestrale-haccp`.

## I termini considerati e NON cercati, col perche'

> ⚠️ **Il perimetro di una ricerca è metà della prova.** Chi rilegge questo artefatto
> deve poter giudicare non solo che cosa è stato cercato, ma che cosa è stato
> **escluso** — ed è il punto che il caso `mS/cm` ha mostrato mancare: una ricerca
> sulla conducibilità che non cercava `mS/cm` lasciava fuori un intero tracciato.

- `riesame trimestrale` — e' la locuzione della sola mail: cercarla intera troverebbe solo la fonte che la scrive
- `ogni tre mesi` — perifrasi cercata a parte, sotto

## Dove è stato trovato

- `AUA_autorizzazione_unica_ambientale_scarichi.pdf` — termine `trimestral`
- `Comunicazione_aumento_listino_farine_indicizzazione.eml` — termine `trimestral`
- `Fwd_Fwd_Fwd_ATTENZIONE_richiamo_prodotto_concorrente_RASFF.eml` — termine `trimestral`
- `PRO-QA-08_gestione_reclami_cliente_rev2.docx` — termine `trimestral`
- `accordo_quadro_private_label_Tosano_2026_firmato.txt` — termine `trimestral`
- `analisi_acque_reflue_autocontrollo_2026.xlsx` — termine `trimestral`
- `analisi_scostamenti_costo_materie_prime.xlsx` — termine `trimestral`
- `bolletta_VenetaEnergia_maggio2026.pdf` — termine `trimestral`
- `bozza_presentazione_nuova_linea_snack_CDA.pptx` — termine `trimestral`
- `capitolato_tecnico_fornitura_imballaggi_plastici.txt` — termine `trimestral`
- `contratto_fornitura_MolinoVeneto_2026_firmato.pdf` — termine `trimestral`
- `contratto_manutenzione_impianto_frigo_TS01.docx` — termine `trimestral`
- `elenco_attrezzature_taratura_strumenti_2026.csv` — termine `trimestral`
- `job_description_responsabile_produzione.docx` — termine `trimestral`
- `manutenzione_fotocopiatrice_contratto_copie.csv` — termine `trimestral`
- `piano_autocontrollo_acqua_potabile_analisi.csv` — termine `trimestral`
- `preventivo_software_ERP_CSB_System_vs_SAP.txt` — termine `trimestral`
- `registro_carico_scarico_rifiuti_estratto_2026.pdf` — termine `trimestral`
- `report_costi_fissi_OpEx_manutenzioni.txt` — termine `trimestral`
- `scheda_allergeni_matrice_cross_contamination.docx` — termine `trimestral`
- `tariffe_vettori_terzi_trasporto_fresco_2026.csv` — termine `trimestral`
- `verbale_CDA_approvazione_investimento_tunnel.docx` — termine `trimestral`

## I file su cui la ricerca è cieca, e va detto

L'estrattore congelato non ha un ramo per le immagini e restituisce stringa vuota:
su questi file la ricerca **non ha guardato**, e chi legge l'artefatto deve saperlo.

- `IMG-20260510-WA0007.jpg` — nessun testo estraibile (immagine o file muto)
- `IMG_20260514_152241_frammento_REC-2026-011.jpg` — nessun testo estraibile (immagine o file muto)
- `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` — nessun testo estraibile (immagine o file muto)
- `SKM_C224e26050408520.jpg` — nessun testo estraibile (immagine o file muto)
- `~$ttera_risposta_Tosano_reclamo_BOZZA_v3.docx` — nessun testo estraibile (immagine o file muto)

---

Prodotto da `06_operativo\cerca_assenza.py`. Non si scrive a mano: si rilancia.
