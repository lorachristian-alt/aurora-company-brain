# -*- coding: utf-8 -*-
"""candidate_r1 — il perimetro del lotto R1, generato da script e mai a memoria.

E35 lo impone: in un lotto di manutenzione **l'elenco delle note lo genera uno script**, e
il criterio con cui lo genera **si scrive nel rapporto**. Un perimetro composto a memoria si
restringe da se', e si restringe proprio sulle note che hanno piu' probabilita' di essere
sfuggite - che sono le stesse che sono sfuggite la prima volta.

IL CRITERIO, in due condizioni che devono valere INSIEME:

  1. la nota **nomina** almeno una delle cinque cose che una fonte prescrittiva governa:
     un punto critico, una taratura o convalida, una frequenza di verifica, un limite, o
     una responsabilita' di processo;
  2. e fra le sue `fonti` **non c'e' la fonte prescrittiva che governa quella famiglia**.
     Per quattro famiglie su cinque questo vuol dire «nessuna fonte prescrittiva», che e' il
     criterio dettato in apertura del lotto. Per la famiglia **punto critico** vuol dire
     specificamente **il manuale HACCP**, e il rafforzamento e' deliberato.

  ⚠️ PERCHE' LA QUINTA FAMIGLIA E' TRATTATA A PARTE, ed e' una correzione al criterio
  dettato, non un capriccio: col criterio generale, **26 note che nominano un punto critico
  senza citare il manuale HACCP uscivano dal perimetro** perche' citavano UN'ALTRA fonte
  prescrittiva - l'elenco delle attrezzature, la checklist del metal detector, il piano di
  manutenzione. Ma il limite critico di un CCP lo prescrive **il manuale**, non il registro
  degli strumenti: `fatto-strumenti-cf-02-e-ccp4` nomina il CCP4 e cita i due registri della
  metrologia, e nessuno dei due dice quale sia il limite critico di quel punto. Lasciarle
  fuori avrebbe fatto mancare a R1 **esattamente le note che lo hanno generato**. Il criterio
  vero e': una nota deve avere sotto mano la fonte che prescrive **cio' di cui parla**, non
  una fonte prescrittiva qualsiasi.

Se valgono entrambe, la nota discute una cosa prescritta senza avere sotto mano il
documento che la prescrive: e' esattamente la classe di difetto che il gate del lotto 1C ha
scoperto, dove in QUATTRO casi su undici la nota **dichiarava mancante** cio' che il manuale
HACCP contiene per esteso.

⚠️ **Il criterio e' deliberatamente LARGO sulla condizione 1.** Il costo di guardare una
nota che non ne aveva bisogno e' un minuto, e si chiude dichiarando che la fonte non serve -
che e' cio' che E29 prescrive di fare. Il costo di NON guardarne una che ne aveva bisogno e'
una nota che afferma il falso dentro la misura «dopo». ⚠️ Lo script **non giudica se la
verticale sia stata fatta BENE**: dice soltanto se la fonte che governa quella famiglia e'
fra le fonti. Il giudizio e' lavoro del lotto.

⚠️ **Il numero di partenza noto e' 30**, dal §11 del rapporto del lotto 1C: le note che
nominano un CCP senza citare il manuale HACCP. Lo script ne trova **40** per quella sola
famiglia, e **71** col criterio completo. **Vince lo script**, e la differenza si spiega nel
rapporto: la famiglia «punto critico» qui e' piu' larga di «nomina un CCP» - comprende anche
`limite critico`, `HACCP`, `prerequisito`, `PRP` - e le altre quattro famiglie non erano
state contate affatto al gate di 1C, dove si guardava il solo manuale.

Cosa resta fuori, e non e' una scelta di comodo: gli `_index` (apparato di navigazione), le
note-strumento del progetto (E20: documentano attrezzi, non fatti dell'azienda), le note di
diario e tutto cio' che sta in `workspace\\` e `sources\\` (metodo_03 §7.0).

Uso:
    python candidate_r1.py               # scrive gli elenchi del lotto e stampa il riepilogo
    python candidate_r1.py --stdout      # solo riepilogo, non scrive niente
Esce 0 se l'elenco e' stato prodotto, 1 se e' vuoto (un perimetro vuoto e' un errore).
"""
import argparse, io, os, re, sys
from datetime import date

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q
from elenco_fonti_prescrittive import FONTI

LOTTO = "r1_riconciliazione_verticale"
DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
EL_GREZZI = os.path.join(DIR_LOTTI, LOTTO + ".txt")
EL_NOTE = os.path.join(DIR_LOTTI, LOTTO + "_note.txt")

PRESCRITTIVE = {nome for nome, _classe, _cosa in FONTI}
MANUALE_HACCP = "manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt"

# Quale fonte prescrittiva GOVERNA una famiglia. Dove la famiglia non compare qui, vale
# «una fonte prescrittiva qualsiasi», che e' il criterio dettato in apertura del lotto.
GOVERNA = {
    "punto critico": {MANUALE_HACCP},
}

# Le cinque famiglie della condizione 1. Ogni famiglia dichiara che cosa cerca, perche' il
# criterio va scritto nel rapporto e un'espressione regolare senza nome non e' un criterio.
FAMIGLIE = [
    ("punto critico", [
        r"\bCCP\s?-?\s?\d\b", r"\bCCP\b", r"punt[oi] critic", r"limit[ei] critic",
        r"\bHACCP\b", r"\bprerequisit", r"\bPRP\b",
    ]),
    ("taratura o convalida", [
        r"taratur", r"ritaratur", r"convalid", r"riferibilit", r"\bcertificat[oi] di taratura",
        r"\bmetrologi",
    ]),
    ("frequenza di verifica", [
        r"frequenz", r"periodicit", r"\bcadenz", r"ogni\s+\d+\s*(mesi|anni|ore|giorni)",
        r"semestral", r"trimestral", r"quadrimestral", r"annual[ei]\b", r"mensil",
        r"scadenz[ae]\b", r"\bscadut",
    ]),
    ("limite o soglia", [
        r"\blimit[ei]\b", r"\bsogli[ae]\b", r"\btett[oi]\b", r"\bmassim[oa]\b", r"\bminim[oa]\b",
        r"\bLIM\s*=", r"valore di allarme", r"\ballarm",
    ]),
    ("responsabilità di processo", [
        r"responsabil", r"chi risponde", r"\bincaricat", r"\bprepost", r"\bdeleg",
        r"a cura di\b", r"\besecutor", r"\bapprovaz",
    ]),
]
FAMIGLIE = [(nome, [re.compile(r, re.I) for r in rx]) for nome, rx in FAMIGLIE]


def testo_della_nota(n):
    """title + summary + corpo senza il blocco Fonti: si cerca cio' che la nota AFFERMA,
    non i nomi dei file che cita - altrimenti «taratura» nel nome di un grezzo basterebbe."""
    fm = n.fm or {}
    return "\n".join([str(fm.get("title") or ""), str(fm.get("summary") or ""),
                      n.corpo_senza_fonti or ""])


def famiglie_toccate(testo):
    return [nome for nome, rx in FAMIGLIE if any(r.search(testo) for r in rx)]


def main():
    ap = argparse.ArgumentParser(description="Genera il perimetro di note del lotto R1.")
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    note = Q.tutte_le_note()
    candidate, gia_coperte, fuori_classe = [], [], 0

    for n in note:
        if n.cartella in Q.ESCLUSE_QUALITA or n.type in ("index", "sessione", "daily") \
                or n.fm is None or Q.e_nota_strumento(n):
            fuori_classe += 1
            continue
        fam = famiglie_toccate(testo_della_nota(n))
        if not fam:
            continue
        fonti = {str(f) for f in n.fonti}
        # una famiglia e' SCOPERTA se la nota non cita nessuna delle fonti che la governano
        scoperte = [f for f in fam if not (fonti & GOVERNA.get(f, PRESCRITTIVE))]
        if scoperte:
            candidate.append((n, scoperte))
        else:
            gia_coperte.append((n, fam, sorted(fonti & PRESCRITTIVE)))

    candidate.sort(key=lambda c: (c[0].cartella, c[0].slug))

    # ---- il riepilogo, che e' cio' che va nel rapporto -------------------------
    print("=" * 78)
    print("PERIMETRO DEL LOTTO R1 — riconciliazione verticale")
    print("generato da candidate_r1.py il %s" % date.today().isoformat())
    print("=" * 78)
    print("Note del vault ................................ %d" % len(note))
    print("  escluse per classe (_index, strumento, diario,")
    print("  workspace\\, sources\\) ....................... %d" % fuori_classe)
    print("  valutate ..................................... %d" % (len(note) - fuori_classe))
    print("")
    print("Nominano qualcosa che una fonte prescrittiva governa:")
    print("  e CITANO gia' una fonte prescrittiva ......... %d  (fuori perimetro)" % len(gia_coperte))
    print("  e NON ne citano nessuna ...................... %d  <-- IL PERIMETRO" % len(candidate))
    print("")
    conta_fam = {}
    for _n, fam in candidate:
        for f in fam:
            conta_fam[f] = conta_fam.get(f, 0) + 1
    print("| Famiglia nominata | Note candidate |")
    print("|---|---|")
    for nome, _rx in FAMIGLIE:
        print("| %s | %d |" % (nome, conta_fam.get(nome, 0)))
    print("")
    per_cartella = {}
    for n, _f in candidate:
        per_cartella[n.cartella] = per_cartella.get(n.cartella, 0) + 1
    print("| Cartella | Note candidate |")
    print("|---|---|")
    for c in sorted(per_cartella):
        print("| `%s\\` | %d |" % (c, per_cartella[c]))
    print("")
    print("Le note gia' coperte, e da quale fonte prescrittiva:")
    for n, _fam, pres in sorted(gia_coperte, key=lambda g: g[0].slug):
        print("  %-58s %s" % (n.slug, ", ".join(pres)))

    if args.stdout:
        return 0 if candidate else 1

    if not candidate:
        print("\nERRORE: perimetro vuoto. Un elenco di note vuoto non e' un lotto di")
        print("manutenzione: e' un errore, e la guardia di E35 lo rifiuta.")
        return 1

    os.makedirs(DIR_LOTTI, exist_ok=True)
    with io.open(EL_GREZZI, "w", encoding="utf-8", newline="\n") as f:
        f.write("# MANUTENZIONE\n")
        f.write("# Lotto R1 - riconciliazione verticale. Nessun grezzo nuovo si canonizza qui:\n")
        f.write("# si riparano note gia' scritte (E35, metodo_03 §9.4-bis). Il perimetro vero\n")
        f.write("# e' l'elenco delle note qui accanto, %s.\n" % os.path.basename(EL_NOTE))
    with io.open(EL_NOTE, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Perimetro del lotto R1, GENERATO da 06_operativo\\candidate_r1.py il %s.\n"
                % date.today().isoformat())
        f.write("# Criterio: la nota nomina un punto critico, una taratura, una frequenza di\n")
        f.write("# verifica, un limite o una responsabilita' di processo, e fra le sue fonti\n")
        f.write("# non c'e' nessuna fonte prescrittiva (elenco di E29). Non si edita a mano:\n")
        f.write("# si rilancia lo script. Le note che il lotto TOCCA in piu' si aggiungono\n")
        f.write("# mentre le si tocca (E32), sotto la riga di separazione.\n")
        for n, fam in candidate:
            f.write("%s\n" % n.slug)
        f.write("# --- da qui in giu': note toccate in corso di lotto (E32) ---\n")
    print("\nscritti:\n  %s\n  %s" % (EL_GREZZI, EL_NOTE))
    print("\nPerimetro: 0 grezzi, %d note." % len(candidate))
    return 0


if __name__ == "__main__":
    sys.exit(main())
