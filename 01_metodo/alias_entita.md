# alias_entita — la tabella alias dell'entity resolution

> **Cos'è** · L'elenco delle varianti con cui le entità di Aurora compaiono nei grezzi
> del corpus v1: sigle, abbreviazioni, codici parziali, degradi OCR, trascrizioni fonetiche.
> **Quando si usa** · Ogni volta che si canonizza (per compilare `aliases` nella scheda
> entità), quando gira `qa_provenance.py` (per non generare falsi allarmi sui file in
> OCR) e in Sessione 3 per la tokenizzazione BM25 della config C, che non deve spezzare
> i codici.
> **Cosa non toccare** · Le righe della **classe B**: sono soggetti diversi che si
> assomigliano, e unirli distrugge una trappola voluta.

> **Gerarchia** · Allegato di `metodo_03_canonizzazione.md` §6. La regola sta nel
> manuale; qui sta solo la tabella. Questo file **cresce**: ogni sessione che canonizza
> aggiunge le varianti nuove che incontra, nella classe che le compete.

---

## Come si legge

Tre classi, con tre trattamenti diversi e non intercambiabili.

| Classe | Cosa sono | Trattamento |
|---|---|---|
| **A** | Varianti della **stessa** entità: sigle, abbreviazioni, codici, degradi OCR che decodificano a un codice valido | Si uniscono. Vanno in `aliases` della nota padrona |
| **B** | **Quasi-omografi che sono soggetti DIVERSI** | Non si uniscono mai. Ogni scheda porta «Da non confondere con» |
| **C** | Codici o riferimenti che divergono e che l'archivio **non riconcilia** | Non si uniscono e non si sceglie: si apre una questione aperta |

⚠️ **Le attribuzioni `PARLANTE_n` → persona sono INFERENZE, non dati della fonte.** Il
file `trascrizione_riunione_direzione_12_05_2026.txt` dichiara in testa «parlanti non
verificati»: i nomi non compaiono accanto alle battute, e l'attribuzione è stata dedotta
dal contenuto (chi viene chiamato per nome, chi rivendica quale ruolo). Valgono come
alias per la ricerca e per la normalizzazione della QA, **ma una nota non può citarle
come se il grezzo le affermasse**: nel locator si scrive `PARLANTE_3`, non «Marchetti»
(metodo_03 §3.1 e §10.12). Stessa cautela per ogni altra identificazione dedotta.

**Regola di ammissione in classe A.** Un degrado OCR si accetta come alias solo se il
codice decodificato **supera il suo algoritmo di controllo** (Luhn per la P.IVA,
modulo-10 GS1 per EAN e ITF-14, CIN + MOD-97 per l'IBAN) o coincide con un codice già
attestato altrove in archivio. Se non lo supera, non è una variante: è un altro codice,
e si tratta come classe C.

Le sostituzioni note dello scanner sono `0`↔`O`, `l`↔`1`, `S`↔`5`.

---

## Classe A — varianti della stessa entità

### A.1 Aurora e i suoi codici

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `self-anagrafica` | `03984710230` · `O39847lOZ3O` (OCR) · «Aurora» · «Aurora Food Group S.r.l.» · «AURORA FOOD GROUP S.R.L.» · `AFG` | visura, bilancio, manuale HACCP, documenti in OCR degradato |
| `self-sede` | «Via dell'Industria 27» · «Cologna Veneta (VR)» · `37044` | visura, manuale HACCP, DDT |

### A.2 Persone

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `entita-giancarlo-bertoldi` | «Bertoldi G.» · «Giancarlo» · `PARLANTE_1` (trascrizione 13/05) · `g.bertoldi@aurorafoodgroup.it` | trascrizione riunione, mail |
| `entita-silvia-bertoldi` | «Silvia» · `PARLANTE_4` (trascrizione 13/05) | trascrizione riunione |
| `entita-marco-fantin` | «Fantin M.» · «ing. Fantin» · «Marco» · `PARLANTE_2` (trascrizione 13/05) · `m.fantin@aurorafoodgroup.it` · «FANTIN MARCO» (visura, procuratore speciale) | MOD-PR-04, mail, visura, trascrizione |
| `entita-elena-marchetti` | «Marchetti E.» · «dott.ssa Elena Marchetti» · `RSGQ` · «team leader HACCP» · `PARLANTE_3` (trascrizione 13/05) · `e.marchetti@aurorafoodgroup.it` · `(E.M.)` (note nei fogli) | manuale HACCP, MOD-QA-31, mail, mass balance |
| `entita-sara-pozzato` | «Pozzato S.» · «Sara» · `(S.P.)` (note nei fogli) · `s.pozzato@aurorafoodgroup.it` | registro NC, mass balance, manuale HACCP |
| `entita-denis-zanella` | «Zanella D.» · «Denis» · `PARLANTE_6` (trascrizione 13/05) | MOD-PR-04, registro NC, trascrizione |
| `entita-ionut-popescu` | «Popescu I.» · «Popescu» · **«popesco»** (trascrizione fonetica) · `IP` (firma sul quaderno) · «il capoturno» (nel contesto Linea 1 turno 2) | MOD-PR-04, quaderno OCR, trascrizione, registro NC |
| `entita-ivano-dal-maso` | «Dal Maso I.» · «dal maso» · «Ivano» · `PARLANTE_7` (trascrizione 13/05) | MOD-PR-04, trascrizione, registro NC |
| `entita-luisa-trentin` | «rag. Luisa Trentin» · «Trentin L.» · «la Trentin» · `PARLANTE_5` (trascrizione 13/05) · «(L.Trentin)» (intestazione listino) | listino v3, inventario, trascrizione |
| `entita-nicola-faggionato` | «Faggionato N.» · «Nicola» | registro NC, inventario FEFO, trascrizione |
| `entita-federica-sartori` | «Federica» | trascrizione, MOD-PR-04 allegato 1 |
| `entita-milena-grigolon` | «Grigolon» · «sig.ra Grigolon» · «la signora grigolon» · «la consumatrice» | MOD-QA-31, mail, trascrizione |
| `entita-anna-perbellini` | «Perbellini» · «dott.ssa Perbellini» · «la QA del cliente» | trascrizione, mail Tosano |
| `entita-mario-rossi` | «Rossi» · «il buyer» · «il buyer di Tosano» | verbale incontro 05/05, trascrizione |
| `entita-adel-ben-salah` | «Ben Salah A.» · «adel» | registro NC, quaderno OCR |
| `entita-roberto-guerra` | «Guerra R.» | registro NC |
| `entita-mirco-bissoli` | «Bissoli M.» · `BISSOLI_M` (log CIP) · «mirco» | log CIP, quaderno OCR |

### A.3 Clienti, fornitori, enti

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `entita-tosano-cerea` | «Tosano Cerea S.p.A.» · «Tosano Cerea SpA» · «Tosano» · «il cliente principale» | listino v3, mass balance, accordo quadro |
| `marchio-bonta-di-casa` | «Bontà di Casa» · «bonta di casa» · «il private label di Tosano» | listino v3, manuale HACCP, trascrizione |
| `entita-ali-spa` | «Alì S.p.A.» · «Alì» · «Ali SpA» · `Al� SpA` (encoding perso) · «ali» | mass balance, registro NC, trascrizione |
| `entita-molino-veneto` | «Molino Veneto SpA» · «Molino Veneto» · «MOLINO VENETO» · «il molino» | contratto, listino farine, DDT, inventario |
| `entita-flexipack-nordest` | «Flexipack Nordest Srl» · «Flexipack» | DoC MOCA, mass balance, capitolato |
| `entita-criotech-impianti` | «Criotech» · «criotech impianti» · **«crio tec»** (trascrizione fonetica) | preventivo, verbale CdA, estratto conto, trascrizione |
| `entita-pakmatic` | «Pakmatic» · «Pakmatic» come costruttore della PKM-450 | MOD-PR-04, manuale d'uso |
| `entita-nordgas` | «Nordgas SpA» · «Nordgas» | bolla azoto, mass balance |
| `entita-lievital` | «Lievital Srl» · «lievito lievital» · «lievital» | mass balance, quaderno OCR |
| `entita-analytica-veneta` | «Analytica Veneta» · «analytica» · «il laboratorio esterno» | rapporto di prova, trascrizione, vendor rating |
| `entita-csqa` | `CSQA` · «l'ente di certificazione» | certificato BRCGS, rilievo audit, conferma incarico |
| `entita-unicredit` | «UniCredit» · «unicredit» · «la filiale di Cologna» | estratto conto, trascrizione |

### A.4 Macchine e impianti

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `macchina-pkm-450` | `PKM-450` · `PKM450` · `PKM 450` · «confezionatrice flow-pack MAP» · «confezionatrice MAP» · «la confezionatrice» | MOD-PR-04, manuale, trascrizione |
| `macchina-pt-104` | `PT-104` · `PT104` · **`PT 1O4`** (OCR) · «il pastorizzatore» · «il trattamento termico» | log datalogger, quaderno OCR, manuale HACCP |
| `macchina-md-3200` | `MD-3200` · `MD3200` · **`MD 32OO`** (OCR) · «il metal detector» | quaderno OCR, MOD-QA-07, trascrizione |
| `macchina-ts-01` | `TS-01` · «il tunnel» (quando è il tunnel esistente, non quello Criotech) | contratto manutenzione frigo, registro NC, trascrizione |
| `macchina-cip-01` | `CIP01` · `CIP-01` · «l'impianto CIP» | log CIP, IO-05 |
| `macchina-ft-01` · `macchina-ft-02` | `FT O1` (OCR) · `FT_01` (log) · «forno 1» · «il bruciatore del FT-02» | quaderno OCR, log pastorizzatore, trascrizione |
| `macchina-cf-01` · `macchina-cf-02` | `CF-01` · `CF-02` · «la cella surgelati» | mass balance, log allarmi cella, trascrizione |

### A.5 Prodotti e lotti

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `prodotto-af-sn-0450` | `AF-SN-0450` · **`0450`** (quaderno) · `8034123450123` (EAN-13) · `18034123450120` (ITF-14) · «snack salato rustico multicereali 100 g ATM» · «il rustico multicereali» | listino, MOD-QA-31, mass balance, quaderno OCR |
| `prodotto-af-sn-0455` | `AF-SN-0455` · **`0455`** · `8034123454558` · «formato promo 3+1» | listino, trascrizione |
| `prodotto-af-cr-0215` | `AF-CR-0215` · **`0215`** · `8034123452158` · «Cornetto Premium PL Tosano 8×45 g surg.» · «il cornetto private label» | listino, trascrizione, analisi marginalità |
| `prodotto-af-fc-0330` | `AF-FC-0330` · `8034123453308` · «Focaccina olio EVO 2×90 g ATM» | listino, registro NC |
| `lotto-l26130` | `L26130` (forma parziale del reclamo) · `L26130-L1-T2` · «lotto 130» · «il 130» | MOD-QA-31, mass balance, log, trascrizione |
| `lotto-l26131` | `L26131` · `L26131-L1-T2` · «il 131» | mass balance, trascrizione |
| `lotto-mv26-0429a` | `MV26-0429/A` · `MV26_0429A` (nel nome del certificato di analisi) · `MV26-0429A` | certificato analisi, inventario FEFO, mass balance |
| `lotto-mv26-0430a` | `MV26-0430/A` · `MV26-0430A` · «il sacco segregato» | inventario FEFO, DDT OCR |

### A.6 Documenti, moduli e pratiche

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `doc-manuale-haccp` | «Manuale HACCP» · «rev. 4 del 15/01/2024» · «rev.5» · «il manuale» | manuale HACCP |
| `doc-io-05-lavaggio-cip` | `IO-05` · `IO 05` · `PRG=IO-05_P2_LINEA1` (nel log) · «l'istruzione operativa del CIP» | IO-05, log CIP |
| `doc-mod-qa-07` | `MOD-QA-07` · `MOD-QA-07 rev.5` · «la checklist del metal detector» | MOD-QA-07, manuale HACCP, trascrizione |
| `doc-mod-qa-12` | `MOD-QA-12` · «il registro cartaceo del pastorizzatore» | trascrizione, mail |
| `doc-mod-qa-31` | `MOD-QA-31` · `MOD-QA-31 rev.4` · «la scheda reclamo» | MOD-QA-31, mail, trascrizione |
| `doc-mod-pr-04` | `MOD-PR-04` · `MOD-PR-04 rev.3` · «n. 2026/087» · «il rapporto di fermo macchina» | rapporto fermo macchina, quaderno OCR |
| `doc-mod-mag-02` | `MOD-MAG-02` · «il registro movimentazioni» | mail, trascrizione, mass balance |
| `progetto-gestione-reclamo-rec-2026-011` | `REC-2026-011` · «la pratica 011» · «il reclamo Grigolon» · «il reclamo corpo estraneo» | MOD-QA-31, mail, trascrizione |
| `doc-certificato-brcgs` | `BRC/IT/24/00871` · «BRCGS Food Issue 9» · «il BRC» | certificato, manuale HACCP |

### A.7 Degradi OCR generici (non entità, ma vanno normalizzati prima del confronto)

| Nel grezzo | Decodifica | File |
|---|---|---|
| `0k` | `ok` | `appunti_capoturno_quaderno_linea1_OCR.txt` |
| `b0lla` | `bolla` | idem |
| `setacc1o` | `setaccio` | idem |
| `pul1to` | `pulito` | idem |
| `2OO dpi` · `RICOH IM C3OO` | `200 dpi` · `RICOH IM C300` | idem (intestazione di scansione) |
| `n0nfe` | `non fe` (non ferroso) | idem |
| `inox 3,O` | `inox 3,0` | idem |
| `pasa` | `passa` | idem |
| `[???]` · `[illeggibile]` · `#####` | testo perduto: **non si ricostruisce** | file in OCR degradato |

⚠️ Un valore numerico coperto da `[???]` o `#####` **non si indovina**. La nota riporta
che il dato è illeggibile nella fonte, e se serve apre una questione aperta.

---

## Classe B — quasi-omografi: soggetti DIVERSI, mai da unire

| Soggetto 1 | Soggetto 2 | Prova che sono diversi | Cosa si fa |
|---|---|---|---|
| **Peruffo Maria Grazia** — revisore legale, Registro revisori legali n. **148223**, nominata con verbale del **28/04/2025**, nata a Vicenza l'08/11/1971 (`visura_camerale_ordinaria_AuroraFoodGroup.pdf`) | **Peruzzi Maurizio** — revisore legale unico, Registro revisori legali n. **118442**, nominato dall'assemblea dei soci del **14/05/2024**, compenso 9.500 € (`bilancio_esercizio_2025_deposito_CCIAA.pdf`) | Due numeri di iscrizione, due date di nomina, due documenti ufficiali distinti | **Due schede entità**, ciascuna con «Da non confondere con», più `questione-revisore-legale` — che vive in `areas\` (`area: amministrazione`), non in `entities\`: vedi metodo_03 §1.1, clausola del passo 5. Prevale l'iscrizione al Registro Imprese, ma la divergenza si dichiara |
| **MV26-0429/A** — farina W300, TMC 30/10/26, stato OK | **MV26-0430/A** — farina W300, TMC 01/11/26, un sacco `SEGREGATO` per lacerazione, «verificare con Marchetti prima di usare» | Righe distinte dell'inventario FEFO, TMC diversi, stati diversi | Due note lotto. La segregazione appartiene solo al secondo |
| **MV26-0429/A** | **MV26-0431/B** — coda del bancale precedente, TMC 06/11/26, 210 kg | Righe distinte del mass balance, foglio «A monte» | Due note lotto |
| **PKM-450** — la macchina di Aurora | **Pakmatic** — il costruttore, fornitore esterno | Una è un impianto, l'altro un'azienda | Due schede: `macchina-pkm-450` in `entities`, `entita-pakmatic` in `entities` |
| **Tosano Cerea S.p.A.** — il cliente | **CE.DI. Cerea** — la sua piattaforma logistica di destinazione | Il primo è la controparte contrattuale, il secondo un luogo di consegna | Il CE.DI. non è una scheda entità propria: è un attributo del cliente |
| **Bontà di Casa** — il marchio private label | **Tosano Cerea S.p.A.** — il titolare del marchio | Marchio ≠ azienda | Due note: `marchio-bonta-di-casa` ed `entita-tosano-cerea`, linkate |
| **TS-01** — il tunnel di surgelazione esistente, «un rottame» | il **tunnel Criotech CR-SP180** — quello da acquistare, acconto 87.000 € | Uno è in servizio, l'altro è un investimento in corso | `macchina-ts-01` in `entities`, `progetto-tunnel-surgelazione` in `projects` |
| **Marco Fantin** — direttore di stabilimento | **«fantini» / «Rossato di Tecnoforni»** — nella trascrizione automatica il parlante si autocorregge | La trascrizione è dichiaratamente non verificata | Non si crea un'entità «Fantini»: si riporta la correzione a verbale |

---

## Classe C — divergenze che l'archivio non riconcilia

| Divergenza | Fonti | Trattamento |
|---|---|---|
| Codice dell'allarme PKM-450 del 10/05: `E-214 GAS` contro `AL-217 "N2 pressure low"` | `IMG-20260510-WA0007.jpg` (foto del pannello) · `report_fermo_macchina_confezionatrice_MAP.txt` (riga «15:05 - chiamata dal capoturno: allarme AL-217») | `questione-codice-allarme-pkm-450` in `areas\` (`area: manutenzione`), `stato: aperto`. La scheda `macchina-pkm-450` la linka, non la ospita. Servirebbe la tabella allarmi del manuale PKM-450, presente in archivio solo per estratto |
| Operatori `RANZATO_F` e `CESTARO_L`, presenti nel log del pastorizzatore ma senza badge nelle timbrature né matricola nel libro unico (compaiono però nell'ordine DPI) | `log_temperature_pastorizzatore_linea1_10_05_26.log` · `log_timbrature_fabbrica_maggio_settimana2.csv` · `libro_unico_lavoro_estratto_maggio2026.xlsx` · `ordine_DPI_scarpe_antinfortunistiche.csv` | Si crea la scheda entità con ciò che i grezzi dicono e una questione aperta sull'export parziale delle timbrature. **Non si inventa una matricola, e non si conclude che le persone non esistono** |
| Lotto del reclamo dichiarato come `L26130`, senza linea e turno | `MOD-QA-31_reclamo_REC-2026-011.pdf` (lotto dichiarato `L26130`) · mass balance e log (`L26130-L1-T2`) | La nota riporta la forma parziale come dichiarata e spiega in una riga come le altre fonti la completano. Entrambe le forme in `aliases`. **Non si riscrive il codice del reclamo** |
| Data della riunione di direzione: il nome del file dice `12_05_2026`, la prima riga della trascrizione dice «13 05 2026» | `trascrizione_riunione_direzione_12_05_2026.txt` · `Convocazione_riunione_direzione_12_05.eml` | Il contenuto batte il nome del file: `data_fatto: 2026-05-13`. Il nome del file **resta quello che è** in `fonti` |

---

## Registro delle aggiunte

Ogni sessione che canonizza aggiunge qui una riga quando estende la tabella.

| Data | Sessione | Cosa è stato aggiunto |
|---|---|---|
| 2026-08-15 | S1 — manuale di canonizzazione | Prima stesura: classi A, B e C compilate sui file campionati del corpus v1 |
