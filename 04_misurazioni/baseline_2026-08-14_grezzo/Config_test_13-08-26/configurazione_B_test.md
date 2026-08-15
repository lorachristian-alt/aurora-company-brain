\*\*Configurazione B — RAG a embedding\*\*



| Parametro | Valore fisso |

|---|---|

| Modello di embedding | `BAAI/bge-m3`, in locale |

| Perché locale | un modello via API può essere aggiornato o deprecato sotto i piedi: il confronto sopravvive solo se il modello è congelato su disco |

| Estrazione testo | la funzione `text\_of` del blueprint §5-bis, identica |

| Chunking | 1.200 caratteri, overlap 200, taglio su \*\*confine di riga\*\* |

| Perché sulla riga | l'archivio è pieno di tabelle e registri: spezzare a metà riga distrugge il record |

| Vector store | Chroma o FAISS in locale, persistito su disco |

| Similarità | coseno |

| `top\_k` | 8 |

| Re-ranking | \*\*nessuno\*\* (aggiungerlo è una seconda variabile) |

| Modello che scrive la risposta | lo stesso della configurazione A, temperatura 0 |

| Metadato per chunk | nome del file di origine, obbligatorio |



Il modello che scrive è lo stesso nelle due configurazioni \*\*apposta\*\*: così la differenza

fra A e B misura il recupero, non la scrittura.

