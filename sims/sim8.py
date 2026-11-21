"""
Spider matter-compiler v8 - PRINTED ENGINE, MODELLED ESTIMATE.
v7 had the engine SUPPLIED (65kg bought). This run prints it.

Engine: 998cc inline-4, modelled as spider-made:
 - Block + head: Al powder, 28 kg
 - Cylinder liners / piston sleeves: steel, 6 kg (hard, wear-resistant, thin wall)
 - Pistons: Al, 2 kg (4x 500g)
 - Crankshaft + con-rods: steel, 8 kg (high strength, needs forging-grade density - hardest part)
 - Valves / camshafts: steel, 4 kg
 - Bearings: NOT ball bearings. Plain journal bearings, steel shell + grease feed.
   Grease is a SWAP, not powder: grease cartridge in tail, dispensed into bearing journals.
   No balls, no races - just a steel sleeve, a shaft, and a grease film.
 - Gaskets / seals: plastic / rubber analogue, 1 kg
 - Total printed engine: ~49 kg, plus 16 kg still supplied (spark plugs, injectors, ECU, clutch plates, etc.)
   -> Engine is now 75% spider-made, 25% supplied precision parts.

Physics / precision notes (modelled, not hand-waved):
 - Al block: metal ultrasonic 30 mm/s, 60% infill, hollow water jackets.
 - Steel liners / crank: 20 mm/s (steel is slower, higher power, 80W sonotrode), 100% dense (no infill - must be solid for strength / wear).
 - Surface finish: ultrasonic laying gives ~0.1mm roughness. Cylinder bores need <0.01mm + honing.
   Spiders must do a SECOND pass: a polishing / honing tail, 0.05mm removal, at 10 mm/s.
   That is modelled as +40% time on liners + crank journals.
 - Grease bearings: plain journal, clearance 0.02-0.05mm, grease film supports load at low-mid RPM.
   At 10,000+ RPM a grease plain bearing will overheat / wipe. Model caps printed engine at 7,000 RPM, ~120 hp (vs 200 hp stock).
   That is the trade-off for no ball bearings.
"""
import math, json

# --- Printed engine parts ---
parts = [
    # name, material, mass_kg, density, infill, speed_mms, area_mm2, honing?
    ("Block + head", "Al", 28, 2.7, 0.60, 30, 0.5, False),
    ("Cylinder liners", "steel", 6, 7.8, 1.00, 20, 0.3, True),
    ("Pistons x4", "Al", 2, 2.7, 0.80, 30, 0.4, False),
    ("Crankshaft + rods", "steel", 8, 7.8, 1.00, 20, 0.4, True),
    ("Valves + cams", "steel", 4, 7.8, 1.00, 20, 0.3, True),
    ("Gaskets/seals", "plastic", 1, 1.24, 0.80, 80, 0.4, False),
]
total_made = 0
total_time_single_min = 0
print("Printed engine parts (single spider):")
for name, mat, mass, dens, infill, speed, area, hone in parts:
    vol_mm3 = mass*1000/dens*1000  # kg->g / density -> cm3 -> mm3 ; mass*1000 g / dens = cm3, *1000 = mm3
    # correct: mass kg = mass*1000 g, /dens g/cm3 = cm3, *1000 = mm3
    vol_mm3 = mass*1000/dens*1000
    t = vol_mm3*infill/area/speed/60*1.3
    if hone:
        t *= 1.4  # honing / polishing pass
        print(f"  {name}: {mass}kg {mat}, {vol_mm3/1000:.0f}cm3, {t:.0f} min (incl. honing +40%)")
    else:
        print(f"  {name}: {mass}kg {mat}, {vol_mm3/1000:.0f}cm3, {t:.0f} min")
    total_made += mass
    total_time_single_min += t

print(f"\nPrinted engine: {total_made} kg spider-made, {total_time_single_min:.0f} min single = {total_time_single_min/60:.1f} h")
print(f"  Grease bearings: grease cartridge swap, not powder. 1 cartridge per engine, ~200g grease.")
print(f"  Grease feed: tail segment swap to grease dispenser, 30s swap, dispense 0.5g per journal x 9 journals = 4.5g total.")

# --- Full bike, printed engine version ---
# v7 spider-made (non-engine): frame etc 35kg, 8,910 min single. Add printed engine.
t_bike_nonengine_single = 8910
t_total_single = t_bike_nonengine_single + total_time_single_min
print(f"\nFull bike, printed engine, single spider: {t_total_single:.0f} min = {t_total_single/60:.1f} h (vs 151.6 h with supplied engine)")
# Placement now: no 45-min engine lift (engine is built in place, in the frame), 
# instead: supplied precision parts placement: plugs, injectors, ECU, clutch, etc. ~60 min single team
t_place_printed = 60
print(f"Placement (supplied precision parts only): {t_place_printed} min, vs 170 min with supplied engine")

for n in [1, 10, 100]:
    overhead = 1.0 if n==1 else 1.15 if n==10 else 1.25
    t_made = t_total_single/n*overhead
    t_place = max(30, t_place_printed/max(1,n//2)*1.1) if n>1 else t_place_printed
    if n==100:
        t_place = 30  # floor: final assembly / torque check cannot be split below 30 min
    total = t_made + t_place
    print(f"Swarm x{n}: made {t_made:.1f} min + placed {t_place:.1f} min = {total:.1f} min ({total/60:.2f} h)")

# --- Performance trade-off ---
print("\nPerformance trade-off, printed engine vs stock:")
print("  Stock R1 engine: 200 hp @ 13,500 RPM, ball bearings, forged crank, Nikasil liners")
print("  Printed engine: ~120 hp @ 7,000 RPM (model cap), grease plain bearings, ultrasonic steel crank")
print("  Why the cap? Grease film in a plain journal bearing overheats above ~7k RPM, and")
print("  ultrasonic-printed steel is not forged - fatigue life is lower, so you derate it.")
print("  You gain: no bought engine, no supply chain, blueprint-only build.")
print("  You lose: ~40% power, top speed, and long-term durability. It is a working engine, not a race engine.")

# --- Fleet 10, printed engine ---
t_made_100 = t_total_single/100*1.25
t_place_100 = 30
pipeline_h = (t_made_100+t_place_100 + 9*t_made_100)/60
print(f"\nFleet 10 bikes, printed engine, 100 spiders, pipelined: {pipeline_h:.1f} h")
print(f"  Per bike: {(t_made_100+t_place_100)/60:.2f} h, steady-state {60/t_made_100:.2f} bikes/hour")
print(f"  Feedstock per bike: 35kg (frame etc) + 49kg (engine) = 84 kg, 10 bikes = 840 kg")
print(f"  Spider-made share: 84kg / 200kg = 42% (vs 17.5% with supplied engine)")

with open("results8.json","w") as f:
    json.dump({"printed_engine_kg":total_made,"bike_100_min":t_made_100+t_place_100},f,indent=2)
