# -*- coding: utf-8 -*-
"""collaudo_suite — la suite QA trova tutto cio' che deve, sulle VIE CHE LA PRODUZIONE USA.

Costruisce un vault finto con TRE note di contenuto: una corretta, costruita su valori
riscontrati nei grezzi veri; una con sei difetti piantati apposta; e una TOCCATA, che non
cita nessun grezzo del lotto e porta un settimo difetto — serve a provare E32. Poi lancia
la suite e verifica che ciascun difetto sia stato trovato, che la nota corretta NON abbia
prodotto errori, e che non abbia prodotto nemmeno gli avvisi elencati in VIETATI — la
prova che un fix che allenta un controllo non ha aperto buchi.

=====================================================================================
LE VIE DI PRODUZIONE, E QUAL E' IL DIFETTO CHE CIASCUNA ESERCITA
=====================================================================================
metodo_03 non ha una sola porta d'ingresso alla suite, ne ha cinque, e un test che ne
prova una sola dichiara una copertura che non ha. §4.29 del passaggio di consegne:
IL COLLAUDO ESERCITA LA VIA CHE LA PRODUZIONE USA, NON UNA VIA EQUIVALENTE — almeno un
difetto piantato PER OGNI VIA, e l'elenco delle vie sta scritto qui, cosi' la copertura
si legge invece di presumerla.

  V1   qa_all --perimetro lotto @lotti/<lotto>.txt --lotto <n>
       Elenco delle note toccate letto per CONVENZIONE. E' la via dei lotti dal 1C in
       poi, ed e' la via principale: qui girano i SETTE difetti sostanziali.

  V2   la stessa, ma con --note-toccate ESPLICITO e nessun `<lotto>_note.txt` accanto
       all'elenco. metodo_03 §7 la dichiara («letto per convenzione, oppure passato con
       --note-toccate»). Difetto proprio: L'INOLTRO DEL FLAG. Prima del FIX 1 qa_all non
       passava --note-toccate ai figli, e ognuno si ricalcolava la convenzione da se':
       chi passava l'elenco esplicitamente se lo vedeva ignorare IN SILENZIO, con la QA
       verde e le note modificate fuori perimetro.

  V3   V1 piu' --pacchetto-giudizio. Difetto proprio: IL TESTO AGGIORNATO (E33) — il
       pacchetto deve riflettere il testo CORRENTE delle note. Il controllo esisteva
       gia', ma passava dai figli: qui passa dal lanciatore.

  V4   qa_all --perimetro vault. E' la via del gate e di ogni misura, e fino al
       19/08/2026 non era mai stata collaudata affatto. Difetto proprio: UN CONTROLLO
       CHE SOLO IL PERIMETRO VAULT EMETTE — le aree popolate (qa_copertura, blocco 4),
       che in perimetro di lotto non viene eseguito. Si verifica in due sensi: che V4 lo
       emetta, e che V1 NON lo emetta.

  V5   qa_all su perimetro di MANUTENZIONE: zero grezzi piu' elenco note (E35). Difetto
       proprio: IL PERIMETRO A ZERO GREZZI — la suite deve accettarlo, dichiararlo in
       chiaro nel report («0 grezzi, N note»), e vedere il difetto della nota. Qui si
       esercita anche il FIX 4: --lotto non e' passato, e l'etichetta del report deve
       prendere il nome dell'elenco, non il default `l26130`.

  V-neg  zero grezzi SENZA elenco note, e zero grezzi con elenco VUOTO: devono
       continuare a uscire in ERRORE. E' la guardia di E35, e una guardia che nessuno
       ha mai visto scattare non e' una guardia. Senza questo caso, la via piu' rapida
       per una QA verde diventerebbe cancellare l'elenco.

  ⚠️ VIA NON DI PRODUZIONE, e va detto: l'invocazione DIRETTA dei quattro figli, con
     --note-toccate esplicito. Nessun lotto la usa. Si tiene perche' serve a ISOLARE un
     guasto quando qa_all e' rosso — non a dimostrare copertura. Un test che non si sa a
     quale via appartiene conta come copertura per sbaglio, ed e' esattamente cosi' che
     «7 difetti su 7» ha significato per mesi piu' di quanto valeva.

=====================================================================================
IL LIMITE DEL NUMERO, ACCANTO AL NUMERO
=====================================================================================
⚠️ Fino al 19/08/2026 questo collaudo invocava i figli DIRETTAMENTE: «5 difetti su 5»
(pilota, lotto 1A) e «7 su 7» (gate 1C) provavano che i CONTROLLI funzionano, NON che
qa_all.py li chiamasse con gli argomenti giusti. La cifra e il suo limite devono
viaggiare insieme, o «7 su 7 verdi» continua a significare piu' di quanto vale.
Non invalida nessun lotto chiuso: la limitazione datata sta nel decision_log.md del
19/08/2026, e distingue il lotto 1C — dove la via per convenzione ha funzionato, ed e'
verificabile su disco — da pilota, 1A e 1B, che la convenzione non ha protetto perche'
non esisteva ancora (E32 nasce al gate di 1C).

⚠️ Due difetti sono piantati per i due emendamenti del gate 1C, che hanno chiuso
altrettanti buchi nel CICLO di controllo, non nelle note:
  - **E32** — una nota MODIFICATA dal lotto ma che non cita i suoi grezzi deve entrare
    nel perimetro se dichiarata in `<lotto>_note.txt`. Senza E32 il suo difetto passa.
  - **E33** — il pacchetto per lo strato di giudizio deve riflettere il testo CORRENTE
    delle note: se si genera prima delle correzioni, manda al giudice testo morto.

Un controllo che non e' stato collaudato non e' un controllo: e' una speranza.

⚠️ Questa cartella NON entra mai nel vault: e' banco di prova, non archivio.

Uso:  python collaudo_suite.py
Esce 0 se il collaudo passa, 1 altrimenti.
"""
import io, os, re, shutil, subprocess, sys

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.dirname(QUI)
sys.path.insert(0, QA)
VAULT = os.path.join(QUI, "vault_finto")
REPORT = os.path.join(QUI, "report")
LOTTI = os.path.join(QUI, "lotti")

# Gli elenchi delle VIE. Ognuno esiste per esercitare una via, e il nome lo dice:
# V1 ha il suo `_note.txt` accanto (convenzione); V2 non ce l'ha apposta, cosi' se il
# lanciatore non inoltra --note-toccate il difetto della nota toccata sparisce.
EL_V1        = os.path.join(LOTTI, "collaudo_v1.txt")
EL_V2        = os.path.join(LOTTI, "collaudo_v2.txt")
EL_V5        = os.path.join(LOTTI, "collaudo_v5.txt")
EL_NEG_SENZA = os.path.join(LOTTI, "collaudo_vneg_senza.txt")
EL_NEG_VUOTO = os.path.join(LOTTI, "collaudo_vneg_vuoto.txt")
ELENCO_TOCCATE = os.path.join(QUI, "note_toccate_collaudo.txt")

# --- i due grezzi veri su cui poggia il collaudo -----------------------------
LOG = "log_temperature_pastorizzatore_linea1_10_05_26.log"
OEE = "calcolo_sfrido_efficienza_OEE_linea_bakery.csv"
# grezzo FUORI dal perimetro del collaudo: la nota che lo cita entra solo per E32
SCHEDA = "scheda_manutenzione_ordinaria_forni_industrial.csv"

INDEX_AREAS = """\
---
title: "areas — collaudo"
summary: "Vault finto per il collaudo della suite QA: due note, una corretta e una con difetti piantati apposta."
type: index
tags: [areas, indice]
data_nota: 2026-08-16
---

# areas

Banco di prova della suite. Non e' un archivio.

## Hub
- [[area-qualita]] — l'hub d'area che regge le note del collaudo.

## Note che non stanno sotto un hub
- [[fatto-collaudo-toccata]] — la nota modificata dal lotto senza citarne i grezzi (E32).
"""

HUB = """\
---
title: "Qualita — hub di collaudo"
summary: "Hub d'area del vault finto, che elenca le due note su cui si collauda la suite QA."
type: hub
area: qualita
tags: [areas, qualita, collaudo]
fonti:
  - %s
stato: risolto
data_nota: 2026-08-16
related: "[[_index-areas]]"
---

# Qualita — hub di collaudo

Hub minimo, che serve solo a dare una radice alle due note del collaudo.

## Le note di questo tema
- [[fatto-collaudo-buono]] — la deviazione del 10/05, con valori riscontrati.
- [[fatto-collaudo-rotto]] — la stessa deviazione, con cinque difetti piantati.

## Fonti
- [[%s]] — riga 14:21:07
""" % (LOG, LOG)

BUONA = """\
---
title: "Deviazione di temperatura del 10/05/2026 — nota di collaudo corretta"
summary: "Il 10/05/2026 il datalogger del PT-104 registra 68,9 gradi al cuore alle 14:21:07 con flag di allarme, sul turno che il foglio OEE chiude a 36,5 alla riga n. 145."
type: atomica
area: qualita
tags: [areas, qualita, collaudo, ccp2]
fonti:
  - %s
  - %s
stato: risolto
aliases: []
data_fatto: 2026-05-10
data_nota: 2026-08-16
related: "[[area-qualita]]"
---

# Deviazione di temperatura del 10/05/2026 — nota di collaudo corretta

Il datalogger del pastorizzatore registra una temperatura al cuore di **68,9 °C**
alle 14:21:07 del 10/05/2026, con flag di allarme sul tracciato.

Lo stesso turno, sul foglio di efficienza, dichiara **5.580** pezzi prodotti e
**5.250** conformi su 14.400 teorici, con un OEE di **36,5** e **220** minuti di
fermo.

## Perche' conta

E' la nota di controllo del collaudo: ogni valore qui sopra e' stato riscontrato
nei due file citati, quindi la suite non deve emettere nessun ERRORE su di essa.
Si aggancia a [[area-qualita]] e alla sua gemella difettosa
[[fatto-collaudo-rotto]].

## Fonti
- [[%s]] — riga 14:21:07
- [[%s]] — riga 145, colonna `Pz_prodotti`
""" % (LOG, OEE, LOG, OEE)

# cinque difetti piantati, uno per riga di specifica:
#  1. fonte inventata          -> qa_frontmatter (non nel manifest)
#  2. numero senza riscontro   -> qa_provenance
#  3. wikilink rotto           -> qa_link_integrity
#  4. area fuori vocabolario   -> qa_frontmatter
#  6. summary multi-frase     -> qa_frontmatter. Piantato al gate del lotto 1B, quando
#     il conteggio delle frasi e' stato reso cieco ai punti di abbreviazione: questo
#     riassunto ha DUE frasi vere e dentro le abbreviazioni dell'elenco chiuso, quindi
#     dimostra che il fix non ha aperto un buco.
#  5. stato sbagliato          -> qa_frontmatter (chiuso fuori da projects\)
ROTTA = """\
---
title: "Deviazione di temperatura del 10/05/2026 — nota di collaudo difettosa"
summary: "La stessa deviazione della nota gemella, riscritta con sei difetti piantati apposta. Il riassunto ha due frasi vere e dentro le abbreviazioni n. e rev., cosi' il controllo deve segnalarlo lo stesso."
type: atomica
area: qualita-alimentare
tags: [areas, qualita, collaudo]
fonti:
  - %s
  - verbale_inesistente_2026.pdf
stato: chiuso
aliases: []
data_fatto: 2026-05-10
data_nota: 2026-08-16
related: "[[area-qualita]]"
---

# Deviazione di temperatura del 10/05/2026 — nota di collaudo difettosa

Il turno del 10/05/2026 ha prodotto **99999** pezzi, valore che non compare in
nessuna delle fonti citate.

Il rimando qui sotto punta a una nota che non esiste: [[nota-che-non-esiste-mai]].

## Fonti
- [[%s]] — riga 14:21:07
- [[verbale_inesistente_2026.pdf]] — pag. 1, §2
""" % (LOG, LOG)

# --- la nota TOCCATA: non cita i grezzi del lotto, e porta un difetto (E32) ---
# Difetto piantato: il numero 77777 non compare nella fonte citata. Se il perimetro di
# lotto non comprende le note modificate, questo errore non viene mai emesso.
TOCCATA = """\
---
title: "Nota toccata dal lotto senza citarne i grezzi"
summary: "Nota estesa durante il lotto ma costruita su un altro grezzo: serve a provare che il perimetro di lotto comprende anche cio' che il lotto ha modificato."
type: atomica
area: qualita
tags: [areas, qualita, collaudo, e32]
fonti:
  - %s
stato: risolto
aliases: []
data_nota: 2026-08-19
related: "[[area-qualita]]"
---

# Nota toccata dal lotto senza citarne i grezzi

Il piano di manutenzione registra 77777 interventi sul pastorizzatore: il numero non
compare in nessuna fonte citata, ed e' il difetto piantato per E32.

## Fonti
- [[%s]] — riga 20
""" % (SCHEDA, SCHEDA)


# --- cosa il collaudo PRETENDE di trovare -------------------------------------
ATTESI = [
    ("fonte inventata",        "qa_frontmatter",     r"verbale_inesistente_2026\.pdf.*manifest|manifest.*verbale_inesistente"),
    ("area fuori vocabolario", "qa_frontmatter",     r"qualita-alimentare.*vocabolario"),
    ("stato sbagliato",        "qa_frontmatter",     r"stato vuole risolto\|aperto"),
    ("wikilink rotto",         "qa_link_integrity",  r"wikilink rotto.*nota-che-non-esiste-mai"),
    ("summary multi-frase",     "qa_frontmatter",     r"fatto-collaudo-rotto.*?piu' di una frase"),
    ("numero senza riscontro", "qa_provenance",      r"99999|99\.999"),
    # E32: senza il perimetro esteso alle note modificate, questo difetto non viene emesso
    ("difetto in nota toccata", "qa_provenance",      r"fatto-collaudo-toccata.*77777|77777.*fatto-collaudo-toccata"),
]


# Cio' che la suite NON deve dire sulla nota CORRETTA, avvisi compresi. Nasce col fix del
# gate 1B: un fix che allenta un controllo si approva solo se il collaudo prova che non apre
# buchi, e la prova sta in due pezzi — il difetto piantato qui sopra, e questo divieto sul
# riassunto della nota buona, che porta un'abbreviazione ed e' una frase sola.
VIETATI = [
    ("summary multi-frase sulla nota corretta", r"piu' di una frase"),
]


def scrivi(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(t)


def prepara():
    if os.path.isdir(VAULT):
        shutil.rmtree(VAULT)
    if os.path.isdir(LOTTI):
        shutil.rmtree(LOTTI)
    scrivi(os.path.join(VAULT, "areas", "_index-areas.md"), INDEX_AREAS)
    scrivi(os.path.join(VAULT, "areas", "area-qualita.md"), HUB)
    scrivi(os.path.join(VAULT, "areas", "fatto-collaudo-buono.md"), BUONA)
    scrivi(os.path.join(VAULT, "areas", "fatto-collaudo-rotto.md"), ROTTA)
    scrivi(os.path.join(VAULT, "areas", "fatto-collaudo-toccata.md"), TOCCATA)

    intestazione = "# elenco del collaudo - %s\n"
    nota_toccata = ("# E32 - la nota che il lotto ha modificato senza citarne i grezzi\n"
                    "fatto-collaudo-toccata\n")

    # V1 - la via per convenzione: l'elenco delle note sta ACCANTO a quello dei grezzi
    scrivi(EL_V1, intestazione % "V1, via per convenzione" + LOG + "\n" + OEE + "\n")
    scrivi(EL_V1[:-4] + "_note.txt", nota_toccata)

    # V2 - la via esplicita: NESSUN `<lotto>_note.txt` accanto, cosi' la convenzione non
    # puo' salvare il caso. Se il flag non viene inoltrato, il difetto della nota toccata
    # non viene emesso e la QA resta verde su una nota fuori perimetro.
    scrivi(EL_V2, intestazione % "V2, via esplicita" + LOG + "\n" + OEE + "\n")
    scrivi(ELENCO_TOCCATE, nota_toccata)

    # V5 - perimetro di MANUTENZIONE (E35): zero grezzi, l'elenco delle note e' il perimetro
    scrivi(EL_V5, "# MANUTENZIONE\n")
    scrivi(EL_V5[:-4] + "_note.txt", nota_toccata)

    # V-neg - le due forme della guardia: elenco note ASSENTE, ed elenco note VUOTO
    scrivi(EL_NEG_SENZA, "# MANUTENZIONE\n")
    scrivi(EL_NEG_VUOTO, "# MANUTENZIONE\n")
    scrivi(EL_NEG_VUOTO[:-4] + "_note.txt", "# nessuna nota: e' il caso negativo\n")

    subprocess.run([sys.executable, os.path.join(QA, "genera_llms.py"), "--vault", VAULT],
                   cwd=QA, capture_output=True, text=True)


# --------------------------------------------------------------- i lanci

def lancia_qa_all(argomenti, cartella):
    """Un giro di qa_all.py - il LANCIATORE, che e' cio' che la produzione usa davvero."""
    d = os.path.join(REPORT, cartella)
    if os.path.isdir(d):
        shutil.rmtree(d)
    r = subprocess.run([sys.executable, os.path.join(QA, "qa_all.py")] + argomenti
                       + ["--vault", VAULT, "--report", d],
                       cwd=QA, capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return (r.stdout or "") + (r.stderr or ""), r.returncode, d


def per_script(uscita):
    """La stdout di qa_all, ritagliata per figlio: i sette regex vivono sulle righe dei figli."""
    pezzi, corrente = {}, None
    for riga in uscita.splitlines():
        m = re.match(r"^=== (\S+\.py) ===$", riga.strip())
        if m:
            corrente = m.group(1).replace(".py", "")
            pezzi[corrente] = []
            continue
        if corrente:
            pezzi[corrente].append(riga)
    return {k: "\n".join(v) for k, v in pezzi.items()}


def esegui_diretto():
    """VIA NON DI PRODUZIONE - i quattro figli invocati uno per uno.

    Nessun lotto la usa: serve a ISOLARE un guasto quando qa_all e' rosso. Non conta come
    copertura, e il suo esito non entra nel verdetto delle vie.
    """
    d = os.path.join(REPORT, "diretto")
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    out = {}
    for s in ("qa_frontmatter.py", "qa_link_integrity.py", "qa_provenance.py", "qa_copertura.py"):
        r = subprocess.run(
            [sys.executable, os.path.join(QA, s), "--perimetro", "lotto", LOG, OEE,
             "--note-toccate", ELENCO_TOCCATE, "--vault", VAULT, "--report", d],
            cwd=QA, capture_output=True, text=True, encoding="utf-8", errors="replace")
        out[s.replace(".py", "")] = (r.stdout or "") + (r.stderr or "")
    return out


def collaudo_pacchetto_giudizio():
    """V3 / E33: il pacchetto riflette il testo CORRENTE delle note, non quello di prima.

    Si genera il pacchetto DAL LANCIATORE, si modifica una nota, si rigenera: se il
    pacchetto non cambia - o se il testo nuovo non c'e' dentro - vuol dire che al giudice si
    puo' mandare testo morto senza accorgersene, che e' esattamente cio' che e' successo al
    primo giro del lotto 1C.
    """
    def genera():
        lancia_qa_all(["--perimetro", "lotto", "@" + EL_V1, "--lotto", "collaudo-v3",
                       "--pacchetto-giudizio"], "v3")
        p = os.path.join(REPORT, "v3", "pacchetto_giudizio_provenance.txt")
        return io.open(p, encoding="utf-8").read() if os.path.isfile(p) else ""

    prima = genera()
    nota = os.path.join(VAULT, "areas", "fatto-collaudo-toccata.md")
    testo = io.open(nota, encoding="utf-8").read()
    marcatore = "FRASE-CORRETTA-DOPO-IL-PACCHETTO"
    io.open(nota, "w", encoding="utf-8").write(testo.replace("## Fonti", marcatore + "\n\n## Fonti"))
    dopo = genera()
    io.open(nota, "w", encoding="utf-8").write(testo)          # si rimette com'era

    return bool(prima) and (prima != dopo) and (marcatore in dopo)


# --------------------------------------------------------------- il verdetto

def registra(esiti, via, etichetta, ok):
    esiti.append((via, etichetta, ok))
    print("%-5s %-56s %s" % (via, etichetta, "TROVATO" if ok else "*** NON TROVATO ***"))


def main():
    prepara()
    esiti = []          # (via, etichetta, ok) - il verdetto si legge VIA PER VIA

    # ---------------- V1: la via dei lotti, per convenzione ----------------------
    print("=" * 78)
    print("V1 - qa_all --perimetro lotto @lotti/collaudo_v1.txt --lotto collaudo-v1")
    print("     elenco delle note toccate letto per CONVENZIONE - la via dei lotti dal 1C")
    print("=" * 78)
    out_v1, _cod_v1, _d1 = lancia_qa_all(
        ["--perimetro", "lotto", "@" + EL_V1, "--lotto", "collaudo-v1"], "v1")
    figli_v1 = per_script(out_v1)
    for etichetta, script, rx in ATTESI:
        testo = figli_v1.get(script, "")
        registra(esiti, "V1", etichetta, re.search(rx, testo, re.I | re.S) is not None)

    # ---------------- V2: la via esplicita, che il FIX 1 ha sanato ----------------
    print("\n" + "=" * 78)
    print("V2 - la stessa via, con --note-toccate ESPLICITO e nessun `_note.txt` accanto")
    print("     difetto proprio: l'INOLTRO DEL FLAG dal lanciatore ai figli (FIX 1)")
    print("=" * 78)
    out_v2, _cod_v2, _d2 = lancia_qa_all(
        ["--perimetro", "lotto", "@" + EL_V2, "--lotto", "collaudo-v2",
         "--note-toccate", ELENCO_TOCCATE], "v2")
    figli_v2 = per_script(out_v2)
    rx_toccata = r"fatto-collaudo-toccata.*77777|77777.*fatto-collaudo-toccata"
    registra(esiti, "V2", "difetto in nota toccata, elenco passato col flag",
             re.search(rx_toccata, figli_v2.get("qa_provenance", ""), re.I | re.S) is not None)

    # ---------------- V3: il pacchetto per il giudizio, dal lanciatore ------------
    print("\n" + "=" * 78)
    print("V3 - qa_all ... --pacchetto-giudizio   difetto proprio: il TESTO AGGIORNATO (E33)")
    print("=" * 78)
    registra(esiti, "V3", "il pacchetto del giudizio riflette il testo corrente",
             collaudo_pacchetto_giudizio())

    # ---------------- V4: il perimetro vault, mai collaudato prima d'oggi ---------
    print("\n" + "=" * 78)
    print("V4 - qa_all --perimetro vault   la via del gate e di ogni misura")
    print("     difetto proprio: un controllo che SOLO il perimetro vault emette")
    print("=" * 78)
    out_v4, _cod_v4, _d4 = lancia_qa_all(["--perimetro", "vault"], "v4")
    figli_v4 = per_script(out_v4)
    rx_area = r"l'area 'commerciale' non ha il suo hub"
    registra(esiti, "V4", "aree popolate: il controllo e' emesso a perimetro vault",
             re.search(rx_area, figli_v4.get("qa_copertura", ""), re.I) is not None)
    registra(esiti, "V4", "...e NON e' emesso a perimetro lotto - e' cio' che lo rende suo",
             re.search(rx_area, figli_v1.get("qa_copertura", ""), re.I) is None)

    # ---------------- V5: il perimetro di manutenzione (E35) ----------------------
    print("\n" + "=" * 78)
    print("V5 - qa_all su perimetro di MANUTENZIONE: zero grezzi + elenco note (E35)")
    print("     senza --lotto: l'etichetta del report deve venire dall'elenco (FIX 4)")
    print("=" * 78)
    out_v5, cod_v5, dir_v5 = lancia_qa_all(["--perimetro", "lotto", "@" + EL_V5], "v5")
    figli_v5 = per_script(out_v5)
    registra(esiti, "V5", "il perimetro a zero grezzi e' accettato, non esce in errore",
             "richiede l'elenco dei grezzi" not in out_v5 and cod_v5 in (0, 1, 2))
    registra(esiti, "V5", "difetto in nota toccata visto col perimetro a zero grezzi",
             re.search(rx_toccata, figli_v5.get("qa_provenance", ""), re.I | re.S) is not None)
    p_v5 = os.path.join(dir_v5, "qa_all.md")
    testo_v5 = io.open(p_v5, encoding="utf-8").read() if os.path.isfile(p_v5) else ""
    registra(esiti, "V5", "il report DICHIARA «perimetro di manutenzione: 0 grezzi, N note»",
             re.search(r"perimetro di manutenzione: 0 grezzi, \d+ note", testo_v5) is not None)
    registra(esiti, "V5", "FIX 4: l'etichetta del lotto viene dall'elenco, non dal default",
             ("collaudo_v5" in testo_v5) and ("l26130" not in testo_v5))

    # ---------------- V-neg: la guardia di E35 deve scattare ----------------------
    print("\n" + "=" * 78)
    print("V-neg - zero grezzi SENZA elenco note, e con elenco VUOTO: devono uscire in ERRORE")
    print("=" * 78)
    for etichetta, elenco, cartella in (
            ("elenco delle note ASSENTE", EL_NEG_SENZA, "vneg_senza"),
            ("elenco delle note VUOTO", EL_NEG_VUOTO, "vneg_vuoto")):
        out_n, cod_n, _dn = lancia_qa_all(["--perimetro", "lotto", "@" + elenco], cartella)
        registra(esiti, "Vneg", "la guardia scatta - " + etichetta,
                 cod_n != 0 and "richiede l'elenco dei grezzi" in out_n)

    # ---------------- i falsi positivi, sulla via principale ----------------------
    print("\n" + "=" * 78)
    print("COLLAUDO - cosa NON doveva segnalare (la nota corretta), su V1")
    print("=" * 78)
    falsi = []
    for testo in figli_v1.values():
        for riga in testo.splitlines():
            if riga.startswith("ERRORE") and "fatto-collaudo-buono" in riga:
                falsi.append(riga.strip())
    if falsi:
        for r in falsi:
            print("*** FALSO POSITIVO ***  " + r)
    else:
        print("nessun ERRORE sulla nota corretta: la suite non spara sui vivi.")

    avvisi_buona = [r.strip() for t in figli_v1.values() for r in t.splitlines()
                    if r.startswith("AVVISO") and "fatto-collaudo-buono" in r]
    if avvisi_buona:
        print("\n(avvisi sulla nota corretta, ammessi e non bloccanti:)")
        for r in avvisi_buona:
            print("   " + r)

    print("\n" + "=" * 78)
    print("COLLAUDO - cosa NON doveva dire, nemmeno come avviso")
    print("=" * 78)
    for etichetta, rx in VIETATI:
        colpiti = [r for r in avvisi_buona if re.search(rx, r, re.I)]
        print("%-56s %s" % (etichetta, "assente, bene" if not colpiti else "*** COMPARSO ***"))
        falsi += colpiti

    # ---------------- la via NON di produzione, dichiarata come tale --------------
    print("\n" + "=" * 78)
    print("VIA NON DI PRODUZIONE - i quattro figli invocati direttamente")
    print("     isola un guasto quando qa_all e' rosso; NON conta come copertura")
    print("=" * 78)
    out_dir = esegui_diretto()
    visti = sum(1 for _e, s, rx in ATTESI if re.search(rx, out_dir.get(s, ""), re.I | re.S))
    print("diagnostica: %d/%d difetti visti per invocazione diretta (fuori dal verdetto)"
          % (visti, len(ATTESI)))

    # ---------------- il verdetto, VIA PER VIA e non aggregato --------------------
    print("\n" + "=" * 78)
    print("VERDETTO - via per via. Un totale aggregato nasconde proprio cio' che §4.29")
    print("           esiste per scoprire: quale via non e' esercitata da nessuno.")
    print("=" * 78)
    conteggio = {}
    for via, _etichetta, ok in esiti:
        t, o = conteggio.get(via, (0, 0))
        conteggio[via] = (t + 1, o + (1 if ok else 0))
    print("| Via   | Attesi | Visti |")
    print("|-------|--------|-------|")
    for via in ("V1", "V2", "V3", "V4", "V5", "Vneg"):
        if via in conteggio:
            tot, ok = conteggio[via]
            print("| %-5s | %6d | %5d%s |" % (via, tot, ok, "" if ok == tot else " ***"))
    mancati = ["%s / %s" % (via, etichetta) for via, etichetta, ok in esiti if not ok]

    print("")
    if mancati or falsi:
        print("COLLAUDO FALLITO")
        for m in mancati:
            print("  - difetto non visto: " + m)
        if falsi:
            print("  - falsi positivi: %d" % len(falsi))
        print("")
        print("Un difetto non visto significa che il FIX corrispondente NON e' finito:")
        print("non si chiude, e lo si dice nel rapporto (passaggio di consegne, 4.29).")
        return 1
    tot = len(esiti)
    print("COLLAUDO SUPERATO - %d difetti su %d, su TUTTE E CINQUE le vie di produzione" % (tot, tot))
    print("          piu' il caso negativo, 0 falsi positivi e 0 avvisi vietati sulla")
    print("          nota corretta. Il numero vale per le vie che ha esercitato: e' per")
    print("          questo che l'elenco delle vie sta nel docstring, e il verdetto e'")
    print("          una tabella e non un totale.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
