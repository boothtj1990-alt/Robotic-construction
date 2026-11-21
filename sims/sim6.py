"""
Spider matter-compiler v6 - FLEET: 10x Optimus, MODELLED ESTIMATE.
100 spiders, reused across all 10 robots, with battery swaps + feedstock refills
scheduled in, pipeline / steady-state throughput.

From v5, per Optimus (100-spider swarm):
 - Spider-made: 106.7 min, Placement: 17.2 min, Total: 123.8 min = 2.06 h
 - Feedstock spider-made: 33 kg (22 Al + 8 plastic + 3 Cu)
 - Supplied parts: 26 kg (40 actuators, battery cells, compute, sensors, hands)
 - Energy per robot (100 spiders): ~7 kWh spider work

Fleet assumptions:
 - 100 spiders total, split: 70 fab (frame/housing/wiring), 30 assembly (placers/solderers)
 - Work is PIPELINED: while Robot N is in assembly, Robot N+1 is already in fab.
   Fab is the bottleneck (106.7 min), assembly is 17.2 min, so pipeline cycle = fab time.
 - Battery: 100Wh pack, avg draw 70W fab / 45W assembly -> runtime ~1.4h fab, ~2.2h assembly.
   A fab spider needs ~1 battery swap per robot. Swap: 20s station + 30s walk = 0.8 min, staggered,
   so no swarm-wide stop - modelled as 5% downtime.
 - Feedstock refills: 15g hopper, 33,000g / 15g = 2,200 refills per robot (Al+plastic+Cu, incl. waste 10%)
   Refill: 30s dock + 30s travel = 1.0 min spider-time per refill.
   BUT: 5 bulk feed stations on the floor, spiders queue. Refill spider-time is the bottleneck
   if done one-by-one. Solution in sim: spiders refill in batches at stations while other spiders
   keep laying - refill time is NOT added to build time if <20% of spiders are refilling at once.
   Modelled as: refill overhead = 15% extra on fab time.
 - Supplied parts: actuators etc. arrive pre-staged, no fab time, placement only.
 - Calibration / test: each finished Optimus needs 30 min self-test / walk calibration before it counts as done.
   That is done by the robot itself, not spiders, so it does NOT block the swarm (parallel).
"""
import math, json

robots = 10
swarm = 100
per_robot_fab_min = 106.7
per_robot_place_min = 17.2
per_robot_total_min = per_robot_fab_min + per_robot_place_min

# --- Sequential (no pipeline): 10 x 2.06h ---
seq_h = robots * per_robot_total_min / 60
print(f"Sequential, no pipeline: {robots} x {per_robot_total_min:.0f} min = {seq_h:.1f} h")

# --- Pipelined: fab bottleneck, assembly overlaps next fab ---
# First robot: fab + place = 123.8 min. Each next robot: + fab time only (assembly overlaps)
pipeline_h = (per_robot_total_min + (robots-1)*per_robot_fab_min) / 60
print(f"Pipelined (fab bottleneck): first {per_robot_total_min:.0f} min + {robots-1} x {per_robot_fab_min:.0f} min = {pipeline_h:.1f} h")
print(f"  Throughput steady-state: 1 Optimus per {per_robot_fab_min:.0f} min = {60/per_robot_fab_min:.56f} per hour".replace("0.56",""))
print(f"  Throughput steady-state: 1 Optimus per {per_robot_fab_min:.0f} min = {60/per_robot_fab_min:.2f} per hour")

# --- Add downtime: battery swaps + refills ---
# Battery: fab spiders 70, each needs 1 swap per robot (1.4h runtime vs 1.78h fab)
# 70 swaps x 0.8 min = 56 spider-min per robot, /100 spiders = 0.56 min wall-clock if staggered, 
# but station queue: 2 charging stations, 20s swap each -> 70*0.33 min /2 stations = 11.7 min queue?
# Model conservatively: battery downtime = 5% of fab time.
# Refills: 15% overhead on fab (see header).
downtime_factor = 1.05 * 1.15  # battery 5% + refill 15%
pipeline_real_h = (per_robot_total_min + (robots-1)*per_robot_fab_min*downtime_factor) / 60
# first robot also has downtime
pipeline_real_h = ((per_robot_total_min*downtime_factor) + (robots-1)*per_robot_fab_min*downtime_factor) / 60
print(f"\nWith downtime (battery 5% + refill 15%): {pipeline_real_h:.1f} h for {robots} robots")
print(f"  Effective cycle: {per_robot_fab_min*downtime_factor:.0f} min per robot, {60/(per_robot_fab_min*downtime_factor):.2f} robots/hour steady-state")
print(f"  First robot out: {per_robot_total_min*downtime_factor/60:.1f} h, last robot out: {pipeline_real_h:.1f} h")

# --- Feedstock totals ---
print(f"\nFeedstock for {robots} robots:")
print(f"  Al powder: {22*robots} kg, Plastic: {8*robots} kg, Cu: {3*robots} kg, Total spider-made: {33*robots} kg")
print(f"  Supplied parts: {26*robots} kg - 400 actuators, 10 battery packs, 10 compute units, 10 hand sets")
print(f"  Hopper refills: {33000*robots/15:,.0f} refills total, {33000/15:,.0f} per robot")
print(f"  Bulk feed stations needed: 5, each dispensing ~{33*robots/5:.0f} kg over the run")

# --- Energy ---
energy_per_robot_kwh = 7.0
total_kwh = energy_per_robot_kwh * robots
print(f"\nEnergy: {energy_per_robot_kwh} kWh per robot (spiders), {total_kwh} kWh total for fleet")
print(f"  Charging: 7kW home station recharges 100 spiders in ~1h, fleet needs {total_kwh/7:.1f} h of charging total (staggered, parallel with work)")
print(f"  At $0.15/kWh, energy cost per Optimus: ${energy_per_robot_kwh*0.15:.2f} - negligible vs parts")

# --- Spider utilisation ---
fab_util = per_robot_fab_min / (per_robot_fab_min*downtime_factor)
print(f"\nSpider utilisation: fab spiders ~{fab_util*100:.0f}% laying, rest swapping/refilling")
print(f"  Assembly spiders (30): only busy {per_robot_place_min/per_robot_fab_min*100:.0f}% of cycle time - they idle / help fab / do calibration assist the rest.")
print(f"  -> Rebalance: 85 fab / 15 assembly would be better. Assembly is NOT the bottleneck.")

# --- Cost / payback ---
spider_cost = 2000
fleet_cost = swarm * spider_cost
optimus_target = 25000
print(f"\nCost: {swarm} spiders @ ${spider_cost:,} = ${fleet_cost:,}")
print(f"  Optimus target $25k each, fleet of 10 = $250,000 retail value")
print(f"  Swarm cost alone = 80% of fleet retail value, BEFORE parts, feedstock, power, space.")
print(f"  Break-even vs buying 10 Optimus: need to build ~{fleet_cost/optimus_target:.0f} Optimus just to cover spider cost, ignoring parts.")
print(f"  At steady-state {60/(per_robot_fab_min*downtime_factor):.2f}/hour, that is {fleet_cost/optimus_target / (60/(per_robot_fab_min*downtime_factor)):.1f} hours of production to break even on spiders alone.")
print(f"  -> Fleet of 10 does NOT pay for itself. Fleet of 50-100, or a remote base with no alternative, does.")

# --- What actually limits throughput? ---
print("\nThroughput limit, in order:")
print(" 1. Fab time (Al frame) - 107 min per robot, 70% of total. Faster metal laying = faster fleet.")
print(" 2. Feedstock refills - 2,200 refills/robot, 15% overhead even with 5 bulk stations.")
print(" 3. Battery swaps - 5%, staggered, manageable.")
print(" 4. Assembly - 17 min, NOT a limit, assembly spiders idle most of the cycle.")
print(" 5. Calibration - 30 min/robot, parallel, does not block swarm, but delays first usable robot by 30 min.")

with open("results6.json","w") as f:
    json.dump({"robots":robots,"pipeline_h":pipeline_h,"pipeline_real_h":pipeline_real_h,"throughput_per_hour":60/(per_robot_fab_min*downtime_factor),"total_kwh":total_kwh},f,indent=2)
