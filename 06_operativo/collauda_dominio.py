# -*- coding: utf-8 -*-
r"""collauda_dominio — E59: la dichiarazione del dominio si collauda PRIMA della misura.

⚠️ NASCE CON E59 (gate del lotto 3B, 23/08/2026), e nasce da tre consuntivi concordi.
E56 dice che le due meta' della dichiarazione — espressioni e fonti — devono corrispondersi.
**Tre dichiarazioni su tre sono nate sbagliate lo stesso**, e la terza sotto E56 gia' in
vigore:

  - **2B-bis**, `allergeni`: troppo **stretta** — mancava il materiale d'aula — e il **9,1 %**
    contava scoperte note che una fonte non dichiarata copriva;
  - **3C**, `certificazione`: troppo **larga** — espressioni sull'audit, fonti sul titolo — e
    il **38,7 %** contava scoperte note governate da altre fonti;
  - **3B**, `formazione`: troppo **larga**, e `\bformazion` **da sola pescava tutte e
    quattordici** le scoperte. Tasso da **63,6 %** a **36,4 %** stringendo una volta.

⚠️ **Una regola che chiede attenzione ha fallito al suo primo impiego: quello che serve non e'
piu' attenzione, e' UNA PROVA.**

=====================================================================================
DUE PROVE, E NON SI SOMMANO
=====================================================================================

**PROVA A — LA SPECIFICITA'. Si puo' fare sempre.** Per ogni espressione: quante note
riconosce, quante ne riconosce **in esclusiva** (nessun'altra espressione del dominio le
prende), e **che quota dell'unione del dominio copre da sola**.

⚠️ **E' la prova che 3B ha eseguito a mano, ed e' quella che ha trovato il difetto**:
`\bformazion` copriva **il 100 %** del dominio da sola. Un'espressione che da sola vale quasi
tutto il dominio non sta riconoscendo il dominio: sta riconoscendo **una parola**, e le altre
espressioni sono decorative. La soglia e' `--copertura`, di default **0,90**.

⚠️ **UNA SOSPETTA NON SI SCARICA CAMBIANDO LA SOGLIA.** Si scarica con `--motivata
<espressione>`, che la registra in chiaro nell'uscita, **e con una ragione scritta nel
rapporto**. La ragione ammessa e' una sola: **la parola e la cosa coincidono** — il dominio si
chiama con quella parola, e chi la usa sta parlando di quello. In `formazione` NON
coincidevano.

**PROVA B — DENTRO E FUORI. Si puo' fare solo se le fonti del dominio sono gia' citate da
qualche nota.** Per ogni espressione: quante delle note riconosciute citano una **fonte del
dominio** e quante citano **soltanto altre** fonti prescrittive. Sopra `--soglia` (default
**0,50**) di riconosciute che stanno **solo** fuori, l'espressione e' generica.

⚠️ **QUANDO IL LOTTO STA PORTANDO LUI LA FONTE DEL DOMINIO, LA PROVA B NON SI PUO' FARE, E
NON SI FA FINTA CHE SI POSSA.** Nessuna nota puo' citare una fonte non ancora canonizzata:
la colonna «dentro» sarebbe zero **per costruzione**, e ogni espressione risulterebbe generica
— **compresa la sigla del modulo che la procedura istituisce**, che e' l'espressione piu'
specifica che il dominio possa avere. ⚠️ **Peggio: una nota che parla di reclami citando il
manuale HACCP non e' «governata altrove», e' SCOPERTA** — cioe' esattamente cio' che il tasso
di E41 esiste per contare. Confonderle farebbe respingere le espressioni giuste e sopravvivere
quelle sbagliate. **Lo script dichiara la prova B NON APPLICABILE e stampa il dettaglio come
diagnostica**, perche' il giudizio di E56 resta e va scritto nel rapporto.

⚠️ **NON E' UN'OCCASIONE PER RESTRINGERE A NUMERO VISTO.** Si prova **l'espressione**, non il
tasso: la prova si chiude quando le espressioni hanno superato il collaudo, non quando il
numero piace (§4.43).

Uso:
    python collauda_dominio.py --dominio reclami
    python collauda_dominio.py --dominio formazione --copertura 0.9
Esce 0 se ogni espressione supera le prove applicabili, 1 altrimenti.
"""
import argparse
import importlib.util
import os
import sys
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q   # noqa: E402

_spec = importlib.util.spec_from_file_location("candidate_r1", os.path.join(QUI, "candidate_r1.py"))
C1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C1)


def note_di_contenuto(vault):
    fuori = []
    for n in Q.tutte_le_note(vault):
        if n.fm is None or n.cartella in Q.ESCLUSE_QUALITA:
            continue
        if n.type in ("index", "sessione", "daily") or Q.e_nota_strumento(n):
            continue
        fuori.append(n)
    return fuori


def main():
    ap = argparse.ArgumentParser(description="E59: il collaudo della dichiarazione del dominio.")
    ap.add_argument("--dominio", required=True, choices=sorted(C1.DOMINI))
    ap.add_argument("--vault", default=Q.VAULT)
    ap.add_argument("--soglia", type=float, default=0.50,
                    help="prova B: quota di riconosciute che stanno SOLO fuori, oltre la quale l'espressione e' generica")
    ap.add_argument("--copertura", type=float, default=0.90,
                    help="prova A: quota dell'unione del dominio coperta da UNA sola espressione, oltre la quale e' sospetta")
    ap.add_argument("--motivata", action="append", default=[], metavar="ESPRESSIONE",
                    help="prova A: una SOSPETTA discussa e tenuta di proposito. Va scritta VERBATIM, "
                         "e il rapporto deve portarne la ragione: il collaudo non la dimentica, "
                         "la registra")
    args = ap.parse_args()

    dom = C1.DOMINI[args.dominio]
    fonti_dom = set(dom["fonti"])
    altre = set(C1.PRESCRITTIVE) - fonti_dom
    note = note_di_contenuto(args.vault)
    quando = datetime.now()

    citate = set()
    for n in note:
        citate |= {str(f) for f in n.fonti}
    non_canonizzate = sorted(f for f in fonti_dom if f not in citate)
    prova_b = len(non_canonizzate) < len(fonti_dom)

    # quali note prende ogni espressione
    presa = {}
    for rx in dom["rx"]:
        presa[rx.pattern] = {n.slug for n in note if rx.search(C1.testo_della_nota(n))}
    unione = set()
    for s in presa.values():
        unione |= s

    print("=" * 92)
    print("E59 - COLLAUDO DELLA DICHIARAZIONE: dominio «%s»" % args.dominio)
    print("misura delle %s del %s" % (quando.strftime("%H:%M:%S"), quando.strftime("%d/%m/%Y")))
    print("=" * 92)
    print("note di contenuto valutate ........ %d" % len(note))
    print("note prese dal dominio (unione) ... %d" % len(unione))
    print("fonti del dominio ................. %d" % len(fonti_dom))
    for f in sorted(fonti_dom):
        print("    %s%s" % (f, "   [NON ANCORA CITATA DA NESSUNA NOTA]" if f in non_canonizzate else ""))
    print("altre fonti prescrittive .......... %d" % len(altre))

    guasti = []
    motivate = []

    # ---------------------------------------------------------------- PROVA A
    print("")
    print("-" * 92)
    print("PROVA A - LA SPECIFICITA'. Un'espressione che da sola vale quasi tutto il dominio")
    print("          non riconosce il dominio: riconosce una parola. Soglia: %.2f" % args.copertura)
    print("-" * 92)
    print("| Espressione | Riconosce | In esclusiva | Quota dell'unione | Esito |")
    print("|---|---|---|---|---|")
    for rx in dom["rx"]:
        s = presa[rx.pattern]
        altri = set()
        for p2, s2 in presa.items():
            if p2 != rx.pattern:
                altri |= s2
        esclusive = s - altri
        quota = (len(s) / len(unione)) if unione else 0.0
        sospetta = bool(unione) and quota > args.copertura and len(dom["rx"]) > 1
        motivata = rx.pattern in args.motivata
        if sospetta and not motivata:
            guasti.append("A: `%s` copre da sola il %.0f %% dell'unione del dominio"
                          % (rx.pattern, 100 * quota))
        if sospetta and motivata:
            motivate.append(rx.pattern)
        etichetta = "ok" if s else "*non riconosce nulla*"
        if sospetta:
            etichetta = "**SOSPETTA MOTIVATA**" if motivata else "**SOSPETTA**"
        print("| `%s` | %d | %d | %.2f | %s |"
              % (rx.pattern, len(s), len(esclusive), quota, etichetta))

    mute = [rx.pattern for rx in dom["rx"] if not presa[rx.pattern]]
    if mute:
        print("")
        print("⚠️  Espressioni che non riconoscono NESSUNA nota del vault: %d" % len(mute))
        for p2 in mute:
            print("      `%s`" % p2)
        print("   Non e' un difetto di per se': una locuzione che il vault non ha ancora usato")
        print("   e' muta finche' il lotto non la scrive. **Ma va guardata**: se resta muta anche")
        print("   a lotto chiuso, non stava riconoscendo niente.")

    # ---------------------------------------------------------------- PROVA B
    print("")
    print("-" * 92)
    if not prova_b:
        print("PROVA B - DENTRO E FUORI: **NON APPLICABILE**, e il motivo va letto prima dei numeri.")
        print("-" * 92)
        print("Nessuna fonte del dominio e' ancora citata da una nota: il lotto la sta portando")
        print("adesso. La colonna «dentro» sarebbe zero PER COSTRUZIONE, e ogni espressione")
        print("risulterebbe generica - compresa la sigla del modulo che la procedura istituisce.")
        print("⚠️  E una nota che parla del dominio citando un'ALTRA fonte prescrittiva non e'")
        print("   «governata altrove»: e' SCOPERTA, cioe' esattamente cio' che il tasso di E41")
        print("   esiste per contare. Il numero qui sotto e' DIAGNOSTICA, non un verdetto.")
    else:
        print("PROVA B - DENTRO E FUORI. Soglia di genericita': %.2f" % args.soglia)
        print("-" * 92)
    print("")
    print("| Espressione | Riconosce | cita il dominio | solo altre prescrittive | nessuna prescrittiva | quota fuori |")
    print("|---|---|---|---|---|---|")
    per_slug = {n.slug: n for n in note}
    for rx in dom["rx"]:
        dentro = fuori_altre = grigie = 0
        for slug in presa[rx.pattern]:
            f = {str(x) for x in per_slug[slug].fonti}
            if f & fonti_dom:
                dentro += 1
            elif f & altre:
                fuori_altre += 1
            else:
                grigie += 1
        tot = dentro + fuori_altre + grigie
        quota = (fuori_altre / tot) if tot else 0.0
        if prova_b and tot and quota > args.soglia:
            guasti.append("B: `%s` riconosce prevalentemente note governate da altre fonti (%.2f)"
                          % (rx.pattern, quota))
        print("| `%s` | %d | %d | %d | %d | %.2f |"
              % (rx.pattern, tot, dentro, fuori_altre, grigie, quota))

    if motivate:
        print("")
        print("SOSPETTE TENUTE DI PROPOSITO: %d" % len(motivate))
        for p2 in motivate:
            print("      `%s`" % p2)
        print("   ⚠️ Una sospetta si scarica con una RAGIONE SCRITTA nel rapporto, non")
        print("   cambiando la soglia. La ragione ammessa e' una sola: **la parola e la cosa")
        print("   coincidono** - il dominio si chiama con quella parola e chi la usa parla di")
        print("   quello. In `formazione` NON coincidevano, e `\\bformazion` prendeva la")
        print("   struttura di un file e un indicatore: il tasso passo' da 63,6 % a 36,4 %.")

    print("")
    if guasti:
        print("COLLAUDO FALLITO: %d rilievi" % len(guasti))
        for g in guasti:
            print("  - " + g)
        print("")
        print("⚠️ Un'espressione respinta NON si tiene «per prudenza»: gonfia il tasso con note")
        print("   che un altro dominio governa, ed e' cio' che ha prodotto il 38,7 % di 3C e il")
        print("   63,6 % di 3B al primo taglio.")
        return 1
    print("COLLAUDO SUPERATO sulle prove applicabili.")
    print("⚠️ Superarlo non vuol dire che il dominio sia giusto: vuol dire che nessuna")
    print("   espressione e' una parola travestita da dominio. **La corrispondenza fra le due")
    print("   meta' (E56) resta un giudizio, e si scrive nel rapporto, espressione per")
    print("   espressione.**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
