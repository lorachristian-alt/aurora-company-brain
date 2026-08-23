# -*- coding: utf-8 -*-
"""qa_link_integrity — zero link rotti, zero orfani, un grafo solo.

metodo_03 §7.2. La promessa del progetto e' che nessuna nota sia irraggiungibile
lungo `llms.txt -> _index -> hub -> nota`: questo script la verifica anello per
anello, primo compreso.

Uso:
    python qa_link_integrity.py --perimetro vault
    python qa_link_integrity.py --perimetro lotto @fetta_l26130.txt
"""
import argparse, os, re, sys
from collections import deque

import qa_comune as Q
import genera_llms

RE_WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")

CONTROLLO = "link"


def costruisci(note, vault):
    """Mappa dei nomi risolvibili e archi orientati del grafo delle note.

    I link verso `sources\\` NON sono archi: sono fonti, non relazioni (§7.2).
    """
    per_slug = {}
    ambigui = []
    for n in note:
        if n.slug in per_slug:
            ambigui.append((n.slug, per_slug[n.slug].cartella, n.cartella))
        per_slug[n.slug] = n
    grezzi = set(os.listdir(Q.SOURCES)) if os.path.isdir(Q.SOURCES) else set()
    return per_slug, grezzi, ambigui


def main():
    ap = argparse.ArgumentParser(description="Integrita' dei collegamenti fra note.")
    Q.aggiungi_argomenti(ap)
    args = ap.parse_args()
    modo, file_lotto = Q.leggi_perimetro(args)

    note = Q.tutte_le_note(args.vault)
    per_slug, grezzi, ambigui = costruisci(note, args.vault)
    rep = Q.Report("qa_link_integrity (perimetro: %s, %d note nel vault)" % (modo, len(note)))

    for slug, c1, c2 in ambigui:
        rep.errore(slug + ".md", CONTROLLO,
                   "nome ambiguo: lo stesso nome esiste in '%s' e in '%s'" % (c1, c2))

    # ---- 1. ogni cartella ha la sua porta -------------------------------------
    # In perimetro lotto si pretende l'_index delle sole cartelle che il lotto
    # tocca; le undici tutte insieme sono un controllo di chiusura (§7, tabella
    # dei perimetri), non di lotto.
    con_index = {n.cartella for n in note if n.type == "index"}
    if modo == "vault":
        attese = set(Q.CARTELLE)
    else:
        attese = {n.cartella for n in note if any(f in file_lotto for f in n.fonti)}
    for c in sorted(attese - con_index):
        rep.errore("_index-%s.md" % c, CONTROLLO, "la cartella '%s' non ha il suo _index" % c)

    # ---- 2. wikilink rotti (ovunque, workspace compresa) -----------------------
    #
    # ⚠️ IL CONTROLLO GUARDAVA IL SOLO CORPO, E `related` NO — riparato il 23/08/2026, lotto
    # 3B. `Nota.wikilink()` legge `self.corpo`, quindi un rimando rotto scritto nel frontmatter
    # era **invisibile**: la QA dava 0 ERRORI su un vault che ne portava due, e uno stava li'
    # da un lotto precedente. ⚠️ **E' la stessa specie di E32**, un controllo il cui perimetro
    # non copre cio' che deve, e per §4 un controllo bacato non e' un candidato: e' un guasto,
    # e si ripara subito. Il caso che l'ha trovato: `doc-scadenzario-formazione-2026` puntava a
    # `[[entita-francesca-sartori]]`, **un nome proprio inventato** — la scheda si chiama
    # `entita-federica-sartori` — e l'ha visto la revisione col canone, non la suite.
    #
    # ⚠️ Il fix AGGIUNGE agganci (§4.9) e ha comunque il suo difetto piantato in
    # `_collaudo\collaudo_related_rotto.py`, o il buco si riapre in silenzio.
    archi = {}
    for n in note:
        uscenti = []
        rel = str((n.fm or {}).get("related") or "")
        da_related = [(m.group(1).strip(), 0) for m in RE_WIKILINK.finditer(rel)]
        for target, riga in list(n.wikilink()) + da_related:
            if target in per_slug:
                uscenti.append(target)
            elif "." in target:
                # ha un'estensione: e' un rimando a un grezzo, non a una nota
                if target not in grezzi:
                    rep.errore(n.nome, CONTROLLO,
                               "wikilink a un file che non esiste in sources\\: [[%s]]" % target, riga)
            else:
                rep.errore(n.nome, CONTROLLO, "wikilink rotto: [[%s]]" % target, riga)
        archi[n.slug] = uscenti

    # ---- 3. orfani: BFS ORIENTATO dagli 11 _index, profondita' illimitata --------
    radici = [n.slug for n in note if n.type == "index"]
    visitati, coda = set(radici), deque(radici)
    while coda:
        cur = coda.popleft()
        for t in archi.get(cur, []):
            if t not in visitati:
                visitati.add(t); coda.append(t)

    valutabili = [n for n in note
                  if n.cartella not in Q.ESCLUSE_QUALITA and n.type != "index"]
    if modo == "lotto":
        dentro = {x.slug for x in Q.note_del_perimetro(note, modo, file_lotto, Q.note_toccate(args))}
        valutabili = [n for n in valutabili if n.slug in dentro]

    for n in valutabili:
        if n.slug not in visitati:
            rep.errore(n.nome, CONTROLLO,
                       "nota orfana: non raggiungibile da nessuno degli _index")

    # ---- 4. prossimita': entro due salti dall'_index della PROPRIA cartella -------
    for n in valutabili:
        radice = "_index-%s" % n.cartella
        if radice not in per_slug:
            continue
        dist, coda = {radice: 0}, deque([radice])
        while coda:
            cur = coda.popleft()
            for t in archi.get(cur, []):
                if t not in dist:
                    dist[t] = dist[cur] + 1; coda.append(t)
        d = dist.get(n.slug)
        if d is None or d > 2:
            rep.avviso(n.nome, CONTROLLO,
                       "lontana dall'_index della propria cartella (%s salti): indizio di cattiva collocazione"
                       % ("non raggiungibile da li'" if d is None else d))

    # ---- 5. componente unica, sul grafo NON orientato -----------------------------
    # In perimetro di lotto la componente si valuta sulle note CHE IL LOTTO HA PRODOTTO —
    # quelle che citano un suo grezzo — piu' gli _index delle loro cartelle. Tirarci dentro
    # le porte di cartelle che il lotto non tocca, o le note-strumento di code\, fa
    # comparire tronconi staccati che non sono un difetto del lotto: sono la prova che il
    # vault non e' ancora completo, che a lotto aperto e' ovvia.
    #
    # ⚠️ E20 (18/08/2026): fuori anche le NOTE-STRUMENTO DEL PROGETTO — la classe definita
    # una volta sola in `qa_comune.e_nota_strumento`, che porta gia' le esenzioni da `fonti`
    # (E1) e dallo strato di giudizio. Documentano attrezzi del progetto, non fatti di
    # Aurora: nessuna nota di contenuto ha ragione di citarle, e aggiungere quel link
    # sarebbe tappezzeria (divieto 25). Restano soggette a schema, wikilink rotti e
    # raggiungibilita' da `_index-code`. Le note di CONTENUTO di `code\` — le automazioni
    # aziendali — restano dentro questo controllo: se sono staccate, e' un difetto vero.
    insieme = [n for n in note
               if n.cartella not in Q.ESCLUSE_QUALITA and not Q.e_nota_strumento(n)]
    # ⚠️ Aritmetica dell'esenzione, non un'esenzione in piu': un `_index` la cui cartella
    # non ha piu' nessuna nota valutabile — perche' e' vuota, o perche' contiene solo
    # note-strumento — resta un vertice isolato per costruzione, e segnalerebbe come
    # difetto del grafo il fatto che quella cartella e' vuota. Rientra da solo nel
    # controllo appena la sua cartella riceve una nota valutabile.
    con_contenuto = {n.cartella for n in insieme if n.type != "index"}
    insieme = [n for n in insieme
               if n.type != "index" or n.cartella in con_contenuto]
    if modo == "lotto":
        del_lotto = [n for n in note if any(f in file_lotto for f in n.fonti)]
        cartelle_toccate = {n.cartella for n in del_lotto}
        dentro = {n.slug for n in del_lotto}
        dentro |= {n.slug for n in note
                   if n.type == "index" and n.cartella in cartelle_toccate}
        insieme = [n for n in insieme if n.slug in dentro]
    slugs = {n.slug for n in insieme}
    vicini = {s: set() for s in slugs}
    for s in slugs:
        for t in archi.get(s, []):
            if t in slugs:
                vicini[s].add(t); vicini[t].add(s)
    if slugs:
        start = sorted(slugs)[0]
        visti, coda = {start}, deque([start])
        while coda:
            cur = coda.popleft()
            for t in vicini[cur]:
                if t not in visti:
                    visti.add(t); coda.append(t)
        if len(visti) != len(slugs):
            fuori = sorted(slugs - visti)
            rep.errore("(grafo)", CONTROLLO,
                       "il grafo ha piu' di una componente connessa: %d note staccate (%s%s)"
                       % (len(fuori), ", ".join(fuori[:5]), "…" if len(fuori) > 5 else ""))

    # ---- 6. minimo di wikilink ------------------------------------------------------
    # I link verso gli _index non contano, e quelli verso sources\ nemmeno.
    # ⚠️ Qui si contano ANCHE i wikilink di `related`, che nel grafo degli orfani non sono
    # archi (§7.2 dice «i wikilink uscenti del suo CORPO») ma sono relazioni dichiarate a
    # tutti gli effetti: e' in `related` che vive il rimando spoke → hub. Contare il solo
    # corpo segnalerebbe come poco collegata una nota che dichiara cinque relazioni.
    for n in valutabili:
        uscenti = {t for t in archi.get(n.slug, []) if not t.startswith("_index-")}
        for t in re.findall(r"\[\[([^\]|]+)", str((n.fm or {}).get("related") or "")):
            t = t.strip()
            if t in per_slug and not t.startswith("_index-"):
                uscenti.add(t)
        if len(uscenti) < 2:
            rep.avviso(n.nome, CONTROLLO,
                       "solo %d wikilink uscenti verso altre note (minimo 2)" % len(uscenti))

    # ---- 7. reciprocita' hub/spoke ----------------------------------------------------
    # ⚠️ Si controlla il PRIMO hub citato in `related`, non tutti. `related` porta anche i
    # link laterali — un fatto che rimanda a un'altra area, una scheda che rimanda a un
    # concetto — e pretendere che OGNI hub citato elenchi la nota trasforma ogni rimando
    # laterale in un avviso: il controllo annega nel proprio rumore e smette di essere
    # letto. Convenzione: il primo hub di `related` e' l'hub PROPRIO della nota.
    for n in note:
        if n.type == "hub":
            continue          # un hub che rimanda a un hub vicino non e' uno spoke
        rel = str((n.fm or {}).get("related") or "")
        for target in re.findall(r"\[\[([^\]|]+)", rel):
            target = target.strip()
            h = per_slug.get(target)
            if h is None or h.type != "hub":
                continue
            if n.slug not in [t for t, _ in h.wikilink()]:
                rep.avviso(n.nome, CONTROLLO,
                           "dichiara l'hub [[%s]] come proprio in related, ma quell'hub non la elenca nel corpo" % target)
            break

    # ---- 8. eredi di un progetto chiuso, e testimone dichiarato -------------------------
    for n in note:
        if n.cartella == "projects" and n.type == "hub" and n.stato == "chiuso":
            eredi = [per_slug[t] for t in archi.get(n.slug, []) if t in per_slug]
            eredi = [e for e in eredi if e.cartella in ("outputs", "areas", "code")]
            if not eredi:
                rep.avviso(n.nome, CONTROLLO,
                           "progetto chiuso senza eredi dichiarati in outputs\\, areas\\ o code\\")
            for e in eredi:
                if "nato da" not in Q.norm(e.corpo):
                    rep.avviso(e.nome, CONTROLLO,
                               "erede di [[%s]] senza la riga «nato da [[progetto-…]]»" % n.slug)

    # ---- 9. il primo anello: llms.txt ---------------------------------------------------
    p_llms = os.path.join(args.vault, "llms.txt")
    if not os.path.isfile(p_llms):
        rep.errore("llms.txt", CONTROLLO,
                   "manca alla radice del vault: rigeneralo con `python genera_llms.py`")
    else:
        attuale = open(p_llms, encoding="utf-8").read()
        atteso = genera_llms.componi(args.vault)
        if attuale.replace("\r\n", "\n") != atteso:
            rep.errore("llms.txt", CONTROLLO,
                       "rigenerandolo cambia: qualcuno l'ha modificato a mano, oppure e' vecchio")
        elencati = set(re.findall(r"^- \[([^\]]+)\]", attuale, re.M))
        for n in note:
            if n.type in ("index", "hub") and n.slug not in elencati:
                rep.errore("llms.txt", CONTROLLO,
                           "l'%s [[%s]] non compare in llms.txt: la catena si rompe al primo anello"
                           % (n.type, n.slug))
        for s in sorted(elencati - set(per_slug)):
            rep.errore("llms.txt", CONTROLLO, "riga che punta a una nota inesistente: %s" % s)

    rep.stampa()
    d = Q.cartella_report(args, modo, "l26130")
    Q.scrivi_report(d, "qa_link_integrity.md", rep.markdown())
    sys.exit(rep.codice())


if __name__ == "__main__":
    main()
