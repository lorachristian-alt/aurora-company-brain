# Suite QA delle note — report unico

- Data: 2026-08-19
- Perimetro: **lotto** (lotto `1b`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 16 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 71 |
| `projects\` | 8 |
| `docs\` | 7 |
| `entities\` | 19 |
| `concepts\` | 5 |
| `data\` | 20 |
| `outputs\` | 1 |
| `code\` | 7 |
| `workspace\` | 5 |
| `sources\` | 1 |
| **totale** | **145** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **139** note.*

| `type` | Note |
|---|---|
| `atomica` | 78 |
| `concetto` | 4 |
| `conflitto` | 24 |
| `entita` | 15 |
| `hub` | 11 |
| `index` | 11 |
| `sessione` | 2 |

---
## qa_frontmatter (perimetro: lotto, 48 note)

- ERRORI: **0**
- AVVISI: **9**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-allarmi-alta-temperatura-cf-02-aprile.md` |  | frontmatter | corpo di 346 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-anomalia-consumo-cf-02-maggio.md` |  | frontmatter | corpo di 348 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-assistenza-esterna-24-04-cf-02.md` |  | frontmatter | corpo di 341 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-cariche-f-gas-impianti-frigoriferi.md` |  | frontmatter | corpo di 327 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-integrita-log-allarmi-cf-02.md` |  | frontmatter | corpo di 311 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-obblighi-registro-f-gas.md` |  | frontmatter | corpo di 341 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-quadratura-consumi-energetici-maggio.md` |  | frontmatter | corpo di 334 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-temperatura-uscita-tunnel-ts-01-aprile.md` |  | frontmatter | corpo di 320 parole: fra 301 e 350, si motiva o si spezza |
| `bozza-contratto-manutenzione-frigo.md` |  | frontmatter | corpo di 346 parole: fra 301 e 350, si motiva o si spezza |


## qa_link_integrity (perimetro: lotto, 145 note nel vault)

- ERRORI: **0**
- AVVISI: **3**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-assistenza-esterna-24-04-cf-02.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `fatto-blackout-21-04-riavvio-centraline.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `fatto-sonda-prodotto-cf-02-in-avaria.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |


## qa_provenance (perimetro: lotto, 48 note)

- ERRORI: **0**
- AVVISI: **4**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-cariche-f-gas-impianti-frigoriferi.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-contatori-reparto-meta-stabilimento.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-integrita-log-allarmi-cf-02.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `entita-frigotecnica-berica.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 48 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### amministrazione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-amministrazione.md` | hub | aperto | 2 |
| `entita-veneta-energia.md` | entita | risolto | 2 |
| `fatto-contatori-reparto-meta-stabilimento.md` | atomica | aperto | 2 |
| `kpi-consumi-energia-maggio-2026.md` | atomica | risolto | 2 |
| `kpi-fattura-energia-maggio-2026.md` | atomica | risolto | 1 |
| `kpi-incremento-energia-maggio-su-aprile.md` | atomica | aperto | 1 |
| `kpi-metano-forni-maggio-2026.md` | atomica | aperto | 2 |
| `kpi-quadratura-consumi-energetici-maggio.md` | atomica | risolto | 1 |
| `questione-costo-energia-elettrica.md` | conflitto | aperto | 2 |

### manutenzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `bozza-contratto-manutenzione-frigo.md` | atomica | aperto | 1 |
| `entita-frigotecnica-berica.md` | entita | aperto | 2 |
| `fatto-anomalia-consumo-cf-02-maggio.md` | atomica | aperto | 4 |
| `fatto-assistenza-esterna-24-04-cf-02.md` | atomica | aperto | 3 |
| `fatto-blackout-21-04-riavvio-centraline.md` | atomica | risolto | 1 |
| `fatto-cariche-f-gas-impianti-frigoriferi.md` | atomica | aperto | 2 |
| `fatto-energia-reattiva-oltre-soglia.md` | atomica | aperto | 1 |
| `fatto-obblighi-registro-f-gas.md` | atomica | aperto | 2 |
| `fatto-potenza-impegnata-quasi-satura.md` | atomica | aperto | 1 |
| `fatto-preventivo-potenza-630-kw-tunnel.md` | atomica | aperto | 1 |
| `fatto-sonda-prodotto-cf-02-in-avaria.md` | atomica | risolto | 1 |
| `fatto-ts-01-fine-vita-dismissione.md` | atomica | aperto | 3 |
| `kpi-sbrinamenti-cf-02-aprile.md` | atomica | aperto | 1 |
| `macchina-cf-01.md` | entita | aperto | 4 |
| `macchina-cf-02.md` | hub | aperto | 2 |
| `macchina-ts-01.md` | entita | aperto | 3 |
| `questione-manutentore-frigo-berica-scaligera.md` | conflitto | aperto | 2 |
| `questione-nc-067-sbrinamenti-tunnel.md` | conflitto | aperto | 3 |
| `questione-refrigerante-ts-01.md` | conflitto | aperto | 2 |
| `questione-sbrinamenti-fascia-notturna-cf-02.md` | conflitto | aperto | 2 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `fatto-forni-in-temperatura-durante-fermo-10-05.md` | atomica | risolto | 2 |
| `fatto-tre-domeniche-produttive-in-fascia-f3.md` | atomica | aperto | 1 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `fatto-allarmi-alta-temperatura-cf-02-aprile.md` | atomica | aperto | 2 |
| `fatto-integrita-log-allarmi-cf-02.md` | atomica | aperto | 1 |
| `fatto-nessuna-nc-per-allarmi-cf-02.md` | atomica | aperto | 2 |
| `fatto-porta-cella-cf-02-aperta-38-minuti.md` | atomica | aperto | 2 |
| `kpi-temperatura-uscita-tunnel-ts-01-aprile.md` | atomica | risolto | 3 |
| `questione-limite-allarme-porta-cf-02.md` | conflitto | aperto | 2 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `bolletta_VenetaEnergia_maggio2026.pdf` | area-amministrazione, fatto-anomalia-consumo-cf-02-maggio, fatto-contatori-reparto-meta-stabilimento, fatto-energia-reattiva-oltre-soglia, fatto-potenza-impegnata-quasi-satura, fatto-preventivo-potenza-630-kw-tunnel, fatto-tre-domeniche-produttive-in-fascia-f3, entita-veneta-energia, kpi-consumi-energia-maggio-2026, kpi-fattura-energia-maggio-2026, kpi-incremento-energia-maggio-su-aprile, kpi-metano-forni-maggio-2026, questione-costo-energia-elettrica |
| `consumi_energetici_forni_kwh_maggio26.csv` | area-amministrazione, fatto-anomalia-consumo-cf-02-maggio, fatto-contatori-reparto-meta-stabilimento, fatto-forni-in-temperatura-durante-fermo-10-05, entita-veneta-energia, macchina-cf-01, kpi-consumi-energia-maggio-2026, kpi-metano-forni-maggio-2026, kpi-quadratura-consumi-energetici-maggio, questione-costo-energia-elettrica |
| `contratto_manutenzione_impianto_frigo_TS01.docx` | fatto-assistenza-esterna-24-04-cf-02, fatto-cariche-f-gas-impianti-frigoriferi, fatto-obblighi-registro-f-gas, fatto-ts-01-fine-vita-dismissione, questione-manutentore-frigo-berica-scaligera, questione-refrigerante-ts-01, entita-frigotecnica-berica, macchina-cf-01, macchina-cf-02, macchina-ts-01, bozza-contratto-manutenzione-frigo |
| `log_allarmi_cella_frigo_surgelati_aprile.log` | fatto-allarmi-alta-temperatura-cf-02-aprile, fatto-anomalia-consumo-cf-02-maggio, fatto-assistenza-esterna-24-04-cf-02, fatto-blackout-21-04-riavvio-centraline, fatto-integrita-log-allarmi-cf-02, fatto-nessuna-nc-per-allarmi-cf-02, fatto-porta-cella-cf-02-aperta-38-minuti, fatto-sonda-prodotto-cf-02-in-avaria, questione-limite-allarme-porta-cf-02, questione-nc-067-sbrinamenti-tunnel, questione-sbrinamenti-fascia-notturna-cf-02, entita-frigotecnica-berica, macchina-cf-02, macchina-ts-01, kpi-sbrinamenti-cf-02-aprile, kpi-temperatura-uscita-tunnel-ts-01-aprile |