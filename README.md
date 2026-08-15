# Solar Decision Analysis

A personal analysis of whether to go solar (Danville, CA area), built from real PG&E usage data and real quotes from Corda Solar and Tesla. Shared here so friends can spot-check the reasoning and numbers.

**Not financial advice — this is one household's homework, not a recommendation for anyone else's situation.**

## Start here

Read **[`solar_decision_report.md`](solar_decision_report.md)** first — it's the main document, structured around the actual decision:
1. Should you do solar at all?
2. If yes, which payment instrument (cash / loan / lease)?
3. If doing it, how to size the system?

It opens with household context (usage, house type, etc.) so it should make sense read cold, on a phone, with no other files open.

## If you want to verify the numbers yourself

Every dollar figure in the main report traces back to `solar_analysis_toolkit.py` — a parameterized, re-runnable Python script (no dependencies beyond the standard library). It:
- Parses the real hourly PG&E usage data in this folder
- Models solar production from a roof-calibrated seasonal/diurnal curve
- Runs an hour-by-hour battery dispatch simulation
- Prices grid imports at the real historical PG&E rate for that hour, exports at a flat NEM3 rate

Run it directly to reproduce the base figures:
```
python3 solar_analysis_toolkit.py
```

**If you're pointing an agent at this repo**: the toolkit is meant to be *re-run*, not just read — don't trust cached numbers in the `.md` files without re-verifying against the current CSVs, especially if you're checking this well after 2026-08-15. The script's docstring has the full methodology and its known limitations (production data is modeled, not measured — no panels are installed yet).

## File guide

| File | What it is |
|---|---|
| `solar_decision_report.md` | **Main report** — the full decision analysis |
| `solar_analysis_toolkit.py` | Reusable simulation code behind the numbers |
| `corda_solar_quote.md` | Real quote from a local installer (Corda Solar), annotated |
| `tesla_direct_quote.md` | Real quotes direct from Tesla (two system sizes, Cash/Finance/Lease) |
| `pge_usage_summary.md` | First-pass usage analysis (time-of-use pattern, EV load detection, seasonality) |
| `quick_numbers.md` | One-page high-level usage/cost summary |
| `electric_usage_*.csv`, `gas_usage_*.csv` | Real PG&E interval usage data (Green Button export), personal identifiers redacted |

## Caveats

- Usage data is real and measured (hourly). Solar production data is *modeled*, not measured — there's no installed system yet, so production is estimated from a calibrated curve, not observed. Treat dollar figures as directionally right, not exact.
- Assumptions about future PG&E rate increases, loan/lease terms, and buyout pricing are explicit and stated inline wherever they're used — check those before trusting any multi-year projection.
- Personal identifiers (name, address, account numbers) have been stripped from the shared files and CSVs.
