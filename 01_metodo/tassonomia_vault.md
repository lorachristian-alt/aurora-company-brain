# Tassonomia del vault — le 11 cartelle di aurora-cervello

> **Cos'è** · La descrizione di riferimento delle 11 cartelle del vault Obsidian:
> etichetta breve (dall'immagine `06_operativo/tassonomia_vault.png`, fornita dal
> titolare del progetto) e criterio esteso di appartenenza.
> **Quando si usa** · In Sessione 1 per scrivere le regole di spareggio di
> `metodo_03_canonizzazione.md`, e in ogni sessione di canonizzazione come
> riferimento rapido. Le regole di spareggio nei casi ambigui vivono in metodo_03:
> questo file dice COSA va dove, metodo_03 decide QUANDO due cartelle se lo contendono.
> **Cosa non toccare** · Le 11 cartelle sono fisse: non se ne aggiungono altre.

| Cartella | Etichetta | Criterio esteso |
|---|---|---|
| `self` | «chi e azienda» | L'identità di Aurora: chi è, com'è fatta oggi, dove vuole andare. Vision, mission, obiettivi, assetto societario, sedi, certificazioni possedute, la fotografia strategico-legale-decisionale. È il punto di riferimento che dà all'AI il contesto di fondo. |
| `areas` | «responsabilità continue» | Le responsabilità che non finiscono mai: produzione & manutenzione, QA/QC, logistica, commerciale & marketing, R&D, amministrazione-finanza-controllo, HR. Ogni area ha il suo hub e le sue note operative. |
| `projects` | «lavoro a tempo, con traguardo» | Ciò che ha un inizio e una fine: sviluppo nuovo prodotto (AF-SN-0470), rinnovo certificazione BRC/IFS, tunnel di surgelazione Criotech, cambio ERP, Aurora Vega, cost saving. Un progetto chiuso resta come storia, non diventa un'area. |
| `sources` | «la inbox grezza» | I 160 file grezzi copiati (byte-identici al manifest) e, a regime, tutto ciò che arriva non ancora distillato: ordini EDI, email e FAX, DDT, portali GDO, esiti di laboratorio, PEC, SDI, fogli ore, estratti conto, registri di linea, segnalazioni verbali. Qui NIENTE markdown: un file server non contiene markdown. |
| `concepts` | «idee, una per nota» | Il glossario concettuale: una definizione per nota, col contesto Aurora. EDI, listing fee, private label/MDD, sell-in/sell-out, SOP, FIFO/FEFO, CCP, NC, ARR/MRR, churn, LTV, CAC, cash flow, CapEx/OpEx, shelf-life, DDT, sfrido. Si riempie per distillazione in canonizzazione: un file server vero non contiene glossari. |
| `docs` | «procedure intere» | Le procedure complete e i documenti normativi interni: SOP, istruzioni operative, manuale HACCP, regulatory & compliance, data architecture, financial blueprint, culture book. La procedura intera sta qui; il concetto che usa sta in concepts; il registro che produce sta in data. |
| `entities` | «schede dei nomi propri» | Le schede di chi ha un nome proprio: clienti (Tosano, Famila...), fornitori (Molino Veneto, Criotech, Flexipack...), persone (Bertoldi, Fantin, Marchetti...), enti e istituzioni (CSQA, ATS, ULSS 9), prodotti (AF-SN-0450...), macchine e impianti (PKM-450, PT-104, MD-3200). Una scheda per entità, con gli alias nel frontmatter. |
| `data` | «i numeri» | Le note che presidiano i numeri: financials, operations, quality, sales & marketing — KPI, budget, consuntivi, serie. La nota inquadra e collega; il file di calcolo grezzo resta in sources ed è citato come fonte. |
| `code` | «script e automazioni» | Script e automazioni dell'ecosistema: data-logging IoT dei PLC con alert sui CCP, integrazione EDI-ERP, scheduling FEFO, digitalizzazione DDT via OCR, la pipeline RAG. Nel vault vive la nota che documenta lo script; i sorgenti vivono nel repository (config C in 05_rag_produzione, strumenti e suite QA in 06_operativo/qa). |
| `outputs` | «deliverable finiti» | Ciò che esce verso l'esterno in forma finita: offerte e presentazioni commerciali, contratti e documenti legali, comunicazioni societarie e finanziarie, documenti ufficiali di qualità. Se è una bozza, non è ancora qui: è in workspace. |
| `workspace` | «bozze e diario» | Il diario delle sessioni di lavoro (journal: sessioni e daily, sempre agganciate alle entità con wikilink) e le bozze in lavorazione. Materiale dinamico: escluso dai conteggi di qualità del vault insieme a sources. |

Regole trasversali già decise (vincolanti per metodo_03):

- I canali commerciali (LinkedIn, fiere, partner) sono TAG, mai cartelle: la stessa
  attività può valere per due canali e in cartella si duplicherebbe.
- Ogni cartella ha la sua nota `_index` (porta della cartella): percorso completo
  llms.txt → `_index` → hub → nota, zero note orfane.
- Il frontmatter è la verità macchina, la cartella è la vetrina: una nota mal
  riposta resta trovabile e collegata.
- `concepts`, `code` e `workspace` si riempiono per distillazione e per lavoro
  vivo, non forzando documenti innaturali.
- Lo showcase (fotografia derivata del grafo) vive FUORI dal vault, in
  `06_operativo/showcase/`: le 11 cartelle restano 11. Nel vault, tra i derivati,
  vive solo `llms.txt`, perché serve alla navigazione ed è parte del sistema
  misurato.

## Il metabolismo del vault — passaggi fra cartelle

Principio madre: **le note non traslocano**. Una nota che cambia natura non cambia
cartella: cambia `stato` nel frontmatter e passa il testimone con un wikilink.
Percorsi stabili significano fonti stabili, misure confrontabili e storia git
leggibile. L'unica eccezione è `workspace`, il banco di bozza: da lì le bozze si
PROMUOVONO alla cartella di destinazione quando sono finite (il journal, invece,
non trasloca mai).

| Transizione | Quando scatta | Come si esegue |
|---|---|---|
| `projects` → `areas` | il progetto genera una gestione continua (il tunnel a regime diventa manutenzione; la certificazione ottenuta diventa mantenimento in QA) | il progetto passa a `stato: chiuso` e resta in projects come storia; in areas nasce o si aggiorna la nota che eredita, con link «nato da [[progetto-…]]» |
| `projects` → `code` | il prodotto del progetto è un'automazione (OCR DDT, integrazione EDI-ERP, pipeline RAG) | progetto chiuso; in code la nota che documenta l'automazione ongoing (cosa fa, dove gira, chi la mantiene), linkata al progetto; il sorgente resta nel repository |
| `projects` → `outputs` | il progetto consegna un deliverable finito | il deliverable vive in outputs, linkato dal progetto; il progetto chiuso elenca i suoi esiti |
| `workspace` → `outputs`/`projects`/`areas` | la bozza è matura | promozione (spostamento) nella destinazione, oppure riscrittura come nota nuova con la bozza che resta a diario |
| `sources` → tutte | sempre | i grezzi non si muovono mai: generano note altrove, che li citano in `fonti` |
| `concepts`/`entities` ← tutte | una nota ha bisogno di un termine o di un nome proprio | la nota concetto/entità nasce (soglia: aggancio nel corpus, non citazione letterale) e da lì in poi si LINKA, non si ridefinisce: è così che «un fatto, un padrone» si mantiene nel tempo |

Frontmatter collegato: il campo `stato` ha vocabolario per type — per le note
conflitto `risolto | aperto`, per le note progetto `attivo | chiuso`.

Controllo QA collegato: ogni nota di progetto con `stato: chiuso` deve linkare
almeno un erede (in outputs, areas o code); un progetto chiuso senza eredi
dichiarati è un avviso.
