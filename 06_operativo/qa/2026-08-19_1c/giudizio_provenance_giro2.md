# Strato di giudizio, lotto 1C — 2º giro (`PROMPT_GIUDIZIO` v2)

⚠️ **Perché questo giro è in markdown e non in `.jsonl` come gli altri due.** Il verdetto del
secondo giro è arrivato con le righe JSON e con una tabella di riepilogo; **qui è riportato il
riepilogo verbatim**, che è la parte su cui sono state fatte le correzioni. Le righe JSON per
nota di questo giro non sono state trascritte: la testimonianza non si riscrive (giurisprudenza
§4.10), e quello che non ho verbatim non lo ricostruisco a memoria.

**Esito: 29 note giudicate — 21 pulite, 8 con rilievi.** Nessuna `fonte_inutile`: in tutte le
note multi-fonte ogni documento elencato sorregge almeno un'affermazione. Tutti gli 8 rilievi
sono di tipo `afferma_oltre`.

| Nota | Frase incriminata | Motivo |
|---|---|---|
| `fatto-catena-riferibilita-tarature-interne.md` | «la catena si chiude sul termometro di riferimento TS-REF» (summary); «i riferimenti sono a loro volta tarati da laboratori esterni» | Il registro non mette `TS-REF` a monte di nulla — il corpo della nota lo dice esplicitamente, il summary lo contraddice; e l'orologio radiocontrollato e il metodo a stufa non hanno ente esterno |
| `fatto-convalida-md-1800-scaduta.md` | «è un punto critico di controllo su una linea diversa da quella del reclamo»; «Un metal detector di linea è un punto critico di controllo» | Né il piano di manutenzione né l'elenco attribuiscono all'`MD-1800` lo stato di CCP (la dicitura «rif. CCP3» sta solo sulla riga dell'`MD-3200`), e nessuna delle due fonti nomina un reclamo |
| `fatto-fornitura-gas-nordgas-06-05.md` | «la miscela che la scheda tecnica del prodotto dichiara **in etichetta**: N2 70% / CO2 30%» | La scheda dichiara la composizione alla voce «Atmosfera protettiva»; l'unica dicitura che attribuisce all'etichetta è «Confezionato in atmosfera protettiva» |
| `fatto-strumenti-cf-02-e-ccp4.md` | «due sonde spillone della Linea 3: `TS-016` … e `TS-012`» | Il registro descrive `TS-012` come «Termometro a sonda Testo 106»; la seconda sonda spillone censita è `TS-017` |
| `fatto-strumenti-esclusi-da-taratura.md` | «Cinque strumenti del registro non hanno taratura periodica»; «strumenti che **non hanno una scadenza di taratura**» | `TS-015` ha taratura 20/03/2026 e scadenza 20/03/2027 — la tabella della nota stessa lo ammette («è tarato, ma la nota lo limita») |
| `fatto-verifica-metrologia-legale-bilance.md` | «la scheda tecnica … dichiara il peso netto di 100 g … e il **controllo gravimetrico su ogni lotto**» | Nella §3 «gravimetrico — ogni lotto» è il metodo dell'**Umidità**; per il peso netto la scheda indica «selezionatrice ponderale in linea» |
| `questione-codici-lotto-azoto-06-05.md` | «gli altri due seguono due **schemi interni** diversi» | Il mass balance porta `NG-26-0506` nella colonna «Lotto fornitore»; la nota stessa, due paragrafi dopo, degrada «riferimento interno del mass balance» a una delle due letture possibili |
| `questione-sigla-kit-tasselli-ccp3.md` | «Nessuna delle quattro fonti ne nomina un'altra» | La riga 104 dell'inventario — citata dalla nota stessa — porta «taratura CCP3 - MOD-QA-07 rev.5»; anche la riga 39 dell'elenco e la riga 34 del piano nominano `MOD-QA-07` |

**Il pattern nominato dal giudice, verbatim:**

> Un pattern ricorrente, che vale più dei singoli rilievi: cinque degli otto stanno nel
> `summary` o nel titolo, non nel corpo — e in tre casi (`catena-riferibilità`,
> `strumenti-esclusi`, `codici-lotto`) il corpo della nota dice la cosa giusta e il summary la
> irrigidisce. Il corpo cautela, l'intestazione afferma. È lì che conviene guardare per primo
> al prossimo giro.

**Esito delle correzioni:** tutti e otto i rilievi accolti. La rilettura di **tutti** i summary
contro il corpo, fatta dopo questo giro, ha trovato due casi in più che il giudice non aveva
segnalato: `fatto-due-registri-paralleli-della-metrologia` ed `entita-metrolab-taratura`.
