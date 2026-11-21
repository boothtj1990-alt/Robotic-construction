"""
Spider matter-compiler v5 - BUILDING AN OPTIMUS-CLASS HUMANOID, MODELLED ESTIMATE.
Not a physical test. Uses published Optimus Gen 2 / Gen 3 specs where available,
and spider rates from sims 2-4.

Optimus (Tesla, public specs):
 - Height ~1.73 m, weight ~57-73 kg (Gen2 ~57kg, Gen3 heavier with more actuators)
 - 40 electromechanical actuators (Gen2), hands 11 DOF each, 22 DOF hands total
 - Walks ~8 km/h (5 mph), carries 20 kg, battery 2.3 kWh, ~40-60 kg payload? 
 - Actuators, battery cells, compute (AI chip), cameras, sensors are PRECISION parts.
   Spiders CANNOT make a brushless motor, a Li-ion cell, or a GPU from powder.
   Those are SUPPLIED components, placed like PCB parts in sim4.
   Spiders CAN make: frame, housings, brackets, wiring looms, covers, joints shells.

Mass breakdown (modelled, ~60 kg total):
 - Structural frame / skeleton (Al alloy, steel joints): 22 kg
 - Housings / covers (plastic): 8 kg
 - Wiring / copper looms: 3 kg
 - Actuators (supplied, 40x): 15 kg (~375g each)
 - Hands / fingers (supplied actuators + spider-made shells): 3 kg
 - Battery pack (supplied cells + spider-made casing): 6 kg (2.3 kWh)
 - Compute / sensors / cameras (supplied): 2 kg
 - Fasteners / misc: 1 kg
"""
import math, json

# --- What spiders make vs place ---
spider_made_kg = 22 + 8 + 3 + 1  # frame + housings + wiring + fasteners (approx, wiring is copper laid)
# frame is Al, not plastic - use metal ultrasonic / laser? In sim, Al frame via powder + ultrasonic metal
# Al density 2.7, plastic 1.24, copper 8.96
frame_vol_cm3 = 22000/2.7
housing_vol_cm3 = 8000/1.24
wiring_vol_cm3 = 3000/8.96
print(f"Spider-made: frame {frame_vol_cm3/1000:.1f} L Al, housings {housing_vol_cm3/1000:.1f} L plastic, wiring {wiring_vol_cm3:.0f} cm3 Cu")
print(f"Spider-made mass: {spider_made_kg} kg / 60 kg total ({spider_made_kg/60*100:.0f}%)")
print(f"Supplied / placed: actuators, battery cells, compute, sensors = {60-spider_made_kg} kg ({(60-spider_made_kg)/60*100:.0f}%)")
print("  -> Spiders do NOT build a robot from ground up. They build the BODY, and ASSEMBLE the bought parts into it.")

# --- Spider-made build rates (from sim2/3) ---
# Plastic housings: 1.0x0.4mm line, 80 mm/s, web infill 60% (structural, not 20%)
# Al frame: metal ultrasonic, slower - 30 mm/s, 1.0x0.5mm line, 50% infill (load bearing)
# Copper wiring: 0.2mm wire, 60 mm/s, total loom length ~80 m (all limbs, torso, head)
def build_time_min(vol_mm3, line_area_mm2, speed_mms, overhead=1.3):
    return vol_mm3/line_area_mm2/speed_mms/60*overhead

housing_vol = housing_vol_cm3*1000*0.6  # 60% web infill, structural
frame_vol = frame_vol_cm3*1000*0.5      # 50% infill, load bearing, hollow tubes
t_housing = build_time_min(housing_vol, 0.4, 80)
t_frame = build_time_min(frame_vol, 0.5, 30)
t_wiring = 80*1000/60/60*1.3  # 80m copper loom at 60mm/s
print(f"\nSpider-made times (single spider, sequential):")
print(f"  Housings (plastic): {t_housing:.0f} min")
print(f"  Frame (Al, metal ultrasonic): {t_frame:.0f} min")
print(f"  Wiring looms (Cu): {t_wiring:.0f} min")
print(f"  Total spider-made, single: {t_housing+t_frame+t_wiring:.0f} min = {(t_housing+t_frame+t_wiring)/60:.1f} h")

# --- Placement: 40 actuators + battery + compute + sensors ---
# Actuator placement: large, heavy, alignment critical, 2 spiders per actuator (lift + bolt)
# 40 actuators x 5 min each (place + fasten, 2-spider team) = 200 min, but parallel teams
# Battery: 1 pack, 10 min. Compute/sensors: 20 units x 2 min = 40 min.
place_min_single_team = 40*5 + 10 + 40
print(f"\nPlacement (supplied parts), single 2-spider team sequential: {place_min_single_team:.0f} min = {place_min_single_team/60:.1f} h")

# --- Swarm scaling ---
# Swarm sizes: 10, 100, 1000 spiders. Split by subsystem, coordination overhead grows.
# Frame/housings/wiring can be split by body part (torso, 2 arms, 2 legs, head = 6 zones)
# Placement can be split by zone too, but actuators need 2 spiders each.
for n in [1, 10, 100, 1000]:
    # spider-made: split across n, overhead 1 + 0.02*(zones) capped
    overhead = 1.15 if n>=10 else 1.0
    if n>=100: overhead = 1.25
    if n>=1000: overhead = 1.40
    t_made = (t_housing+t_frame+t_wiring)/n*overhead
    # placement: max parallel teams = n//2, each team 5 min/actuator, 40 actuators
    teams = max(1, n//2)
    t_place = (40*5/teams + 10 + 40/max(1,teams//2)) * 1.1
    total = t_made + t_place
    print(f"Swarm x{n}: made {t_made:.1f} min + placed {t_place:.1f} min = {total:.1f} min ({total/60:.2f} h)")

# --- Energy / feedstock ---
# Al frame powder: 22kg Al powder, plastic 8kg, copper 3kg = 33kg feedstock
# Battery: spiders need charging. Total spider energy: made parts ~?
# Rough: Al metal ultrasonic 60W, plastic 25W, walk 30W. Average 70W per spider while working.
# For 100-spider swarm, 1h build: 100*70W*1h = 7 kWh. Charging station: home 240V / 7kW = 1h to recharge all.
print(f"\nFeedstock: 33 kg spider-made material (22 Al + 8 plastic + 3 Cu) + 26 kg supplied parts + 1 kg fasteners")
print(f"  A 100-spider swarm building in ~1h uses ~7 kWh - one home charging station (7kW) recharges it in ~1h")
print(f"  Powder hoppers: Al powder 22kg / 15g per spider = 1,467 refills - spiders MUST refill at station, cannot carry it all.")
print(f"  -> Feedstock logistics, not laying speed, is the real bottleneck at Optimus scale.")

# --- Cost sanity ---
# If a spider costs $2,000 (drone-class + ultrasonic tail), 100 spiders = $200,000
# Optimus target price $20-30k at scale, current build ~$50-100k
# Swarm must build >7-10 Optimus to pay for itself vs buying one, ignoring labour / time saved.
print(f"\nCost sanity: 100 spiders @ $2,000 = $200,000. Optimus target $20-30k.")
print(f"  Swarm pays for itself after ~7-10 Optimus builds, IF it replaces a factory line.")
print(f"  For ONE Optimus, a swarm is wildly uneconomic. For a FLEET / remote base, it makes sense.")

# --- What breaks first at Optimus scale? ---
print("\nWhat breaks first, in order:")
print(" 1. Precision: actuator mounts need <0.05mm alignment. Spider walking accuracy is ~0.1-0.5mm. Needs vision + fine-adjust, not just walking.")
print(" 2. Feedstock logistics: 33kg of powder, 1,467 hopper refills at 15g each. Needs bulk feed stations, not onboard hoppers.")
print(" 3. Metal frame: Al ultrasonic at 30mm/s is slow. 22kg Al frame is ~70% of spider-made time.")
print(" 4. Hands: 22 DOF, tiny tendons, 0.5mm parts - below spider placement accuracy. Needs a dedicated micro-spider, or supplied pre-assembled hands.")
print(" 5. Calibration: after assembly, the robot needs to learn its own body - joint offsets, tendon tension. Spiders build it, software still has to teach it to walk.")

with open("results5.json","w") as f:
    json.dump({"spider_made_kg":spider_made_kg,"single_h":(t_housing+t_frame+t_wiring+place_min_single_team)/60},f,indent=2)
