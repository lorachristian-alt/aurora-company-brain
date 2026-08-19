# Registro degli emendamenti a `metodo_03`

> **Cos'è** · L'indice genealogico dei 27 emendamenti al manuale di canonizzazione: chi li
> ha approvati, quando, e dove vive oggi la regola. **È un indice, non una copia.**
> **Cosa NON contiene** · Il testo delle regole. Quello vive in
> `01_metodo\metodo_03_canonizzazione.md`, che ne resta l'unico padrone: qui c'è l'oggetto
> in una riga, quel tanto che basta a riconoscere l'emendamento, e il puntatore a dove
> leggerlo per intero.
> **Perché esiste** · Fino al 19/08/2026 la genealogia stava sparsa fra i rapporti di gate
> (§9 del gate S2 per E1-E17, §13 del rapporto 1A per E20-E25) e il decision log. Tre
> emendamenti non erano in nessuna tabella — **E18** e **E19**, nati al gate S2 dopo che il
> rapporto era già scritto, ed **E26**, approvato al gate del lotto 1B — e **E27 è nato
> fuori da un gate**. Senza un indice unico, un numero senza riga diventa un numero senza
> storia.

## Come si legge

- **Dove nasce** · l'occasione in cui il coordinatore l'ha approvato. Gli emendamenti li
  approva il coordinatore: **il gate è l'occasione tipica, non la condizione.**
- **Vive in** · la sezione di `metodo_03` dove sta la regola oggi.
- **Marcatore** · dice se nel testo del manuale compare la sigla `(Enn)`. Dove manca,
  l'emendamento è stato applicato riscrivendo il passaggio: è il caso dei refusi, che non
  lasciano cicatrice perché non c'è nulla da ricordare oltre al testo corretto.
- **Il perché** · il documento che porta la motivazione estesa e il caso che l'ha generata.

Sezioni e presenza dei marcatori sono verificate contro `metodo_03` da
`06_operativo\verifica_emendamenti.py`, non a occhio.

## I 27 emendamenti

| # | Data | Dove nasce | Tipo | Oggetto, in una riga | Vive in | Marc. | Il perché |
|---|---|---|---|---|---|---|---|
| **E1** | 17/08/2026 | gate S2 | regola nuova | `fonti` facoltativo per le note-strumento del progetto | §2.4 | sì | `rapporto_gate_s2.md` §9 · decision log 17/08 |
| **E2** | 17/08/2026 | gate S2 | regola nuova | riconciliazione incrociata dei numeri fra le fonti del lotto | §5.1-bis | sì | `rapporto_gate_s2.md` §9 |
| **E3** | 17/08/2026 | gate S2 | regola nuova | mai dichiarare un'assenza senza averla cercata su tutto `sources\` | §10, divieto 12-bis | no | `rapporto_gate_s2.md` §9 |
| **E4** | 17/08/2026 | gate S2 | refuso | la grammatica `.xlsx` ammette `riga <n>` **e** `righe <n>-<m>` | §2.3 | no | `rapporto_gate_s2.md` §9 |
| **E5** | 17/08/2026 | gate S2 | chiarimento | il locator è un prefisso della riga, non la riga intera | §2.3 | sì | `rapporto_gate_s2.md` §9 |
| **E6** | 17/08/2026 | gate S2 | regola nuova | verifica testuale solo per le citazioni di almeno cinque parole | §2.3 · §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E7** | 17/08/2026 | gate S2 | regola nuova | anche i valori **contati** si dichiarano, non solo quelli sommati | §5.4 · §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E8** | 17/08/2026 | gate S2 | chiarimento | la normalizzazione toglie il quoting delle mail e genera le varianti di data | §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E9** | 17/08/2026 | gate S2 | chiarimento | dopo le correzioni si **rigiudica**, non si rilancia solo la QA | §9.5, passo 5 | sì | `rapporto_gate_s2.md` §9 |
| **E10** | 17/08/2026 | gate S2 | chiarimento | il delimitatore del pacchetto per il giudice non può comparire nei grezzi | §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E11** | 17/08/2026 | gate S2 | chiarimento | la reciprocità si verifica sul **primo** hub di `related`, che è l'hub proprio | §2.1 · §7.2 | sì | `rapporto_gate_s2.md` §9 |
| **E12** | 17/08/2026 | gate S2 | chiarimento | il minimo di due wikilink conta anche quelli di `related` | §4.4 · §7.2 | sì | `rapporto_gate_s2.md` §9 |
| **E13** | 17/08/2026 | gate S2 | chiarimento | in perimetro di lotto, copertura `_index` e componente unica solo sulle cartelle toccate | §7 | sì | `rapporto_gate_s2.md` §9 |
| **E14** | 17/08/2026 | gate S2 | refuso | la coerenza interna si controlla dopo aver rimosso gli orari | §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E15** | 17/08/2026 | gate S2 | refuso | l'esempio compilato di §3.1 non corrispondeva al file: 49 `ALARM`, non 50 | §3.1 | no | `rapporto_gate_s2.md` §9 |
| **E16** | 17/08/2026 | gate S2 | refuso | il locator dell'esempio `concetto-fefo` era fuori dalla grammatica `.csv` | §3.5 | no | `rapporto_gate_s2.md` §9 |
| **E17** | 17/08/2026 | gate S2 | chiarimento | il budget di un lotto si misura sulle **note di contenuto** | §9.4 | sì | `rapporto_gate_s2.md` §9 |
| **E18** | 17/08/2026 | gate S2 · ⚠️ **fuori dalla tabella del rapporto** | regola nuova | se una nota stabilisce una regola decisionale, il `summary` la enuncia | §2.1 | sì | decision log 17/08 — origine: la riserva del giudice su Q237 |
| **E19** | 17/08/2026 | gate S2 · ⚠️ **fuori dalla tabella del rapporto** | refuso | il piè di pagina di un `.log` non era puntabile: `§piè di pagina`, `§intestazione` | §2.3 | sì | decision log 17/08 |
| **E20** | 18/08/2026 | gate della matrice | regola nuova | le note-strumento fuori dalla componente unica; l'esenzione è della **classe** | §2.4 · §7.0 · §7.2 | sì | `rapporto_lotto_1a.md` §13 · decision log 18/08 |
| **E21** | 18/08/2026 | gate del lotto 1A | regola nuova | il budget si controlla **prima** di scrivere; oltre il +25 % il lotto si spezza | §9.4 | sì | `rapporto_lotto_1a.md` §13 |
| **E22** | 18/08/2026 | gate del lotto 1A | chiarimento | la data di verifica di un'assenza rimanda a `data_nota`, non si riscrive nel corpo | §10, divieto 12-bis | sì | `rapporto_lotto_1a.md` §13 |
| **E23** | 18/08/2026 | gate del lotto 1A | chiarimento | il marcatore di un valore derivato va **accanto al numero**, entro sessanta caratteri | §5.4 · §7.1 | sì | `rapporto_lotto_1a.md` §13 |
| **E24** | 18/08/2026 | gate del lotto 1A | chiarimento | date e orari si riportano nella grafia della fonte | §10, divieto 4-bis | sì | `rapporto_lotto_1a.md` §13 |
| **E25** | 18/08/2026 | gate del lotto 1A | regola nuova | non si anticipa una divergenza di cui una sola gamba è canonizzata | §10, divieto 9-bis | sì | `rapporto_lotto_1a.md` §13 |
| **E26** | 19/08/2026 | gate del lotto 1B · ⚠️ **nessuna tabella di registro in quel gate** | regola nuova | regola d'arresto del ri-giudizio: zero rilievi accolti, e comunque il terzo giro col pattern nominato | §9.5, passo 5 | sì | `rapporto_lotto_1b.md` appendice A |
| **E27** | 19/08/2026 | ⚠️ **FUORI da un gate — ordine diretto del coordinatore** | regola nuova | l'aggiornamento del passaggio di consegne è il **quinto gesto** del rituale di chiusura | §9.5, passo 8 | sì | decision log 19/08 · principio 5 della scaletta |

## Le tre anomalie di genealogia, dette per nome

1. **E18 ed E19 non sono nella tabella del rapporto S2** perché sono nati *durante* il
   gate, dopo che il rapporto era stato scritto: il decision log del 17/08 ne conta
   «diciannove», la tabella ne elenca diciassette. Nessuno dei due è mai stato in
   discussione — mancava solo la riga.
2. **E26 non ha una riga di registro** da nessuna parte: il rapporto del lotto 1B lo cita
   nell'appendice A come obbligo già approvato, ma quel gate non ha prodotto una tabella
   di emendamenti come avevano fatto S2 e 1A.
3. **E27 è nato fuori da un gate**, su ordine diretto del coordinatore del 19/08/2026, ed
   è approvato a pieno titolo. La convenzione del progetto è **«gli emendamenti li approva
   il coordinatore»**, non «solo ai gate»: sta scritto qui perché fra un anno un numero
   senza gate accanto non sembri un numero senza padre.

## Regola di manutenzione

Ogni emendamento nuovo prende **una riga qui, nello stesso turno** in cui entra in
`metodo_03`. Se nasce a un gate, la motivazione estesa resta nel rapporto di quel gate; se
nasce fuori, la porta il decision log. **Questo file non è il padrone di nessuna regola:**
se una riga qui diverge da `metodo_03`, vince `metodo_03` e la riga si corregge nello
stesso turno.
