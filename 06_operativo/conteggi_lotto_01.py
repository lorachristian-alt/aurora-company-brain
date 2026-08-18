# -*- coding: utf-8 -*-
"""conteggi_lotto_01 — i numeri contati del lotto 1 (Linea 1).

Regola d'oro 5: nessun numero si dichiara senza che uno script l'abbia contato.
Ogni conteggio che entra in una nota del lotto 1 nasce qui, e il criterio di
conteggio e' scritto accanto al numero — perche' un conteggio e' un valore
derivato (metodo_03 §5.4, E7) e va dichiarato col suo criterio.

⚠️ `scheda_manutenzione_ordinaria_forni_industrial.csv` ha separatore INCOERENTE:
alcune righe usano `;`, altre `,` con i campi fra virgolette. Un parser a
separatore unico legge male meta' file. Si sniffa riga per riga.

Uso:  python conteggi_lotto_01.py
"""
import csv, io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
SRC = r"C:\Users\buulo\Desktop\aurora-cervello\sources"


def righe(nome):
    return io.open(os.path.join(SRC, nome), encoding="utf-8", errors="replace").read().splitlines()


def campi(riga):
    """Sniffa il separatore della SINGOLA riga: ; se ce n'e' almeno uno fuori
    dalle virgolette, altrimenti la virgola."""
    fuori, dentro = 0, False
    for c in riga:
        if c == '"':
            dentro = not dentro
        elif c == ";" and not dentro:
            fuori += 1
    sep = ";" if fuori else ","
    return next(csv.reader([riga], delimiter=sep))


def titolo(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


# ---------------------------------------------------------------- manutenzioni
titolo("scheda_manutenzione_ordinaria_forni_industrial.csv")
rr = righe("scheda_manutenzione_ordinaria_forni_industrial.csv")
dati, sep_pv, sep_vg = [], 0, 0
for r in rr[1:]:
    if not r.strip() or r.startswith("NB ") or set(r) <= {";", ","}:
        continue
    c = campi(r)
    if len(c) < 12:
        continue
    dati.append(c)
    if ";" in r.split('"')[0]:
        sep_pv += 1
    else:
        sep_vg += 1

print("righe di dato ................. %d" % len(dati))
print("  di cui separate da ';' ...... %d" % sep_pv)
print("  di cui separate da ',' ...... %d   <- separatore incoerente nello stesso file" % sep_vg)

stati = {}
for c in dati:
    stati[c[10].strip()] = stati.get(c[10].strip(), 0) + 1
print("\nstati (colonna 'Stato'):")
for k in sorted(stati, key=lambda k: -stati[k]):
    print("   %-14s %3d" % (k or "(vuoto)", stati[k]))

# ⚠️ il file contiene righe DUPLICATE alla lettera: si contano le voci distinte e si
# dichiara quante sono le ripetizioni. La duplicazione e' un fatto del file, non un
# errore di conta, e va registrata come tale (metodo_03: l'integrita' e' contenuto).
arretrate_tutte = [c for c in dati if c[10].strip() in ("SCADUTO", "RIMANDATO")]
viste, arretrate = set(), []
for c in arretrate_tutte:
    k = (c[0], c[1], c[6], c[10])
    if k in viste:
        continue
    viste.add(k)
    arretrate.append(c)
dup = len(dati) - len({tuple(c) for c in dati})
print("\nrighe duplicate alla lettera .... %d" % dup)
print("arretrate (SCADUTO + RIMANDATO) . %d distinte, su %d righe e %d voci di dato"
      % (len(arretrate), len(arretrate_tutte), len(dati)))
tosano = [c for c in arretrate if "tosano" in (c[12] if len(c) > 12 else "").lower()]
ricambio = [c for c in arretrate if "manca ricambio" in (c[12] if len(c) > 12 else "").lower()]
print("  motivate dalla produzione Tosano %d" % len(tosano))
print("  motivate da 'manca ricambio' ... %d" % len(ricambio))
print("\nelenco delle arretrate (macchina | componente | prossima scadenza | stato | nota):")
for c in arretrate:
    print("   %-9s %-45s %-12s %-10s %s"
          % (c[0], c[1][:45], c[6], c[10], (c[12] if len(c) > 12 else "")[:60]))

macchine = sorted({c[0].strip() for c in dati})
print("\nmacchine censite (%d): %s" % (len(macchine), ", ".join(macchine)))

# ---------------------------------------------------------------- MOD-QA-07
titolo("checklist_metal_detector_manuale_operaio.txt — seconde firme CCP3")
rr = righe("checklist_metal_detector_manuale_operaio.txt")
# una riga di verifica comincia con hh:mm ed elenca gli esiti; la seconda firma
# e' l'ULTIMO campo: due lettere maiuscole (sigla) oppure `--` se manca.
data_corr, turno_corr = None, None
verifiche = []
for r in rr:
    if r.startswith("FOGLIO") or re.match(r"^\d{2}/\d{2}/\d{2} ", r):
        m = re.search(r"(\d{2}/\d{2}/\d{2})", r)
        if m:
            data_corr = m.group(1)
    m = re.search(r"TURNO (\d)", r)
    if m:
        turno_corr = m.group(1)
    m = re.match(r"^~*(\d{2}):(\d{2})\s+(.*)$", r.strip())
    if not m or "Fe" not in m.group(3):
        continue
    coda = m.group(3).split()
    firma2 = coda[-1]
    verifiche.append((data_corr, turno_corr, "%s:%s" % (m.group(1), m.group(2)),
                      firma2, r.strip()))

print("righe di verifica oraria riconosciute .. %d" % len(verifiche))
mancanti = [v for v in verifiche if v[3] == "--"]
print("con seconda firma ..................... %d" % (len(verifiche) - len(mancanti)))
print("SENZA seconda firma ('--') ............ %d" % len(mancanti))


def prima_dell_11(d):
    if not d:
        return None
    g, m, a = d.split("/")
    return (int(a), int(m), int(g)) < (26, 5, 11)


pre = [v for v in verifiche if prima_dell_11(v[0]) is True]
post = [v for v in verifiche if prima_dell_11(v[0]) is False]
print("\ncriterio: righe con orario di verifica e almeno un esito 'Fe';")
print("la seconda firma e' l'ultimo campo della riga, '--' = assente.")
print("  PRIMA dell'11/05 . %3d verifiche, %3d senza seconda firma (%.0f%%)"
      % (len(pre), len([v for v in pre if v[3] == "--"]),
         100.0 * len([v for v in pre if v[3] == "--"]) / max(len(pre), 1)))
print("  DALL'11/05 ....... %3d verifiche, %3d senza seconda firma (%.0f%%)"
      % (len(post), len([v for v in post if v[3] == "--"]),
         100.0 * len([v for v in post if v[3] == "--"]) / max(len(post), 1)))

print("\nverifiche registrate il 10/05 sul turno 2 (le ore contestate):")
for v in verifiche:
    if v[0] == "10/05/26" and v[1] == "2":
        print("   %s  %s" % (v[2], v[4][:90]))

# ---------------------------------------------------------------- log CF-02
titolo("log_allarmi_cella_frigo_surgelati_aprile.log — allarmi CF-02")
rr = righe("log_allarmi_cella_frigo_surgelati_aprile.log")
al = [r for r in rr if "EVT ALARM HIGH_TEMP" in r]
print("allarmi HIGH_TEMP ............. %d" % len(al))
print("con ACK=NO .................... %d" % len([r for r in al if "ACK=NO" in r]))
for r in al:
    ts = r.split()[0]
    t = re.search(r"T=(-?[\d.]+)", r).group(1)
    dur = re.search(r"DUR=([\d:]+)", r).group(1)
    ack = re.search(r"ACK=(\w+)", r).group(1)
    print("   %s  T=%-6s DUR=%s  ACK=%s" % (ts, t, dur, ack))
print("\nrighe totali del file ......... %d" % len(rr))
print("record RD di CF02 ............. %d" % len([r for r in rr if " CF02 RD " in r]))
print("record RD di TS01 ............. %d" % len([r for r in rr if " TS01 RD " in r]))
print("eventi di sbrinamento (START) . %d" % len([r for r in rr if "DEFROST_START" in r]))
print("righe con RTC=NOSYNC .......... %d" % len([r for r in rr if "RTC=NOSYNC" in r]))
print("ultima riga (troncata): %r" % rr[-1][:60])

# ---------------------------------------------------------------- consumi
titolo("consumi_energetici_forni_kwh_maggio26.csv — riepilogo maggio")
rr = righe("consumi_energetici_forni_kwh_maggio26.csv")
tot = {}
for r in rr[2:]:
    c = r.split(";")
    if len(c) < 9 or not re.match(r"^(\d{2}/\d{2}/\d{2}|\d{4}-\d{2}-\d{2})$", c[0].strip()):
        continue
    kwh = c[5].replace(".", "").replace(",", ".")
    if not kwh:
        continue
    tot[c[1].strip()] = tot.get(c[1].strip(), 0.0) + float(kwh)
print("centri di costo e somma dei kWh giornalieri di maggio (contati sulle righe):")
somma = 0.0
for k in sorted(tot, key=lambda k: -tot[k]):
    print("   %-24s %10.0f" % (k, tot[k]))
    somma += tot[k]
print("   %-24s %10.0f  <- somma delle letture di reparto" % ("TOTALE", somma))
print("\nbolletta Veneta Energia, stesso mese: 178.480 kWh di stabilimento.")
print("scarto: %.0f kWh non coperti dai contatori di reparto (%.0f%% del totale)"
      % (178480 - somma, 100.0 * (178480 - somma) / 178480))

# ---------------------------------------------------------------- shelf life
titolo("test_shelf_life_accelerata_confezione_MAP_snack.csv — O2 residuo per lotto")
rr = righe("test_shelf_life_accelerata_confezione_MAP_snack.csv")
per_lotto = {}
for r in rr[2:]:
    c = r.split(";")
    if len(c) < 20 or not c[0].startswith("P"):
        continue
    prova, lotto, T, giorno, o2 = c[0], c[2], c[5], c[6], c[10]
    if not re.match(r"^\d+([.,]\d+)?$", o2.strip()):
        continue
    per_lotto.setdefault((prova, lotto, T), {})[giorno] = float(o2.replace(",", "."))

# ⚠️ ogni lotto ha PIU' prove alla stessa temperatura (repliche): non si accorpano,
# altrimenti si spaccia la lettura di una replica per quella dell'altra. Una riga
# per prova, con l'id della prova accanto.
print("O2 residuo %, una riga per PROVA (le repliche restano distinte):")
print("   %-5s %-14s %-3s %s" % ("prova", "lotto", "T", "giorno 0 / 7 / 14 / 21 / 30 / 45 / 60 / 90"))
for k in sorted(per_lotto, key=lambda k: (k[1], int(k[2]), k[0])):
    d = per_lotto[k]
    serie = " / ".join(("%.1f" % d[g]) if g in d else "-"
                       for g in ("0", "7", "14", "21", "30", "45", "60", "90"))
    print("   %-5s %-14s %-3s %s" % (k[0], k[1], k[2], serie))
print("\nrighe di dato totali .......... %d"
      % len([r for r in rr[2:] if r.split(";")[0].startswith("P")]))
prove = sorted({r.split(";")[0] for r in rr[2:] if r.split(";")[0].startswith("P")})
print("prove distinte (%d): %s" % (len(prove), ", ".join(prove)))
