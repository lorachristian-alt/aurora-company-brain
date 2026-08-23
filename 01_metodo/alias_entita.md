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
| `entita-federica-sartori` | «Federica» · **«Sartori F.»** · **`f.sartori`** | trascrizione, MOD-PR-04 allegato 1, **politica per la qualita' 2026** e **scadenzario formazione** *(le due fonti aggiunte dal lotto 3B del 23/08/2026)*. ⚠️ **Che «f.sartori» e «Sartori F.» siano la stessa persona di «Federica» e' un'INFERENZA**, fondata sull'iniziale: nessuna fonte le mette una accanto all'altra, e la scheda entita' lo dichiara |
| `entita-milena-grigolon` | «Grigolon» · «sig.ra Grigolon» · «la signora grigolon» · «la consumatrice» | MOD-QA-31, mail, trascrizione |
| `entita-anna-perbellini` | «Perbellini» · «dott.ssa Perbellini» · «la QA del cliente» | trascrizione, mail Tosano |
| `entita-mario-rossi` | «Rossi» · «il buyer» · «il buyer di Tosano» | verbale incontro 05/05, trascrizione |
| `entita-adel-ben-salah` | «Ben Salah A.» · «adel» | registro NC, quaderno OCR |
| `entita-roberto-guerra` | «Guerra R.» | registro NC |
| `entita-mirco-bissoli` | «Bissoli M.» · `BISSOLI_M` (log CIP) · «mirco» | log CIP, quaderno OCR |
| `entita-chiara-vicentini` | «dott.ssa Chiara Vicentini» · **«C. Vicentini»** · **«Vicentini C.»** · «il consulente esterno» | manuale HACCP, **rapporto d'audit CSQA §2** *(le due fonti che danno il nome per esteso, dal lotto 3C del 22/08/2026: prima era una sola)*, scheda allergeni, formazione allergeni |

⚠️ **Il nome per esteso lo dà UNA fonte sola**, il manuale di autocontrollo: la scheda allergeni
e il materiale di formazione la nominano sempre e solo per iniziale. **Chi canonizza quei due
documenti senza il manuale non può sapere come si chiami** — ed è successo: la prima stesura
della scheda entità le aveva attribuito un nome sbagliato, corretto dallo strato di giudizio al
primo giro del lotto 2B-bis.

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
| `entita-frigotecnica-berica` | «FRIGOTECNICA BERICA S.r.l.» · «Frigotecnica Berica» · P.IVA `02744810249` · certificato F-gas d'impresa `IT-FG-0044821` | contratto di manutenzione frigo (bozza rev. 3) |
| `entita-veneta-energia` | «VENETA ENERGIA S.P.A.» · «Veneta Energia S.p.A.» · «Veneta Energia» · `F0081` (codice fornitore interno) · POD `IT001E63488210` | fattura energia elettrica, contatori di reparto |

### A.4 Macchine e impianti

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `macchina-pkm-450` | `PKM-450` · `PKM450` · `PKM 450` · **`PKM450-1808-0342`** (matricola) · «confezionatrice flow-pack MAP» · «confezionatrice MAP» · «la confezionatrice» | MOD-PR-04, manuale, trascrizione, corrispondenza ricambi |
| `macchina-pt-104` | `PT-104` · `PT104` · **`PT 1O4`** (OCR) · «il pastorizzatore» · «il trattamento termico» | log datalogger, quaderno OCR, manuale HACCP |
| `macchina-md-3200` | `MD-3200` · `MD3200` · **`MD 32OO`** (OCR) · «il metal detector» | quaderno OCR, MOD-QA-07, trascrizione |
| `macchina-ts-01` | `TS-01` · **`TS01`** (log della centralina) · «tunnel di surgelazione a piastre» · «il tunnel» (quando è il tunnel esistente, non quello Criotech) | contratto manutenzione frigo, log allarmi, registro NC, trascrizione |
| `macchina-cip-01` | `CIP01` · `CIP-01` · «l'impianto CIP» | log CIP, IO-05 |
| `macchina-ft-01` · `macchina-ft-02` | `FT O1` (OCR) · `FT_01` (log) · «forno 1» · «il bruciatore del FT-02» | quaderno OCR, log pastorizzatore, trascrizione |
| `macchina-cf-01` · `macchina-cf-02` | `CF-01` · `CF-02` · **`CF02`** (log della centralina) · «CELLA SURGELATI CF-02» e «CELLA FRIGO CF-01» (centri di costo nei contatori di reparto) · «la cella surgelati» · «cella refrigerata» | mass balance, log allarmi cella, contatori di reparto, contratto manutenzione frigo, trascrizione |

### A.5 Prodotti e lotti

| Nota padrona | Alias attestati | Dove |
|---|---|---|
| `prodotto-af-sn-0450` | `AF-SN-0450` · **`0450`** (quaderno) · `8034123450123` (EAN-13) · `18034123450120` (ITF-14) · «snack salato rustico multicereali 100 g ATM» · «il rustico multicereali» | listino, MOD-QA-31, mass balance, quaderno OCR |
| `prodotto-af-sn-0455` | `AF-SN-0455` · **`0455`** · `8034123454558` · «formato promo 3+1» | listino, trascrizione |
| `prodotto-af-cr-0215` | `AF-CR-0215` · **`0215`** · `8034123452158` · «Cornetto Premium PL Tosano 8×45 g surg.» · «il cornetto private label» | listino, trascrizione, analisi marginalità |
| `prodotto-af-fc-0330` | `AF-FC-0330` · `8034123453308` · «Focaccina olio EVO 2×90 g ATM» | listino, registro NC |
| `lotto-l26130` | `L26130` (forma parziale del reclamo) · `L26130-L1-T2` · **`L26l3O-L1-T2`** (OCR) · «lotto 130» · «il 130» | MOD-QA-31, mass balance, log, trascrizione, quaderno OCR |
| `lotto-l26124` | `L26124` · `L26124-L1-T2` · **`L26l24-L1-T2`** (OCR) | quaderno OCR, MOD-QA-07 |
| `lotto-l26128` | `L26128` · `L26128-L1-T2` | quaderno OCR, MOD-QA-07, prove di shelf life |
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
| `L26l24` · `L26l3O` | `L26124` · `L26130` (giorno giuliano: la `l` e' un `1`) | `appunti_capoturno_quaderno_linea1_OCR.txt` |
| `4.1OO` · `6.O85` · `2OO` | `4.100` · `6.085` · `200` (cifre con `O` al posto di `0`) | idem |
| `[pagina strappata a meta]` · `[macchia]` · `[macchia grande]` | porzione perduta: **non si ricostruisce** | idem |
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
| **Attilio Peruffo** — legale rappresentante di **Frigotecnica Berica S.r.l.**, Montecchio Maggiore (VI), firma i commenti di trattativa come «Peruffo A. (Frigotecnica)» (`contratto_manutenzione_impianto_frigo_TS01.docx`) | **Peruffo Maria Grazia** — revisore legale di Aurora, Registro n. 148223 (`visura_camerale_ordinaria_AuroraFoodGroup.pdf`) · e **Peruzzi Maurizio**, n. 118442 (`bilancio_esercizio_2025_deposito_CCIAA.pdf`) | Un fornitore esterno e un revisore legale: ruoli, documenti e numeri di iscrizione diversi. **Il cognome Peruffo compare ora su due persone diverse, e in archivio ci sono tre quasi-omografi** | Tre schede distinte. ⚠️ La riga «Da non confondere con» sulle schede dei revisori si scrive nel lotto che canonizza visura e bilancio: oggi quelle note non esistono, e un rimando non può nascere prima della nota |
| **Peruzzi Erika** — operaia Linea 2, `HACCP base` 05/05/2024→05/05/2027, «CESSATA 19/04 - riga da eliminare» (`registro_presenze_corsi_HACCP_scaduti.csv` riga 101) | **Peruffo Maria Grazia** (visura, revisore) · **Peruzzi Maurizio** (bilancio, revisore) · **Attilio Peruffo** (Frigotecnica) | Un'operaia di linea accanto a due revisori legali e a un legale rappresentante: quattro ruoli, quattro documenti, **nessun identificativo in comune** | Non si uniscono mai. ⚠️ **La famiglia sale a quattro nel vault e a sei nel corpus**: 🚫 `PERUZZI Loris` (operaio Linea 1 impasti) e 🚫 `Peruzzi Luciano` (presidente d'assemblea) stanno in due grezzi non canonizzati e **non entrano finche' il loro lotto non li porta** |
| **`NC-26-018`** — ruote dei carrelli di farcitura fuori limite, registro tamponi `MOD-QA-19`, 14/02/2026 | **`NC-2026-018`** — fermo del forno `FT-01` per pressostato gas in avaria, registro non conformità `MOD-QA-18` | Due registri diversi, due date diverse, due oggetti che non hanno nulla in comune | Le due sigle **non si uniscono mai**. La nota `fatto-nc-26-018-ruote-carrelli-febbraio` porta «Da non confondere con» |
| **`NC-26-041`** — Listeria nello scarico sotto `PT-104`, `MOD-QA-19`, 13/04/2026 | **`NC-2026-041`** — ordine straordinario Tosano, cambio formato non pianificato, `MOD-QA-18`, 05/03/2026 | Idem | Idem |
| **`NC-26-055`** — nastro del forno `FT-01` a 52 UFC/cm², `MOD-QA-19`, 11/05/2026 | **`NC-2026-055`** — prototipo `AF-SN-0470` v12, sesamo lavorato in saletta pilota senza segregazione, `MOD-QA-18`, 25/03/2026 | Idem | Le due sigle **non si uniscono mai**. La nota `fatto-nc-26-055-nastro-forno-maggio` porta «Da non confondere con» |
| **`NC-26-056`** — ganasce `PKM-450` a 1,2×10³ UFC/cm², `MOD-QA-19`, 11/05/2026 | **`NC-2026-056`** — quarta dimissione in cinque mesi su Linea 2, `MOD-QA-18`, 26/03/2026 | Idem | Le due sigle **non si uniscono mai**. La nota `fatto-nc-26-056-ganasce-pkm-450-maggio` porta «Da non confondere con» |

⚠️ **Le quattro righe qui sopra sono una FAMIGLIA, non quattro casi**, e vanno lette insieme:
l'archivio porta **tre serie parallele di numerazione delle non conformità** — `NC-26-nnn` nel
registro dei tamponi `MOD-QA-19`, `NC-2026-nnn` nel registro delle non conformità interne
`MOD-QA-18`, `NC-ACQ-26-nn` nel registro dell'acqua — e **nessun documento le riconcilia**.
⚠️ **La differenza fra le prime due grafie è di due cifre nell'anno, e nient'altro**: una
ricerca per sigla che normalizzi `26` e `2026` unisce eventi che non hanno nulla in comune.
⚠️ **E nessuna non conformità dei due registri analitici compare in `MOD-QA-18`**, che pure
dichiara nel proprio titolo di essere il registro delle non conformità interne.
*(Trovate dalla revisione del lotto 2B, 21/08/2026; il caso sta nel canone, sezione del
21/08/2026, rilievo B4.)*

---

## Classe C — divergenze che l'archivio non riconcilia

| Divergenza | Fonti | Trattamento |
|---|---|---|
| Codice dell'allarme PKM-450 del 10/05: `E-214 GAS` contro `AL-217 "N2 pressure low"` | `IMG-20260510-WA0007.jpg` (foto del pannello) · `report_fermo_macchina_confezionatrice_MAP.txt` (riga «15:05 - chiamata dal capoturno: allarme AL-217») | `questione-codice-allarme-pkm-450` in `areas\` (`area: manutenzione`), `stato: aperto`. La scheda `macchina-pkm-450` la linka, non la ospita. Servirebbe la tabella allarmi del manuale PKM-450, presente in archivio solo per estratto |
| Operatori `RANZATO_F` e `CESTARO_L`, presenti nel log del pastorizzatore ma senza badge nelle timbrature né matricola nel libro unico (compaiono però nell'ordine DPI) | `log_temperature_pastorizzatore_linea1_10_05_26.log` · `log_timbrature_fabbrica_maggio_settimana2.csv` · `libro_unico_lavoro_estratto_maggio2026.xlsx` · `ordine_DPI_scarpe_antinfortunistiche.csv` | Si crea la scheda entità con ciò che i grezzi dicono e una questione aperta sull'export parziale delle timbrature. **Non si inventa una matricola, e non si conclude che le persone non esistono** |
| Lotto del reclamo dichiarato come `L26130`, senza linea e turno | `MOD-QA-31_reclamo_REC-2026-011.pdf` (lotto dichiarato `L26130`) · mass balance e log (`L26130-L1-T2`) | La nota riporta la forma parziale come dichiarata e spiega in una riga come le altre fonti la completano. Entrambe le forme in `aliases`. **Non si riscrive il codice del reclamo** |
| Data della riunione di direzione: il nome del file dice `12_05_2026`, la prima riga della trascrizione dice «13 05 2026» | `trascrizione_riunione_direzione_12_05_2026.txt` · `Convocazione_riunione_direzione_12_05.eml` | Il contenuto batte il nome del file: `data_fatto: 2026-05-13`. Il nome del file **resta quello che è** in `fonti` |
| Codice del kit valvola azoto originale della PKM-450: `PK45-VN2-08` contro `PKV-088-N2` (gruppo) e `PKV-088-KIT` (kit) | `report_fermo_macchina_confezionatrice_MAP.txt` (codice interno) · `R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml` (codice del costruttore) | `questione-codice-ricambio-valvola-pkm-450` in `areas\` (`area: manutenzione`), `stato: aperto`. **Non si uniscono**: nessun documento mette i due codici uno accanto all'altro |
| Materiale della guarnizione provvisoria della PKM-450: «silicone» · «gomma» · polimero fluorurato (PTFE/FKM) | trascrizione 13/05 · risposta scritta allegata al MOD-PR-04 · `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` | `questione-materiale-guarnizione-pkm-450` in `areas\`. ⚠️ Le fonti **non parlano dello stesso oggetto**: le prime due della guarnizione montata, la terza del frammento del reclamo |
| Lotto farina `MV26-0429/A`: TMC 29/12/2026 · 04/11/2026 · 30/10/2026; consegna sfusa in autocisterna (DDT 1187/26) contro sacchi da 25 kg (DDT 48392) | `certificato_analisi_lotto_farina_MV26_0429A.pdf` · `tracciabilita_lotti_massbalance_L26130.xlsx` · `inventario_magazzino_scadenze_FEFO_maggio.csv` | `questione-tmc-farina-mv26-0429a` e `questione-consegna-farina-mv26-0429a`, entrambe in `areas\` (`area: logistica`). **Non si sceglie**: il criterio non è dichiarato da nessuna delle fonti interne |

---

### Aggiunte di classe C dal lotto 1B — 19/08/2026

| Divergenza | Fonti | Trattamento |
|---|---|---|
| Nome dell'impresa che manutiene gli impianti frigoriferi: **Frigotecnica Berica** contro **Frigotecnica Scaligera**, sugli stessi impianti | `contratto_manutenzione_impianto_frigo_TS01.docx` (intestazione delle parti, con P.IVA e certificato F-gas) · `scheda_manutenzione_ordinaria_forni_industrial.csv` (righe 42, 44, 47, 51, 53) | `questione-manutentore-frigo-berica-scaligera` in `areas\` (`area: manutenzione`), `stato: aperto`. **Non si uniscono**: la scheda entità sta sul nome che ha un identificativo verificabile. Il piano di manutenzione non porta partita IVA né codice fornitore |
| Refrigerante del tunnel `TS-01`: **R404A** (48,0 kg, GWP 3.922) contro **R448A** | `contratto_manutenzione_impianto_frigo_TS01.docx` §art. 2.1 · `scheda_manutenzione_ordinaria_forni_industrial.csv` riga 44 | `questione-refrigerante-ts-01` in `areas\`, `stato: aperto`. Sono due miscele diverse: cambiano GWP, tonnellate equivalenti e frequenza del controllo perdite |
| Sigla `FRIGOTEC-11` dell'operatore esterno in assistenza sulla centralina della cella | `log_allarmi_cella_frigo_surgelati_aprile.log`, righe 08:55:02 e 11:40:47 del 24/04 | **Non si scioglie.** La sigla richiama «Frigotecnica», ma nessun documento la lega a una ragione sociale, e la questione su chi sia il manutentore è aperta: la sigla **non entra** negli `aliases` di nessuna entità |

## Registro delle aggiunte

Ogni sessione che canonizza aggiunge qui una riga quando estende la tabella.

| Data | Sessione | Cosa è stato aggiunto |
|---|---|---|
| 2026-08-15 | S1 — manuale di canonizzazione | Prima stesura: classi A, B e C compilate sui file campionati del corpus v1 |
| 2026-08-18 | S4 lotto 1A — Linea 1: turno, CCP, confezionatrice | Classe A: i lotti `L26124` e `L26128` con le loro forme OCR, la forma `L26l3O-L1-T2` sul lotto L26130, e tre degradi generici del quaderno del capoturno (cifre con `O` al posto di `0`, la `l` al posto dell'`1` nel giorno giuliano, i marcatori di porzione perduta). Nessuna riga di classe B o C: le divergenze trovate in questo lotto hanno tutte una nota-questione |
| 2026-08-19 | S4 lotto 1B — freddo ed energia | Classe A: le forme `CF02` e `TS01` del log della centralina, i due centri di costo dei contatori di reparto, e due fornitori nuovi — Frigotecnica Berica (con P.IVA e certificato F-gas) e Veneta Energia (con codice fornitore e POD). Classe B: **il terzo quasi-omografo Peruffo**, Attilio Peruffo di Frigotecnica accanto ai due revisori legali. Classe C: tre divergenze nuove — nome del manutentore, refrigerante del tunnel, e la sigla `FRIGOTEC-11` che non si scioglie |
| 2026-08-16 | S2 — fetta pilota L26130 | Classe A: matricola `PKM450-1808-0342` sulla PKM-450. Classe C: quattro divergenze nuove trovate dal revisore indipendente — codice del kit valvola, materiale della guarnizione provvisoria, TMC e modo di consegna del lotto farina MV26-0429/A. Tutte con la loro nota-questione nel vault e la riga corrispondente nel canone |
| 2026-08-21 | S4 lotto 2B — autocontrollo analitico | Classe A: il laboratorio esterno `Analytica Veneta S.r.l.` con la sua forma accreditata. **Classe B: le tre serie parallele di numerazione delle non conformità** — `NC-26-nnn`, `NC-2026-nnn`, `NC-ACQ-26-nn` — con la tabella delle collisioni e la nota di famiglia: **due cifre nell'anno separano eventi che non hanno nulla in comune** |
| 2026-08-21 | S4 lotto 2B-bis — gli allergeni | Classe A: `entita-chiara-vicentini`, **con l'avvertenza che il nome per esteso lo dà una fonte sola**. ⚠️ **La riga esiste perché questa sessione aveva INVENTATO un nome proprio** — «Claudia» invece di «Chiara» — canonizzando due documenti che il nome non lo portano: **è il caso che ha insegnato che un'iniziale non si scioglie a naso** |
| 2026-08-23 | S4 lotto 3B — politica e formazione | Classe A: `entita-federica-sartori`, con **due fonti nuove** — la politica e lo scadenzario — e la mansione «HR e segreteria» che il registro dichiara. ⚠️ **Che «f.sartori», «Sartori Federica» e «Sartori F.» siano la stessa persona resta un'INFERENZA**, e la scheda lo dichiara. Classe B: il quarto quasi-omografo **Peruzzi**. ⚠️ **E un errore da non ripetere**: la prima stesura di `doc-scadenzario-formazione-2026` puntava a un `entita-francesca-sartori` **che non esiste** — nome proprio inventato, come gia' successe per Vicentini — e la QA non lo vedeva perche' non guardava `related`. Riparata la QA lo stesso giorno |
