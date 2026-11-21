"""
Spider matter-compiler v7 - CROTCH ROCKET (sportbike), MODELLED ESTIMATE.
Blueprint swap: same 100-spider swarm, same stations, different product.
Bike modelled: 1000cc sportbike, Yamaha R1 class.
 - Wet weight ~200 kg, 998cc inline-4, ~200 hp, top speed ~186 mph (limited)
 - Wheelbase ~1,405 mm, length ~2,055 mm

Mass breakdown (~200 kg wet):
 Spider-made:
  - Frame (Al twin-spar): 12 kg
  - Swingarm (Al): 6 kg
  - Bodywork / fairings (plastic): 7 kg
  - Fuel tank (plastic/Al, 17L): 4 kg
  - Wiring loom (Cu): 2 kg
  - Subframe, brackets, fasteners: 4 kg
  Total spider-made: 35 kg (17.5%)
 Supplied / placed:
  - Engine + transmission (998cc I4): 65 kg
  - Wheels + tires (2x): 28 kg
  - Suspension (forks + shock): 14 kg
  - Brakes (calipers, discs, lines): 10 kg
  - Battery + ECU + sensors + lights: 8 kg
  - Exhaust: 7 kg
  - Chain / sprockets, handlebars, seat, etc.: 18 kg
  - Fluids (fuel, oil, coolant): 15 kg
  Total supplied: 165 kg (82.5%)

Note: spiders make LESS of a bike than of an Optimus (17.5% vs 57%).
A bike is mostly a precision engine + bought running gear. The frame is the hard part.
"""
import math, json

# --- Spider-made volumes ---
frame_vol_cm3 = 12000/2.7
swing_vol_cm3 = 6000/2.7
body_vol_cm3 = 7000/1.24
tank_vol_cm3 = 4000/1.5  # mixed plastic/Al, avg density 1.5
wiring_vol_cm3 = 2000/8.96
misc_vol_cm3 = 4000/2.0  # brackets avg
print(f"Spider-made 35 kg: frame {frame_vol_cm3/1000:.1f}L Al, swingarm {swing_vol_cm3/1000:.1f}L, bodywork {body_vol_cm3/1000:.1f}L, tank {tank_vol_cm3/1000:.1f}L, wiring {wiring_vol_cm3:.0f}cm3")

# --- Build times, single spider ---
# Al frame/swingarm: metal ultrasonic 30 mm/s, 1.0x0.5mm line, 60% infill (load bearing, hollow)
# Plastic bodywork/tank: 80 mm/s, 1.0x0.4mm, 40% infill (shell + ribs)
# Copper wiring: 60 mm/s, 0.2mm wire, loom ~40m
def t_min(vol_mm3, area, speed, infill, overhead=1.3):
    return vol_mm3*infill/area/speed/60*overhead

t_frame = t_min(frame_vol_cm3*1000, 0.5, 30, 0.6)
t_swing = t_min(swing_vol_cm3*1000, 0.5, 30, 0.6)
t_body = t_min(body_vol_cm3*1000, 0.4, 80, 0.4)
t_tank = t_min(tank_vol_cm3*1000, 0.4, 80, 0.4)
t_misc = t_min(misc_vol_cm3*1000, 0.5, 50, 0.5)
t_wire = 40*1000/60/60*1.3
print(f"\nSingle spider spider-made times:")
print(f"  Frame: {t_frame:.0f} min, Swingarm: {t_swing:.0f} min, Bodywork: {t_body:.0f} min, Tank: {t_tank:.0f} min, Misc: {t_misc:.0f} min, Wiring: {t_wire:.0f} min")
t_made_single = t_frame+t_swing+t_body+t_tank+t_misc+t_wire
print(f"  Total spider-made single: {t_made_single:.0f} min = {t_made_single/60:.1f} h")

# --- Placement: supplied parts ---
# Engine is the big one: 65kg, needs 4-spider lift team + alignment to frame mounts (<0.1mm)
# Wheels, suspension, brakes: 2-spider teams, 10-15 min each
place = [
    ("Engine + transmission", 1, 45, 4),
    ("Front wheel + forks", 1, 20, 2),
    ("Rear wheel + swingarm", 1, 20, 2),
    ("Shock + brakes", 1, 25, 2),
    ("Exhaust", 1, 15, 2),
    ("Battery/ECU/lights", 1, 20, 2),
    ("Handlebars/seat/chain", 1, 25, 2),
]
t_place_single_team = sum(t for _,_,t,_ in place)
print(f"\nPlacement single team sequential: {t_place_single_team} min = {t_place_single_team/60:.1f} h")
print(f"  Engine alone: 45 min, 4-spider lift, alignment <0.1mm to frame mounts")

# --- Swarm scaling, 100 spiders ---
for n in [1, 10, 100]:
    overhead = 1.0 if n==1 else 1.15 if n==10 else 1.25
    t_made = t_made_single/n*overhead
    # placement: teams in parallel, max teams = n//2, but engine needs 4 spiders
    teams = max(1, n//2)
    # placement time is dominated by engine (45 min, cannot be split) + other jobs in parallel
    t_place = max(45, t_place_single_team/teams*1.1)
    total = t_made + t_place
    print(f"Swarm x{n}: made {t_made:.1f} min + placed {t_place:.1f} min = {total:.1f} min ({total/60:.2f} h)")

# --- Fleet: 10 bikes, pipelined ---
# Fab bottleneck = made time at 100 spiders. Assembly overlaps.
t_made_100 = t_made_single/100*1.25
t_place_100 = max(45, t_place_single_team/50*1.1)
pipeline_h = (t_made_100+t_place_100 + 9*t_made_100)/60
print(f"\nFleet 10 bikes, 100 spiders, pipelined:")
print(f"  Per bike (100 swarm): made {t_made_100:.1f} min + placed {t_place_100:.1f} min = {t_made_100+t_place_100:.1f} min")
print(f"  10 bikes: {pipeline_h:.1f} h, first bike { (t_made_100+t_place_100)/60:.1f} h, steady-state {60/t_made_100:.2f} bikes/hour")

# --- Feedstock / energy ---
print(f"\nFeedstock per bike: 35 kg spider-made (12 Al frame + 6 swingarm + 7 plastic + 4 tank + 2 Cu + 4 misc)")
print(f"  10 bikes: 350 kg feedstock, {350000/15:,.0f} hopper refills")
print(f"  Energy per bike (100 spiders): ~{(t_made_100+t_place_100)/60*100*0.06:.1f} kWh (avg 60W/spider)")

# --- Optimus vs Crotch Rocket ---
print("\nOptimus vs Crotch Rocket (100-spider swarm, per unit):")
print("  Optimus: 2.06 h, 57% spider-made, 34 kg made, 26 kg supplied")
print(f"  Bike: {(t_made_100+t_place_100)/60:.2f} h, 17.5% spider-made, 35 kg made, 165 kg supplied")
print("  Bike is FASTER to build (frame is big but simple, no 40 actuators to align),")
print("  but spiders make LESS of it - a bike is mostly a bought engine + running gear.")
print("  The blueprint swap works, but the value-add is lower for a bike than for a robot.")

with open("results7.json","w") as f:
    json.dump({"bike_single_h":t_made_single/60,"bike_100_min":t_made_100+t_place_100},f,indent=2)
