# -*- coding: utf-8 -*-
"""grandezze_condivise — l'artefatto d'apertura di E2, che dice DOVE guardare.

⚠️ NASCE CON E60 (gate del lotto 3B, 23/08/2026), e nasce da due consuntivi.
`metodo_03` §5.1-bis prescrive la riconciliazione ORIZZONTALE dal gate S2 (E2) e la chiama
«la regola piu' redditizia del metodo». Per **due lotti di fila** l'ha eseguita **il revisore
al posto del ciclo**:

  - **3A**: il rilievo era testuale, «mai contro il vault intorno»;
  - **3B**: **sette delle otto divergenze scrivibili** nascono dall'accostamento col verbale
    di riesame **canonizzato il giorno prima**, non dai due grezzi del lotto.

⚠️ **Il difetto non era la diligenza: era che non c'era niente da guardare.** Chi apre un lotto
sa quali documenti ha in mano; **non sa quali note, scritte settimane fa, parlano delle stesse
cose**. Questo script glielo dice **prima** che scriva, non dopo.

CHE COSA PRODUCE, e sono due elenchi che rispondono a due domande diverse:

  A. **DENTRO IL LOTTO** — le grandezze che compaiono in **piu' di un grezzo**. E' la
     riconciliazione orizzontale classica: due documenti che dicono la stessa cosa, e il
     confronto va scritto (§5.1-bis: coincidono / divergono con vincitore / divergono senza).

  B. **FRA IL LOTTO E IL VAULT** — le grandezze dei grezzi che **una nota gia' scritta porta
     gia'**, con il nome della nota. E' la meta' che nessuno guardava, ed e' quella che in 3B
     ha prodotto sette divergenze su otto.

⚠️ **LA GRAMMATICA DELLE GRANDEZZE NON E' NUOVA, ED E' DELIBERATO**: si riusa
`qa_provenance.estrai_affermazioni`, cioe' la **stessa** definizione di «affermazione
verificabile» che la QA usa per bocciare una nota — numeri, date, orari, codici, citazioni.
**Una seconda definizione divergerebbe in un mese** (un fatto, un padrone), e per giunta
farebbe guardare a chi apre il lotto cose diverse da quelle su cui verra' giudicato.

⚠️ **Le entita' si riconoscono dal vault, non da una lista**: sono i nomi che le note
`entita-*` gia' portano, con i loro `aliases`. Un'entita' che il vault non conosce ancora non
e' una grandezza CONDIVISA: e' una grandezza nuova, e il lotto la scoprira' scrivendo.

⚠️ **QUESTO SCRIPT NON CONCLUDE NIENTE.** Dice dove guardare. Se due grezzi portano lo stesso
numero, non dice se coincidono nel merito: dice che vanno letti insieme. **Il rapporto dichiara
i confronti fatti, uno per uno** (E60), e un confronto non dichiarato non si distingue da un
confronto non fatto.

Uso:
    python grandezze_condivise.py --lotto lotto_03d_reclami
    python grandezze_condivise.py --lotto <nome> --stdout    # non scrive l'artefatto
Esce 0 se l'artefatto e' stato prodotto, 1 se l'elenco del lotto non esiste.
"""
import argparse
import io
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q            # noqa: E402
import estrazione_cantiere as EC  # noqa: E402
import qa_provenance as P        # noqa: E402

DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
DIR_USCITA = os.path.join(QUI, "grandezze_condivise")

# I generi che vale la pena confrontare. Le CITAZIONI restano fuori: due documenti che
# ripetono la stessa frase non sono una divergenza di grandezza, sono una copia — e la
# copia la prende gia' il controllo delle citazioni testuali.
GENERI = ("codice", "data", "ora", "numero")

# Un numero identificante: almeno tre cifre significative. Stesso criterio di
# `qa_copertura`, che lo usa per le doppie padrone — e per la stessa ragione: «3» e «2026»
# compaiono ovunque e non identificano niente.
def identificante(genere, testo):
    if genere != "numero":
        return True
    cifre = "".join(c for c in testo if c.isdigit()).lstrip("0")
    if len(cifre) < 3:
        return False
    # gli anni da soli non sono grandezze: sono contesto
    return not re.fullmatch(r"(19|20)\d\d", testo)


def grezzi_del_lotto(lotto):
    p = os.path.join(DIR_LOTTI, lotto + ".txt")
    if not os.path.isfile(p):
        return None
    fuori = []
    for riga in io.open(p, encoding="utf-8"):
        riga = riga.strip()
        if riga and not riga.startswith("#"):
            fuori.append(riga)
    return fuori


def entita_del_vault(note):
    """Nome -> slug della nota, per le note `entita-*`: title, aliases e nome proprio.

    ⚠️ Si prendono solo i token di almeno quattro lettere: un alias di due lettere
    riscontrerebbe dappertutto, ed e' la stessa ragione per cui `verifica_dominio` tiene
    separati i riscontri forti dai deboli."""
    fuori = {}
    for n in note:
        if n.type != "entita" or n.fm is None:
            continue
        nomi = [str(n.fm.get("title") or "")]
        al = n.fm.get("aliases") or []
        nomi += [str(a) for a in (al if isinstance(al, list) else [al])]
        for nome in nomi:
            # dal title si tiene la parte prima del trattino lungo: «Elena Marchetti — RSGQ»
            nome = re.split(r"\s+[—–-]\s+", nome)[0].strip()
            if len(nome) >= 4 and not nome.startswith("_"):
                fuori.setdefault(nome, n.slug)
    return fuori


def main():
    ap = argparse.ArgumentParser(description="E60: le grandezze condivise, in apertura di lotto.")
    ap.add_argument("--lotto", required=True)
    ap.add_argument("--vault", default=Q.VAULT)
    ap.add_argument("--stdout", action="store_true", help="non scrive l'artefatto")
    args = ap.parse_args()

    grezzi = grezzi_del_lotto(args.lotto)
    if grezzi is None:
        print("ERRORE: elenco mancante: %s" % os.path.join(DIR_LOTTI, args.lotto + ".txt"))
        return 1
    if not grezzi:
        print("ERRORE: l'elenco del lotto non porta nessun grezzo (lotto di manutenzione?)")
        return 1

    quando = datetime.now()
    righe = []
    def out(s=""):
        righe.append(s)

    out("# Grandezze condivise — lotto `%s`" % args.lotto)
    out("")
    out("> **Artefatto d'apertura di E2** (E60), generato da `06_operativo\\grandezze_condivise.py`")
    out("> il **%s alle %s**. ⚠️ **Dice DOVE guardare, non che cosa concludere**: se due"
        % (quando.strftime("%d/%m/%Y"), quando.strftime("%H:%M")))
    out("> documenti portano la stessa grandezza, vanno letti insieme — l'esito del confronto lo")
    out("> scrive il rapporto, uno per uno.")
    out("")
    out("**%d grezzi nel lotto**: %s" % (len(grezzi), ", ".join("`%s`" % g for g in grezzi)))
    out("")

    # ---- estrazione, grezzo per grezzo ---------------------------------------------
    per_grandezza = defaultdict(set)     # (genere, testo) -> {grezzi}
    for g in grezzi:
        try:
            testo = EC.testo_cantiere(g)
        except Exception as ex:
            out("⚠️ **estrazione fallita** su `%s`: %s" % (g, str(ex)[:100]))
            continue
        for genere, tok in P.estrai_affermazioni(testo):
            if genere in GENERI and identificante(genere, tok):
                per_grandezza[(genere, tok)].add(g)

    # ---- A. dentro il lotto ---------------------------------------------------------
    dentro = {k: v for k, v in per_grandezza.items() if len(v) > 1}
    out("## A. Dentro il lotto — le grandezze che compaiono in più di un grezzo")
    out("")
    if not dentro:
        out("**Nessuna.** ⚠️ Non è un esito neutro: un lotto i cui grezzi non condividono nessuna")
        out("grandezza è un lotto **senza riconciliazione orizzontale interna**, e il rapporto lo")
        out("dichiara invece di tacerlo.")
    else:
        out("| Genere | Grandezza | In quali grezzi |")
        out("|---|---|---|")
        for (genere, tok), gs in sorted(dentro.items(), key=lambda x: (-len(x[1]), x[0][0], x[0][1])):
            out("| %s | `%s` | %s |" % (genere, tok, ", ".join("`%s`" % x for x in sorted(gs))))
    out("")
    out("**%d grandezze condivise fra i grezzi del lotto.**" % len(dentro))
    out("")

    # ---- B. fra il lotto e il vault --------------------------------------------------
    note = Q.tutte_le_note(args.vault)
    valutabili = [n for n in note
                  if n.cartella not in Q.ESCLUSE_QUALITA and n.type != "index"
                  and not Q.e_nota_strumento(n)]
    # il testo di una nota: corpo PIU' intestazione, la stessa superficie della QA (§7.1)
    testo_nota = {}
    for n in valutabili:
        testa = "%s\n%s" % ((n.fm or {}).get("title") or "", (n.fm or {}).get("summary") or "")
        t = Q.norm(n.corpo + "\n" + testa)
        testo_nota[n.slug] = (t, t.replace(" ", ""))

    out("## B. Fra il lotto e il vault — le grandezze che una nota già scritta porta già")
    out("")
    out("⚠️ **È la metà che nessuno guardava**, e in 3B ha prodotto **sette divergenze su otto**.")
    out("")
    trovate = []
    for (genere, tok), gs in sorted(per_grandezza.items()):
        if genere == "numero":
            varianti = P.varianti_numero(tok)
        elif genere == "data":
            varianti = P.varianti_data(tok)
        else:
            varianti = {tok}
        dove = []
        for slug, (t, c) in testo_nota.items():
            if any(Q.presente(v, t, c) for v in varianti):
                dove.append(slug)
        if dove:
            trovate.append((genere, tok, sorted(gs), dove))

    if not trovate:
        out("**Nessuna.** Il lotto non tocca nessuna grandezza che il vault già porti.")
    else:
        out("| Genere | Grandezza | Nei grezzi | Le note del vault che la portano già |")
        out("|---|---|---|---|")
        for genere, tok, gs, dove in sorted(trovate, key=lambda x: (-len(x[3]), x[0], x[1])):
            elenco = ", ".join("`%s`" % d for d in dove[:8])
            if len(dove) > 8:
                elenco += " … e altre %d" % (len(dove) - 8)
            out("| %s | `%s` | %s | %s |"
                % (genere, tok, ", ".join("`%s`" % x for x in gs), elenco))
    out("")
    out("**%d grandezze del lotto sono già nel vault**, su %d estratte."
        % (len(trovate), len(per_grandezza)))
    out("")

    # ---- C. le entita' del vault nominate dai grezzi ----------------------------------
    entita = entita_del_vault(note)
    out("## C. Le entità che il vault già conosce, nominate dai grezzi del lotto")
    out("")
    out("⚠️ **Sono le porte del grafo**: una scheda entità già scritta è il posto in cui la")
    out("divergenza fra il lotto e il vault diventa visibile — ed è dove va aggiornata.")
    out("")
    trovate_e = []
    for nome, slug in sorted(entita.items()):
        n_norm = Q.norm(nome)
        dove = []
        for g in grezzi:
            try:
                t = Q.norm(EC.testo_cantiere(g))
            except Exception:
                continue
            if n_norm in t:
                dove.append(g)
        if dove:
            trovate_e.append((nome, slug, dove))
    if not trovate_e:
        out("**Nessuna.**")
    else:
        out("| Entità nominata | Scheda nel vault | In quali grezzi |")
        out("|---|---|---|")
        for nome, slug, dove in sorted(trovate_e, key=lambda x: (-len(x[2]), x[0])):
            out("| %s | `%s` | %s |" % (nome, slug, ", ".join("`%s`" % x for x in dove)))
    out("")
    out("**%d entità del vault sono nominate dai grezzi del lotto.**" % len(trovate_e))

    testo = "\n".join(righe) + "\n"
    if args.stdout:
        sys.stdout.write(testo)
        return 0
    if not os.path.isdir(DIR_USCITA):
        os.makedirs(DIR_USCITA)
    dest = os.path.join(DIR_USCITA, "%s_%s.md" % (args.lotto, quando.strftime("%Y-%m-%d")))
    with io.open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)
    print("artefatto scritto: %s" % dest)
    print("  A. grandezze condivise fra i grezzi ........ %d" % len(dentro))
    print("  B. grandezze del lotto gia' nel vault ...... %d su %d"
          % (len(trovate), len(per_grandezza)))
    print("  C. entita' del vault nominate dai grezzi ... %d" % len(trovate_e))
    print("  misura delle %s del %s" % (quando.strftime("%H:%M:%S"), quando.strftime("%d/%m/%Y")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
