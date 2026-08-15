# PG&E Usage Summary — for Solar Salesman Call
Data source: PG&E interval exports, **2025-07-12 to 2026-07-01** (355 days — essentially one full year; note 2025-07 and 2026-07 are partial months in the monthly table below).

## Key numbers to lead with

| Metric | Value |
|---|---|
| **Total annual electric usage** | **8,914.8 kWh** |
| Annualized (scaled 355→365 days) | ~9,167 kWh |
| Average daily usage | 25.1 kWh/day |
| **Total annual electric cost** | **$3,606.22** |
| Effective blended rate | $0.4045/kWh |
| Total annual gas usage | 530.1 therms |
| Total annual gas cost | $1,536.69 |
| **Combined annual PG&E bill (electric+gas)** | **$5,142.91** |

A salesman will usually size a system off the ~8,900–9,200 kWh/year figure. Your effective electric rate (~$0.40/kWh) is quite high, which is good context for a payback-period conversation.

## Monthly electric usage
| Month | kWh | Cost |
|---|---|---|
| 2025-07 (partial, 20 days) | 511.4 | $241.67 |
| 2025-08 | 1,150.9 | $562.87 |
| 2025-09 | 981.5 | $460.20 |
| 2025-10 | 894.7 | $410.20 |
| 2025-11 | 701.7 | $292.22 |
| 2025-12 | 864.0 | $340.30 |
| 2026-01 | 825.7 | $307.42 |
| 2026-02 | 491.0 | $185.49 |
| 2026-03 | 531.7 | $169.86 |
| 2026-04 | 618.2 | $197.50 |
| 2026-05 | 874.1 | $285.23 |
| 2026-06 | 433.6 | $141.65 |
| 2026-07 (partial, 1 day) | 36.4 | $11.61 |

- Highest usage month: **August 2025** (1,150.9 kWh) — likely AC load.
- Lowest full month: **June 2026** (433.6 kWh).
- Highest single day: **2025-09-03** at 81.6 kWh.
- Summer (Jun–Sep) usage: 3,113.8 kWh vs. rest of year: 5,801.0 kWh — usage is fairly winter-heavy, likely due to heating/other load, not just AC.

## Time-of-use shape (relevant to NEM 3.0 / battery economics)
Using PG&E's common 4pm–9pm peak window:
- **Peak (4–9pm): 1,901.2 kWh (21.3%)**
- **Off-peak (all other hours): 7,013.7 kWh (78.7%)**

Notable: usage actually spikes late at night (10pm–1am average 2.0–2.5 kWh/hr) and overnight/early morning is also elevated relative to midday — worth asking what's running then (EV charging, pool pump, etc.), since that's off-peak-only load solar alone won't offset without a battery or shifted schedule. Midday (10am–3pm, when solar production peaks) usage is comparatively low (~0.5–0.7 kWh/hr), meaning a lot of solar production would be exported rather than self-consumed — a strong argument for **pairing solar with a battery** under NEM 3.0's low export credit rates.

## Natural gas (for context if discussing electrification/heat pumps)
| Month | Therms | Cost |
|---|---|---|
| 2025-07 | 12.60 | $33.95 |
| 2025-08 | 19.96 | $54.16 |
| 2025-09 | 19.88 | $55.00 |
| 2025-10 | 25.15 | $72.17 |
| 2025-11 | 58.61 | $172.49 |
| 2025-12 | 126.43 | $408.44 |
| 2026-01 | 108.88 | $324.42 |
| 2026-02 | 70.71 | $194.12 |
| 2026-03 | 27.35 | $66.75 |
| 2026-04 | 26.07 | $66.83 |
| 2026-05 | 22.90 | $59.04 |
| 2026-06 | 11.52 | $29.32 |
| 2026-07 | 0.00 | $0.00 |

Gas is heavily winter-loaded (Dec/Jan alone = $732.86, ~48% of annual gas cost) — likely space heating. 530 therms ≈ 15,530 kWh-equivalent of energy, useful if the salesman pitches heat-pump electrification alongside solar (that would substantially raise the electric load solar needs to cover).

## Questions this raises for the salesman
1. What system size (kW) are they proposing, and what annual production (kWh) do they estimate? Compare against the ~9,000 kWh/yr baseline above.
2. Under NEM 3.0, what export rate applies, and given the low midday self-consumption shown above, are they recommending a battery?
3. How does their production estimate handle the winter-heavy usage pattern (fewer solar hours when your usage/gas heating load is highest)?

## Payback timeline (modeled from your actual hourly data)

**Correction on the 30% federal credit:** the Section 25D residential solar tax credit was repealed by the "One Big Beautiful Bill Act" (signed July 2025) — it only applies to systems placed in service on or before **2025-12-31**. As of today (2026-08-14), a **cash/loan purchase gets $0 federal credit**. If the salesman is still quoting 30% off, ask whether they mean a lease/PPA (third-party-owned, they claim a different commercial credit, 48E, through 2027) — that's a different deal, you don't own the system. Also ask about **SGIP** (CA's Self-Generation Incentive Program, still active) for a battery rebate — some high-fire-threat zones in CA qualify for the higher "Equity Resiliency" tier (worth checking your specific address); this is independent of the dead federal credit and worth pushing on.

Simulation used your real hourly load + a modeled CA production curve (placeholder pricing: $3.75/W panels+inverter, $11,500/Powerwall installed, $3k roof/gutter — **swap in the salesman's actual quoted numbers**):

| System | Batteries | Self-consumption | Annual savings | Upfront cost (no credit) | Simple payback |
|---|---|---|---|---|---|
| 6kW | 0 | 23.9% | $1,370 | $25,500 | 18.6 yrs |
| 6kW | **1** | **56.7%** | **$2,377** | **$37,000** | **15.6 yrs** ← best |
| 6kW | 2 | 66.7% | $2,682 | $48,500 | 18.1 yrs |
| 7kW | 1 | 50.1% | $2,536 | $40,750 | 16.1 yrs |
| 8kW | 1 | 44.5% | $2,671 | $44,500 | 16.7 yrs |

Takeaways:
- **1 Powerwall beats 2 in every system size tested** — 2nd battery's marginal savings never justify its marginal cost. Confirms the earlier load analysis.
- **Solar-only (no battery) self-consumption is only ~20-24%** — the rest exports at NEM 3.0's low avoided-cost rate (~$0.07/kWh vs your ~$0.40/kWh retail rate), which is exactly why "NEM3 is marginal" is correct without storage.
- **Bigger systems pay back slower**, not faster — excess production above what you can self-consume or store just exports at the crushed NEM3 rate. 6kW+1 battery beat 7kW and 8kW options.
- These are simple paybacks (no electricity rate inflation ~3-6%/yr historically, no panel degradation ~0.5%/yr — roughly offsetting, real payback likely ±1-2 yrs of these numbers).
- The $3k roof/gutter work is very unlikely to qualify for any credit even when 25D existed (only costs integral to the solar install itself count) — treat it as a flat add-on to upfront cost regardless of incentive scenario.
- Once you have the salesman's real quoted price and production estimate, recompute: `payback = (their total price - any real applicable credit) / (your current annual bill − their quoted new bill)`.

**How the best-case $2,377/yr (~$198/mo) savings figure was derived** (6kW system + 1 Powerwall row): it's `$3,606 actual current annual bill − $1,229 simulated new bill`. The $1,229 came from an hour-by-hour dispatch simulation over your real 8,760-hour usage data: modeled solar production (6kW × CA seasonal/diurnal production curve) charges the battery with excess daytime production; the battery discharges to cover evening/night deficits up to its 13.5kWh capacity; any remaining shortfall imports from the grid priced at **your actual historical PG&E rate for that specific hour** (pulled from the CSV's real cost column, so real TOU rates are baked in); any leftover excess production exports at the flat NEM3 ~$0.07/kWh assumption.

## Financing vs. cash

Financing turns a slow payback into a **negative monthly cash flow** in every realistic scenario — the loan payment exceeds the $198/mo cash savings at every term/APR combination tested (principal $37,000, the 6kW+1 Powerwall case):

| Term | APR | Monthly payment | Net vs. $198/mo savings | Total interest | True breakeven (incl. interest) |
|---|---|---|---|---|---|
| 10yr | 6% | $411/mo | **−$213/mo** | $12,271 | 20.8 yrs |
| 15yr | 8% | $353/mo | **−$155/mo** | $26,608 | 26.8 yrs |
| 20yr | 8% | $309/mo | **−$111/mo** | $37,221 | >30 yrs |
| 25yr | 6% | $238/mo | **−$40/mo** | $34,450 | >30 yrs |
| 25yr | 10% | $336/mo | **−$138/mo** | $63,788 | never within 30yrs |

Several scenarios never break even inside the panel/inverter's 25-year warranty (Powerwall warranty is only 10 years). Longer terms lower the monthly bite but balloon total interest, pushing true breakeven out further, not closer.

Two things to press the salesman on:
1. **Ask for both the cash price and the loan price for the identical system.** Solar loans commonly bake a 10–20% "dealer fee" into the principal behind a teaser low APR — if the loan price is meaningfully higher than the cash price, that gap is the hidden fee.
2. **Get their actual proposed APR/term** and check whether it produces a *positive* monthly cash flow (payment < ~$198/mo) — if not, financing costs you more per month than PG&E does today, for the life of the loan.

## Lease / PPA (quick breakdown)

No real lease quote yet, so this uses illustrative representative CA market terms — **replace with their actual numbers**. Structurally: a lease/PPA means a third party owns the system; they capture the (still-active, through 2027) 48E business credit themselves — it is not passed through transparently, and the price they charge you is whatever they set it at, not a guaranteed 30%-off equivalent. Leases/PPAs also commonly **exclude the battery** (extra $50–150/mo if you want one added) and in many contracts **the developer, not you, keeps the NEM3 export credit** — both of which matter a lot here since your data shows storage is what makes the economics work.

25-year nominal total cost (not discounted), same 6kW system baseline, no battery for lease/PPA:

| Option | 25-yr total cost |
|---|---|
| Do nothing (stay on PG&E, ~5%/yr rate inflation) | $172,104 |
| **Cash purchase (6kW + 1 Powerwall, $37k upfront)** | **$81,808** |
| Loan purchase (15yr @ 8%) | $108,348 |
| Lease (illustrative: $180/mo, 2.9%/yr escalator, no battery) | $170,846 |
| PPA (illustrative: $0.18/kWh, 2.9%/yr escalator, no battery) | $167,326 |

Headline: at these illustrative (but market-typical) terms, **lease/PPA barely beats doing nothing at all** — losing both the battery's self-consumption boost and the export-credit passthrough eats nearly all of the benefit under NEM3. Ownership (cash or loan) is the only path that captures real savings in this model.

Questions to ask specifically about a lease/PPA offer:
1. Is a battery included, or extra — and if extra, how much/month?
2. Who keeps the NEM3 export credit, you or them?
3. What's the annual escalator rate, and is it capped?
4. What happens at year 25 (buyout price, removal cost, or forced renewal)?
5. What happens to the lease if you sell the house (transfer to buyer vs. payoff requirement) — this can complicate a home sale.
