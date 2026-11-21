"""
Spider matter-compiler v9 - POWER RELAY STATION, 2000 SPIDERS, TRAILER DEPLOYED.
MODELLED ESTIMATE, not a physical test.

Job: small distribution substation / power relay station, 30m x 20m yard.
 - Concrete pad + footings: SUPPLIED (truck-poured, spiders cannot make 400+ tonnes of concrete from powder)
 - Steel gantry / busbar supports: spider-made, structural steel
 - Control house: spider-made walls/roof (plastic/composite + steel frame), 6m x 4m x 3m
 - Busbars / cable: copper, spider-laid
 - Fencing + gates: steel, spider-made
 - Transformers, breakers, switchgear: SUPPLIED, placed by heavy teams
 - Gravel / grounding grid: supplied bulk, spiders spread / place

Swarm: 2000 spiders, size variance (like real spiders - different sizes for different jobs):
 - S - micro, 0.2 kg, 500 spiders: wiring, connectors, control panel internals, precision
 - M - medium, 1.0 kg, 1200 spiders: general fab - walls, fencing, busbar supports, cable
 - L - large, 10 kg, 300 spiders: heavy lift, steel gantry, transformer placement, concrete formwork
 Total swarm mass: 500*0.2 + 1200*1 + 300*10 = 4,300 kg
 Trailer: 53ft semi, payload ~20,000 kg. Spiders 4,300kg + feedstock + stations + batteries fits in 1 trailer?
  Feedstock spider-made: see below ~18,000 kg - NO, feedstock does NOT fit in 1 trailer.
  -> Trailer carries spiders + stations + 1 day feedstock, bulk feedstock arrives by separate truck(s).

Segment replacers: tool stations on trailer, spiders swap tails in 30s.
 - M spiders carry 2-3 tails each (plastic, steel, copper)
 - S spiders: micro-solder / wire tail only
 - L spiders: heavy steel / lifting tail

Materials - best form per material (from sims 2-8):
 - Steel frame: POWDER (bulk, 8,000 kg) - metal ultrasonic, 30 mm/s
 - Plastic/composite walls: POWDER (2,000 kg)
 - Copper busbar/cable: SPOOL wire (1,500 kg) - powder copper rejected, oxidises
 - Grease / sealant: CARTRIDGE swap
 - Concrete: SUPPLIED, truck
"""
import math, json

# --- Station scope ---
print("Power relay station: 30m x 20m yard, 6x4m control house")
print("Swarm: 2000 spiders - 500x S (0.2kg), 1200x M (1kg), 300x L (10kg), total 4,300 kg")

# Spider-made work
# Steel gantry: lattice, ~8,000 kg steel, but hollow lattice = 40% solid volume
# Use mass directly: laying rate for steel (from sim8): 20-30 mm/s, line 0.5mm2, density 7.8
# Energy / time per kg steel: approx from sim8: 6kg liners took 3,889 min single at 20mm/s, 0.3mm2
# -> ~648 min/kg single spider. That is the rate used here.
steel_kg = 8000
plastic_kg = 2000
copper_kg = 1500
print(f"\nSpider-made: steel {steel_kg}kg, plastic {plastic_kg}kg, copper {copper_kg}kg = {steel_kg+plastic_kg+copper_kg:,}kg")
print(f"Supplied: concrete ~432,000kg, transformers 3x 5,000kg, breakers/switchgear 2,000kg, gravel 50,000kg")

# Rates (single-spider minutes per kg, from sims 5-8, scaled)
# Steel: 648 min/kg (20mm/s, dense), Plastic: ~200 min/kg (80mm/s, 40% infill), Copper wire: ~20 min/kg (60mm/s, thin wire, long runs)
rate_steel = 648
rate_plastic = 200
rate_copper = 20
t_steel_single = steel_kg * rate_steel
t_plastic_single = plastic_kg * rate_plastic
t_copper_single = copper_kg * rate_copper
print(f"\nSingle-spider times: steel {t_steel_single/60:,.0f}h, plastic {t_plastic_single/60:,.0f}h, copper {t_copper_single/60:,.0f}h")
print(f"  Total single: {(t_steel_single+t_plastic_single+t_copper_single)/60:,.0f}h = {(t_steel_single+t_plastic_single+t_copper_single)/60/24:.1f} days")

# --- Swarm, by size class ---
# Steel: L spiders (300) do heavy steel, M help (1200, slower at steel - 50% rate)
# Plastic: M spiders (1200)
# Copper: S spiders (500) + M help
# Effective spider count per material (weighted):
eff_steel = 300 + 1200*0.5
eff_plastic = 1200
eff_copper = 500 + 1200*0.3
for label, t_single, eff in [("steel",t_steel_single,eff_steel),("plastic",t_plastic_single,eff_plastic),("copper",t_copper_single,eff_copper)]:
    t = t_single/eff*1.25/60
    print(f"{label}: effective spiders {eff:.0f}, swarm time {t:.1f}h")

t_steel_swarm = t_steel_single/eff_steel*1.25/60
t_plastic_swarm = t_plastic_single/eff_plastic*1.25/60
t_copper_swarm = t_copper_single/eff_copper*1.25/60
# These run in parallel (different zones), so total fab = max, not sum, plus placement
t_fab = max(t_steel_swarm, t_plastic_swarm, t_copper_swarm)
print(f"\nFab (parallel, bottleneck = steel): {t_fab:.1f}h")

# Placement: transformers 3x, each needs 100x L spiders, 2h per transformer (lift, align, bolt, connect)
# Breakers/switchgear: 20 units, 10x M spiders each, 1h each, parallel
t_transformers = 2.0  # 3 in parallel, 100 L each, 300 L total - fits
t_breakers = 20*1.0 / 10  # 10 teams in parallel? model: 20 units / 10 teams = 2h
t_place = max(t_transformers, t_breakers)
print(f"Placement: transformers {t_transformers}h, breakers {t_breakers}h, bottleneck {t_place}h")

# Concrete: supplied, pour + cure. Spiders do formwork (in steel time), concrete cures 24-48h - THAT is the real wait.
# Model: concrete pour day 0, cure 24h before spiders can load it, but spiders can build gantry/control house on footings in parallel.
print(f"\nConcrete cure: 24h, parallel with fab - does NOT add to total if fab >24h, which it is.")

total_h = t_fab + t_place
print(f"\nTOTAL (2000 spiders): fab {t_fab:.1f}h + placement {t_place:.1f}h = {total_h:.1f}h = {total_h/24:.1f} days")
print(f"  First usable power: after placement + testing, +4h test/commissioning = {total_h+4:.1f}h")

# --- Trailer / logistics ---
print(f"\nTrailer deployment:")
print(f"  Spiders: 4,300 kg, 2,000 units - fits in 1x 53ft trailer (20t payload)")
print(f"  Segment replacers / tool stations: 10 stations, 500 kg, on trailer")
print(f"  Charging stations: 20x 7kW, 1,000 kg, on trailer + generator / grid hookup")
print(f"  Feedstock day-1: steel powder 2,000kg, plastic 500kg, copper spool 500kg = 3,000 kg")
print(f"  Trailer total: ~8,800 kg - fits, 1 trailer for spiders + stations + day-1 feed")
print(f"  Bulk feedstock: {steel_kg+plastic_kg+copper_kg:,} kg total, needs {math.ceil((steel_kg+plastic_kg+copper_kg)/20000)} additional bulk truck(s) over the build")
print(f"  Battery swaps: L spiders 10kg, 200Wh pack, 2h runtime at heavy work -> ~{total_h/2:.0f} swaps per L spider over build, staggered")
print(f"  S spiders: 50Wh pack, 4h runtime, ~{total_h/4:.0f} swaps each")

# --- Energy ---
# Avg power: L 150W, M 60W, S 20W, weighted avg = (300*150+1200*60+500*20)/2000 = 63.5W
avg_w = (300*150+1200*60+500*20)/2000
total_kwh = avg_w*2000*total_h/1000
print(f"\nEnergy: avg {avg_w:.0f}W/spider x 2000 x {total_h:.1f}h = {total_kwh:,.0f} kWh")
print(f"  At $0.15/kWh: ${total_kwh*0.15:,.0f} - again negligible vs materials / transformers")

# --- Size variance benefit ---
print("\nSize variance - what it buys you:")
print("  S (500): can get inside control panels, wire 0.2mm traces, work in cable trenches. M/L cannot fit.")
print("  M (1200): the bulk workforce, walls, fencing, busbars. Best power/weight.")
print("  L (300): lift transformers (5t each, 100x L = 50kg lift each), steel gantry, formwork.")
print("  Without variance: 2000x M spiders could NOT lift a transformer, and could NOT wire a panel.")
print("  With variance: each size does the job it fits, no spider is wasted on a job too big/small for it.")

with open("results9.json","w") as f:
    json.dump({"total_h":total_h,"feedstock_kg":steel_kg+plastic_kg+copper_kg,"energy_kwh":total_kwh},f,indent=2)
