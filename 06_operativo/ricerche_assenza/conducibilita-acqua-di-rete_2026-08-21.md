# Ricerca di assenza — `conducibilita-acqua-di-rete`

> **Che cos'è** · L'artefatto che E43 impone a chi dichiara un'assenza: la prova che
> la ricerca su tutto `sources\` è stata **eseguita**, con i termini e il perimetro
> che ha avuto. ⚠️ Non prova che l'assenza sia vera — nessuno script può — prova che
> il gesto è stato fatto.

| | |
|---|---|
| Eseguita il | **21/08/2026 alle 12:42:51** |
| Termini cercati | `conducibilit` · `conductivity` · `µS/cm` · `uS/cm` · `mS/cm` · `27888` |
| Perimetro | i **160** file del manifest `manifest_corpus_v1.1.json`, in `sources\` |
| File con testo estraibile | **155** |
| File senza testo estraibile | **5** — elencati sotto |
| Confronto | senza accenti, senza distinzione di maiuscole — **largo apposta** |
| Esito | **TROVATO: 10 occorrenze in 7 file — l'assenza NON si scrive** |

Dichiarata nella nota `kpi-conducibilita-acqua-per-punto`.

## I termini considerati e NON cercati, col perche'

> ⚠️ **Il perimetro di una ricerca è metà della prova.** Chi rilegge questo artefatto
> deve poter giudicare non solo che cosa è stato cercato, ma che cosa è stato
> **escluso** — ed è il punto che il caso `mS/cm` ha mostrato mancare: una ricerca
> sulla conducibilità che non cercava `mS/cm` lasciava fuori un intero tracciato.

- `COND` — il tag del log del CIP, ma come sottostringa matcha SECONDO, CONDIZIONI, CONDOTTA: provato il 21/08, restituisce 96 file su 155 e rende la ricerca inservibile
- `microsiemens` — forma estesa dell'unita', mai usata nei grezzi; il confronto senza accenti su «µS/cm» e «uS/cm» la copre
- `TDS` — sigla di una grandezza diversa (solidi disciolti), correlata ma non la stessa
- `salinita` — idem, grandezza diversa

## Dove è stato trovato

- `IO-05_istruzione_operativa_lavaggio_CIP.docx` — termine `conducibilit`
- `IO-05_istruzione_operativa_lavaggio_CIP.docx` — termine `µS/cm`
- `log_lavaggio_CIP_linea1_maggio.log` — termine `mS/cm`
- `non_conformita_interne_registro_2026.csv` — termine `conducibilit`
- `nota_commercialista_credito_imposta_beni_strumentali.docx` — termine `conducibilit`
- `piano_autocontrollo_acqua_potabile_analisi.csv` — termine `conducibilit`
- `piano_autocontrollo_acqua_potabile_analisi.csv` — termine `µS/cm`
- `piano_autocontrollo_acqua_potabile_analisi.csv` — termine `27888`
- `scheda_allergeni_matrice_cross_contamination.docx` — termine `conducibilit`
- `scheda_manutenzione_ordinaria_forni_industrial.csv` — termine `conducibilit`

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
