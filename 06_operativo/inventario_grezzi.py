# -*- coding: utf-8 -*-
"""inventario_grezzi — quanti grezzi sono canonizzati, quanti restano, e quali.

Serve alla pianificazione dei lotti delle Sessioni 4-5 (metodo_03 §9.3) e a
ricontare, a ogni lotto, i file che il lotto dichiara. **Mai numeri a mano**
(regola d'oro 5): questo script e' l'unico che li produce.

Legge le note del vault con `qa_comune` (stesso caricamento della suite QA),
raccoglie l'unione dei campi `fonti` e la confronta con i file presenti in
`aurora-cervello\\sources\\` e con `manifest_corpus_v1.1.json`.

Uso:
    python inventario_grezzi.py                      # riepilogo + elenco dei restanti
    python inventario_grezzi.py --elenco coperti     # solo i coperti
    python inventario_grezzi.py --conta @lista.txt   # riconta i file di un elenco di lotto
    python inventario_grezzi.py --csv fuori.csv      # restanti in CSV (nome;ext;byte)

Non modifica niente: riporta.
"""
import argparse, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "qa"))
import qa_comune as Q


def leggi_elenco(percorso):
    """Un file per riga; righe vuote e commenti `#` ignorati."""
    fuori = []
    for riga in open(percorso, encoding="utf-8"):
        riga = riga.strip()
        if riga and not riga.startswith("#"):
            fuori.append(riga)
    return fuori


def main():
    ap = argparse.ArgumentParser(description="Inventario dei grezzi canonizzati e restanti.")
    ap.add_argument("--vault", default=Q.VAULT)
    ap.add_argument("--elenco", choices=["restanti", "coperti", "nessuno"], default="restanti")
    ap.add_argument("--conta", help="elenco di file di un lotto (@file o percorso) da ricontare")
    ap.add_argument("--csv", help="scrive i restanti in un CSV")
    args = ap.parse_args()

    sources = os.path.join(args.vault, "sources")
    su_disco = sorted(n for n in os.listdir(sources)
                      if os.path.isfile(os.path.join(sources, n)) and not n.lower().endswith(".md"))
    manifest = Q.manifest_nomi()

    note = Q.tutte_le_note(args.vault)
    citati = set()
    for n in note:
        for f in n.fonti:
            if f:
                citati.add(str(f))

    coperti = [n for n in su_disco if n in citati]
    restanti = [n for n in su_disco if n not in citati]
    fantasma = sorted(citati - set(su_disco))          # citati ma non su disco
    fuori_manifest = sorted(set(su_disco) - set(manifest))

    print("Vault ........................ %s" % args.vault)
    print("Note caricate ................ %d" % len(note))
    print("Grezzi su disco in sources\\ .. %d" % len(su_disco))
    print("Nomi nel manifest v1.1 ....... %d" % len(manifest))
    print("Grezzi CITATI da almeno una nota %d" % len(coperti))
    print("Grezzi RESTANTI .............. %d" % len(restanti))
    if fuori_manifest:
        print("\n⚠ su disco ma non nel manifest (atteso: l'avvertenza non e' del corpus):")
        for n in fuori_manifest:
            print("   %s" % n)
    if fantasma:
        print("\n⚠ CITATI ma non presenti in sources\\ — da correggere:")
        for n in fantasma:
            print("   %s" % n)

    # ripartizione per estensione dei restanti: serve a dimensionare i lotti
    per_ext = {}
    for n in restanti:
        e = os.path.splitext(n)[1].lower() or "(senza estensione)"
        per_ext[e] = per_ext.get(e, 0) + 1
    print("\nRestanti per estensione:")
    for e in sorted(per_ext, key=lambda k: (-per_ext[k], k)):
        print("   %-8s %3d" % (e, per_ext[e]))

    if args.elenco != "nessuno":
        quali = restanti if args.elenco == "restanti" else coperti
        print("\n--- %s (%d) ---" % (args.elenco.upper(), len(quali)))
        for n in quali:
            print("%s" % n)

    if args.csv:
        with open(args.csv, "w", encoding="utf-8", newline="") as f:
            f.write("nome;estensione;byte\n")
            for n in restanti:
                p = os.path.join(sources, n)
                f.write("%s;%s;%d\n" % (n, os.path.splitext(n)[1].lower(), os.path.getsize(p)))
        print("\nCSV scritto: %s" % args.csv)

    if args.conta:
        p = args.conta[1:] if args.conta.startswith("@") else args.conta
        if not os.path.isabs(p):
            p = os.path.join(Q.QA_DIR, p)
        elenco = leggi_elenco(p)
        mancanti = [n for n in elenco if n not in su_disco]
        gia_coperti = [n for n in elenco if n in citati]
        doppi = sorted({n for n in elenco if elenco.count(n) > 1})
        print("\n--- RICONTO DELL'ELENCO %s ---" % p)
        print("righe utili .................. %d" % len(elenco))
        print("nomi distinti ................ %d" % len(set(elenco)))
        print("non presenti in sources\\ ..... %d %s" % (len(mancanti), mancanti or ""))
        print("gia' citati da una nota ...... %d %s" % (len(gia_coperti), gia_coperti or ""))
        print("ripetuti nell'elenco ......... %d %s" % (len(doppi), doppi or ""))


if __name__ == "__main__":
    main()
