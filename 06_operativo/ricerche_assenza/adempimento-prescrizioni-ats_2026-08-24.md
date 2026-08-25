# Ricerca di assenza — `adempimento-prescrizioni-ats`

> **Che cos'è** · L'artefatto che E43 impone a chi dichiara un'assenza: la prova che
> la ricerca su tutto `sources\` è stata **eseguita**, con i termini e il perimetro
> che ha avuto. ⚠️ Non prova che l'assenza sia vera — nessuno script può — prova che
> il gesto è stato fatto.

| | |
|---|---|
| Eseguita il | **24/08/2026 alle 22:15:05** |
| Termini cercati | `evidenze di adempimento` · `adempimento prescrizione` · `ottemperanza` · `2026/SIAN/00214` |
| Perimetro | i **160** file del manifest `manifest_corpus_v1.1.json`, in `sources\` |
| File con testo estraibile | **155** |
| File senza testo estraibile | **5** — elencati sotto |
| Confronto | senza accenti, senza distinzione di maiuscole — **largo apposta** |
| Esito | **TROVATO: 4 occorrenze in 3 file — l'assenza NON si scrive** |

## I termini considerati e NON cercati, col perche'

> ⚠️ **Il perimetro di una ricerca è metà della prova.** Chi rilegge questo artefatto
> deve poter giudicare non solo che cosa è stato cercato, ma che cosa è stato
> **escluso** — ed è il punto che il caso `mS/cm` ha mostrato mancare: una ricerca
> sulla conducibilità che non cercava `mS/cm` lasciava fuori un intero tracciato.

⚠️ **Nessuno dichiarato.** Chi ha lanciato la ricerca non ha registrato quali
termini abbia considerato e scartato: l'artefatto prova che il gesto è stato
fatto, **non che il perimetro fosse quello giusto**.

## Dove è stato trovato

- `Verbale_ispezione_ATS_09_06_2026.pdf` — termine `evidenze di adempimento`
- `Verbale_ispezione_ATS_09_06_2026.pdf` — termine `2026/SIAN/00214`
- `procedura_ritiro_prodotto_CRISI_GDO.txt` — termine `ottemperanza`
- `verifica_periodica_impianto_terra_DPR462.pdf` — termine `ottemperanza`

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
