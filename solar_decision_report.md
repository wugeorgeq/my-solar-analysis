# Solar Decision Report

This report is structured around the actual decision hierarchy: **first, whether solar makes sense at all; second, if so, how to pay for it; third, how to size it.** Everything here is built from real PG&E usage data (hourly, measured) combined with a roof-calibrated production model and real quotes from Corda Solar and Tesla — see the Addendum for full methodology and how to re-verify.

## Household context

- Two-story house, Bay Area (PG&E territory)
- One electric vehicle, charged at home — roughly 40-45% of total electric usage
- Gas heat and gas stove/range (not an all-electric home — no electric heat pump load to offset)
- **~9,000 kWh/yr electric usage, ~$300/mo average PG&E electric bill** (real measured: ~9,017 kWh/yr, ~$291/mo — see Addendum for exact source data)
- No particular value placed on backup power / outage resilience (removes one common non-financial justification for solar)
- **Roof is in good condition** — no replacement expected during the system's early life, so mid-lease panel removal/reinstall costs (a real risk for aging roofs, and on the lessor's fee schedule under a lease) are treated as out of scope
- **The EV is home during midday hours often enough that daytime charging is realistic** — confirmed, not aspirational; this matters because daytime charging is the single biggest economic lever in this analysis (Part 3)

---

# Part 1: Should you do solar at all?

## The case for

- **Real usage baseline**: ~9,017 kWh/yr electric, ~$3,496/yr (~$291/mo) actual measured bill, effective rate ~$0.39-0.40/kWh — a genuinely high rate that gives solar more room to matter than in many other utility territories.
- **Long-run savings are real, not just sales-pitch framing.** Modeled against your actual usage, cumulative savings vs. doing nothing turn clearly positive by roughly year 9-13 on a right-sized ownership purchase (sooner with daytime EV charging), and the gap widens every year after — because you're comparing a bill that keeps rising against a cost that's mostly fixed once paid.
- **Reasonably robust across rate assumptions — but the robustness depends on the instrument.** Ownership works even at a conservative 2%/yr escalation (below the historical trend) and still pays back (~11-13yr) if rates stay completely flat. The lease is a different animal: its payment escalates 3%/yr contractually, so at 2% PG&E escalation it's roughly breakeven, and under flat rates it goes cash-flow negative around year 7 — *unless* daytime EV charging is adopted, which keeps it positive through ~year 20 even with flat rates (see Part 2). You don't need the salesman's optimistic 6% for the math to function, but the lease needs more rate escalation (or the charging habit) than ownership does.
- **A real, controllable lever exists that meaningfully improves the numbers**: shifting EV charging to midday (when solar produces) instead of overnight raises the lease's net monthly cash flow from +$26/mo to +$52/mo (~2x) in the corrected model, and doubles as the hedge that keeps the lease viable if PG&E rates stagnate. This isn't a hypothetical — it's a scheduling change Tesla's app supports directly, and the car being home midday has been confirmed.
- **If done via ownership, there's a real (if uncertain) resale-value case too** — published research (Berkeley Lab, CA-specific studies) shows owned solar systems adding measurable home value, on the order of ~$4/watt. Note the Corda structure is third-party-owned for its first 5 years (that's how the 30% credit works — see Part 2), so the "owned system" premium applies only after ownership transfers; it never applies to a continuing Tesla lease.

## The case against / honest limitations

- **This is fundamentally a bet that PG&E rates keep rising**, at least modestly, over the years you hold the system. Trailing 10-year CAGR is ~7.2%, but 2024-2026 rates have actually *fallen* ~11% from Jan-2024 levels due to regulatory pressure and cost-cutting. The direction has reversed before, even if briefly — this isn't a risk-free assumption.
- **PG&E's revenue is structurally shifting from per-kWh rates to fixed charges — and solar can only offset the per-kWh part.** The CPUC-approved income-graduated fixed charge (~$24/mo) moves a slice of the bill out of solar's reach, and part of the recent "rate cuts" reflects this restructuring rather than genuinely cheaper power. This is a distinct and arguably worse risk than "rates stay flat": even if total bills resume rising, the *offsettable* portion may rise slower than headline history suggests. Every projection here uses the volumetric rates embedded in the historical data; further fixed-charge expansion would erode savings under any instrument.
- **The return is real but entirely rate-contingent — a spread, not a number.** On a right-sized ownership purchase (~$23k estimated — see Part 2), the 25-year IRR including maintenance and two replacement cycles is **~9% if PG&E escalates 5%/yr (~11% with daytime EV charging), but ~0% if rates stay flat**. The expected case now clears CD/bond territory comfortably — the earlier "3-6%" figure was computed on the oversized 8.36kW system — but the flat-rate downside is roughly a zero-return parking spot for the capital. You're not buying a yield; you're buying exposure to PG&E's rate trajectory.
- **Real equipment risk exists that's easy to leave out of a rosy projection.** Powerwall and inverter carry only a 10-year warranty (vs. 25-30yr for panels) — a 20+ year hold likely means one or two replacement cycles (~$10,000 each, rough estimate) that most sales-facing savings tables (including the installer's own) quietly omit.
- **You've stated you don't personally value backup power / outage resilience** — which removes one of the two most common non-financial justifications people use for going solar (the other being environmental preference, which is a personal values call, not a financial one).
- **A ~$23k outlay (estimated right-sized Corda price; $28k+ at the originally quoted oversize) is a meaningful capital commitment to lock into a single illiquid, hard-to-reverse asset for over a decade** — worth weighing deliberately against other uses of that capital, independent of whether the ROI math works on paper.
- **"Not a slam dunk" is the right level of conviction, not indecision.** Every number in this report required real digging to get right (the federal credit's actual applicability, NEM3's crushed export value, financing dealer-fee risk, buyout-price uncertainty) — the fact that it took this much work to find a defensible "yes" case is itself informative. A genuinely obvious decision wouldn't need this much scrutiny to hold up.

## What actually tips this decision

Not the payment instrument — that's Part 2. The primary decision comes down to three questions only you can answer:

1. **How confident are you that you'll stay in this house 10-15+ years?** Below that horizon, the financial case is weak-to-negative under most structures. Above it, the case strengthens meaningfully.
2. **Do you believe PG&E rates resume their historical upward drift**, even after the recent pause? If you think the recent rate cuts represent a durable new trend rather than a temporary regulatory-driven dip, the case weakens substantially.
3. **Is there non-financial value to you beyond the ROI number** — environmental preference, a hedge against volatility, or simply wanting to be less exposed to a utility you don't control? If the honest answer is "no, I only care about the math," the decision reduces to question 2: the expected-case return (~9-11% IRR on right-sized ownership) is genuinely good, but it only materializes if rates rise — a pass is defensible if and only if you genuinely expect PG&E rates to stay flat for a decade-plus.

## Bottom line on Part 1

There is a real, defensible case for doing this — it is not solar-salesman fiction, and at the right-sized price the expected-case return (~9-11% IRR) is genuinely attractive. But it is a **long-horizon bet whose entire upside depends on PG&E rates rising**, with a flat-rate downside near 0%, not an obviously correct move. If your honest answer to the three questions above leans toward "uncertain," declining to act and revisiting in a year or two (once PG&E's rate trajectory and your own housing plans are clearer) is a legitimate, non-lazy outcome of this analysis — not a failure to decide.

---

# Part 2: If yes — which payment instrument?

**Resolved since the first draft of this report**: Corda's pricing is genuinely all-in. The 30% federal credit survives 25D's repeal because Corda holds the system in a 5-year lease/PPA structure — they claim the commercial (48E) credit as owner and pass the savings through in the price — after which ownership transfers to you at **no additional cost, no hidden buyout**. Two practical notes: get the $0-cost year-5 transfer in writing before signing, and know that selling the house within the first 5 years means assigning that agreement to the buyer.

**A sizing correction that changes the whole comparison**: Corda's $28,377 quote is for an 8.36kW system — the size Part 3 recommends *against* — while the Tesla lease numbers are for 5.88kW. Comparing them directly was apples-to-oranges. This section instead uses an **estimated Corda price of ~$23,000 for a right-sized ~5.7kW system** (13 panels): Corda's own quote implies ~$2.97/W on the panel portion (almost exactly Tesla's $2.98/W) plus ~$15.7k for the Powerwall 3, giving ~$32.7k gross → ~$22.9k after the 30% credit. **This is an estimate, not a quote — getting Corda's real price at 13-14 panels is now the top open question.**

## The three options at a glance (5.88kW-class, 1 Powerwall)

- **Corda ownership (~$23,000 est., all-in)**: pays back around year 9 at 5%/yr PG&E escalation (year 8 with daytime EV charging), and ~11-13yr even if rates stay completely flat. 25-year IRR including maintenance and two ~$10k replacement cycles: **~9% at 5%/yr escalation, ~11% with daytime charging, ~0% if rates stay flat**. You own the asset (home resale premium applies after the year-5 transfer).
- **Tesla lease ($500 down, $152/mo, 3%/yr escalator, 25-yr term)**: cash-flow positive from day one (+$26/mo at the current charging pattern, +$52/mo with daytime charging), and Tesla bears maintenance (~$300-520/yr, normally owner-borne) and the 10-year Powerwall/inverter replacement risk. The catch: the contractual 3% escalator makes it the instrument *most* exposed to the flat-rate scenario (below).
- **A loan**: still the weakest option. At realistic rates (6-10% solar financing; Tesla's in-house 7.24% was verified clean of dealer-fee markup), monthly cash flow runs negative for years. With ownership available at ~$23k estimated, borrowing at 7%+ to avoid that outlay beats neither alternative.

## Head-to-head: ownership vs. lease, consistent assumptions

Total cumulative cost (lower is better). Assumptions: PG&E +5%/yr, lease +3%/yr, ownership maintenance $410/yr, ~$10k Powerwall/inverter replacement at year 12 (and again at year 24 for the 25-yr row):

| Horizon | Ownership, no replacement needed | Ownership, with replacement(s) | Lease (continued) |
|---|---|---|---|
| 15yr | $58,454 | $68,454 | $63,728 |
| 20yr | $76,104 | $86,104 | $94,415 |
| 25yr | $98,063 | $118,063 | $131,815 |

- **At 15 years it's a coin flip decided by replacement timing**: if the Powerwall/inverter dies inside the window, the lease wins by ~$4.7k; if it lasts, ownership wins by ~$5.3k. (The first draft's claim that they cost "almost exactly the same" at 15 years was computed without the replacement cycle it said it included; this is the honest version.)
- **At 20-25 years ownership wins even with replacements fully priced in** (~$8k ahead at 20yr, ~$14k at 25yr) — the lease escalator compounds forever while ownership's costs are front-loaded and flatten.
- The daytime-charging scenario improves both paths and leaves the relative picture similar.

## The scenario that separates them: what if PG&E rates don't rise?

The lease payment escalates 3%/yr **contractually, regardless of what PG&E does**. Re-running the comparison with rates held completely flat:

- **Lease, current charging pattern**: annual cash flow turns negative in **year 7**, cumulative savings peak around +$500 and are gone by year 10, ending ~**-$13,600 by year 25** — inside a contract with no exit before year 5 and only a fair-market-value buyout after.
- **Lease, daytime charging**: stays cash-flow positive until ~year 11 and cumulatively positive through ~year 19 (~-$5,800 by year 25). **Daytime charging is the hedge that keeps the lease survivable under flat rates** — though a thinner one than the first-pass numbers suggested.
- **Ownership under flat rates**: still pays back in ~11-13 years; IRR ~0% (current pattern) to ~3.3% (daytime charging). Dull, not disastrous.
- At 2%/yr escalation: the lease is roughly breakeven over 10-25yr on the current pattern and solidly positive with daytime charging; ownership is comfortably positive either way.

**This is the decisive asymmetry: the lease is a leveraged bet on PG&E escalation; ownership is merely a bet that rates don't fall.**

## 5/10/15-year outlook: Do Nothing vs. Ownership vs. Lease

All columns are total cumulative cost; "Saved" is measured against doing nothing. Assumptions match the head-to-head section: PG&E +5%/yr, lease +3%/yr with $500 upfront, ownership at the ~$23k estimated right-sized price plus $410/yr maintenance, with the ~$10k year-12 replacement included in the 15-yr row (the 5/10-yr rows fall before it). *(Correction: the first draft of this table omitted roughly half the lease-path cost and overstated savings ~4-6x; these figures reconcile exactly with the +$26/+$52 monthly cash-flow numbers.)*

**Current EV charging pattern:**

| Horizon | Do nothing | Ownership (~$23k est.) | Saved | Lease | Saved |
|---|---|---|---|---|---|
| 5yr | $19,318 | $32,554 | **-$13,236** | $17,688 | **+$1,630** |
| 10yr | $43,972 | $44,181 | **-$208** | $38,491 | **+$5,481** |
| 15yr | $75,439 | $68,454 | **+$6,985** | $63,728 | **+$11,711** |

**With daytime EV charging (the plan of record):**

| Horizon | Do nothing | Ownership (~$23k est.) | Saved | Lease | Saved |
|---|---|---|---|---|---|
| 5yr | $19,318 | $30,839 | **-$11,521** | $15,973 | **+$3,345** |
| 10yr | $43,972 | $40,277 | **+$3,695** | $34,587 | **+$9,385** |
| 15yr | $75,439 | $61,756 | **+$13,683** | $57,031 | **+$18,408** |

How to read this: **ownership starts deep underwater** (the $23k hole) and breaks even against doing nothing around year 11 (year 9 with daytime charging). **The lease is positive from day one** — no capital hole, and Tesla carries the maintenance and replacement costs the ownership column is paying — which is why it leads at every horizon shown here. But the lease's escalating payment never stops: **ownership overtakes the lease around year 17 in both scenarios** and wins by ~$8k at 20 years and ~$14k at 25 (see the head-to-head table above). A robustness point worth noting: because both paths pay the identical (reduced) PG&E bill, the year-17 crossover is **independent of the rate-escalation assumption entirely** — it depends only on the lease's contractual 3% escalator vs. ownership's maintenance and replacement costs. The honest one-line summary: lease wins the first 15 years, ownership wins the last 10, and the crossover sits right at the edge of the 10-15 year confidence horizon from Part 1.

## Buyout, exit, and term-mismatch risks (lease path)

- **Confirmed directly with Tesla: buyout is available any time in years 5-25**, not a one-time year-5-only window.
- **Not fixed**: buyout price is "fair market value," calculated per-contract, no public schedule. Any quoted figure today (e.g., $19,028 on the 5.88kW system) is an estimate for *if exercised now* — not binding at a future date.
- **Industry pattern is unfavorable to the buyer**: Sunrun/Sunnova data shows quoted buyout prices often running 20-30%+ above independent appraisal. Treat any quoted buyout figure as a floor. An independent solar appraisal ($300-600) is a documented, worthwhile move before accepting a buyout price when the time comes.
- **Note the lease+buyout path is dominated by Corda ownership if the ~$23k estimate holds**: $500 + ~$9,684 in payments + $19,028 quoted buyout ≈ $29,200 to own at year 5 — ~$6k more than just buying from Corda up front, with FMV risk on top.
- **No free early exit before year 5.** Tesla's lease disclosure states no early termination rights after installation. Pre-year-5 options are lease transfer to a home buyer (requires their agreement, not guaranteed) or an early termination fee (industry range $5,000-40,000).
- **Term-horizon mismatch**: the lease runs 25 years, but Part 1's key question is only whether you'll stay 10-15. Selling in year 10-15 means either transferring the lease to the buyer — a documented friction point that shrinks the buyer pool and complicates sales — or exercising the FMV buyout on Tesla's number at exactly the moment you have the least leverage.
- **Counterparty risk over 25 years**: solar lessors routinely sell their lease portfolios (the SolarCity-era books changed hands this way). "Tesla owns and services it" describes today's counterparty; your servicer in year 15 may be whoever bought the paper.
- **Open question, unresolved**: one source describes the Powerwall specifically as having a 12-year lease sub-term within the 25-year solar lease, distinct from the panels. Unclear what happens at year 12. **Ask Tesla directly before signing.**

## Bottom line on Part 2

With Corda's credit structure confirmed and the comparison re-run at the right size, **ownership (~$23k est.) is the stronger pure-financial instrument for a confident long hold — the crossover vs. the lease sits around year 17**: better cost from there out even with replacements priced in, immune to the lease escalator, ~9-11% expected IRR, and it survives the flat-rate scenario. **The lease remains the defensible choice if capital preservation and risk transfer matter more than long-run cost** — it's positive from day one, Tesla carries equipment risk, and daytime charging hedges its worst scenario — but go in knowing it is the more leveraged bet on PG&E rates and the harder contract to leave. First step either way: get Corda's real quote at 13-14 panels to replace the ~$23k estimate.

---

# Part 3: If doing this — sizing decisions

These are largely orthogonal to Parts 1 and 2 (they hold regardless of payment instrument, with lease-specific notes called out where they differ).

## System size: 5.88kW, not 8.40kW

- Real measured usage (~9,017 kWh/yr) is closer to what a 5.88kW system produces (~85% offset) than an 8.40kW system (~122% offset, oversized).
- Under NEM3, exported excess is worth ~$0.07/kWh vs. your ~$0.39-0.40/kWh retail rate — an oversized system mostly generates cheap exports, not real savings.
- **Lease-specific finding**: at the current charging pattern, upsizing to 8.40kW under the lease is a **net financial loss** — the extra panels cost $38/mo more in payment but only save $31.50/mo on the PG&E bill (-$6.50/mo), before even counting the larger buyout figure (~$5.2k higher).
- **With daytime EV charging (the confirmed plan), the corrected model flips this to mildly positive**: marginal savings rise to ~$52/mo against the $38/mo payment (+$14/mo). That's still modest — it only holds while the daytime habit holds, and it buys a bigger 25-year commitment and buyout figure for ~$14/mo. Staying at 5.88kW remains the lease-path recommendation; upsizing is no longer *wrong*, just not clearly worth the added commitment.
- Under ownership, marginal panels run ~$7,500 gross (~$5,300 net of the 30% credit — both vendors price panels near $2.98/W): payback ~14yr at the current pattern but **~8-9yr with daytime charging — comparable to the base system's own payback, so upsizing is no longer weak on the ownership path if the daytime habit is real**. (An earlier revision priced marginal panels gross while pricing everything else net-of-credit, which overstated the case against upsizing.) The remaining arguments for staying small are softer ones: extra production still tails off into $0.07 exports, the model runs slightly optimistic, and the sizing can be settled with real quotes at both sizes rather than this estimate.

## Battery count: 1 Powerwall, not 2

- Marginal cost of a 2nd Powerwall: ~$5,900 credit-adjusted (~$8,200 gross). Marginal annual savings in the corrected model: **$223/yr at the current charging pattern, collapsing to ~$104/yr with daytime charging**. **Payback: 26 years at best, ~57-79 years in the daytime-charging scenario** — never close to reasonable.
- The 2nd battery's original justification (catching EV-charging-night overflow) doesn't hold up: even 2 Powerwalls combined (27kWh) don't fully cover a typical ~40kWh overnight charging session.
- **If EV charging shifts to daytime, the case for a 2nd battery gets weaker, not stronger** — marginal savings drop by more than half because the overnight overflow it would catch mostly disappears once that load doesn't need storage at all.
- **No battery count solves winter grid dependence.** Modeled December production (~12 kWh/day) is *below* even one Powerwall's 13.5kWh capacity and January (~14 kWh/day) barely above it — while winter daily usage runs far higher. The constraint is production, not storage, and no amount of battery fixes a day when the panels simply didn't make enough energy.

## The highest-leverage move available: daytime EV charging

Roughly 43% of annual usage (~3,860 kWh/yr per the toolkit's EV-detection heuristic) is EV charging, historically concentrated overnight. Shifting it to ~10am-3pm (Tesla supports solar-aware scheduled charging) has a bigger impact on the economics than any sizing decision above. *(Figures corrected twice from the first draft — the shifted-scenario simulation had bugs in both rev 1 and rev 2; see the Addendum's correction history.)*

| | Current pattern (mostly overnight) | EV shifted to midday |
|---|---|---|
| Annual PG&E bill (5.88kW+1PW) | $1,358/yr (~$113/mo) | **$1,048/yr (~$87/mo)** |
| Net monthly cash flow vs. $152/mo lease payment | **+$26/mo** | **+$52/mo** |

The practical prerequisite — the car actually being home midday often enough — has been confirmed, so this is treated as the plan of record rather than an aspiration. It still deserves to be treated as a real commitment: beyond the +$26/mo, it's also the hedge that keeps the lease viable if PG&E rates stay flat (Part 2), which makes it load-bearing for the lease path specifically.

---

# Part 4: Underlying assumptions and open risks

- **The core bet, restated**: every long-horizon number in this report leans on PG&E's rate trajectory (Part 1's central caveat). Trailing 10yr CAGR ~7.2%, but 2024-2026 has seen actual cuts, and the structural shift toward fixed charges moves part of the bill out of solar's reach entirely. Scenarios were tested at flat (0%), 2%, 5%, and 7%/yr — **the two instruments fail differently at the low end**: ownership degrades to a ~0% return but still pays back; the lease goes outright cash-flow negative by year 7 under flat rates unless daytime charging is adopted (Part 2).
- **Maintenance/replacement risk** is real and asymmetric between structures — Tesla bears it during an active lease; an owner bears it directly, and most vendor-provided savings projections (including Corda's own) explicitly exclude it.
- **Buyout pricing uncertainty** (Part 2) means the long-run "lease now, buy out later" plan has a real unknown embedded in it — plan for the buyout to come in above any quoted estimate.
- **Company/product legitimacy**: Corda Solar — CSLB #1019424, licensed C-46/C-10, in business since 2007 — checks out. Tesla's own financing was verified to have no hidden dealer-fee markup. **The federal-credit question is now resolved**: Corda's 30% credit is legitimate via a 5-year lease/PPA structure (Corda claims the 48E commercial credit and passes it through; ownership transfers at no cost at year 5) — confirmed no hidden buyout. One timing/compliance wrinkle: the 48E begin-construction safe harbor (July 4, 2026) has passed, so the system must be **placed in service by Dec 31, 2027** for Corda's credit to exist, and foreign-entity-of-concern (FEOC) component-sourcing rules now apply to the claim — both are Corda's compliance problem *only if the contract says so*. Remaining diligence items: get the $0-cost transfer in writing, **get in writing that the quoted price does not change if Corda's 48E claim fails or is reduced**, and get a real quote at the recommended 13-14 panel size to replace this report's ~$23k estimate.

---

# Addendum: data sources, methodology, and how to re-verify

**Raw data (in this folder):**
- `electric_usage_2025-08-13_to_2026-08-13.csv` — real hourly electric usage/cost, 366-day clean window (most authoritative usage source)
- `gas_usage_2025-08-13_to_2026-08-12.csv` — real daily gas usage/cost, same window
- An older, partial-year electric/gas pair (2025-07-12 to 2026-07-01) also present — superseded by the above, kept for reference only

**Quotes/proposals (in this folder):**
- `corda_solar_quote.md` — itemized breakdown of Corda Solar's real proposal (1-battery and 2-battery options), including the PPA/credit caveat that started the financing-structure investigation
- `tesla_direct_quote.md` — Tesla's own Cash/Lease/Finance quotes at 8.40kW, including the verified-clean financing math
- `quick_numbers.md` — original high-level usage/cost summary
- `pge_usage_summary.md` — first-pass usage analysis (TOU shape, EV load detection, seasonal pattern)

**Calculation methodology — `solar_analysis_toolkit.py` (in this folder):**
A parameterized, re-runnable Python module containing the core simulation behind every dollar figure in this report:
- `load_usage()` — parses the real hourly CSV
- `simulate(rows, system_kw, battery_capacity_kwh, ...)` — hour-by-hour dispatch: models solar production via a calibrated seasonal/diurnal curve (see module docstring), charges/discharges the battery, prices grid imports at the real historical hourly PG&E rate, credits exports at a flat NEM3 rate (default $0.07/kWh)
- `shift_ev_load_to_midday()` — the EV-charging-optimization scenario used in Part 3
- Run `python3 solar_analysis_toolkit.py` directly to reproduce the base and EV-shifted 5.88kW/8.40kW + 1 Powerwall figures as a sanity check

**Modeling limitations, stated plainly**: usage-side data is real and hourly. Production-side data is *modeled*, not measured (no panels installed yet) — calibrated to Corda's roof-specific annual estimate but distributed via an idealized clear-sky curve with no simulated day-to-day weather variability. Also not modeled: panel degradation (~0.4-0.5%/yr, so ~7% less output by year 15), battery round-trip losses (~10%), and the rate-plan switch that comes with solar enrollment — NEM3's Solar Billing Plan with a battery typically means moving to an electrification rate (e.g., E-ELEC, ~$15/mo base charge, different TOU shape), while this model prices everything at the historical tariff embedded in the CSV. All of these push the same direction — modeled savings are *slightly optimistic* vs. real-world results. Trust the shape of every conclusion (seasonal mismatch, EV-load dominance, panel-vs-battery tradeoffs); treat exact dollar figures as directionally right, not precise to the dollar.

**Correction history (2026-08-15, rev 2)**: the first draft's EV-shift scenario had two simulation bugs in `shift_ev_load_to_midday()` — moved load was appended as extra rows (double-counting midday solar production by ~29%) and residual load in former EV hours inherited an inflated per-kWh rate. Both fixed; the shifted-scenario bill corrected from $524/yr to $894/yr and net lease cash flow from +$96/mo to +$65/mo. The first draft's Part 2 lease projection table also omitted roughly half the lease-path cost and was rebuilt from scratch. Every downstream number was recomputed after the fixes.

**Correction history (2026-08-15, rev 3 — independent review)**: rev 2's rate fix was incomplete. `simulate()` built its month-hour fallback rate table from the rows passed in, so in the shifted scenario the synthetic rows' corrupted cost/usage ratios (original cost ÷ inflated midday usage → fake ~$0.04/kWh midday rates; full EV-session cost ÷ 1kWh residual → fake ~$2.70/kWh overnight rates) polluted the very averages used to price synthetic imports. Fixed by excluding synthetic rows from rate-table construction. Shifted-scenario bill corrected from $894/yr to $1,048/yr, daytime lease cash flow from +$65/mo to +$52/mo (2x the current pattern, not 2.5x), daytime ownership IRR from ~12% to ~11% (flat-rate: ~4.6% to ~3.3%), and the flat-rate lease's daytime survivability from "positive through ~year 20" to "through ~year 19, cash-flow negative from year 11." Two non-simulation errors also fixed: Part 3's marginal-panel cost was quoted gross ($7,500) while every other price was net of the 30% credit (~$5,300 net — which changes ownership-path upsizing from "weak" to ~8-9yr payback with daytime charging), and the winter-production figure ("9-10 kWh/day") didn't match the model's own output (~12-14 kWh/day; the storage-vs-production conclusion stands). All qualitative conclusions survived rev 3; the daytime-charging lever remains the biggest one, just ~20% smaller than rev 2 stated.

**Multi-year projection tables** (Parts 1 and 2) were built as standalone compounding-sum calculations on top of `simulate()`'s annual output, not saved as separate scripts — they're simple formulas (do-nothing bill vs. lease/ownership cost, escalating at stated rates) that don't require re-running the full simulation each time. Exact rates are stated inline wherever a table appears. Ownership-side assumptions used throughout Part 2: ~$23,000 right-sized Corda price (estimated — $2.97/W panel portion + $15.7k Powerwall, ×0.7 for the credit), $410/yr maintenance (midpoint of $300-520), one ~$10,000 Powerwall/inverter replacement at year 12 (plus a second at year 24 on the 25-yr horizon).

**For anyone re-verifying this analysis**: re-run `solar_analysis_toolkit.py` against the current CSV before trusting any number here — don't assume figures are still current if usage patterns, quotes, or the PG&E rate environment have changed materially since this report was written (2026-08-15).
