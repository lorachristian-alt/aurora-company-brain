# Ricerca di assenza — `pro-qa-11-e-pro-qa-14-messe-in-relazione`

> **Che cos'è** · L'artefatto che E43 impone a chi dichiara un'assenza: la prova che
> la ricerca su tutto `sources\` è stata **eseguita**, con i termini e il perimetro
> che ha avuto. ⚠️ Non prova che l'assenza sia vera — nessuno script può — prova che
> il gesto è stato fatto.

| | |
|---|---|
| Eseguita il | **24/08/2026 alle 13:16:36** |
| Termini cercati | `PRO-QA-11` · `PRO-QA-14` |
| Perimetro | i **160** file del manifest `manifest_corpus_v1.1.json`, in `sources\` |
| File con testo estraibile | **155** |
| File senza testo estraibile | **5** — elencati sotto |
| Confronto | senza accenti, senza distinzione di maiuscole — **largo apposta** |
| Esito | **TROVATO: 6 occorrenze in 6 file — l'assenza NON si scrive** |

Dichiarata nella nota `questione-due-codici-per-la-procedura-di-ritiro`.

## I termini considerati e NON cercati, col perche'

> ⚠️ **Il perimetro di una ricerca è metà della prova.** Chi rilegge questo artefatto
> deve poter giudicare non solo che cosa è stato cercato, ma che cosa è stato
> **escluso** — ed è il punto che il caso `mS/cm` ha mostrato mancare: una ricerca
> sulla conducibilità che non cercava `mS/cm` lasciava fuori un intero tracciato.

- `ritiro e richiamo` — e' il titolo, non la sigla: troverebbe ogni documento che parla di ritiri

## Dove è stato trovato

- `MOD-QA-31_reclamo_REC-2026-011.pdf` — termine `PRO-QA-14`
- `PRO-QA-08_gestione_reclami_cliente_rev2.docx` — termine `PRO-QA-11`
- `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` — termine `PRO-QA-14`
- `non_conformita_interne_registro_2026.csv` — termine `PRO-QA-14`
- `organigramma_aziendale_aggiornato_marzo26.pptx` — termine `PRO-QA-14`
- `procedura_ritiro_prodotto_CRISI_GDO.txt` — termine `PRO-QA-14`

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
