# -*- coding: utf-8 -*-
"""conta_perimetro_lotto — i numeri del perimetro di un lotto, letti e non ricomposti.

Nasce il 19/08/2026, e nasce da un difetto pagato: **la tabella §1 del rapporto di lotto era
l'ultimo posto del progetto dove i numeri si scrivevano a mano**, ed e' uscita sbagliata tre
volte su tre nello stesso rapporto in cui erano appena state sanate tre versioni divergenti
dello stesso conteggio di avvisi. La medicina e' quella di `conta_stato.py`, applicata
all'ultimo malato: **i numeri del perimetro si leggono dagli elenchi e dai report della suite,
o non si dichiarano.**

Che cosa legge, e da dove:
  - `qa\\lotti\\<lotto>.txt` .......... i grezzi del lotto. Un elenco che porta `# MANUTENZIONE`
    in testa e nessuna riga utile e' un **lotto di manutenzione** (E35), e lo si dice;
  - `qa\\lotti\\<lotto>_note.txt` ..... il perimetro delle note, in **tre sezioni**:
      1. le note **candidate**, generate dallo script che apre il lotto;
      2. le note **toccate** in corso di lotto, dichiarate mentre le si tocca (E32);
      3. le note **nate** nel lotto, dichiarate quando si creano.
    ⚠️ La distinzione fra toccate e nate **non si deduce a fine lotto**: si dichiara al
    momento, come E32 impone per le toccate. Un numero ricostruito a memoria e' esattamente
    cio' che questo script esiste per impedire;
  - il report della suite, per ERRORI e AVVISI e per la ripartizione degli avvisi in famiglie.

Uso:
    python conta_perimetro_lotto.py --lotto r1_riconciliazione_verticale
    python conta_perimetro_lotto.py --lotto <nome> --report <cartella del report>

Esce 0 se il perimetro e' leggibile, 1 se manca un elenco o se il perimetro e' vuoto.
"""
import argparse, io, os, re, sys
from datetime import date

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
DIR_QA = os.path.join(QUI, "qa")

SEP_TOCCATE = "note toccate in corso di lotto"
SEP_NATE = "note NATE in questo lotto"


def righe_utili(testo):
    return [r.strip() for r in testo.splitlines() if r.strip() and not r.strip().startswith("#")]


def sezioni_delle_note(percorso):
    """(candidate, toccate, nate). Le sezioni sono separate da righe di commento marcate."""
    testo = io.open(percorso, encoding="utf-8").read()
    blocchi, correnti = {"candidate": [], "toccate": [], "nate": []}, "candidate"
    for riga in testo.splitlines():
        s = riga.strip()
        if s.startswith("#"):
            if SEP_TOCCATE in s:
                correnti = "toccate"
            elif SEP_NATE in s:
                correnti = "nate"
            continue
        if s:
            blocchi[correnti].append(s)
    return blocchi["candidate"], blocchi["toccate"], blocchi["nate"]


def per_classe(slugs, note):
    """Ripartisce per classe: contenuto, `_index`, note-strumento, diario."""
    fuori = {"contenuto": [], "_index": [], "note-strumento": [], "diario": []}
    for s in slugs:
        n = note.get(s)
        if n is None:
            fuori["contenuto"].append(s)          # non trovata: la si dichiara comunque
        elif n.type == "index":
            fuori["_index"].append(s)
        elif Q.e_nota_strumento(n):
            fuori["note-strumento"].append(s)
        elif n.type in ("sessione", "daily"):
            fuori["diario"].append(s)
        else:
            fuori["contenuto"].append(s)
    return fuori


def esiti_della_suite(cartella):
    """(errori, avvisi, famiglie) dal report unico, riletti e non ricordati."""
    p = os.path.join(cartella, "qa_all.md")
    if not os.path.isfile(p):
        return None, None, {}
    t = io.open(p, encoding="utf-8").read()
    err = sum(int(x) for x in re.findall(r"- ERRORI: \*\*(\d+)\*\*", t))
    avv = sum(int(x) for x in re.findall(r"- AVVISI: \*\*(\d+)\*\*", t))
    famiglie = {}
    parti = re.split(r"^## (qa_\w+)", t, flags=re.M)
    for corpo in parti[2::2]:
        m = re.search(r"### Avvisi\n\n\| Nota \| Riga \| Controllo \| Rilievo \|\n\|---\|---\|---\|---\|\n((?:\|.*\n)+)",
                      corpo)
        if not m:
            continue
        for riga in m.group(1).splitlines():
            if not riga.startswith("|"):
                continue
            msg = riga.rsplit("|", 2)[-2].strip()
            chiave = re.sub(r"\d+", "N", msg)
            famiglie[chiave] = famiglie.get(chiave, 0) + 1
    return err, avv, famiglie


def main():
    ap = argparse.ArgumentParser(description="I numeri del perimetro di un lotto, da script.")
    ap.add_argument("--lotto", required=True)
    ap.add_argument("--report", default=None)
    args = ap.parse_args()

    el_grezzi = os.path.join(DIR_LOTTI, args.lotto + ".txt")
    el_note = os.path.join(DIR_LOTTI, args.lotto + "_note.txt")
    errori = []
    for p in (el_grezzi, el_note):
        if not os.path.isfile(p):
            errori.append("elenco mancante: %s" % p)
    if errori:
        for x in errori:
            print("ERRORE: " + x)
        return 1

    testa_grezzi = io.open(el_grezzi, encoding="utf-8").read()
    grezzi = righe_utili(testa_grezzi)
    # ⚠️ Il marcatore si cerca fra TUTTE le righe di commento in testa, non nella prima:
    # alla chiusura del lotto `# CHIUSO <data>` si mette in cima e sposta tutto di una riga.
    commenti = []
    for riga in testa_grezzi.splitlines():
        if riga.strip().startswith("#"):
            commenti.append(riga)
        elif riga.strip():
            break
    manutenzione = any("# MANUTENZIONE" in r for r in commenti)
    candidate, toccate, nate = sezioni_delle_note(el_note)
    tutte = candidate + toccate + nate

    if not tutte:
        print("ERRORE: perimetro vuoto. Un elenco di note vuoto non e' un lotto.")
        return 1

    note = {n.slug: n for n in Q.tutte_le_note()}
    mancanti = [s for s in tutte if s not in note]
    cl_nate = per_classe(nate, note)

    cartella = args.report
    if cartella is None:
        candidati = sorted(d for d in os.listdir(DIR_QA)
                           if d.endswith("_" + args.lotto) and os.path.isdir(os.path.join(DIR_QA, d)))
        cartella = os.path.join(DIR_QA, candidati[-1]) if candidati else None
    err, avv, famiglie = esiti_della_suite(cartella) if cartella else (None, None, {})

    print("<!-- PERIMETRO DEL LOTTO — generato da `06_operativo\\conta_perimetro_lotto.py`")
    print("     il %s. Si incolla VERBATIM nella tabella §1 del rapporto di lotto." % date.today().isoformat())
    print("     I numeri del perimetro non si ricompongono a mano. -->")
    print("")
    print("| Voce | Valore |")
    print("|---|---|")
    print("| Specie del lotto | **%s** |"
          % ("lotto di MANUTENZIONE (E35): perimetro di sole note" if manutenzione
             else "lotto di canonizzazione"))
    print("| Grezzi nell'elenco | **%d** |" % len(grezzi))
    print("| Note **candidate** dallo script di apertura | **%d** |" % len(candidate))
    print("| Note **toccate** in corso di lotto (E32) | **%d** |" % len(toccate))
    print("| Note **nate** nel lotto | **%d** — %s |"
          % (len(nate),
             " · ".join("%d %s" % (len(v), k) for k, v in cl_nate.items() if v) or "nessuna"))
    print("| **Note controllate in tutto** | **%d** |" % len(tutte))
    if err is not None:
        print("| Esito della suite | **%d ERRORI, %d AVVISI** |" % (err, avv))
    if famiglie:
        print("")
        print("| Famiglia di avviso | Quanti |")
        print("|---|---|")
        for k, v in sorted(famiglie.items(), key=lambda kv: -kv[1]):
            print("| %s | **%d** |" % (k[:110], v))
    print("")

    if mancanti:
        print("ERRORI: %d note dell'elenco non esistono nel vault" % len(mancanti))
        for s in mancanti:
            print("  - " + s)
        return 1
    print("Perimetro leggibile: %d grezzi, %d note (%d candidate + %d toccate + %d nate)."
          % (len(grezzi), len(tutte), len(candidate), len(toccate), len(nate)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
