"""
Spider matter-compiler v10 - IN-PLACE TRANSFORMERS, MODELLED ESTIMATE.
v9 had transformers SUPPLIED (3x 5,000kg, placed in 2h by 100x L spiders each).
This run: spiders BUILD them in place, starting at the mounting joints and working out.

Transformer: 5 MVA distribution, ~5,000 kg each, 3x = 15,000 kg total.
In-place build order (spiders start at the pad, never lift the finished unit):
 1. Mounting joints / base frame: steel, bolted to concrete pad
 2. Core: laminated silicon steel, stacked layer by layer, ~2,000 kg per transformer
    Laminations: 0.3mm sheets, stacked, no air gaps >0.05mm or efficiency collapses.
    Spiders lay sheets like shingles, S-spiders do the precision stacking.
 3. Windings: copper wire, ~1,000 kg per transformer, wound in place around the core limbs.
    Spool copper, 0.5-2mm wire, layer by layer, insulation paper between layers (supplied paper, placed).
    Winding is SLOW - it is a continuous coil, cannot be split across many spiders easily.
 4. Tank: steel, ~1,200 kg, built AROUND the core+windings, like a shell.
    Spiders build the tank walls outward from the base, sealing as they go.
 5. Radiators / cooling fins: steel, 400 kg, attached to tank sides.
 6. Bushings, tap changer, oil: SUPPLIED precision parts, placed. Oil: 1,500 L per transformer, trucked in, pumped in.
    Oil is a liquid, spiders cannot make it from powder.
 7. Test: insulation resistance, ratio, oil test - 4h per transformer, parallel.

Rates (from sims 5-9):
 - Core laminations: steel, 20 mm/s, 0.3mm sheet, 100% dense, + honing for flatness. Rate ~648 min/kg single (same as steel liners).
 - Windings: copper spool, 60 mm/s, but winding is sequential - max 4 spiders per transformer winding at once (one per limb), cannot use 500.
 - Tank/radiators: steel, 30 mm/s, 60% infill, ~400 min/kg.
"""
import math, json

# --- Per transformer, spider-made ---
# Core 2000kg steel, windings 1000kg Cu, tank 1200kg steel, radiators 400kg steel, misc 200kg
parts = [
    ("Core laminations", "steel", 2000, 648),
    ("Windings", "copper", 1000, 20),  # copper wire rate, min/kg
    ("Tank", "steel", 1200, 400),
    ("Radiators", "steel", 400, 400),
    ("Misc / mounts", "steel", 200, 400),
]
print("Per transformer, spider-made (single spider):")
total_single_min = 0
for name, mat, kg, rate in parts:
    t = kg*rate
    total_single_min += t
    print(f"  {name}: {kg}kg {mat}, {t/60:,.0f}h")
print(f"  Total per transformer single: {total_single_min/60:,.0f}h = {total_single_min/60/24:.1f} days")
print(f"  3 transformers single: {total_single_min*3/60:,.0f}h")

# --- Swarm, in-place ---
# Core: can split by limb (3 limbs), S-spiders precision, M/L help. Effective ~200 spiders per transformer, 3 transformers in parallel = 600 spiders on cores.
# Windings: bottleneck - only 4 spiders per transformer can wind at once (one per limb, sequential coil).
#  That means windings CANNOT be parallelised by swarm size. It is a serial job.
# Tank: can split, ~200 spiders per transformer.
print("\nSwarm, in-place, 3 transformers in parallel:")
# Core time: 2000kg * 648 min/kg / 200 eff spiders *1.25 = ?
t_core = 2000*648/200*1.25/60
print(f"  Core: {t_core:.1f}h per transformer (200 eff spiders)")
# Windings: 1000kg * 20 min/kg = 20,000 min single, /4 spiders = 5,000 min = 83.3h, NO swarm scaling beyond 4
t_wind = 1000*20/4/60
print(f"  Windings: {t_wind:.1f}h per transformer (ONLY 4 spiders can wind at once - serial bottleneck)")
t_tank = (1200+400+200)*400/200*1.25/60
print(f"  Tank+rad: {t_tank:.1f}h per transformer (200 eff spiders)")
# Sequential per transformer: core -> windings -> tank (cannot tank before windings are in)
t_per_transformer = t_core + t_wind + t_tank
print(f"  Per transformer sequential: {t_per_transformer:.1f}h")
print(f"  3 transformers in parallel (different spiders): {t_per_transformer:.1f}h total for all 3")
print(f"  + supplied parts placement (bushings, tap, oil fill): 2h, + test 4h = {t_per_transformer+6:.1f}h")

# --- Compare to v9 supplied transformers ---
print("\nCompare:")
print("  v9 supplied: transformers placed in 2.0h, 100x L spiders lift 5t each, total station 122.0h")
print(f"  v10 in-place: transformers built in {t_per_transformer+6:.1f}h, total station = fab 120h (steel gantry etc, parallel) + transformers {t_per_transformer+6:.1f}h")
# Fab (gantry etc) and transformers can run in parallel (different zones), so total = max(fab, transformers) + test?
# Fab 120h, transformers ~? t_per_transformer = ?
total_v10 = max(120, t_per_transformer+6) + 4  # +4h final commissioning
print(f"  v10 total station: ~{total_v10:.1f}h = {total_v10/24:.1f} days (vs v9 5.1 days)")
print(f"  Difference: +{total_v10-122:.1f}h, +{(total_v10-122)/122*100:.0f}% slower, BUT no 5t lifts, no transformer delivery trucks, no crane.")

# --- What in-place buys you ---
print("\nWhat in-place buys you:")
print("  - No crane, no 5t lift, no transformer truck. Spiders start at the mounting joints and grow the transformer outward.")
print("  - No size limit: a transformer bigger than a spider can lift is still buildable, because it is never lifted.")
print("  - Repair: a failed winding can be rebuilt in place, without removing the transformer.")
print("\nWhat it costs you:")
print(f"  - Windings are SERIAL: only 4 spiders per transformer can wind at once. That is {t_wind:.1f}h you cannot parallelise away, no matter how many spiders you have.")
print("  - Core laminations need <0.05mm gaps. S-spiders must do it, M/L are too coarse.")
print("  - Oil, bushings, tap changer still supplied. Spiders cannot make insulating oil from powder.")
print("  - Total feedstock: +15,000kg spider-made (core+windings+tank), total station feedstock 11,500 + 15,000 = 26,500kg, +1 more bulk truck.")

with open("results10.json","w") as f:
    json.dump({"t_per_transformer_h":t_per_transformer,"total_v10_h":total_v10},f,indent=2)
