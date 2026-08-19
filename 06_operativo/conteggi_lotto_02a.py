# -*- coding: utf-8 -*-
"""conteggi_lotto_02a — i numeri contati del lotto 2A (lavaggio CIP).

Regola d'oro 5: nessun numero si dichiara senza che uno script l'abbia contato.
Ogni conteggio che entra in una nota del lotto 2A nasce qui, e il criterio di
conteggio e' scritto accanto al numero — perche' un conteggio e' un valore
derivato (metodo_03 §5.4, E7) e va dichiarato col suo criterio.

⚠️ QUESTO SCRIPT NON GIUDICA, CONTA. Il confronto fra cio' che il log registra e
cio' che IO-05 prescrive e' una CONTRADDIZIONE CON VINCITORE gia' registrata
(metodo_03 §5.2, esempio 17): vince IO-05, il log resta com'e', e non si apre
nessuna questione. Le soglie qui sotto sono quelle scritte in IO-05 e servono a
contare quante letture ci stanno dentro e quante no — non a correggere il log.

⚠️ IL CRITERIO DI CONDUCIBILITA' DEL RISCIACQUO FINALE NON E' VERIFICABILE SUL
LOG, ed e' un risultato, non un limite dello script. IO-05 lo scrive come
DIFFERENZA — «≤ 50 µS/cm sopra il valore dell'acqua di rete» — e il log non
registra mai il valore dell'acqua di rete. Percio' lo script riporta i valori
ASSOLUTI e il margine ammesso, e lascia al lettore la sola inferenza che regge:
anche assumendo un'acqua di rete a 0 µS/cm — che non esiste — il margine sarebbe
superato. Un criterio differenziale contro un dato assoluto non si «adatta»: si
dichiara non verificabile.

Uso:  python conteggi_lotto_02a.py
"""
import collections, datetime, io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
SRC = r"C:\Users\buulo\Desktop\aurora-cervello\sources"

LOG = "log_lavaggio_CIP_linea1_maggio.log"
IO05 = "IO-05_istruzione_operativa_lavaggio_CIP.docx"
SDS = "scheda_sicurezza_detergente_acido_lavaggio_CIP.txt"

# Cio' che IO-05 PRESCRIVE, tabella «SEQUENZA DELLE FASI» e «CRITERI DI
# ACCETTAZIONE». Si scrive qui una volta sola: e' il termine di paragone, e va
# letto in IO-05, non ricopiato in ogni nota (E40).
#   fase nel log -> (minuti prescritti, T minima, T massima)
PRESCRITTO = {
    "PRERISCIACQUO":     (10, None, None),
    "SODA_2PC":          (30, 75.0, 80.0),
    "RISCIACQUO_INT":    (10, None, None),
    "ACIDO_HNO3_1.5PC":  (20, 60.0, 65.0),
    "RISCIACQUO_FIN":    (15, None, None),
    "SANIF_PAA":         (15, None, None),
}
PORTATA_PRESCRITTA = 15.0          # m3/h, uguale per tutte e sei le fasi
MARGINE_COND_US = 50.0             # µS/cm sopra l'acqua di rete, criterio IO-05


def righe(nome):
    return [r for r in io.open(os.path.join(SRC, nome), encoding="utf-8",
                               errors="replace").read().splitlines() if r.strip()]


def titolo(t):
    print("\n" + "=" * 74)
    print(t)
    print("=" * 74)


def leggi_log():
    """I cicli del log, ciascuno con le sue letture per fase."""
    cicli, cur, fase = [], None, None
    for r in righe(LOG):
        c = r.split(";")
        if len(c) < 8:
            continue
        ts, ev, val, esito = c[0], c[2], c[3], c[5]
        if ev == "CYCLE_START":
            cur = {"start": ts, "esito": None, "esito_col": None, "eventi": [],
                   "prg": c[6], "op": c[7], "letture": collections.defaultdict(list),
                   "durate": {}}
            cicli.append(cur)
            fase = None
        if cur is None:
            continue
        if ev == "FASE_START":
            fase = val
        elif ev == "FASE_END":
            m = re.match(r"(\S+) DUR=(\d+)s", val)
            if m:
                cur["durate"][m.group(1)] = int(m.group(2))
        elif ev in ("COND", "TT_CIP", "FT_CIP") and fase:
            cur["letture"][(fase, ev)].append((ts, float(val), esito))
        elif ev == "CYCLE_END":
            cur["esito"] = val.replace("ESITO=", "")
            cur["esito_col"] = esito
        elif ev in ("ALM_LOW_COND", "ALM_COND_PROBE", "CIP_ABORT", "NOTE_SYS",
                    "DOSING_SODA", "TANK_LEVEL_SODA"):
            cur["eventi"].append((ts, ev, val, esito))
    return cicli


def main():
    rig = righe(LOG)
    cicli = leggi_log()
    giorni = sorted({r.split(";")[0][:10] for r in rig})

    titolo("1. IL LOG DEL LAVAGGIO CIP — forma del file")
    print("righe non vuote ............................. %d" % len(rig))
    print("prima riga .................................. %s" % rig[0].split(";")[0])
    print("ultima riga ................................. %s" % rig[-1].split(";")[0])
    print("giorni distinti con almeno una riga ......... %d" % len(giorni))
    d0 = datetime.date(2026, 5, 1)
    senza = [(d0 + datetime.timedelta(days=i)).isoformat() for i in range(31)
             if (d0 + datetime.timedelta(days=i)).isoformat() not in giorni]
    print("giorni di maggio SENZA nessuna riga ......... %d  (%s)"
          % (len(senza), ", ".join(senza)))
    tipi = collections.Counter(r.split(";")[2] for r in rig)
    print("\n| Tipo di evento | Righe |")
    print("|---|---|")
    for t, n in tipi.most_common():
        print("| `%s` | %d |" % (t, n))
    print("\ncolonna esito, conteggio per valore:")
    for e, n in collections.Counter(r.split(";")[5] for r in rig).most_common():
        print("  %-6s %d" % (e, n))

    titolo("2. I CICLI")
    esiti = collections.Counter(c["esito"] for c in cicli)
    print("cicli (righe `CYCLE_START`) ................. %d" % len(cicli))
    for e, n in esiti.most_common():
        print("  di cui esito %-6s ....................... %d" % (e, n))
    prg = {c["prg"] for c in cicli}
    print("programmi dichiarati nel campo PRG .......... %d  (%s)"
          % (len(prg), ", ".join(sorted(prg))))
    op = collections.Counter(c["op"] for c in cicli)
    print("operatori sui cicli:")
    for o, n in op.most_common():
        print("  %-16s %d cicli" % (o.replace("OP=", ""), n))

    # i cicli chiusi PASS con la sonda di conducibilita' in guasto
    guasti = [c for c in cicli
              if any(ev == "ALM_COND_PROBE" for _t, ev, _v, _e in c["eventi"])]
    print("\ncicli con allarme sonda di conducibilita' `ALM_COND_PROBE`: %d" % len(guasti))
    for c in guasti:
        print("  %s  esito=%-5s colonna=%-5s  %s" % (
            c["start"], c["esito"], c["esito_col"],
            "; ".join("%s %s" % (ev, v) for _t, ev, v, _e in c["eventi"])))
    abort = [c for c in cicli if c["esito"] == "ABORT"]
    print("\ncicli interrotti `ABORT`: %d" % len(abort))
    for c in abort:
        print("  %s  %s" % (c["start"],
              "; ".join("%s %s" % (ev, v) for _t, ev, v, _e in c["eventi"])))

    titolo("3. LE DURATE DELLE FASI — log contro IO-05")
    print("| Fase | n cicli | durata log (s) | minuti log | IO-05 (min) | scarto |")
    print("|---|---|---|---|---|---|")
    for fase, (min_presc, _tmin, _tmax) in PRESCRITTO.items():
        v = [c["durate"][fase] for c in cicli if fase in c["durate"]]
        if not v:
            continue
        u = sorted(set(v))
        print("| `%s` | %d | %s | %.0f | %d | **-%.0f min** |"
              % (fase, len(v), "·".join(str(x) for x in u), v[0] / 60.0,
                 min_presc, min_presc - v[0] / 60.0))
    print("\ntutte le durate sono COSTANTI ciclo per ciclo: %s"
          % all(len({c["durate"][f] for c in cicli if f in c["durate"]}) == 1
                for f in PRESCRITTO))

    titolo("4. LE TEMPERATURE — letture fuori dai limiti di IO-05")
    print("| Fase | letture TT_CIP | min | max | limite IO-05 | fuori limite | % |")
    print("|---|---|---|---|---|---|---|")
    for fase, (_m, tmin, tmax) in PRESCRITTO.items():
        v = [x for c in cicli for _t, x, _e in c["letture"][(fase, "TT_CIP")]]
        if not v:
            continue
        if tmin is None:
            print("| `%s` | %d | %.1f | %.1f | *(ambiente)* | — | — |"
                  % (fase, len(v), min(v), max(v)))
        else:
            fuori = [x for x in v if x < tmin or x > tmax]
            print("| `%s` | %d | %.1f | %.1f | %.0f-%.0f °C | **%d** | %.1f %% |"
                  % (fase, len(v), min(v), max(v), tmin, tmax, len(fuori),
                     100.0 * len(fuori) / len(v)))

    titolo("5. LA PORTATA — IO-05 prescrive %.0f m3/h su tutte le fasi" % PORTATA_PRESCRITTA)
    ft = [x for c in cicli for k in c["letture"] if k[1] == "FT_CIP"
          for _t, x, _e in c["letture"][k]]
    sotto = [x for x in ft if x < PORTATA_PRESCRITTA]
    print("letture `FT_CIP` .......................... %d" % len(ft))
    print("intervallo ................................ %.1f - %.1f m3/h" % (min(ft), max(ft)))
    print("sotto i %.0f m3/h prescritti ............... %d  (%.1f %%)"
          % (PORTATA_PRESCRITTA, len(sotto), 100.0 * len(sotto) / len(ft)))
    print("massimo misurato in %% del prescritto ...... %.1f %%"
          % (100.0 * max(ft) / PORTATA_PRESCRITTA))

    titolo("6. LA CONDUCIBILITA' DEL RISCIACQUO FINALE")
    cond = [(c["start"], t, x, e) for c in cicli
            for t, x, e in c["letture"][("RISCIACQUO_FIN", "COND")]]
    validi = [x for _s, _t, x, _e in cond if x > -900]
    fault = [(s, t, x) for s, t, x, _e in cond if x <= -900]
    print("letture `COND` in fase `RISCIACQUO_FIN` ... %d" % len(cond))
    print("  di cui valore di guasto `-999.9` ....... %d  %s"
          % (len(fault), [t for _s, t, _x in fault]))
    print("  letture con un valore ................... %d" % len(validi))
    print("intervallo ................................ %.1f - %.1f mS/cm"
          % (min(validi), max(validi)))
    print("in microsiemens ........................... %.0f - %.0f µS/cm"
          % (min(validi) * 1000, max(validi) * 1000))
    print("margine ammesso da IO-05 .................. %.0f µS/cm SOPRA l'acqua di rete"
          % MARGINE_COND_US)
    print("valore dell'acqua di rete nel log ......... MAI REGISTRATO")
    print("→ il criterio e' DIFFERENZIALE e il termine di riferimento non esiste nel")
    print("  file: il criterio NON e' verificabile sul log. L'unica cosa che il log")
    print("  permette di dire e' che il valore assoluto piu' basso, %.0f µS/cm, e' gia'"
          % (min(validi) * 1000))
    print("  %.0f volte il solo margine ammesso." % (min(validi) * 1000 / MARGINE_COND_US))
    ultime = [c["letture"][("RISCIACQUO_FIN", "COND")][-1][1] for c in cicli
              if c["letture"][("RISCIACQUO_FIN", "COND")]]
    print("\nultima lettura di ogni ciclo che arriva al risciacquo finale: %d cicli"
          % len(ultime))
    print("  intervallo %.1f - %.1f mS/cm" % (min(ultime), max(ultime)))

    titolo("7. LA CONDUCIBILITA' NELLE ALTRE FASI, e la soglia del pannello")
    print("| Fase | letture COND | min | max |")
    print("|---|---|---|---|")
    for fase in PRESCRITTO:
        v = [x for c in cicli for _t, x, _e in c["letture"][(fase, "COND")] if x > -900]
        if v:
            print("| `%s` | %d | %.1f | %.1f |" % (fase, len(v), min(v), max(v)))
    print("\nla sola soglia che il pannello IMPLEMENTA compare nel testo dell'allarme:")
    for c in cicli:
        for _t, ev, v, _e in c["eventi"]:
            if ev == "ALM_LOW_COND":
                print("  %s -> «%s»" % (ev, v))
                break

    titolo("8. LE FASI ESEGUITE CONTRO IL PROGRAMMA DICHIARATO")
    seq = collections.Counter()
    for c in cicli:
        seq[tuple(sorted(c["durate"]))] += 1
    for s, n in seq.most_common():
        print("  %d cicli eseguono le fasi: %s" % (n, ", ".join(s)))
    print("\nIO-05 assegna al programma P2 le fasi 1-2-3-4-5 (senza sanificazione);")
    print("la fase 6, sanificazione PAA, appartiene a P4 e P5.")
    print("cicli che eseguono `SANIF_PAA` ............ %d"
          % sum(1 for c in cicli if "SANIF_PAA" in c["durate"]))

    titolo("9. LA SCHEDA DI SICUREZZA — forma del file e integrita' autodichiarata")
    r = righe(SDS)
    print("righe non vuote ........................... %d" % len(r))
    pagine = sorted({int(m.group(1)) for x in r
                     for m in [re.search(r"Pagina (\d+) di 11", x)] if m})
    print("numeri di pagina presenti ................. %s" % pagine)
    print("mancanti sulle 11 dichiarate .............. %s"
          % [p for p in range(1, 12) if p not in pagine])
    for x in r:
        if "non presente nell OCR" in x or "annotazione a margine" in x \
                or "TIMBRO ILLEGGIBILE" in x or "aggiornare raccoglitore" in x \
                or "la rev in linea" in x:
            print("  dichiarazione nel file: %s" % x.strip())

    titolo("10. LE DUE FONTI PRESCRITTIVE NOMINANO LO STESSO PRODOTTO?")
    io05 = ""
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "qa"))
        import qa_comune as Q
        io05 = Q.testo_fonte(IO05)
    except Exception as ex:
        print("  (estrazione IO-05 non riuscita: %s)" % str(ex)[:60])
    sds = "\n".join(r)
    for sigla in ("AN-15", "CS-40", "SAN-P5", "ACIDFOOD CIP 25", "CF-AC-025",
                  "Chemifood", "CHEMIFOOD"):
        print("  %-18s  in IO-05: %-3s   nella scheda di sicurezza: %s"
              % (sigla, "si" if sigla in io05 else "NO",
                 "si" if sigla in sds else "NO"))


if __name__ == "__main__":
    main()
