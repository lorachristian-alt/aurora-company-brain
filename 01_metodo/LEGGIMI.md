# 01_metodo — i documenti che governano il progetto

Qui vive il METODO: la teoria e le regole. L'ordine di lettura è la numerazione.

- `metodo_01_generazione_archivio.md` — come è stato costruito l'archivio simulato
  (e come replicarlo su un'altra azienda).
- `metodo_02_misurazione.md` — come si misura, con le configurazioni congelate e il
  verbale della baseline del 14/08/2026.
- `metodo_03_canonizzazione.md` — il manuale della trasformazione dei grezzi in note
  atomiche collegate: spareggio fra le 11 cartelle, metabolismo delle note, frontmatter,
  i sei template, naming e link, «un fatto un padrone», entity resolution, suite QA,
  derivati, processo a lotti. Scritto e approvato in Sessione 1 (16/08/2026).
  - `alias_entita.md` — suo allegato: la tabella alias dell'entity resolution
    (classe A si uniscono · B mai · C questione aperta). **Cresce a ogni lotto.**
- `metodo_04_rag_produzione.md` — la pipeline RAG di produzione (configurazione C):
  architettura, costruzione passo-passo, manutenzione.
- `canone_aurora.md` — la chiave di lettura della simulazione: l'arbitro di ogni dato.
- `tassonomia_vault.md` — le 11 cartelle del vault: etichette, criteri estesi e
  regole trasversali. Riferimento per le regole di spareggio di metodo_03.

Gerarchia: il metodo_01 è il sorgente; misurazione e canonizzazione ne discendono.
Una regola si cambia nel sorgente e si rigenera il derivato, mai il contrario.
Per le cartelle del vault il padrone è `tassonomia_vault.md`: dice COSA va dove,
metodo_03 decide QUANDO due cartelle se lo contendono.
