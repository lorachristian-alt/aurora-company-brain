\*\*Configurazione A — retrieval agentico\*\*



| Parametro | Valore fisso |

|---|---|

| Sistema | Claude Code, sessione nuova, nessuna memoria del progetto |

| Modello | `claude-opus-5` — annotalo: se un giorno cambi modello, il confronto riparte da zero |

| Fast mode | \*\*off\*\* |

| Strumenti concessi | `Read`, `Grep`, `Glob`, `Write` (solo sul file di output) |

| Strumenti negati | `Bash`, `Edit`, `WebSearch`, `WebFetch`, `Agent` |

| Working directory | la radice del vault |

| Perimetro in lettura | `sources/` |

| Blocco di lavoro | 30 domande per volta |



