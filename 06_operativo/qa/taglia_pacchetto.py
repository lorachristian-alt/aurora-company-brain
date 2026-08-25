# -*- coding: utf-8 -*-
"""taglia_pacchetto — ritaglia il pacchetto del giudizio in fette, SENZA perdere le fonti.

Il pacchetto di un lotto denso non entra in un solo subagente. Si taglia in fette, e ogni
fetta va da un giudice diverso a contesto pulito.

=====================================================================================
PERCHE' QUESTO SCRIPT ESISTE, E PERCHE' HA UNA GUARDIA
=====================================================================================
⚠️ **Lo strumento di taglio del lotto R1 SCARTAVA l'appendice col testo estratto delle
fonti**, e i due giudici di quel giro si sono trovati a confrontare le note **con se'
stesse**. Se ne sono accorti da soli e hanno rifiutato di pronunciarsi — vedi §4.31 del
passaggio di consegne — e quel giro e' costato zero invece di produrre verdetti costruiti
sul nulla. E' la classe di difetto di §4.29: *un controllo che non e' nel percorso che si
esegue non e' un controllo*, applicata a un artefatto invece che a un test.

Percio' questo script:

  1. porta a OGNI fetta il testo estratto di **tutte le fonti che le note di quella fetta
     citano** — non un estratto, non un campione: il testo che il pacchetto contiene;
  2. **si rifiuta di scrivere una fetta priva di appendice**, o con l'appendice vuota. E'
     una GUARDIA, non un controllo di cortesia: una fetta senza fonti non e' una fetta
     piu' piccola, e' un ingresso degradato, e va trattata come un errore;
  3. stampa per ogni fetta quante note e quali fonti porta, cosi' la copertura si legge
     invece di presumerla.

Il taglio segue l'ordine del pacchetto e non spezza mai una nota.

Uso:
    python taglia_pacchetto.py --report <cartella> [--fette N]
Esce 0 se tutte le fette sono complete, 1 se anche una sola non lo e'.
"""
import argparse, io, os, re, sys

SEP_NOTA = ">>>>> NOTA DA GIUDICARE:"
# ⚠️ E10, SECONDO DELIMITATORE (lotto 3F): era `--- <nome> ---`, e quella forma COMPARE
# dentro i grezzi. La notifica ATS ne porta due, e la fonte principale del lotto arrivava
# al giudice troncata a 638 caratteri su 13.186 — in due fette su tre senza le mail.
SEP_FONTE = ">>>>> FONTE:"
TITOLO_APPENDICE = "TESTO ESTRATTO DELLE FONTI CITATE"


def spezza(testo):
    """(prologo, [(nome, corpo)], {fonte: testo}) — le tre parti del pacchetto."""
    i = testo.find(TITOLO_APPENDICE)
    if i < 0:
        raise SystemExit("ERRORE: il pacchetto non porta l'appendice delle fonti. "
                         "Non si taglia un pacchetto gia' degradato.")
    testa, coda = testo[:i], testo[i:]

    pezzi = re.split(r"\n-{60,}\n(?=%s)" % re.escape(SEP_NOTA), testa)
    prologo, note = pezzi[0], []
    for p in pezzi[1:]:
        m = re.match(r"%s\s*(\S+)" % re.escape(SEP_NOTA), p)
        if m:
            note.append((m.group(1), p))

    fonti, nome, buf = {}, None, []
    for riga in coda.split("\n"):
        m = re.match(r"^%s\s*(\S.*)$" % re.escape(SEP_FONTE), riga)
        if m:
            if nome:
                fonti[nome] = "\n".join(buf)
            nome, buf = m.group(1), []
        elif nome:
            buf.append(riga)
    if nome:
        fonti[nome] = "\n".join(buf)
    return prologo, note, fonti


def fonti_citate(corpo_nota, fonti):
    """Le fonti che quella nota nomina. Deliberatamente LARGO: nel dubbio la fonte si
    porta, perche' il costo di una fonte in piu' e' qualche riga, quello di una in meno
    e' un giudice che confronta la nota con se' stessa."""
    return [f for f in fonti if f in corpo_nota]


def main():
    ap = argparse.ArgumentParser(description="Taglia il pacchetto del giudizio in fette.")
    ap.add_argument("--report", required=True, help="cartella del report del lotto")
    ap.add_argument("--fette", type=int, default=3)
    args = ap.parse_args()

    sorgente = os.path.join(args.report, "pacchetto_giudizio_provenance.txt")
    testo = io.open(sorgente, encoding="utf-8").read()
    prologo, note, fonti = spezza(testo)

    print("pacchetto: %d note, %d fonti, %d caratteri" % (len(note), len(fonti), len(testo)))
    if not note:
        raise SystemExit("ERRORE: nessuna nota nel pacchetto.")

    per_fetta = (len(note) + args.fette - 1) // args.fette
    guasti = []
    for n in range(args.fette):
        blocco = note[n * per_fetta:(n + 1) * per_fetta]
        if not blocco:
            continue
        usate = sorted({f for _nome, corpo in blocco for f in fonti_citate(corpo, fonti)})

        r = [prologo.rstrip(), ""]
        r.append("=" * 70)
        r.append("FETTA %d DI %d — %d note da giudicare." % (n + 1, args.fette, len(blocco)))
        r.append("Giudichi SOLO le note di questa fetta, contro le fonti in coda a questo")
        r.append("file. ⚠️ Se l'appendice delle fonti mancasse o non contenesse i documenti")
        r.append("che le note citano, DICHIARA L'INGRESSO DEGRADATO e non emettere verdetti:")
        r.append("è un esito legittimo e vale più di un verdetto costruito sul nulla.")
        r.append("=" * 70)
        for _nome, corpo in blocco:
            r.append("\n" + "-" * 70)
            r.append(corpo.rstrip())
        r.append("\n\n" + "=" * 70)
        r.append(TITOLO_APPENDICE)
        r.append("=" * 70)
        for f in usate:
            r.append("\n%s %s" % (SEP_FONTE, f))
            r.append(fonti[f])
        fetta = "\n".join(r)

        # LA GUARDIA. Una fetta senza appendice, o con appendice vuota, non si scrive.
        # ⚠️ E DAL LOTTO 3F LA GUARDIA CONFRONTA I CARATTERI, non la presenza: l'appendice
        # deve portare OGNI fonte per intero, com'e' nel pacchetto. Un'appendice che c'e'
        # ma porta un decimo del documento e' un ingresso degradato quanto una che manca,
        # e la vecchia guardia — «piu' di 200 caratteri» — la dichiarava completa.
        coda = fetta.split(TITOLO_APPENDICE, 1)[-1]
        interi = all(fonti[f] in coda for f in usate)
        completa = bool(usate) and len(coda.strip()) > 200 and interi
        p = os.path.join(args.report, "fetta_%d_giudizio.txt" % (n + 1))
        print("| fetta %d | %d note | %d fonti | %d caratteri | %s |"
              % (n + 1, len(blocco), len(usate), len(fetta),
                 "completa" if completa else "*** DEGRADATA ***"))
        for f in usate:
            print("|   fonte | %s | %d caratteri |" % (f, len(fonti[f])))
        if not completa:
            guasti.append(n + 1)
            continue
        io.open(p, "w", encoding="utf-8").write(fetta)

    if guasti:
        print("\nGUARDIA SCATTATA sulle fette %s: appendice mancante o vuota."
              % ", ".join(str(g) for g in guasti))
        print("Non sono state scritte. Un giudice non riceve un ingresso degradato.")
        return 1
    print("\nTutte le fette portano l'appendice delle fonti che le loro note citano.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
