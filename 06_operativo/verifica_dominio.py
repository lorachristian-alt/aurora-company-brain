# -*- coding: utf-8 -*-
"""verifica_dominio — E53: il dominio della riconciliazione verticale si VERIFICA, non si dichiara.

PERCHE' ESISTE, ed e' un errore pagato.
All'apertura del lotto 3A il prompt del gate scriveva «E37 non scatta: ne' il verbale ne' il
cruscotto sono fonti prescrittive». Era **formalmente corretto e sbagliato nel merito**: il
verbale di riesame CITAVA il criterio del mock recall di `PRO-QA-14` e lo CAMBIAVA, da quattro
ore a due. Il dominio c'era, e l'esenzione — dettata dall'alto, e percio' non contraddetta —
e' costata il quinto punto della serie dei due tassi (E41/E46), che 3A non ha.

⚠️ **Un'esenzione non si presenta come un ordine da verificare: si presenta come un lavoro che
non c'e' da fare**, e non esiste il gesto di verificare un lavoro che non si deve fare. Per
questo la risposta non poteva essere la diligenza e doveva essere uno script.

IL CRITERIO (E53, metodo_03 §9.5 passo 5-ter).
Il dominio si decide su **cio' che i grezzi FANNO**, non su cio' che sono. Un documento che
CITA un criterio prescrittivo entra nel dominio anche se non prescrive nulla di suo, e a
maggior ragione se lo CAMBIA. Un rapporto d'audit REGISTRA rilievi — ma un audit di schema
cita clausole e criteri per costruzione, e quindi il dominio quasi certamente c'e'.

COME CERCA, in due passate distinte e mai sommate:

  A. **le fonti prescrittive per nome.** Per ciascuna delle fonti dell'elenco si cercano nel
     testo di cantiere dei grezzi del lotto le SIGLE del nome del file (i pezzi in maiuscolo,
     con o senza cifre: `IO-05`, `PRO-QA-08`, `AUA`, `CPI`, `DVR`, `PKM450`) e i tokens lunghi
     e parlanti (`HACCP`, `allergeni`, `taratura`). ⚠️ I termini si derivano DAL NOME DEL FILE
     dell'elenco, non dalla memoria di chi apre il lotto: cosi' l'elenco resta il padrone e lo
     script non ha una seconda verita' dentro.

  B. **i marcatori di prescrizione senza nome.** Espressioni con cui un documento cita un
     criterio che non e' nel corpus o che non nomina: «clausola», «requisito», «ai sensi di»,
     «il piano prevede», «previsto da», un termine perentorio, un obbligo.
     ⚠️ Questa passata **non decide un dominio**: dice se il grezzo parla la lingua della
     prescrizione, e quindi se un «nessun dominio» va guardato due volte prima di crederci.

⚠️ **Lo script non conclude: MISURA.** «Nessun dominio» resta una dichiarazione di chi apre
il lotto, ma da qui in avanti si motiva con l'esito di questa ricerca — mai con la natura del
documento, e mai sulla parola di chi coordina.

⚠️ **Le fonti il cui lotto non e' ancora canonizzato si riportano, marcate `NON CITABILE`.**
Vale il limite di E29 e il divieto 9-bis: la nota non le cita e non ne scrive il contenuto,
ma il fatto che il grezzo le nomini e' un obbligo di tracciamento, non un silenzio.

Uso:
    python verifica_dominio.py --lotto lotto_03c_certificazione_audit
    python verifica_dominio.py --lotto <nome> --contesto 0   # senza le righe di riscontro
Esce sempre 0: e' una misura, non un cancello.
"""
import argparse, io, os, re, sys
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import estrazione_cantiere as EC
from elenco_fonti_prescrittive import FONTI, elenchi_dei_lotti

DIR_LOTTI = os.path.join(QUI, "qa", "lotti")

# I lotti gia' canonizzati: una fonte prescrittiva di un lotto che non c'e' ancora e' NON
# CITABILE (E29, e divieto 9-bis).
#
# ⚠️ QUESTO INSIEME SI LEGGE DAL DISCO, E NON SI SCRIVE A MANO. Fino al 23/08/2026 era una
# lista di nomi codificata qui dentro, ed era una COPIA di un fatto il cui padrone e' altrove:
# si e' disallineata in silenzio, come ogni copia. Al gate del lotto 3C portava
# `lotto_02b_autocontrollo_igiene`, **un nome morto dal 20/08** — quando il lotto 2B si spezzo'
# in apertura, l'elenco fu rinominato in `..._analitico` (registro delle modifiche della
# matrice) — e **non portava ne' `lotto_02b_autocontrollo_analitico`, ne'
# `lotto_03c_certificazione_audit`, ne' `r1_riconciliazione_verticale`, tutti CHIUSI**.
#
# ⚠️ IL COSTO SAREBBE STATO ESATTAMENTE QUELLO CHE E53 ESISTE PER IMPEDIRE: in apertura del
# lotto 3B lo script dichiarava `Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` NON CITABILE,
# quando 3C lo aveva canonizzato il giorno prima. Una fonte governante esclusa dalla
# dichiarazione del dominio e' il verso "troppo stretto" di E56, che in 2B-bis e' costato un
# 9,1 % gonfiato.
#
# ⚠️ E' la seconda volta che QUESTO script mente in silenzio: la prima fu il `` in coda alla
# sigla. **Uno script che tace non e' uno script che assolve** — e la difesa non e' rileggerlo
# meglio, e' togliergli le copie: il marcatore `# CHIUSO` in testa all'elenco e' lo stesso dato
# che `verifica_matrice_lotti.py` gia' pretende, e non puo' invecchiare separatamente.
def lotti_canonizzati():
    """I lotti chiusi, letti dal marcatore `# CHIUSO` in testa al loro elenco.

    Il pilota non ha un elenco — e' anteriore alla matrice — e si aggiunge per nome, con
    l'etichetta che `elenchi_dei_lotti()` gli da'.
    """
    fuori = {"pilota (fetta L26130)"}
    for n in sorted(os.listdir(DIR_LOTTI)):
        if not n.endswith(".txt") or n.endswith("_note.txt"):
            continue
        with io.open(os.path.join(DIR_LOTTI, n), encoding="utf-8") as fh:
            if fh.readline().lstrip().upper().startswith("# CHIUSO"):
                fuori.add(n[:-4])
    return fuori


CANONIZZATI = lotti_canonizzati()

# Parole del nome di un file che non identificano nulla: cercarle darebbe un riscontro
# ovunque. Non e' una lista di comodo — e' l'elenco delle parole con cui questo corpus dice
# «documento», e ogni voce sta qui perche' riscontrava dappertutto.
RUMORE = {
    "estratto", "reale", "aurora", "food", "group", "corpus", "documento", "allegato",
    "scheda", "elenco", "piano", "manuale", "contratto", "listino", "circolare", "mail",
    "rev", "pdf", "docx", "txt", "csv", "xlsx", "pptx", "eml", "log", "ocr", "firmato",
    "della", "delle", "degli", "dell", "sulla", "sulle", "per", "con", "del", "prodotto",
    "nuovo", "base", "tipo", "gestione", "tecnico", "tecnica", "interno", "aziendale",
}

# Una sigla: due o piu' fra maiuscole e cifre, eventualmente legate da trattino — `IO-05`,
# `PRO-QA-08`, `MOD-QA-12`, `HACCP`. ⚠️ Niente `\b` in coda: vedi la nota in `termini()`.
RX_SIGLA = re.compile(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)*(?![a-z])")

MARCATORI = [
    ("clausola di schema", r"\bcl(?:ausola)?\.?\s*\d+(?:\.\d+)+"),
    ("requisito", r"\brequisit[oi]\b"),
    ("ai sensi di / norma", r"\bai sensi\b|\bex\s+Reg\.|\bD\.Lgs\.|\bReg\.\s*(?:UE|CE)\b"),
    ("il piano/la procedura prevede", r"\b(?:il piano|la procedura|il protocollo|il regolamento)\s+(?:interno\s+)?(?:prevede|richiede|impone)"),
    ("previsto / prescritto da", r"\bprevist[oa]\s+d[ai]\b|\bprescritt[oa]\b|\bda protocollo\b|\bda piano\b"),
    ("termine imposto", r"\btermine\s+(?:ultimo|perentorio|di)\b|\bentro\s+\d+\s*(?:giorni|gg|mesi)\b|\bscadenza:"),
    ("obbligo di conformita'", r"\bdev[eo]no?\s+essere\b|\bdeve\s+\w+re\b|\bobbligo\b|\brichiest[ao]:"),
]
MARCATORI = [(n, re.compile(r, re.I)) for n, r in MARCATORI]


def termini(nome_file):
    """I termini del NOME della fonte prescrittiva, in DUE classi di forza.

    Il nome e' il padrone: lo script non conosce nessun termine che non venga da li'.

    ⚠️ **forte** = una SIGLA — `IO-05`, `HACCP`, `DVR`, `CPI`, `AUA`, `PKM450`. Una sigla
    dentro un documento e' una CITAZIONE: chi scrive «IO-05» sta indicando quel documento,
    non sta usando una parola della lingua.

    ⚠️ **debole** = una parola comune del nome — `certificato`, `manutenzione`, `produzione`,
    `febbraio`. Un riscontro debole non dimostra nulla da solo: al primo giro su 3C ne
    bastavano per far risultare «nominate» **28 fonti su 36**, cioe' quasi tutto l'elenco,
    e un elenco che dice sempre di si' non e' una verifica.

    ⚠️ **Le due classi si riportano separate e non si sommano MAI**, per la stessa ragione
    per cui il collaudo tiene distinti i difetti che scattano dai controlli di non-scatto.

    ⚠️ NOTA DI CANTIERE, 22/08/2026 — il primo `RX_SIGLA` finiva con `\b`, e fra la `I` di
    `CPI_certificato_...` e l'underscore **non c'e' un confine di parola**: l'underscore e'
    un carattere di parola. Ogni sigla del corpus veniva scartata in silenzio e restavano i
    soli riscontri deboli — 28 fonti su 36, che sembravano un dominio larghissimo e invece
    erano il rumore della lingua. Per questo il gambo si spezza sugli underscore PRIMA di
    cercare le sigle. ⚠️ **Uno script che tace non e' uno script che assolve.**
    """
    gambo = os.path.splitext(nome_file)[0]
    sigle = {s for s in RX_SIGLA.findall(gambo.replace("_", " "))
             if len(s) >= 3 and s.lower() not in RUMORE}
    tok = {t for t in re.split(r"[^A-Za-z0-9]+", gambo)
           if len(t) >= 5 and t.lower() not in RUMORE and not t.isdigit() and t not in sigle}
    return (sorted(sigle, key=lambda s: (-len(s), s)),
            sorted(tok, key=lambda s: (-len(s), s)))


def grezzi_del_lotto(lotto):
    p = os.path.join(DIR_LOTTI, lotto + ".txt")
    with open(p, encoding="utf-8") as fh:
        return [r.strip() for r in fh if r.strip() and not r.lstrip().startswith("#")]


def righe_con(testo, rx, quante=2):
    fuori = []
    for i, riga in enumerate(testo.splitlines(), 1):
        if rx.search(riga):
            fuori.append((i, riga.strip()[:104]))
            if len(fuori) >= quante:
                break
    return fuori


def fonti_normalizzate():
    """(nome, classe, cosa, lotto). ⚠️ Il lotto NON si scrive qui: si chiede a
    `elenchi_dei_lotti()`, che e' la funzione con cui lo script padrone dell'elenco lo
    ricava dagli elenchi veri. Due copie dello stesso mestiere divergono, e questa e'
    la meta' che divergerebbe in silenzio."""
    dove = elenchi_dei_lotti()
    for f in FONTI:
        yield f[0], f[1], f[2], dove.get(f[0], "(nessun lotto)")


def main():
    ap = argparse.ArgumentParser(description="E53 — verifica da script il dominio di un lotto.")
    ap.add_argument("--lotto", required=True)
    ap.add_argument("--contesto", type=int, default=2,
                    help="righe di riscontro per termine trovato (0 = nessuna)")
    a = ap.parse_args()

    grezzi = grezzi_del_lotto(a.lotto)
    testi = {g: EC.testo_cantiere(g) for g in grezzi}
    fonti = list(fonti_normalizzate())

    print("=" * 78)
    print("E53 - VERIFICA DEL DOMINIO: %s" % a.lotto)
    print("misura delle %s" % datetime.now().strftime("%H:%M:%S del %d/%m/%Y"))
    print("=" * 78)
    print("%d grezzi nel lotto, %d fonti prescrittive nell'elenco.\n" % (len(grezzi), len(fonti)))

    print("-" * 78)
    print("A. LE FONTI PRESCRITTIVE NOMINATE NEI GREZZI DEL LOTTO")
    print("-" * 78)
    forti, deboli = [], []
    for nome, _classe, _cosa, lotto_f in fonti:
        sigle, parole = termini(nome)
        colpi = {"sigla": [], "parola": []}
        for classe, elenco in (("sigla", sigle), ("parola", parole)):
            for g in grezzi:
                for t in elenco:
                    # ⚠️ La sigla si cerca CASE SENSITIVE: `AUA` e' una sigla, `aua` dentro
                    # una parola no. La parola comune, invece, si cerca ignorando il caso.
                    rx = re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])",
                                    0 if classe == "sigla" else re.I)
                    r = righe_con(testi[g], rx, max(a.contesto, 1))
                    if r:
                        colpi[classe].append((g, t, r))
        if colpi["sigla"]:
            forti.append((nome, lotto_f, lotto_f in CANONIZZATI, colpi))
        elif colpi["parola"]:
            deboli.append((nome, lotto_f, lotto_f in CANONIZZATI, colpi))

    print("\nA.1 RISCONTRI FORTI - la SIGLA della fonte compare nel grezzo: e' una citazione")
    if not forti:
        print("     nessuno.")
    for nome, lotto_f, canon, colpi in forti:
        stato = "CITABILE" if canon else "NON CITABILE - lotto %s non canonizzato" % lotto_f
        print("\n  %s   [%s]" % (nome, stato))
        for g, t, righe in colpi["sigla"]:
            print("    - <<%s>> in %s" % (t, g))
            for i, riga in righe[:a.contesto]:
                print("        riga %d: %s" % (i, riga))

    print("\nA.2 RISCONTRI DEBOLI - solo una parola comune del nome. NON dimostrano nulla da")
    print("    soli e NON si sommano ai forti: si guardano a mano, o si lasciano stare.")
    for nome, lotto_f, canon, colpi in deboli:
        parole = sorted({t for _g, t, _r in colpi["parola"]})
        print("  %-56s %s" % (nome[:56], ", ".join(parole[:6])))

    print()
    print("-" * 78)
    print("B. I MARCATORI DI PRESCRIZIONE (non decidono un dominio: lo mettono in dubbio)")
    print("-" * 78)
    for g in grezzi:
        conta = [(n, len(rx.findall(testi[g]))) for n, rx in MARCATORI]
        conta = [(n, k) for n, k in conta if k]
        print("\n  %s - %d riscontri" % (g, sum(k for _, k in conta)))
        for n, k in sorted(conta, key=lambda x: -x[1]):
            print("      %-34s %3d" % (n, k))

    print()
    print("=" * 78)
    print("ESITO: %d fonti CITATE PER SIGLA nei grezzi del lotto, di cui %d CITABILI (lotto"
          % (len(forti), sum(1 for _, _, c, _ in forti if c)))
    print("gia' canonizzato); %d fonti con i soli riscontri deboli, che non contano." % len(deboli))
    print("La dichiarazione del dominio, e la sua motivazione, stanno nel rapporto di lotto:")
    print("questo script misura, non conclude.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
