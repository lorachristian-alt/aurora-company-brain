# Ricerca di assenza — `formazione-master-xlsx_2026-08-23`

> **Che cos'è** · L'artefatto che E43 impone a chi dichiara un'assenza: la prova che
> la ricerca su tutto `sources\` è stata **eseguita**, con i termini e il perimetro
> che ha avuto. ⚠️ Non prova che l'assenza sia vera — nessuno script può — prova che
> il gesto è stato fatto.

| | |
|---|---|
| Eseguita il | **23/08/2026 alle 17:02:05** |
| Termini cercati | `formazione_master` · `formazione master` · `MOD-HR-11 registro presenze` |
| Perimetro | i **160** file del manifest `manifest_corpus_v1.1.json`, in `sources\` |
| File con testo estraibile | **155** |
| File senza testo estraibile | **5** — elencati sotto |
| Confronto | senza accenti, senza distinzione di maiuscole — **largo apposta** |
| Esito | **TROVATO: 1 occorrenze in 1 file — l'assenza NON si scrive** |

Dichiarata nella nota `doc-scadenzario-formazione-2026`.

## I termini considerati e NON cercati, col perche'

> ⚠️ **Il perimetro di una ricerca è metà della prova.** Chi rilegge questo artefatto
> deve poter giudicare non solo che cosa è stato cercato, ma che cosa è stato
> **escluso** — ed è il punto che il caso `mS/cm` ha mostrato mancare: una ricerca
> sulla conducibilità che non cercava `mS/cm` lasciava fuori un intero tracciato.

- `formazione` — compare in decine di grezzi
- `master` — parola comune

## Dove è stato trovato

- `registro_presenze_corsi_HACCP_scaduti.csv` — termine `formazione_master`

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
