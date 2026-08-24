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
import estrazione_cantiere as EC

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
    # E55, 22/08/2026: un `.eml` puo' essere una CATENA — piu' messaggi quotati uno dentro
    # l'altro — e allora «corpo, punto 1)» indica quattro punti diversi nello stesso file.
    # La forma lunga nomina prima quale messaggio, con la sua data. La forma breve resta
    # valida per un `.eml` a messaggio unico, che e' il caso di tutti i lotti precedenti.
    "eml":  [r"corpo\s+del\s+messaggio\s+del\s+\d{1,2}/\d{1,2}\s*,",
             r"§(?:pi[eè] di pagina|intestazione)\s+del\s+messaggio\s+del\s+\d{1,2}/\d{1,2}\s*:",
             r"corpo\s*,\s*punto\s+\d+", r"header\s+[\w-]+"],
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
    #
    # ⚠️ IL CAMPO `verifica` HA DUE VALORI, E CIASCUNO HA LA SUA CONDIZIONE.
    #   `visiva`      -> la nota cita un `.jpg`, che l'estrattore congelato non legge (§2.3).
    #   `strutturale` -> il riscontro sta in uno STRATO DI CANTIERE (E48): una formula di
    #                    foglio di calcolo o un passaggio barrato. Sono cose che stanno nel
    #                    file e che il testo estratto non restituisce come tali.
    #
    # ⚠️ IL PERIMETRO E' CHIUSO, ed e' la condizione di §4.9 per un fix che ALLENTA: prima
    # del 21/08/2026 questo controllo vietava il campo `verifica` su qualunque nota senza
    # `.jpg`, e quindi rendeva impossibile la forma che E48 prescrive. Ora `strutturale` e'
    # ammesso **solo** se almeno una fonte porta davvero uno strato — non basta dichiararlo.
    # Il collaudo pianta entrambi i versi: una nota che lo dichiara e ha lo strato deve
    # passare, una che lo dichiara senza strato deve restare rossa.
    fonti = nota.fonti
    ha_jpg = any(str(f).lower().endswith((".jpg", ".jpeg")) for f in fonti)
    ha_strati = any(EC.strati(str(f)) for f in fonti)
    v = fm.get("verifica")
    if ha_jpg and v != "visiva":
        rep.errore(n, CONTROLLO, "fonti contiene un .jpg: serve `verifica: visiva` (§2.3)")
    elif v == "strutturale" and not ha_strati:
        rep.errore(n, CONTROLLO,
                   "`verifica: strutturale` ma nessuna fonte porta uno strato di cantiere "
                   "(formule o barrato): E48 chiede il riscontro, non la dichiarazione")
    elif v is not None and v not in ("visiva", "strutturale"):
        rep.errore(n, CONTROLLO, "`verifica` ammette solo `visiva` o `strutturale`: «%s»" % v)
    elif not ha_jpg and v == "visiva":
        rep.errore(n, CONTROLLO, "`verifica: visiva` ma nessuna fonte .jpg")

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

    # --- E43: l'assenza dichiarata lascia l'artefatto della ricerca -------------------
    controlla_artefatto_assenza(nota, rep)


# ---- E43 ---------------------------------------------------------------------------
# Nessuno script puo' verificare il CONTENUTO di un'assenza: non esiste modo automatico di
# stabilire che «nessun grezzo dice X» sia vero. La PROCEDURA si': che la ricerca sia stata
# eseguita, con quali termini e su quale perimetro, e' un fatto che lascia un file.
#
# ⚠️ E3 e' stato pagato QUATTRO volte in cinque lotti — PRP-09 nel pilota, l'ossigeno residuo
# in 1A, due note in 2A dove la formula di attestazione era scritta SENZA che la ricerca fosse
# stata fatta. E' §4.20 al rovescio: quando una regola viene violata sempre, il difetto non e'
# nella diligenza di chi la applica, e' nel fatto che nessuno puo' verificarla.
FORMULA_E3 = re.compile(r"(?:assenza\s+verificata|verificat[ao]\s+su\s+tutto\s+`?sources)", re.I)
RIMANDO_E3 = re.compile(r"ricerche_assenza[\\/]([\w.\-]+)", re.I)
DIR_RICERCHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "ricerche_assenza")

# ⚠️ E43 NASCE IL 20/08/2026, E UN CONTROLLO NUOVO NON PUO' RENDERE ROSSO IL PREGRESSO.
# Al momento in cui la regola entra, 29 note gia' scritte dichiarano un'assenza senza
# artefatto: pretenderlo da loro bloccherebbe ogni lotto futuro su un difetto che nessuno
# poteva evitare quando quelle note sono nate. La regola vale quindi IN AVANTI — ERRORE dalle
# note nate con E43 in vigore — e sul pregresso emette un AVVISO che dichiara il debito.
# E' la stessa disciplina dell'esperimento del lotto 2A: il debito ereditato si misura e si
# programma, non si nasconde e non si spaccia per produzione corrente.
NASCITA_E43 = date(2026, 8, 20)

# ⚠️ IL CONTROLLO SMETTE DI CERCARE LA FORMULA E COMINCIA A CERCARE L'ASSENZA.
# Gate del lotto 3D, 24/08/2026, e nasce da E3 pagato per la QUINTA volta in sette lotti.
#
# Il caso: `questione-data-apertura-rec-2026-011` elencava fra le cose che sarebbero servite
# per chiuderla «la mail automatica di notifica della segnalazione, CHE L'ARCHIVIO NON
# CONTIENE». L'archivio la contiene, ed e' il primo grezzo del lotto 3D. ⚠️ **Il controllo non
# poteva prenderla**: quell'assenza non usa la formula di attestazione, e' dichiarata dentro un
# elenco di «cosa servirebbe per chiuderla».
#
# ⚠️ LA SUPERFICIE IN CUI UN'ASSENZA SI NASCONDE E' PIU' LARGA DELLA FORMULA CHE LA DICHIARA,
# ed e' la stessa scoperta che il gate del lotto 3B ha fatto sull'intestazione, un piano piu' in
# la': un difetto che non e' una contraddizione non si trova rileggendo il codice — il codice e
# il manuale concordavano — si trova facendo l'elenco delle superfici.
#
# ⚠️ CHE COSA CAMBIA, ESATTAMENTE: cambia l'AGGANCIO, non il requisito. Il requisito resta
# quello di E43 — chi dichiara un'assenza lascia l'artefatto della ricerca — e adesso l'assenza
# si riconosce per DUE vie che non si sostituiscono:
#   1. la FORMULA di attestazione di E3 (`FORMULA_E3`), com'e' sempre stato;
#   2. il RICONOSCITORE DELLA CLASSE `assenza` di `qa_comune` — quantificatore piu' termine di
#      perimetro dentro la finestra, in esistenziale negativo — cioe' la stessa grammatica con
#      cui `censimento_superlativi.py` conta la classe per T142. **Una definizione sola**: se
#      il controllo ne avesse una propria, il progetto conterebbe una classe e ne fermerebbe
#      un'altra.
#
# ⚠️ E UN CONTROLLO NUOVO NON PUO' RENDERE ROSSO IL PREGRESSO (§4.35, come per E43 il 20/08 e
# come per la superficie dell'intestazione il 23/08). La seconda via vale IN AVANTI — ERRORE
# per le note nate dal 24/08/2026 — e sul pregresso emette un AVVISO che dichiara il debito,
# contato nella sua riga di tracciamento.
NASCITA_ASSENZA_FUORI_FORMULA = date(2026, 8, 24)


def _nata_dal(nota, quando):
    """Vero se la nota e' nata quando la regola era gia' in vigore."""
    dn = (nota.fm or {}).get("data_nota")
    try:
        return datetime.strptime(str(dn), "%Y-%m-%d").date() >= quando
    except Exception:
        return isinstance(dn, date) and dn >= quando


def _regime(nota, rep, quando, coda_debito):
    """La coppia (come segnalare, con quale coda) per una regola nata in una data."""
    nuova = _nata_dal(nota, quando)
    return (rep.errore if nuova else rep.avviso), ("" if nuova else coda_debito)


def controlla_artefatto_assenza(nota, rep):
    """Chi dichiara un'assenza rimanda all'artefatto della ricerca, e l'artefatto esiste.

    L'assenza si riconosce per due vie — la formula di attestazione di E3 e il riconoscitore
    della classe `assenza` — e ognuna porta il proprio regime di data.
    """
    if nota.type in ("index", "sessione", "daily"):
        return

    con_formula = bool(FORMULA_E3.search(nota.corpo))
    # ⚠️ LE NOTE-STRUMENTO DEL PROGETTO RESTANO FUORI DALLA SECONDA VIA (E20), e non e' una
    # deroga: parlano degli attrezzi del progetto, non di Aurora, e «la promessa del vault e' che
    # nessuna nota sia irraggiungibile» non e' un'assenza dichiarata sul corpus. E' lo stesso
    # perimetro che `censimento_superlativi.py` esclude, e per la stessa ragione.
    # La formula di E3, invece, resta controllata ovunque: se una nota la scrive, l'artefatto
    # deve esserci comunque.
    assenze = []
    if not Q.e_nota_strumento(nota):
        _superlativi, assenze, _omonimie = Q.occorrenze_di_perimetro(nota)
    if not con_formula and not assenze:
        return

    rimandi = RIMANDO_E3.findall(nota.corpo)

    if con_formula:
        segnala, coda = _regime(nota, rep, NASCITA_E43,
                                " — debito anteriore a E43, da sanare a fine corsa")
        se_manca = ("dichiara un'assenza con la formula di E3 ma non rimanda a un artefatto "
                    "di ricerca in 06_operativo\\ricerche_assenza\\ (E43)%s" % coda)
    else:
        # ⚠️ L'assenza c'e' e la formula no: e' la superficie che il gate del lotto 3D ha
        # aperto. Si cita la frase, perche' un rilievo su una forma va mostrato a chi lo legge.
        segnala, coda = _regime(
            nota, rep, NASCITA_ASSENZA_FUORI_FORMULA,
            " — debito anteriore al riconoscitore della classe `assenza`, da sanare a "
            "fine corsa")
        dove, _q, _p, frase = assenze[0]
        se_manca = ("dichiara un'assenza sull'archivio FUORI dalla formula di attestazione di "
                    "E3, in `%s` («%s»), e non rimanda a nessun artefatto di ricerca "
                    "in 06_operativo\\ricerche_assenza\\: si riscrive con la formula e la "
                    "ricerca lascia il suo artefatto, oppure si restringe il perimetro "
                    "(E3, E43)%s" % (dove, _taglia(frase), coda))

    if not rimandi:
        segnala(nota.nome, CONTROLLO, se_manca)
        return
    for r in rimandi:
        if not os.path.isfile(os.path.join(DIR_RICERCHE, r)):
            segnala(nota.nome, CONTROLLO,
                    "rimanda all'artefatto di ricerca '%s', che non esiste in "
                    "06_operativo\\ricerche_assenza\\ (E43)%s" % (r, coda))


def _taglia(frase, quante=140):
    return frase if len(frase) <= quante else frase[:quante].rstrip() + "…"


# ---- I FINE RIGA DEL VAULT ---------------------------------------------------------
# ⚠️ E' il primo controllo del progetto che non guarda il CONTENUTO di una nota ma il suo
# SUPPORTO, e c'e' una ragione perche' esista: il vault e' l'oggetto che la Sessione 6
# misurera', e fino al lotto 2A nessuno script ne guardava la forma fisica. In quel lotto 39
# note sono nate con terminatori CRLF in un vault che usa LF — se ne e' accorto un occhio, non
# uno strumento — e poi altre 21 ci sono tornate perche' ogni riscrittura le riportava al
# terminatore della piattaforma: quella seconda volta non se n'era accorto nessuno.
#
# Il controllo non impone un terminatore: pretende OMOGENEITA'. Il riferimento e' la
# maggioranza delle note del VAULT — non del perimetro — perche' un lotto piccolo scritto
# tutto male si dichiarerebbe altrimenti conforme a se stesso.

def terminatori(percorso):
    """(crlf, lf_isolati) di un file, contati sui byte."""
    d = open(percorso, "rb").read()
    crlf = d.count(b"\r\n")
    return crlf, d.count(b"\n") - crlf


def stile_dominante(note):
    """Il terminatore che il vault usa davvero: 'crlf' o 'lf', a maggioranza."""
    c = l = 0
    for n in note:
        crlf, lf = terminatori(n.percorso)
        if crlf and not lf:
            c += 1
        elif lf and not crlf:
            l += 1
    return "crlf" if c > l else "lf"


def controlla_fine_riga(nota, rep, dominante):
    crlf, lf = terminatori(nota.percorso)
    if crlf and lf:
        rep.errore(nota.nome, CONTROLLO,
                   "fine riga MISTI dentro lo stesso file: %d CRLF e %d LF isolati" % (crlf, lf))
        return
    suo = "crlf" if crlf else "lf"
    if (crlf or lf) and suo != dominante:
        rep.errore(nota.nome, CONTROLLO,
                   "fine riga %s in un vault che usa %s: il supporto del vault va omogeneo"
                   % (suo.upper(), dominante.upper()))


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
    dominante = stile_dominante(note)
    for n in perimetro:
        controlla(n, rep, oggi, nomi_manifest, aree_con_hub)
        controlla_fine_riga(n, rep, dominante)

    rep.stampa()
    d = Q.cartella_report(args, modo, "l26130")
    Q.scrivi_report(d, "qa_frontmatter.md", rep.markdown())
    sys.exit(rep.codice())


if __name__ == "__main__":
    main()
