# Suite QA delle note — report unico

- Data: 2026-08-19
- Perimetro: **lotto** (lotto `l26130`)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 0 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro lotto · **0 ERRORI, 14 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 93 |
| `projects\` | 8 |
| `docs\` | 7 |
| `entities\` | 22 |
| `concepts\` | 5 |
| `data\` | 22 |
| `outputs\` | 1 |
| `code\` | 7 |
| `workspace\` | 6 |
| `sources\` | 1 |
| **totale** | **173** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **166** note.*

| `type` | Note |
|---|---|
| `atomica` | 93 |
| `concetto` | 4 |
| `conflitto` | 32 |
| `entita` | 18 |
| `hub` | 12 |
| `index` | 11 |
| `sessione` | 3 |

---
## qa_frontmatter (perimetro: lotto, 51 note)

- ERRORI: **0**
- AVVISI: **6**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-cariche-f-gas-impianti-frigoriferi.md` |  | frontmatter | corpo di 346 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-convalida-md-1800-scaduta.md` |  | frontmatter | corpo di 320 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-due-registri-paralleli-della-metrologia.md` |  | frontmatter | corpo di 335 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-sonde-pt-104-in-taratura.md` |  | frontmatter | corpo di 330 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-strumenti-cf-02-e-ccp4.md` |  | frontmatter | corpo di 333 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-strumenti-esclusi-da-taratura.md` |  | frontmatter | corpo di 348 parole: fra 301 e 350, si motiva o si spezza |


## qa_link_integrity (perimetro: lotto, 173 note nel vault)

- ERRORI: **0**
- AVVISI: **0**


## qa_provenance (perimetro: lotto, 51 note)

- ERRORI: **0**
- AVVISI: **8**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `area-logistica.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-cariche-f-gas-impianti-frigoriferi.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-due-elenchi-in-un-file-strumenti.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-convalida-md-1800-scaduta-o-valida.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-due-registri-tarature-pt-104.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-posizione-md-3200-in-linea.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-sigla-kit-tasselli-ccp3.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-tassello-inox-non-passato.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 51 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### logistica

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-logistica.md` | hub | aperto | 1 |
| `entita-nordgas.md` | entita | risolto | 3 |
| `fatto-fornitura-gas-nordgas-06-05.md` | atomica | risolto | 3 |
| `fatto-verifica-metrologia-legale-bilance.md` | atomica | aperto | 2 |
| `questione-azoto-quantita-e-livello-06-05.md` | conflitto | aperto | 3 |
| `questione-codici-lotto-azoto-06-05.md` | conflitto | aperto | 3 |

### manutenzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-manutenzione.md` | hub | aperto | 1 |
| `fatto-cariche-f-gas-impianti-frigoriferi.md` | atomica | aperto | 2 |
| `fatto-strumenti-esclusi-da-taratura.md` | atomica | aperto | 2 |
| `fatto-strumenti-map-azoto-pkm-450.md` | atomica | risolto | 2 |
| `macchina-cf-02.md` | hub | aperto | 2 |
| `macchina-pkm-450.md` | entita | risolto | 2 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-produzione.md` | hub | aperto | 1 |
| `fatto-azoto-due-vie-serbatoio-e-rampa.md` | atomica | risolto | 4 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 1 |
| `entita-calservice-italia.md` | entita | risolto | 1 |
| `entita-metrolab-taratura.md` | entita | risolto | 1 |
| `fatto-accettazione-con-riserva-gas-06-05.md` | atomica | risolto | 2 |
| `fatto-buchi-registro-strumenti.md` | atomica | aperto | 1 |
| `fatto-catena-riferibilita-tarature-interne.md` | atomica | risolto | 1 |
| `fatto-certificato-analisi-gas-alimentari.md` | atomica | aperto | 2 |
| `fatto-convalida-md-1800-scaduta.md` | atomica | aperto | 3 |
| `fatto-datalogger-dl-001-in-taratura.md` | atomica | risolto | 1 |
| `fatto-due-elenchi-in-un-file-strumenti.md` | atomica | risolto | 1 |
| `fatto-due-registri-paralleli-della-metrologia.md` | atomica | aperto | 3 |
| `fatto-sonde-pt-104-in-taratura.md` | atomica | risolto | 1 |
| `fatto-strumenti-cf-02-e-ccp4.md` | atomica | risolto | 2 |
| `fatto-strumenti-taratura-scaduta-in-uso.md` | atomica | aperto | 3 |
| `fatto-tassello-aisi-clip-rotta.md` | atomica | risolto | 2 |
| `kpi-parco-strumenti-taratura-2026.md` | hub | aperto | 1 |
| `lotto-l26130.md` | hub | aperto | 2 |
| `macchina-md-3200.md` | entita | risolto | 6 |
| `macchina-pt-104.md` | entita | risolto | 2 |
| `questione-convalida-md-1800-scaduta-o-valida.md` | conflitto | aperto | 3 |
| `questione-convalida-md-3200-due-registri.md` | conflitto | aperto | 3 |
| `questione-due-registri-tarature-pt-104.md` | conflitto | aperto | 3 |
| `questione-posizione-md-3200-in-linea.md` | conflitto | aperto | 4 |
| `questione-sigla-kit-tasselli-ccp3.md` | conflitto | aperto | 4 |
| `questione-taratura-termoregistratore-cf-02.md` | conflitto | aperto | 3 |
| `questione-tassello-inox-non-passato.md` | conflitto | aperto | 2 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|
| `bolla_ingresso_azoto_alimentare_Nordgas_OCR.txt` | fatto-accettazione-con-riserva-gas-06-05, fatto-azoto-due-vie-serbatoio-e-rampa, fatto-certificato-analisi-gas-alimentari, fatto-fornitura-gas-nordgas-06-05, questione-codici-lotto-azoto-06-05, entita-nordgas, questione-azoto-quantita-e-livello-06-05 |
| `elenco_attrezzature_taratura_strumenti_2026.csv` | fatto-buchi-registro-strumenti, fatto-catena-riferibilita-tarature-interne, fatto-convalida-md-1800-scaduta, fatto-datalogger-dl-001-in-taratura, fatto-due-elenchi-in-un-file-strumenti, fatto-due-registri-paralleli-della-metrologia, fatto-strumenti-cf-02-e-ccp4, fatto-strumenti-esclusi-da-taratura, fatto-strumenti-map-azoto-pkm-450, fatto-strumenti-taratura-scaduta-in-uso, fatto-tassello-aisi-clip-rotta, fatto-verifica-metrologia-legale-bilance, questione-convalida-md-1800-scaduta-o-valida, questione-convalida-md-3200-due-registri, questione-due-registri-tarature-pt-104, questione-posizione-md-3200-in-linea, questione-sigla-kit-tasselli-ccp3, questione-taratura-termoregistratore-cf-02, entita-calservice-italia, entita-metrolab-taratura, macchina-md-3200, kpi-parco-strumenti-taratura-2026 |