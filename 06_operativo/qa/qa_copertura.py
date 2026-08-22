# -*- coding: utf-8 -*-
"""qa_copertura — nessun file muto, nessun fatto senza padrone.

metodo_03 §7.4.

⚠️ Cio' che questo script NON fa, ed e' una scelta dichiarata: il confronto col
canone. Richiederebbe di leggere `canone_aurora.md`, che nel vault non entra, e
di giudicare se una nota «copre» un fatto — cioe' di dichiarare un exit code su
un giudizio umano. Qui si produce l'ELENCO DELLE NOTE CANDIDATE per tema; il
verdetto lo da' il revisore indipendente, col canone alla mano. Un fatto chiave
senza padrona resta bloccante come un ERRORE, ma per mano di una persona.

Uso:
    python qa_copertura.py --perimetro lotto @fetta_l26130.txt
    python qa_copertura.py --perimetro vault
"""
import argparse, os, re, sys

import qa_comune as Q
import qa_provenance as P

CONTROLLO = "copertura"


def main():
    ap = argparse.ArgumentParser(description="Copertura dei grezzi e unicita' delle padrone.")
    Q.aggiungi_argomenti(ap)
    args = ap.parse_args()
    modo, file_lotto = Q.leggi_perimetro(args)

    note = Q.tutte_le_note(args.vault)
    perimetro = Q.note_del_perimetro(note, modo, file_lotto, Q.note_toccate(args))
    rep = Q.Report("qa_copertura (perimetro: %s, %d note)" % (modo, len(perimetro)))

    # ---- 1. nessun documento muto ------------------------------------------
    citati = set()
    for n in note:
        citati |= {str(f) for f in n.fonti}
    if modo == "vault":
        attesi = Q.manifest_nomi()
    else:
        attesi = set(file_lotto)
    muti = sorted(attesi - citati)
    for f in muti:
        rep.errore("(copertura)", CONTROLLO,
                   "il grezzo '%s' non compare in `fonti` di nessuna nota" % f)

    # file citati ma inesistenti: lo dice gia' qa_frontmatter, qui solo il conteggio
    print("   grezzi nel perimetro: %d · citati: %d · muti: %d"
          % (len(attesi), len(attesi & citati), len(muti)))

    # ---- 2. fatti senza fonte ------------------------------------------------
    # e' l'aggancio a §7.1: una nota che afferma numeri senza avere fonti da cui
    # verificarli e' un fatto senza fonte, e cade sotto il divieto §10.6.
    for n in perimetro:
        if n.type in ("index", "sessione", "daily") or n.fm is None:
            continue
        if Q.e_nota_strumento(n):
            continue                      # attrezzo del progetto, non un fatto del corpus
        if not n.fonti:
            aff = P.estrai_affermazioni(n.corpo_senza_fonti)
            if aff:
                rep.errore(n.nome, CONTROLLO,
                           "afferma %d fra numeri, date e codici ma non dichiara nessuna fonte" % len(aff))

    # ---- 3. doppie padrone -----------------------------------------------------
    # Due note che affermano lo stesso fatto come proprio: una delle due deve
    # linkare l'altra. La soglia e' alta apposta — su un lotto tematico tutte le
    # note condividono qualche numero, e un controllo isterico qui produrrebbe
    # link inventati, che costano piu' del difetto che segnalano.
    #
    # ⚠️ FIX DEL 22/08/2026, gate del lotto 3A. PERIMETRO CHIUSO (§4.9): il controllo
    # ALLENTA, e le due condizioni che aggiunge sono entrambe necessarie.
    #
    # IL CASO. Dal gate di 2A il controllo portava un rilievo, tenuto rosso «finche' non
    # avra' il suo turno». Col lotto 3A e' passato da 1 a 4, tutti contro la stessa nota:
    # `kpi-indicatori-mensili-2026`, una tabella di dieci indicatori per cinque mesi, che
    # porta **cinquanta decimali piccoli in una nota sola**. I valori «in comune» erano
    # 0,8 · 0,9 · 1,1 · 1,4 · 6,1 — numeri che in questo archivio compaiono ovunque, dalla
    # conducibilita' alle percentuali di lotti bloccati.
    #
    # ⚠️ **Un controllo il cui rosso cresce col lavoro fatto bene e' un controllo che verra'
    # ignorato** (§4.35). E i temi 3-6 portano altre tabelle come questa.
    #
    # LE DUE CONDIZIONI, e perche' non basta l'una senza l'altra:
    #
    #   1. FONTE CONDIVISA. Due note sono doppie padrone dello stesso fatto solo se il
    #      fatto viene dallo **stesso grezzo**. Se le fonti sono disgiunte i fatti sono
    #      diversi, e la coincidenza dei numeri e' aritmetica, non semantica. ⚠️ Tutte e
    #      quattro le coppie segnalate il 22/08 — **compresa quella originaria di 2A** —
    #      avevano **zero fonti in comune**: era un falso positivo dal principio.
    #
    #   2. VALORI IDENTIFICANTI. Un numero a una sola cifra decimale non identifica nulla
    #      in un archivio che misura temperature, percentuali e conducibilita': «0,9» e'
    #      un valore di sfondo. Contano solo i numeri con almeno **tre cifre significative**
    #      — cosi' `18.600`, `99,6` e `1,42` contano, `0,9` e `1,1` no.
    #
    # ⚠️ La prima da sola lascerebbe scattare due note dello stesso lotto che condividono
    # tre decimali di sfondo — ed e' il caso piu' probabile, non il piu' raro, perche' le
    # note di un lotto citano gli stessi grezzi. La seconda da sola lascerebbe scattare due
    # note di lotti diversi che nominano lo stesso peso o lo stesso importo per ragioni
    # scollegate. **Insieme descrivono la doppia padrona: stesso fatto, stessa fonte.**
    def identificante(s):
        """Almeno tre cifre significative: sotto, il numero e' rumore di sfondo."""
        cifre = "".join(c for c in s if c.isdigit()).lstrip("0")
        return len(cifre) >= 3

    profili = {}
    for n in perimetro:
        if n.type in ("index", "hub", "conflitto") or n.fm is None:
            continue
        num = {t for g, t in P.estrai_affermazioni(n.corpo_senza_fonti)
               if g == "numero" and identificante(t)}
        if num:
            profili[n.slug] = (n, num, {str(f) for f in n.fonti})
    slugs = sorted(profili)
    for i, a in enumerate(slugs):
        for b in slugs[i + 1:]:
            na, sa, fa = profili[a]; nb, sb, fb = profili[b]
            comuni = sa & sb
            if len(comuni) < 3:
                continue
            if not (fa & fb):
                continue
            link_a = {t for t, _ in na.wikilink()}
            link_b = {t for t, _ in nb.wikilink()}
            if b not in link_a and a not in link_b:
                rep.errore(na.nome, CONTROLLO,
                           "possibile doppia padrona con '%s': %d valori identificanti in comune (%s), fonte condivisa, e nessun wikilink fra le due"
                           % (nb.nome, len(comuni), ", ".join(sorted(comuni)[:4])))

    # ---- 4. aree popolate (solo a vault) ------------------------------------------
    if modo == "vault":
        hub_area = {n.slug[len("area-"):]: n for n in note
                    if n.slug.startswith("area-") and n.type == "hub"}
        for a in sorted(Q.AREE):
            if a not in hub_area:
                rep.errore("(copertura)", CONTROLLO,
                           "l'area '%s' non ha il suo hub area-%s in areas\\" % (a, a))
            elif hub_area[a].cartella != "areas":
                rep.errore(hub_area[a].nome, CONTROLLO,
                           "hub d'area fuori da areas\\: sta in '%s'" % hub_area[a].cartella)

    # ---- 5. elenco delle candidate per tema, per il revisore ------------------------
    righe = ["## Note candidate per tema\n",
             "*Il verdetto sulla copertura dei fatti chiave lo da' il revisore indipendente,",
             "col canone alla mano. Questo elenco e' il materiale su cui lavora.*\n"]
    per_tema = {}
    for n in perimetro:
        if n.type == "index":
            continue
        tema = (n.fm or {}).get("area") or "(senza area)"
        per_tema.setdefault(tema, []).append(n)
    for tema in sorted(per_tema):
        righe.append("### %s\n" % tema)
        righe.append("| Nota | type | stato | fonti |")
        righe.append("|---|---|---|---|")
        for n in sorted(per_tema[tema], key=lambda x: x.slug):
            righe.append("| `%s` | %s | %s | %d |"
                         % (n.nome, n.type, n.stato or "—", len(n.fonti)))
        righe.append("")
    righe.append("### Grezzi del perimetro e note che li citano\n")
    righe.append("| Grezzo | Note che lo citano |")
    righe.append("|---|---|")
    for f in sorted(attesi):
        chi = [n.slug for n in note if f in {str(x) for x in n.fonti}]
        righe.append("| `%s` | %s |" % (f, ", ".join(chi) if chi else "**nessuna**"))

    rep.stampa()
    d = Q.cartella_report(args, modo, "l26130")
    Q.scrivi_report(d, "qa_copertura.md", rep.markdown() + "\n\n" + "\n".join(righe))
    sys.exit(rep.codice())


if __name__ == "__main__":
    main()
