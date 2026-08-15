# Tesla Direct Quote — Reference

Two system sizes configured in Tesla's online ordering tool, both with 1x Tesla Powerwall 3. Screenshots from Tesla's ordering flow, 2026-08-15.

---

# 8.40kW System

Customized to roughly match Corda's spec (8.36kW, 1 Powerwall 3, see `corda_solar_quote.md`). All three payment tabs (Cash/Finance/Lease) captured.

## Cash
- 8.40kW Solar Panel: $25,032
- 1 Powerwall 3: $15,700
- Installation: Included
- Solar & Powerwall Discount: -$4,900
- 8.40kW Discount: -$840
- Solar Renewable Energy Credit: -$504
- Taxes: $975
- **Cash Price: $35,463**
- No federal 30% credit line shown on any tab (Cash/Lease/Finance) — consistent with 25D being dead for direct purchase; Tesla's tool does NOT show a disputed PPA-linked credit the way Corda's proposal does.

## Finance
- Same equipment/discounts as Cash → Cash Price $35,463
- $3,949 down, 180 months (15yr), 7.24% APR → **$288/mo**
- **Verified clean**: financing $31,514 (Cash Price − down) at 7.24%/180mo computes to $287.50/mo — matches Tesla's stated $288 almost exactly (~$0.50 gap, rounding only). No evidence of a hidden dealer-fee markup on principal (contrast with the general solar-loan market, where installer-sourced loans often inflate principal 20-30% via a dealer fee).
- Total cost over full 15yr term: down + 180×$288 = **$55,789** (total interest ~$20,326)
- **Paid off early at year 5**: $3,949 down + 60×$288 ($17,280) + remaining balance payoff (~$24,464) = **$45,692.83 total to fully own at year 5**

## Lease
- Same equipment/discounts, Cash Price basis $34,488 (no separate taxes line shown)
- $500 upfront, $190/mo starting payment, 25yr term, 3%/yr escalator
- **Optional buyout after 5 years: $24,208 (as quoted in tool)**
- ⚠️ **Buyout is NOT contractually fixed** — described as "fair market value," similar to vehicle leasing. Tesla's 5yr-buyout-with-Powerwall-3 program is new; no Tesla-specific track record exists yet.
- **Industry pattern (Sunrun/Sunnova, older SolarCity-era leases) is unfavorable**: buyout prices are calculated on projected "value," not honest depreciation — real examples show buyouts landing close to the cost of comparable *new* equipment. Quoted buyout prices have been found 20-30% above independent appraisal; some customers pay $300-600 for an independent solar appraisal specifically to negotiate the number down at exercise time. Treat $24,208 as a floor/best case, not a reliable planning number.
- **Total cost to own at year 5 (as quoted)**: $500 + $12,104.83 (60 escalating payments) + $24,208 buyout = **$36,812.83**
- **Stress-tested** (buyout comes in above quote, per industry pattern):
  - +10% buyout ($26,629): total $39,233.63
  - +20% buyout ($29,050): total $41,654.43
  - +30% buyout ($31,470): total $44,075.23

---

# 5.88kW System

This is the **"minimum recommended" size Tesla's tool suggested** — the one ultimately recommended over 8.40kW (see `solar_decision_report.md` Part 3 for the full sizing rationale). Only the **Lease tab** was captured; Cash and Finance figures for this specific size were not screenshotted, so they're not included here rather than estimated.

## Lease
- 5.88kW Solar Panel: $17,522
- 1 Powerwall 3: $15,700
- Installation: Included
- Solar & Powerwall Discount: -$4,900
- Solar Renewable Energy Credit: -$353
- **No "5.88kW Discount" line** — unlike the 8.40kW system's extra -$840 size-based discount, this smaller system doesn't qualify for it. Confirmed this makes the 8.40kW system ~3.4% cheaper per watt on the panel line — but that discount was already factored into the sizing comparison in `solar_decision_report.md`, and upsizing was still a net loss under the lease even accounting for it.
- **Cash Price: $27,970** (no separate taxes line shown, consistent with the Lease tab pattern seen at 8.40kW)
- $500 upfront, **$152/mo** starting payment, 25yr term, 3%/yr escalator
- **Optional buyout after 5 years: $19,028** (as quoted — subject to the same "fair market value, not fixed" caveat as the 8.40kW system's $24,208 figure above)

## Total cost to own at year 5 (as quoted, same methodology as 8.40kW above)

| | 5.88kW | 8.40kW (for comparison) |
|---|---|---|
| Upfront | $500 | $500 |
| 60 escalating lease payments | $9,683.86 | $12,104.83 |
| Buyout at year 5 (quoted) | $19,028 | $24,208 |
| **Total to own at yr5** | **$29,211.86** | $36,812.83 |

## Key comparisons run so far
- **Finance (pay off at yr5, $45,692.83) vs. Lease+buyout (as quoted, $36,812.83)**: Lease path is $8,880 cheaper at face value. Even worst-case buyout (+30%) still favors Lease, but only by ~$1,618 — margin nearly disappears under realistic buyout inflation.
- **Implied effective APR of Lease+buyout path (financing $33,988 over 5yr via payments+balloon): ~1.58%**, vs. Finance's stated 7.24% — likely because Tesla (as lessor) captures the 30% commercial (48E) credit during the lease and passes some value through via the payment/buyout structure. Same mechanism as Corda's PPA-linked credit.
- **Corda cash ($28,376.60) vs. Tesla Lease+buyout**: if Corda's price is genuinely all-in with no separate later buyout, Corda is $8,436 (vs. quoted Tesla buyout) to $15,698 (vs. worst-case Tesla buyout) cheaper. **Unconfirmed and important**: since Corda's credit is also PPA-linked (per the disclaimer flagged in `corda_solar_quote.md`), it's unknown whether Corda's $28,377 already includes full ownership transfer or whether a separate buyout payment is due later, same as Tesla's structure. This needs to be asked directly, same as the existing open questions for Nathan.

## Open questions this raises for Corda (add to existing list)
- Does the $28,376.60 "cash" price include full, no-additional-cost ownership transfer, or is there a separate buyout payment due at the end of the PPA/recapture period (mirroring Tesla's Lease buyout)?
- If there is a later buyout, what is it, and is it contractually fixed or "fair market value" (same red flag as Tesla's)?
