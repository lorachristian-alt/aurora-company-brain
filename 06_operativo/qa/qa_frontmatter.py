# -*- coding: utf-8 -*-
"""qa_frontmatter — lo schema dei metadati, per `type`.

metodo_03 §7.3. Il frontmatter e' l'unica interfaccia macchina del vault: lo
leggono questa suite, il generatore di llms.txt e il payload filtrabile di
Qdrant. Uno schema che va a caso li' dentro rende inutile tutto il resto.

Uso:
    python qa_frontmatter.py --perimetro vault
    python qa_frontmatter.py --perimetro lotto @fetta_l26130.txt

Esce 0 (verde) · 1 (almeno un ERRORE) · 2 (solo AVVISI).
"""
import argparse, os, re, sys
from datetime import date, datetime

import qa_comune as Q

CONTROLLO = "frontmatter"

# ---- obbligatorieta' per type (metodo_03 §2.4): ● obbligatorio, o facoltativo, x vietato
SCHEMA = {
    #            title summ type area tags fonti stato alias d_fat d_not rel  verif
    "atomica":  dict(area="●", fonti="●", stato="●", aliases="o", data_fatto="o", related="o"),
    "hub":      dict(area="●", fonti="●", stato="●", aliases="o", data_fatto="o", related="●"),
    "entita":   dict(area="●", fonti="●", stato="●", aliases="●", data_fatto="o", related="o"),
    "conflitto":dict(area="●", fonti="●", stato="●", aliases="o", data_fatto="o", related="●"),
    "concetto": dict(area="o", fonti="●", stato="●", aliases="o", data_fatto="x", related="o"),
    "index":    dict(area="x", fonti="x", stato="x", aliases="x", data_fatto="x", related="x"),
    "sessione": dict(area="o", fonti="o", stato="x", aliases="x", data_fatto="x", related="o"),
    "daily":    dict(area="x", fonti="o", stato="x", aliases="x", data_fatto="x", related="o"),
}
SEMPRE = ["title", "summary", "type", "tags", "data_nota"]

# ---- grammatica CHIUSA dei locator (metodo_03 §2.3), una forma per formato.
# Il locator sta all'INIZIO del testo dopo il trattino: se non aggancia li', non
# e' un locator ma una parafrasi del nome del file (§10.18).
ORA = r"\d{1,2}:\d{2}(?::\d{2})?"
NOME = r"[`\"]?[\w .,;/()\-à-ÿ]+[`\"]?"
LOCATOR = {
    # E19: il piè di pagina di un .log non ha timestamp, quindi non era puntabile con
    # nessuna delle due forme a orario. Un riepilogo di export e' una fonte come le altre.
    "log":  [r"righe\s+%s\s*(?:→|->)\s*%s\s*,\s*campo\s+%s" % (ORA, ORA, NOME),
             r"riga\s+%s" % ORA,
             r"§(?:pi[eè] di pagina|intestazione)"],
    "csv":  [r"riga\s+\d+\s*,\s*colonna\s+%s" % NOME,
             r"riga\s+\d+", r"riga\s+`[^`]+`", r"riga\s+%s\s*,\s*colonna\s+%s" % (NOME, NOME)],
    "xlsx": [r"foglio\s+«[^»]+»\s*,\s*(?:riga|righe)\s+\d+(?:\s*-\s*\d+)?",
             r"foglio\s+«[^»]+»\s*!\s*[A-Z]{1,3}\d+",
             r"foglio\s+«[^»]+»\s*,\s*riga\s+`[^`]+`"],
    "pdf":  [r"pag\.\s*\d+\s*,\s*§"],
    "eml":  [r"corpo\s*,\s*punto\s+\d+", r"header\s+[\w-]+"],
    "txt":  [r"\[%s\]\s*,\s*PARLANTE_\d+" % ORA, r"§"],
    "docx": [r"§", r"slide\s+\d+"],
    "pptx": [r"slide\s+\d+", r"§"],
    "xml":  [r"elemento\s+[\w/]+"],
    "p7m":  [r"busta\s*,\s*contenuto\s+\S+\.xml\s*,\s*elemento\s+[\w/]+"],
    "jpg":  [r"verifica\s+visiva"],
    "jpeg": [r"verifica\s+visiva"],
}


def controlla(nota, rep, oggi, nomi_manifest, aree_con_hub):
    n = nota.nome

    # --- il frontmatter esiste e si legge ---------------------------------
    if nota.errore_fm:
        rep.errore(n, CONTROLLO, nota.errore_fm, nota.riga_fm)
        return
    fm = nota.fm

    # --- type -------------------------------------------------------------
    t = fm.get("type")
    if t not in Q.TYPE_AMMESSI:
        rep.errore(n, CONTROLLO, "type '%s' non e' uno degli 8 valori ammessi" % t)
        return
    schema = SCHEMA[t]

    # --- obbligatori e vietati -------------------------------------------
    for campo in SEMPRE:
        if not fm.get(campo):
            rep.errore(n, CONTROLLO, "campo obbligatorio mancante o vuoto: %s" % campo)
    for campo, regola in schema.items():
        val = fm.get(campo)
        vuoto = val is None or (isinstance(val, (list, str)) and len(val) == 0)
        # `aliases: []` su una scheda entita' e' esplicitamente ammesso
        if campo == "aliases" and t == "entita" and isinstance(val, list):
            vuoto = False
        # le note-strumento sono esenti da `fonti`: vedi e_nota_strumento in qa_comune
        if campo == "fonti" and Q.e_nota_strumento(nota):
            continue
        if regola == "●" and vuoto:
            rep.errore(n, CONTROLLO, "campo obbligatorio per type %s mancante o vuoto: %s" % (t, campo))
        if regola == "x" and campo in fm:
            rep.errore(n, CONTROLLO, "campo vietato per type %s ma presente: %s" % (t, campo))
    if "verifica" in fm and t in ("index", "sessione", "daily"):
        rep.errore(n, CONTROLLO, "campo vietato per type %s ma presente: verifica" % t)

    # --- area --------------------------------------------------------------
    area = fm.get("area")
    if area is not None:
        if area not in Q.AREE:
            rep.errore(n, CONTROLLO, "area '%s' fuori dal vocabolario chiuso di §2.2" % area)
        elif area not in aree_con_hub:
            rep.errore(n, CONTROLLO, "area '%s' dichiarata ma manca areas\\area-%s.md" % (area, area))

    # --- stato: due vocabolari, mai mescolati (§2.2-bis) -------------------
    stato = fm.get("stato")
    if stato is not None:
        nota_progetto = (nota.cartella == "projects" and t == "hub")
        if nota_progetto:
            if stato not in ("attivo", "chiuso"):
                rep.errore(n, CONTROLLO, "la nota-progetto vuole stato attivo|chiuso, trovato '%s'" % stato)
        else:
            if stato not in ("risolto", "aperto"):
                rep.errore(n, CONTROLLO, "fuori dalla nota-progetto stato vuole risolto|aperto, trovato '%s'" % stato)
        if t == "conflitto" and stato != "aperto":
            rep.errore(n, CONTROLLO, "un type conflitto e' sempre stato: aperto (§2.4)")

    # --- tags ---------------------------------------------------------------
    tags = fm.get("tags") or []
    if isinstance(tags, list) and tags:
        if tags[0] != nota.cartella:
            rep.errore(n, CONTROLLO, "tags[0] deve essere il nome della cartella '%s', trovato '%s'"
                       % (nota.cartella, tags[0]))
        for tg in tags[1:]:
            s = str(tg)
            if s != s.lower() or " " in s or Q.senza_accenti(s) != s:
                rep.avviso(n, CONTROLLO, "tag non normalizzato: '%s' (minuscolo, senza accenti, senza spazi)" % s)

    # --- date ----------------------------------------------------------------
    date_lette = {}
    for campo in ("data_fatto", "data_nota"):
        v = fm.get(campo)
        if v is None:
            continue
        if isinstance(v, date):
            date_lette[campo] = v
            continue
        try:
            date_lette[campo] = datetime.strptime(str(v), "%Y-%m-%d").date()
        except ValueError:
            rep.errore(n, CONTROLLO, "%s non e' una data reale in formato YYYY-MM-DD: '%s'" % (campo, v))
    if "data_fatto" in date_lette and t not in ("sessione", "daily"):
        if date_lette["data_fatto"] == oggi:
            rep.errore(n, CONTROLLO, "data_fatto coincide con la data di esecuzione della QA: "
                                     "mai la data di oggi come data_fatto (§10.13)")
    if "data_fatto" in date_lette and "data_nota" in date_lette:
        if date_lette["data_fatto"] > date_lette["data_nota"]:
            rep.errore(n, CONTROLLO, "data_fatto (%s) successiva a data_nota (%s)"
                       % (date_lette["data_fatto"], date_lette["data_nota"]))

    # --- fonti ----------------------------------------------------------------
    fonti = nota.fonti
    ha_jpg = any(str(f).lower().endswith((".jpg", ".jpeg")) for f in fonti)
    if ha_jpg and fm.get("verifica") != "visiva":
        rep.errore(n, CONTROLLO, "fonti contiene un .jpg: serve `verifica: visiva` (§2.3)")
    if not ha_jpg and fm.get("verifica") is not None:
        rep.errore(n, CONTROLLO, "`verifica` presente ma nessuna fonte .jpg")

    for f in fonti:
        f = str(f)
        if f not in nomi_manifest:
            rep.errore(n, CONTROLLO, "fonte non presente nel manifest del corpus: '%s'" % f)
        elif not os.path.isfile(os.path.join(Q.SOURCES, f)):
            rep.errore(n, CONTROLLO, "fonte nel manifest ma assente da sources\\: '%s'" % f)
    if t == "conflitto" and len(set(map(str, fonti))) < 2:
        rep.errore(n, CONTROLLO, "un type conflitto vuole almeno 2 file diversi in fonti (§2.4)")

    # --- related su una riga sola ---------------------------------------------
    rel = fm.get("related")
    if rel is not None:
        if not isinstance(rel, str):
            rep.errore(n, CONTROLLO, "related deve essere una stringa fra virgolette su una riga sola")
        elif "\n" in rel:
            rep.errore(n, CONTROLLO, "related e' su piu' righe")

    # --- summary ---------------------------------------------------------------
    s = str(fm.get("summary") or "")
    if len(s) > 250:
        rep.avviso(n, CONTROLLO, "summary di %d caratteri (tetto 250)" % len(s))
    if Q.conta_frasi(s) > 1:
        rep.avviso(n, CONTROLLO, "summary contiene piu' di una frase")

    # --- budget di parole della nota atomica ------------------------------------
    if t == "atomica":
        p = nota.parole_corpo()
        if p > 350:
            rep.errore(n, CONTROLLO, "corpo di %d parole: oltre il tetto di 350, la nota va divisa" % p)
        elif p > 300:
            rep.avviso(n, CONTROLLO, "corpo di %d parole: fra 301 e 350, si motiva o si spezza" % p)

    # --- nome del file ------------------------------------------------------------
    if not any(nota.slug.startswith(p) for p in Q.PREFISSI):
        rep.avviso(n, CONTROLLO, "il nome non comincia con un prefisso della tabella §4.1")
    if nota.slug != Q.senza_accenti(nota.slug).lower() or " " in nota.slug:
        rep.avviso(n, CONTROLLO, "il nome del file va in minuscolo ASCII con trattini")

    # --- grammatica dei locator ------------------------------------------------------
    controlla_locator(nota, rep)


def controlla_locator(nota, rep):
    """Ogni riga del blocco `## Fonti` porta un wikilink al grezzo e, subito dopo
    il trattino, un locator della grammatica chiusa di §2.3, coerente con
    l'estensione del file citato."""
    if nota.type == "index":
        return
    blocco = nota.blocco_fonti
    if nota.fonti and not blocco.strip():
        rep.errore(nota.nome, CONTROLLO, "la nota dichiara fonti ma non ha la sezione `## Fonti`")
        return
    base = nota.corpo.count("\n") - blocco.count("\n")
    citati = set()
    for i, riga in enumerate(blocco.splitlines()):
        if not riga.strip().startswith("-"):
            continue
        m = re.match(r"\s*-\s*\[\[([^\]|]+)\]\]\s*(?:—|-{1,2})\s*(.+)", riga)
        if not m:
            if "[[" in riga:
                rep.errore(nota.nome, CONTROLLO,
                           "riga di Fonti senza locator dopo il trattino lungo", base + i + 1)
            continue
        nomefile, locator = m.group(1).strip(), m.group(2).strip()
        citati.add(nomefile)
        est = nomefile.rsplit(".", 1)[-1].lower()
        forme = LOCATOR.get(est)
        if forme is None:
            rep.errore(nota.nome, CONTROLLO,
                       "nessuna grammatica di locator per l'estensione .%s" % est, base + i + 1)
            continue
        if not any(re.match(f, locator, re.I) for f in forme):
            rep.errore(nota.nome, CONTROLLO,
                       "locator fuori grammatica per .%s: \"%s\"" % (est, locator[:60]), base + i + 1)
    for f in nota.fonti:
        if str(f) not in citati:
            rep.errore(nota.nome, CONTROLLO,
                       "fonte '%s' nel frontmatter ma senza riga nel blocco `## Fonti`" % f)


def main():
    ap = argparse.ArgumentParser(description="Valida lo schema del frontmatter delle note.")
    Q.aggiungi_argomenti(ap)
    args = ap.parse_args()
    modo, file_lotto = Q.leggi_perimetro(args)

    note = Q.tutte_le_note(args.vault)
    perimetro = Q.note_del_perimetro(note, modo, file_lotto, Q.note_toccate(args))
    aree_con_hub = {n.slug[len("area-"):] for n in note
                    if n.cartella == "areas" and n.slug.startswith("area-")}
    nomi_manifest = Q.manifest_nomi()
    oggi = date.today()

    rep = Q.Report("qa_frontmatter (perimetro: %s, %d note)" % (modo, len(perimetro)))
    for n in perimetro:
        controlla(n, rep, oggi, nomi_manifest, aree_con_hub)

    rep.stampa()
    d = Q.cartella_report(args, modo, "l26130")
    Q.scrivi_report(d, "qa_frontmatter.md", rep.markdown())
    sys.exit(rep.codice())


if __name__ == "__main__":
    main()
