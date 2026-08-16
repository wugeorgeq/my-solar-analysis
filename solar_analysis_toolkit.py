"""
Reusable functions for a Bay Area residential solar/battery analysis.

IMPORTANT for future turns: this is a TOOLKIT, not a cached result. Re-run it against
whatever the CURRENT data files are — don't trust old numbers in the .md reports without
re-verifying if usage patterns, quotes, or assumptions have changed. File paths below point
to the newest known-good CSVs as of 2026-08-15; check ELEC_CSV_DEFAULT still exists and is
still the most recent download before relying on it.

Methodology summary (see solar_decision_report.md Addendum for full writeup):
- USAGE side: real, hourly, measured from PG&E Green Button interval data. High fidelity.
- PRODUCTION side: MODELED, not measured (no real panels installed yet). Calibrated to
  Corda Solar's roof-specific annual estimate (10,910 kWh/yr for 8.36kW => 1305.5 kWh/kW/yr),
  distributed across months using typical Bay Area seasonal weighting, and within each day
  via an idealized sine curve between that month's sunrise/sunset. Every day within a given
  month gets an IDENTICAL shape/magnitude -- no simulated weather variability (clouds, fog,
  smoke days). This likely makes modeled self-consumption/savings slightly OPTIMISTIC vs.
  reality. Trust the shape of conclusions (seasonal mismatch, EV-load dominance, panel vs.
  battery tradeoffs); treat exact dollar figures as directionally right, not precise.
- BATTERY DISPATCH: simple greedy hour-by-hour simulation. Excess production charges the
  battery first, remainder exports at a flat NEM3 rate; production shortfall discharges the
  battery first, remainder imports at that hour's REAL historical PG&E rate (derived from
  the CSV's own cost/usage ratio per hour, so actual TOU structure is reflected for imports).
- EV CHARGING DETECTION: hourly intervals with usage > 4.0 kWh are treated as EV-charging-like
  (sustained ~8-9kWh/hr for multiple hours = Level 2 charger signature, confirmed by manually
  inspecting raw rows early in the analysis). This threshold is a heuristic, not a measured fact.
"""
import csv, math
from collections import defaultdict
from datetime import datetime

import os
ELEC_CSV_DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "electric_usage_2025-08-13_to_2026-08-13.csv")

PROD_FACTOR_DEFAULT = 10910 / 8.36  # kWh/kW/yr, calibrated to Corda's real roof-specific estimate (see corda_solar_quote.md)

EV_THRESHOLD_KWH = 4.0  # hourly usage above this = treated as EV-charging-like load

SUNRISE_SUNSET = {  # (sunrise_hr, sunset_hr) decimal, ~37.8N latitude (SF Bay Area) approx incl. DST
    1: (7.4, 17.25), 2: (7.0, 17.85), 3: (7.25, 19.25), 4: (6.5, 19.75),
    5: (6.0, 20.25), 6: (5.85, 20.6), 7: (6.0, 20.5), 8: (6.4, 20.0),
    9: (6.85, 19.25), 10: (7.25, 18.5), 11: (6.75, 17.1), 12: (7.25, 16.9),
}

MONTH_WEIGHT_RAW = {1: .058, 2: .072, 3: .093, 4: .104, 5: .112, 6: .115,
                     7: .116, 8: .106, 9: .090, 10: .075, 11: .056, 12: .050}
_wsum = sum(MONTH_WEIGHT_RAW.values())
MONTH_WEIGHT = {k: v / _wsum for k, v in MONTH_WEIGHT_RAW.items()}

DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def parse_money(s):
    s = s.strip()
    if not s:
        return 0.0
    neg = s.startswith('-')
    s = s.replace('$', '').replace('-', '')
    v = float(s) if s else 0.0
    return -v if neg else v


def load_usage(csv_path=ELEC_CSV_DEFAULT):
    """Returns list of dicts: date, month, hour, usage (kWh), cost ($)."""
    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        lines = f.readlines()
    header_idx = next(i for i, l in enumerate(lines) if l.startswith('TYPE,DATE'))
    reader = csv.DictReader(lines[header_idx:])
    rows = []
    for r in reader:
        if not r.get('DATE'):
            continue
        dt = datetime.strptime(r['DATE'].strip(), '%Y-%m-%d')
        hour = int(r['START TIME'].strip().split(':')[0])
        usage = float(r['USAGE (kWh)']) if r['USAGE (kWh)'].strip() else 0.0
        cost = parse_money(r['COST'])
        rows.append({'date': dt.date(), 'month': dt.month, 'hour': hour, 'usage': usage, 'cost': cost})
    return rows


def _production_shape_for_hour(month, hour):
    sr, ss = SUNRISE_SUNSET[month]
    if hour + 1 <= sr or hour >= ss:
        return 0.0
    lo, hi = max(hour, sr), min(hour + 1, ss)
    if hi <= lo:
        return 0.0
    span = ss - sr
    steps = 20
    total = 0.0
    for i in range(steps):
        t = lo + (hi - lo) * (i + 0.5) / steps
        total += max(0, math.sin(math.pi * (t - sr) / span))
    return total / steps * (hi - lo)


def build_month_hour_shape():
    shape = {}
    for m in range(1, 13):
        vals = [_production_shape_for_hour(m, h) for h in range(24)]
        s = sum(vals)
        shape[m] = [v / s if s > 0 else 0 for v in vals]
    return shape


def shift_ev_load_to_midday(rows, midday_hours=(10, 11, 12, 13, 14), ev_threshold=EV_THRESHOLD_KWH):
    """Returns a new rows list with EV-like load (> ev_threshold kWh/hr) moved to midday hours,
    approximating 'what if EV charging happened during peak solar production instead'.

    The moved load is MERGED into the existing midday rows (never appended as extra rows) so
    each (date, hour) appears exactly once — simulate() computes production per row, so a
    duplicate hour would double-count that hour's solar production. Modified rows keep their
    original 'cost' (so the baseline bill stays the real historical bill) but are flagged
    synthetic=True: their cost/usage ratio no longer means anything as a per-kWh rate, so
    simulate() must price their imports at the month-hour average rate instead."""
    by_day = defaultdict(list)
    for r in rows:
        by_day[r['date']].append(r)
    shifted = []
    for day, day_rows in by_day.items():
        ev_total = sum(r['usage'] - 1.0 for r in day_rows if r['usage'] > ev_threshold)
        per_hour = ev_total / len(midday_hours) if ev_total > 0 else 0.0
        for r in sorted(day_rows, key=lambda x: x['hour']):
            r2 = dict(r)
            if r2['usage'] > ev_threshold:
                r2['usage'] = 1.0
                r2['synthetic'] = True
            if per_hour and r2['hour'] in midday_hours:
                r2['usage'] += per_hour
                r2['synthetic'] = True
            shifted.append(r2)
    return shifted


def simulate(rows, system_kw, battery_capacity_kwh, prod_factor=PROD_FACTOR_DEFAULT,
             nem3_export_rate=0.07, use_real_hourly_rate=True):
    """Hour-by-hour dispatch simulation. Returns dict with new_bill, savings, self-consumed %,
    imported kWh, offset %. `rows` can be raw load_usage() output or shift_ev_load_to_midday() output."""
    month_hour_shape = build_month_hour_shape()

    baseline_annual_bill = sum(r['cost'] for r in rows if r['cost'])
    total_usage = sum(r['usage'] for r in rows)

    month_kwh = defaultdict(float)
    month_cost = defaultdict(float)
    for r in rows:
        month_kwh[r['month']] += r['usage']
        month_cost[r['month']] += r['cost']
    month_avg_rate = {m: (month_cost[m] / month_kwh[m] if month_kwh[m] > 0 else 0.39) for m in range(1, 13)}

    hour_rate = defaultdict(lambda: defaultdict(list))
    for r in rows:
        if r['usage'] > 0 and r['cost']:
            hour_rate[r['month']][r['hour']].append(r['cost'] / r['usage'])

    def get_rate(m, h):
        vals = hour_rate[m].get(h)
        return sum(vals) / len(vals) if vals else month_avg_rate[m]

    annual_production = system_kw * prod_factor
    soc = 0.0
    import_cost = 0.0
    export_credit = 0.0
    self_consumed = 0.0
    exported = 0.0
    imported_kwh = 0.0

    for r in rows:
        m, h = r['month'], r['hour']
        day_total = annual_production * MONTH_WEIGHT[m] / DAYS_IN_MONTH[m]
        prod = day_total * month_hour_shape[m][h]
        load = r['usage']
        if use_real_hourly_rate and load > 0 and r['cost'] and not r.get('synthetic'):
            rate = r['cost'] / load
        else:
            rate = get_rate(m, h)
        net = prod - load
        if net >= 0:
            self_consumed += load
            charge = min(net, battery_capacity_kwh - soc)
            soc += charge
            export = net - charge
            exported += export
            export_credit += export * nem3_export_rate
        else:
            deficit = -net
            self_consumed += prod
            discharge = min(deficit, soc)
            soc -= discharge
            self_consumed += discharge
            remaining = deficit - discharge
            imported_kwh += remaining
            import_cost += remaining * rate

    new_bill = import_cost - export_credit
    savings = baseline_annual_bill - new_bill
    return {
        'annual_production': annual_production,
        'new_bill': new_bill,
        'savings': savings,
        'self_consumed_pct': 100 * self_consumed / annual_production if annual_production else 0,
        'imported_kwh': imported_kwh,
        'exported_kwh': exported,
        'offset_pct': 100 * annual_production / total_usage if total_usage else 0,
        'baseline_annual_bill': baseline_annual_bill,
        'total_usage': total_usage,
    }


if __name__ == '__main__':
    rows = load_usage()
    print(f"Loaded {len(rows)} hourly rows from {ELEC_CSV_DEFAULT}")
    shifted = shift_ev_load_to_midday(rows)
    for kw, cap in [(5.88, 13.5), (8.40, 13.5)]:
        res = simulate(rows, kw, cap)
        print(f"{kw}kW + {cap}kWh battery: new bill ${res['new_bill']:.0f}/yr, "
              f"savings ${res['savings']:.0f}/yr, offset {res['offset_pct']:.0f}%")
        res_s = simulate(shifted, kw, cap)
        print(f"  ... with EV charging shifted to midday: new bill ${res_s['new_bill']:.0f}/yr")
