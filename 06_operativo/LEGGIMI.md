# 06_operativo — il quaderno di bordo del progetto

- `scaletta_end_to_end.md` — IL PIANO: le sessioni da qui alla pubblicazione, con
  stop-loss. È il primo file da riaprire dopo una pausa.
- `decision_log.md` — le decisioni prese, datate e motivate. Si aggiunge, non si riscrive.
- `manifest_corpus_v1.json` — il congelamento del corpus: hash SHA-256 dei 160 file.
  Ogni misura si dichiara vincolata a questo hash.
- `tassonomia_vault.png` — le 11 cartelle del vault, il riferimento visivo.
- `stato_canonizzazione.md` — lo stato del vault: cosa e' canonizzato e cosa resta.
- `stato_rag_produzione.md` — lo stato della pipeline C: cosa esiste, cosa e' congelato,
  cosa e' stato misurato. **Due linee di lavoro, due file di stato**: un fatto, un padrone.
- `rapporto_gate_s2.md` · `rapporto_gate_s3.md` — cosa e' stato portato al gate e con
  quale esito. Non si riscrivono dopo l'approvazione.
- `qa/` — gli script della suite di controlli delle note e i loro report per lotto.
- `prompt/` — i prompt pronti da incollare nelle sessioni di terminale, uno per file.
  Contiene anche `prompt_corpus_v2_espansione.txt` (RINVIATO: solo dopo il ciclo v1).

Modello di lavoro: la chat Cowork è il cervello (decisioni, piani, revisioni);
il terminale è le mani (ogni sessione si apre in una cartella precisa e incolla un
prompt preciso). Ogni sessione chiude con: stato aggiornato qui, voce nel decision log,
`passaggio_di_consegne_coordinatore.md` aggiornato, commit git e `git push`.
