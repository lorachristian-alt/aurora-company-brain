# -*- coding: utf-8 -*-
"""conteggi_lotto_1b — i numeri contati del lotto 1B (freddo ed energia).

Regola d'oro 5: nessun numero si dichiara senza che uno script l'abbia contato.
Ogni conteggio che entra in una nota del lotto 1B nasce qui, e il criterio di
conteggio e' scritto accanto al numero — perche' un conteggio e' un valore
derivato (metodo_03 §5.4, E7) e va dichiarato col suo criterio.

⚠️ `consumi_energetici_forni_kwh_maggio26.csv` NON e' un file con errori di
calcolo (metodo_03 §5.5, divieto 4): le colonne sono arrotondate all'intero e il
costo e' calcolato sul consumo reale con i decimali. Lo script lo VERIFICA, non
lo assume.

Uso:  python conteggi_lotto_1b.py
"""
import io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
SRC = r"C:\Users\buulo\Desktop\aurora-cervello\sources"

LOG = "log_allarmi_cella_frigo_surgelati_aprile.log"
CSV = "consumi_energetici_forni_kwh_maggio26.csv"


def righe(nome):
    return io.open(os.path.join(SRC, nome), encoding="utf-8",
                   errors="replace").read().splitlines()


def num(s):
    """'1.486' -> 1486 ; '270,50' -> 270.5 ; '' -> None"""
    s = (s or "").strip()
    if not s:
        return None
    s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


# ===================================================== 1. LOG ALLARMI CELLA
print("=" * 72)
print("1. %s" % LOG)
print("=" * 72)
r = righe(LOG)
print("righe totali del file ................ %d" % len(r))

rd = {"CF02": 0, "TS01": 0}
evt = {}
sys_ = []
malformate = []
prima = ultima = None
for i, x in enumerate(r, 1):
    m = re.match(r"^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2}) (CF02|TS01) (RD|EVT|SYS) (.*)$", x)
    if not m:
        malformate.append((i, x))
        continue
    ts = m.group(1) + "T" + m.group(2)
    prima = prima or ts
    ultima = ts
    if m.group(4) == "RD":
        rd[m.group(3)] += 1
    elif m.group(4) == "EVT":
        k = m.group(5).split()[0]
        evt[k] = evt.get(k, 0) + 1
    else:
        sys_.append((ts, m.group(3), m.group(5)))

print("prima riga ben formata ............... %s" % prima)
print("ultima riga ben formata .............. %s" % ultima)
print("letture RD CF02 ...................... %d" % rd["CF02"])
print("letture RD TS01 ...................... %d" % rd["TS01"])
print("righe MALFORMATE (troncature/corruz.)  %d" % len(malformate))
for i, x in malformate:
    print("   riga %d: %r" % (i, x[:90]))
print("eventi EVT per tipo:")
for k in sorted(evt):
    print("   %-16s %d" % (k, evt[k]))
print("righe SYS:")
for ts, dev, testo in sys_:
    print("   %s %s %s" % (ts, dev, testo))

print("")
print("-- allarmi, uno per uno --")
for x in [y for y in r if " EVT ALARM" in y]:
    print("   " + x)

apert = [x for x in r if " EVT ALARM " in x and "ALARM_RESET" not in x]
apert_con_dur = [x for x in apert if "DUR=" in x]
print("")
print("record di APERTURA allarme che contengono gia' DUR= : %d su %d"
      % (len(apert_con_dur), len(apert)))

giorni = sorted({x[:10] for x in r if re.match(r"^\d{4}-\d{2}-\d{2}T", x)})
print("giorni distinti con almeno una riga .. %d (dal %s al %s)"
      % (len(giorni), giorni[0], giorni[-1]))

dur = [x for x in r if "DEFROST_END" in x]
mm = [re.search(r"DUR=(\d{2}):(\d{2}):(\d{2})", x) for x in dur]
sec = [int(g.group(1)) * 3600 + int(g.group(2)) * 60 + int(g.group(3)) for g in mm if g]
print("sbrinamenti conclusi ................. %d, durata media %.1f min (calcolata)"
      % (len(sec), sum(sec) / len(sec) / 60.0))

print("eventi porta:")
for x in [y for y in r if "DOOR_" in y]:
    print("   " + x)

# ===================================================== 2. CONSUMI ENERGETICI
print("")
print("=" * 72)
print("2. %s" % CSV)
print("=" * 72)
r = righe(CSV)
print("righe totali del file ................ %d" % len(r))

dati, intest, subtot, altre = [], 0, 0, []
for i, x in enumerate(r, 1):
    c = x.split(";")
    if len(c) < 10:
        altre.append((i, x))
        continue
    if c[0].strip() == "Data":
        intest += 1
        continue
    if c[0].strip().startswith("SUBTOT"):
        subtot += 1
        altre.append((i, x))
        continue
    if re.match(r"^(\d{2}/\d{2}/\d{2}|\d{4}-\d{2}-\d{2})$", c[0].strip()):
        dati.append((i, c))
    else:
        altre.append((i, x))

print("righe di dato ........................ %d (contate: prima colonna una data)" % len(dati))
print("intestazioni ripetute ................ %d" % intest)
print("righe SUBTOT con formula rotta ....... %d" % subtot)

formati = {}
for i, c in dati:
    f = "gg/mm/aa" if "/" in c[0] else "aaaa-mm-gg"
    formati[f] = formati.get(f, 0) + 1
print("formati di data nello stesso campo ... %s" % formati)

centri = {}
for i, c in dati:
    centri[c[1].strip()] = centri.get(c[1].strip(), 0) + 1
print("centri di costo ...................... %d" % len(centri))
for k in sorted(centri):
    print("   %-24s %d righe" % (k, centri[k]))

tot_mese = {}
for i, c in dati:
    v = num(c[5])
    if v is not None:
        tot_mese[c[1].strip()] = tot_mese.get(c[1].strip(), 0) + v
print("kWh totali del mese, per centro (sommati dalle righe):")
for k in sorted(tot_mese):
    print("   %-24s %10.0f kWh" % (k, tot_mese[k]))
print("   %-24s %10.0f kWh  <-- somma di tutti i centri" % ("TOTALE", sum(tot_mese.values())))

sf, ct, entro = 0, 0, 0
for i, c in dati:
    f1, f2, f3, tt = num(c[2]), num(c[3]), num(c[4]), num(c[5])
    cu, cts = num(c[7]), num(c[8])
    if None not in (f1, f2, f3, tt) and abs(f1 + f2 + f3 - tt) > 0.001:
        sf += 1
    if None not in (cu, cts, tt) and abs(cts - tt * cu) > 0.005:
        ct += 1
    if None not in (cu, cts, f1, f2, f3) and cu:
        reale = cts / cu
        if abs(f1 + f2 + f3 - reale) <= 1.5:
            entro += 1
print("righe in cui la somma delle fasce NON fa il totale .............. %d su %d" % (sf, len(dati)))
print("righe in cui il costo NON e' esattamente totale x tariffa ....... %d su %d" % (ct, len(dati)))
print("righe in cui la somma delle fasce cade entro 1,5 kWh dal consumo")
print("   reale ricavato come costo / tariffa (cioe': arrotondamenti) .. %d su %d" % (entro, len(dati)))

tar = sorted({c[7].strip() for i, c in dati if c[7].strip()})
print("tariffe distinte dichiarate nel file . %s" % tar)

print("")
print("righe con annotazione in coda:")
for i, c in dati:
    if len(c) > 9 and c[9].strip():
        print("   riga %d | %s | %s | %s" % (i, c[0], c[1], c[9].strip()))
print("")
print("righe non di dato (code, subtotali, confronto):")
for i, x in altre:
    if x.strip(";").strip():
        print("   riga %d: %s" % (i, x.rstrip(";")))

# ===================================================== 3. DERIVATI BOLLETTA
print("")
print("=" * 72)
print("3. valori derivati dalla bolletta (bolletta_VenetaEnergia_maggio2026.pdf)")
print("=" * 72)
F1, F2, F3, TOT = 82410, 51220, 44850, 178480
IMPONIBILE, TOTALE = 30949.18, 34044.10
print("F1+F2+F3 = %d  (dichiarato in fattura: %d)" % (F1 + F2 + F3, TOT))
print("quota F3 sul totale ......... %.1f %% (calcolata)" % (100.0 * F3 / TOT))
print("imponibile / kWh ............ %.4f EUR/kWh (calcolato)" % (IMPONIBILE / TOT))
print("totale con IVA / kWh ........ %.4f EUR/kWh (calcolato)" % (TOTALE / TOT))
print("potenza max prelevata / impegnata ... %.1f %% (calcolato: 482,4 / 500,0)"
      % (100.0 * 482.4 / 500.0))
somma_centri = sum(tot_mese.values())
print("contatori di reparto (somma delle righe) .... %.0f kWh" % somma_centri)
print("prelievo di stabilimento in fattura ......... %d kWh" % TOT)
print("quota coperta dai contatori di reparto ...... %.1f %% (calcolata)"
      % (100.0 * somma_centri / TOT))
print("differenza .................................. %.0f kWh (calcolata)"
      % (TOT - somma_centri))

r_log = righe(LOG)

print("")
print("-- cadenza degli sbrinamenti di CF-02, per periodo --")
per_giorno = {}
for x in r_log:
    if "DEFROST_START" in x:
        per_giorno[x[:10]] = per_giorno.get(x[:10], 0) + 1
periodi = [("2026-04-01", "2026-04-11"), ("2026-04-12", "2026-04-19"),
           ("2026-04-20", "2026-04-24"), ("2026-04-25", "2026-04-30")]
for a, b in periodi:
    gg = [g for g in sorted(per_giorno) if a <= g <= b]
    tot = sum(per_giorno[g] for g in gg)
    print("   dal %s al %s: %2d giorni, %3d sbrinamenti, %.0f al giorno (calcolato), uno ogni %.0f ore (calcolato)"
          % (a, b, len(gg), tot, tot / len(gg), 24.0 / (tot / len(gg))))
print("   totale sbrinamenti automatici: %d" % sum(per_giorno.values()))

print("")
print("-- aggiunte dopo la revisione del 19/08 --")
r_log = righe(LOG)
cf02_rd_tutte = [x for x in r_log if "CF02 RD" in x]
cf02_rd_ok = [x for x in r_log if re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} CF02 RD ", x)]
print("righe che contengono 'CF02 RD' .............. %d" % len(cf02_rd_tutte))
print("di cui ben formate (timestamp integro) ...... %d" % len(cf02_rd_ok))

ts = [x for x in r_log if re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} TS01 RD ", x)]
attivo = [x for x in ts if "BELT=1" in x]
vals = [float(re.search(r"TPRODOUT=([+-][\d.]+)", x).group(1)) for x in attivo
        if re.search(r"TPRODOUT=([+-][\d.]+)", x)]
gg = sorted({x[:10] for x in attivo})
print("letture TS01 ................................ %d" % len(ts))
print("di cui con nastro attivo (BELT=1) ........... %d, su %d giornate" % (len(attivo), len(gg)))
print("TPRODOUT con nastro attivo: min %.1f  max %.1f (calcolati)" % (min(vals), max(vals)))
print("letture con TPRODOUT sopra -18,0 ............ %d" % len([v for v in vals if v > -18.0]))

r_csv = righe(CSV)
met = []
for x in r_csv:
    c = x.split(";")
    if len(c) >= 10 and re.match(r"^(\d{2}/\d{2}/\d{2}|\d{4}-\d{2}-\d{2})$", c[0].strip()):
        v = num(c[6])
        if v is not None:
            met.append((c[0].strip(), v))
print("righe con metano dichiarato ................. %d" % len(met))
print("metano di maggio ............................ %.0f m3 (sommati)" % sum(v for _, v in met))
print("minimo giornaliero %.0f  massimo %.0f" % (min(v for _, v in met), max(v for _, v in met)))

apr, mag = 169302.0, 178480.0
print("incremento mag su apr dal grafico dei 12 mesi %.1f %% (calcolato: 178.480 su 169.302)"
      % (100.0 * (mag - apr) / apr))
print("39,95 su 34.044,10 .......................... %.2f per mille (calcolato)" % (1000.0 * 39.95 / 34044.10))
