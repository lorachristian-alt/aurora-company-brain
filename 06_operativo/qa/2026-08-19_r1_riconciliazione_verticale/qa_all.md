# Suite QA delle note — report unico

- Data: 2026-08-19
- Perimetro: **lotto** (lotto `r1_riconciliazione_verticale`) — **perimetro di manutenzione: 0 grezzi, 85 note** (E35)
- Vault: `C:\Users\buulo\Desktop\aurora-cervello`

| Controllo | Codice di uscita |
|---|---|
| `qa_frontmatter.py` | 2 |
| `qa_link_integrity.py` | 2 |
| `qa_provenance.py` | 2 |
| `qa_copertura.py` | 0 |

## Riga di riepilogo per lo stato di sessione

> suite QA · perimetro manutenzione (0 grezzi, 85 note) · **0 ERRORI, 51 AVVISI** · esito **GIALLO**

---

## Inventario delle note

| Cartella | Note |
|---|---|
| `self\` | 1 |
| `areas\` | 96 |
| `projects\` | 8 |
| `docs\` | 9 |
| `entities\` | 22 |
| `concepts\` | 5 |
| `data\` | 22 |
| `outputs\` | 1 |
| `code\` | 11 |
| `workspace\` | 7 |
| `sources\` | 1 |
| **totale** | **183** |

*Escluse `workspace\` e `sources\` dai conteggi di qualità: **175** note.*

| `type` | Note |
|---|---|
| `atomica` | 100 |
| `concetto` | 4 |
| `conflitto` | 34 |
| `entita` | 18 |
| `hub` | 12 |
| `index` | 11 |
| `sessione` | 4 |

---
## qa_frontmatter (perimetro: lotto, 93 note)

- ERRORI: **0**
- AVVISI: **29**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-accettazione-con-riserva-gas-06-05.md` |  | frontmatter | corpo di 344 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-allarme-acustico-md-3200-basso.md` |  | frontmatter | corpo di 319 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-datalogger-dl-001-in-taratura.md` |  | frontmatter | corpo di 345 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-decisione-proseguire-valvola-08-05.md` |  | frontmatter | corpo di 350 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-fermo-forno-ft-01-05-05.md` |  | frontmatter | corpo di 343 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-fermo-pkm-450-l26130.md` |  | frontmatter | corpo di 330 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-integrita-log-allarmi-cf-02.md` |  | frontmatter | corpo di 311 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-microperdite-saldatura-l26130.md` |  | frontmatter | corpo di 328 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nc-102-origine-interna.md` |  | frontmatter | summary di 258 caratteri (tetto 250) |
| `fatto-nc-102-origine-interna.md` |  | frontmatter | corpo di 324 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-nessuna-nc-per-allarmi-cf-02.md` |  | frontmatter | corpo di 343 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-operatore-senza-formazione-haccp-l26130.md` |  | frontmatter | corpo di 332 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-operatori-ccp3-linea1-maggio.md` |  | frontmatter | corpo di 334 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` |  | frontmatter | corpo di 348 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-riepilogo-datalogger-inaffidabile.md` |  | frontmatter | corpo di 345 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-risalita-termica-post-riavvio-l26130.md` |  | frontmatter | corpo di 336 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-sonde-pt-104-in-taratura.md` |  | frontmatter | corpo di 342 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-strumenti-cf-02-e-ccp4.md` |  | frontmatter | corpo di 337 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-valvola-modulante-pt-104-revisione-rimandata.md` |  | frontmatter | corpo di 339 parole: fra 301 e 350, si motiva o si spezza |
| `questione-validazione-ccp2-mai-confermata.md` |  | frontmatter | corpo di 329 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-blocco-cautelativo-lotti.md` |  | frontmatter | corpo di 335 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-misura-frammento-rec-2026-011.md` |  | frontmatter | corpo di 326 parole: fra 301 e 350, si motiva o si spezza |
| `fatto-richiesta-relazione-48-ore.md` |  | frontmatter | corpo di 345 parole: fra 301 e 350, si motiva o si spezza |
| `doc-mod-qa-07.md` |  | frontmatter | corpo di 350 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-mass-balance-l26130.md` |  | frontmatter | corpo di 332 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-quadratura-consumi-energetici-maggio.md` |  | frontmatter | corpo di 334 parole: fra 301 e 350, si motiva o si spezza |
| `kpi-shelf-life-af-sn-0450.md` |  | frontmatter | corpo di 349 parole: fra 301 e 350, si motiva o si spezza |
| `script-candidate-r1.md` |  | frontmatter | corpo di 338 parole: fra 301 e 350, si motiva o si spezza |
| `script-fonti-prescrittive.md` |  | frontmatter | corpo di 340 parole: fra 301 e 350, si motiva o si spezza |


## qa_link_integrity (perimetro: lotto, 183 note nel vault)

- ERRORI: **0**
- AVVISI: **2**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `fatto-blackout-21-04-riavvio-centraline.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |
| `fatto-sonda-prodotto-cf-02-in-avaria.md` |  | link | lontana dall'_index della propria cartella (3 salti): indizio di cattiva collocazione |


## qa_provenance (perimetro: lotto, 93 note)

- ERRORI: **0**
- AVVISI: **20**

### Avvisi

| Nota | Riga | Controllo | Rilievo |
|---|---|---|---|
| `area-logistica.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-giro-di-vite-seconde-firme-ccp3.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-integrita-log-allarmi-cf-02.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-durata-deviazione-ccp2-l26130.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-sigla-kit-tasselli-ccp3.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-tassello-inox-non-passato.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «Verifica di fine turno (capoturno)» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «dalle 15 alle 18.45 linea ferma per rottura valvola azoto. verifiche n» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | citazione senza riscontro in nessuna fonte citata: «prodoto nn confezionato si acumula meso su carelli in CF O1 / temp cel» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «18:50» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | ora senza riscontro in nessuna fonte citata: «19:55» — la nota cita un .jpg, riscontro visivo da chiudere a mano |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` |  | provenance | fonte immagine 'MOD-QA-07_10-05-26_L1_T2_scansione.jpg': riscontro visivo, da chiudere a mano |
| `fatto-misura-frammento-rec-2026-011.md` |  | provenance | fonte immagine 'IMG_20260514_152241_frammento_REC-2026-011.jpg': riscontro visivo, da chiudere a mano |
| `doc-gestione-reclami-haccp.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `doc-scheda-tecnica-af-sn-0450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `entita-ivano-dal-maso.md` |  | provenance | la fonte 'R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml' non aggancia nessuna affermazione della nota: rumore nel payload |
| `concetto-fefo.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `kpi-shelf-life-af-sn-0450.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |
| `questione-scarti-riavvio-l26130.md` |  | provenance | summary e title si sovrappongono per meno del 20%: da ispezionare |


## qa_copertura (perimetro: lotto, 93 note)

- ERRORI: **0**
- AVVISI: **0**


## Note candidate per tema

*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,
col canone alla mano. Questo elenco e' il materiale su cui lavora.*

### (senza area)

| Nota | type | stato | fonti |
|---|---|---|---|
| `concetto-ccp.md` | concetto | risolto | 3 |

### amministrazione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-amministrazione.md` | hub | aperto | 2 |
| `entita-veneta-energia.md` | entita | risolto | 2 |
| `kpi-fattura-energia-maggio-2026.md` | atomica | risolto | 1 |
| `kpi-incremento-energia-maggio-su-aprile.md` | atomica | aperto | 1 |
| `kpi-metano-forni-maggio-2026.md` | atomica | aperto | 2 |
| `kpi-quadratura-consumi-energetici-maggio.md` | atomica | risolto | 1 |
| `questione-costo-energia-elettrica.md` | conflitto | aperto | 2 |

### commerciale

| Nota | type | stato | fonti |
|---|---|---|---|
| `fatto-richiesta-relazione-48-ore.md` | atomica | risolto | 2 |
| `prodotto-af-sn-0450.md` | entita | risolto | 5 |

### direzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-direzione.md` | hub | aperto | 1 |
| `fatto-riunione-direzione-reclamo-l26130.md` | atomica | risolto | 1 |

### logistica

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-logistica.md` | hub | aperto | 1 |
| `concetto-fefo.md` | concetto | risolto | 2 |
| `lotto-mv26-0429a.md` | entita | risolto | 5 |
| `questione-tmc-farina-mv26-0429a.md` | conflitto | aperto | 4 |

### manutenzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-manutenzione.md` | hub | aperto | 1 |
| `entita-ivano-dal-maso.md` | entita | risolto | 4 |
| `fatto-allarme-acustico-md-3200-basso.md` | atomica | risolto | 2 |
| `fatto-blackout-21-04-riavvio-centraline.md` | atomica | risolto | 1 |
| `fatto-decisione-proseguire-valvola-08-05.md` | atomica | risolto | 4 |
| `fatto-energia-reattiva-oltre-soglia.md` | atomica | aperto | 1 |
| `fatto-fermo-forno-ft-01-05-05.md` | atomica | risolto | 3 |
| `fatto-fermo-pkm-450-l26130.md` | atomica | risolto | 4 |
| `fatto-potenza-impegnata-quasi-satura.md` | atomica | aperto | 1 |
| `fatto-sonda-prodotto-cf-02-in-avaria.md` | atomica | risolto | 1 |
| `fatto-valvola-modulante-pt-104-revisione-rimandata.md` | atomica | aperto | 3 |
| `kpi-sbrinamenti-cf-02-aprile.md` | atomica | aperto | 1 |
| `macchina-cf-01.md` | entita | aperto | 4 |
| `macchina-cf-02.md` | hub | aperto | 3 |
| `macchina-pkm-450.md` | entita | risolto | 3 |
| `macchina-ts-01.md` | entita | aperto | 4 |
| `questione-sbrinamenti-fascia-notturna-cf-02.md` | conflitto | aperto | 2 |

### produzione

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-produzione.md` | hub | aperto | 1 |
| `entita-ionut-popescu.md` | entita | risolto | 4 |
| `fatto-operatori-ccp3-linea1-maggio.md` | atomica | aperto | 4 |
| `fatto-quaderno-capoturno-linea1.md` | atomica | risolto | 1 |
| `macchina-linea-1.md` | hub | aperto | 4 |
| `questione-scarti-riavvio-l26130.md` | conflitto | aperto | 2 |

### qualita

| Nota | type | stato | fonti |
|---|---|---|---|
| `area-qualita.md` | hub | aperto | 1 |
| `doc-gestione-deviazioni-haccp.md` | atomica | risolto | 1 |
| `doc-gestione-reclami-haccp.md` | atomica | risolto | 1 |
| `doc-mod-qa-07.md` | atomica | risolto | 3 |
| `doc-scheda-tecnica-af-sn-0450.md` | atomica | risolto | 1 |
| `entita-calservice-italia.md` | entita | risolto | 1 |
| `entita-metrolab-taratura.md` | entita | risolto | 1 |
| `fatto-accettazione-con-riserva-gas-06-05.md` | atomica | risolto | 3 |
| `fatto-blocco-cautelativo-lotti.md` | atomica | risolto | 6 |
| `fatto-datalogger-dl-001-in-taratura.md` | atomica | risolto | 2 |
| `fatto-giro-di-vite-seconde-firme-ccp3.md` | atomica | risolto | 3 |
| `fatto-integrita-log-allarmi-cf-02.md` | atomica | aperto | 1 |
| `fatto-microperdite-saldatura-l26130.md` | atomica | risolto | 2 |
| `fatto-misura-frammento-rec-2026-011.md` | atomica | risolto | 3 |
| `fatto-nc-102-origine-interna.md` | atomica | risolto | 2 |
| `fatto-nessuna-nc-per-allarmi-cf-02.md` | atomica | aperto | 3 |
| `fatto-operatore-senza-formazione-haccp-l26130.md` | atomica | risolto | 2 |
| `fatto-porta-cella-cf-02-aperta-38-minuti.md` | atomica | aperto | 2 |
| `fatto-prodotto-non-segregato-deviazione-ccp2.md` | atomica | aperto | 2 |
| `fatto-riepilogo-datalogger-inaffidabile.md` | atomica | aperto | 2 |
| `fatto-risalita-termica-post-riavvio-l26130.md` | atomica | aperto | 2 |
| `fatto-sonde-pt-104-in-taratura.md` | atomica | risolto | 2 |
| `fatto-strumenti-cf-02-e-ccp4.md` | atomica | risolto | 3 |
| `fatto-tassello-aisi-clip-rotta.md` | atomica | risolto | 3 |
| `kpi-mass-balance-l26130.md` | atomica | aperto | 2 |
| `kpi-parco-strumenti-taratura-2026.md` | hub | aperto | 2 |
| `kpi-seconde-firme-ccp3-maggio.md` | atomica | risolto | 2 |
| `kpi-shelf-life-af-sn-0450.md` | atomica | aperto | 3 |
| `questione-carrello-ricambi-dichiarato-rimosso.md` | conflitto | aperto | 4 |
| `questione-data-apertura-rec-2026-011.md` | conflitto | aperto | 4 |
| `questione-durata-deviazione-ccp2-l26130.md` | conflitto | aperto | 3 |
| `questione-limite-allarme-porta-cf-02.md` | conflitto | aperto | 2 |
| `questione-periodicita-taratura-canali-datalogger-ccp2.md` | conflitto | aperto | 3 |
| `questione-sigla-kit-tasselli-ccp3.md` | conflitto | aperto | 5 |
| `questione-taratura-termoregistratore-cf-02.md` | conflitto | aperto | 4 |
| `questione-tassello-inox-non-passato.md` | conflitto | aperto | 3 |
| `questione-validazione-ccp2-mai-confermata.md` | atomica | aperto | 1 |
| `questione-verifiche-ccp3-10-05-tre-versioni.md` | conflitto | aperto | 4 |
| `script-candidate-r1.md` | atomica | risolto | 0 |
| `script-conta-perimetro-lotto.md` | atomica | risolto | 0 |
| `script-conta-tracciamento.md` | atomica | risolto | 0 |
| `script-fonti-prescrittive.md` | atomica | risolto | 0 |
| `sessione-r1-riconciliazione-verticale.md` | sessione | — | 0 |

### Grezzi del perimetro e note che li citano

| Grezzo | Note che lo citano |
|---|---|