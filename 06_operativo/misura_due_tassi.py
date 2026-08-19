# -*- coding: utf-8 -*-
"""misura_due_tassi — il debito e la produzione, contati separatamente e mai mescolati.

Il lotto R1 ha misurato un tasso di difetto della riconciliazione verticale del **57,7 %**
su 71 note. Quel numero misura note scritte **prima** che E29 ed E36 esistessero: e'
l'ipotesi del **debito storico**, e da sola non dice niente su quanto il metodo, con la
regola in vigore, produca il difetto invece di ereditarlo.

Questo script produce i **DUE TASSI DISTINTI** che il gate del lotto R1 ha prescritto, e li
tiene separati perche' misurano due grandezze diverse:

  1. **TASSO DI RIAPERTURA — misura il DEBITO.** Quante note gia' scritte la riconciliazione
     verticale arretrata (E37) ha riaperto per questo lotto, e quante ne sono state corrette
     agganciandole alla prescrizione. Le altre si chiudono dichiarando che quella fonte non
     le governa, ed e' un esito legittimo: il criterio di apertura e' deliberatamente largo.

  2. **TASSO DI DIFETTO DI PRODUZIONE — misura il METODO.** Sulle note **nate** nel lotto,
     quante parlano del dominio prescrittivo del lotto **senza avere fra le proprie fonti**
     la fonte che quel dominio lo governa. E' lo stesso criterio di `candidate_r1.py`,
     applicato alle note nuove invece che a quelle vecchie.

⚠️ **E' il secondo a decidere.** Vicino a zero, il debito era storico e la rete finale
bastera'. Lontano da zero, E29 in vigore NON basta e la regola va ripensata, non ripetuta.

⚠️ **I due non si sommano e non si mediano.** Mescolarli e' lo stesso errore del calcolo
lineare che diede 903 note e 36 lotti: mettere insieme grandezze che non misurano la stessa
cosa. Lo script li stampa in due blocchi separati apposta.

⚠️ **Le note-strumento restano fuori** dal denominatore della produzione (E20): documentano
attrezzi del progetto, non fatti dell'azienda, e non hanno fonti da agganciare.

Uso:
    python misura_due_tassi.py --lotto lotto_02a_cip --dominio cip --corrette 4
Esce 0 sempre: e' una misura, non un controllo.
"""
import argparse, importlib.util, io, os, sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

_spec = importlib.util.spec_from_file_location("candidate_r1", os.path.join(QUI, "candidate_r1.py"))
C1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C1)


def sezioni(percorso):
    """Le tre sezioni dell'elenco delle note: candidate, toccate, nate."""
    sez, fuori = None, {"candidate": [], "toccate": [], "nate": []}
    for r in io.open(percorso, encoding="utf-8"):
        r = r.strip()
        if r.startswith("# --- da qui in giu': note toccate"):
            sez = "toccate"; continue
        if r.startswith("# --- da qui in giu': note NATE"):
            sez = "nate"; continue
        if not r or r.startswith("#"):
            continue
        fuori[sez or "candidate"].append(r)
    return fuori


def main():
    ap = argparse.ArgumentParser(description="I due tassi di un lotto: debito e produzione.")
    ap.add_argument("--lotto", required=True)
    ap.add_argument("--dominio", required=True, choices=sorted(C1.DOMINI))
    ap.add_argument("--corrette", type=int, required=True,
                    help="quante delle note riaperte sono state corrette agganciando la prescrizione")
    args = ap.parse_args()

    dom = C1.DOMINI[args.dominio]
    el = sezioni(os.path.join(QUI, "qa", "lotti", args.lotto + "_note.txt"))
    note = {n.slug: n for n in Q.tutte_le_note()}

    def stato(slug):
        """None = fuori classe · False = non parla del dominio · True = ne parla ed e' scoperta."""
        n = note.get(slug)
        if n is None or n.fm is None:
            return None
        if n.cartella in Q.ESCLUSE_QUALITA or n.type in ("index", "sessione", "daily") \
                or Q.e_nota_strumento(n):
            return None
        if not any(rx.search(C1.testo_della_nota(n)) for rx in dom["rx"]):
            return False
        return not ({str(f) for f in n.fonti} & dom["fonti"])

    riaperte = el["candidate"]
    print("=" * 74)
    print("I DUE TASSI DEL LOTTO %s — dominio «%s»" % (args.lotto, args.dominio))
    print("Si leggono separati: misurano due grandezze diverse e non si mediano.")
    print("=" * 74)

    print("\n--- 1. TASSO DI RIAPERTURA — misura il DEBITO -------------------------")
    print("note riaperte da `candidate_r1.py --dominio %s` ......... %d" % (args.dominio, len(riaperte)))
    print("  corrette agganciando la prescrizione .................. %d" % args.corrette)
    print("  chiuse dichiarando che la fonte non le governa ........ %d" % (len(riaperte) - args.corrette))
    if riaperte:
        print("TASSO DI RIAPERTURA ..................................... %.1f %%  (calcolato: %d su %d)"
              % (100.0 * args.corrette / len(riaperte), args.corrette, len(riaperte)))

    print("\n--- 2. TASSO DI DIFETTO DI PRODUZIONE — misura il METODO --------------")
    valutate, scoperte, fuori = [], [], []
    for s in el["nate"]:
        e = stato(s)
        if e is None:
            fuori.append(s)
        else:
            valutate.append(s)
            if e:
                scoperte.append(s)
    print("note NATE nel lotto ..................................... %d" % len(el["nate"]))
    print("  fuori classe: note-strumento del progetto (E20) ....... %d" % len(fuori))
    print("  valutate ............................................. %d" % len(valutate))
    print("  parlano del dominio SENZA la fonte che lo governa ..... %d" % len(scoperte))
    for s in scoperte:
        print("      - %s" % s)
    if valutate:
        print("TASSO DI DIFETTO DI PRODUZIONE .......................... %.1f %%  (calcolato: %d su %d)"
              % (100.0 * len(scoperte) / len(valutate), len(scoperte), len(valutate)))
    print("\n⚠️ Il secondo e' il numero che decide se E29 in vigore basti. Il primo dice")
    print("   soltanto quanto debito il lotto ha trovato dietro di se'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
