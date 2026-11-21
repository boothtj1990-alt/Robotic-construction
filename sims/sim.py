"""
Spider matter-compiler simulation - MODELLED ESTIMATE, not a physical test.
Bead-by-bead plastic figurine, ultrasonic (sound-only) bonding, no melt pool.
Parameters grounded in ultrasonic plastic welding literature:
 - 20-35 kHz typical, amplitude 10-100 um, weld cycle 0.1-0.5 s per spot
 - PLA: density 1.24 g/cm3, Cp ~1.8 J/gK, melt ~180C, ambient 25C
 - FDM comparison: 0.4mm nozzle, 0.2mm layers, 50 mm/s print speed
"""
import math, json

# --- Figurine: simple pawn-like solid, 40 mm tall, avg cross-section ---
height_mm = 40.0
avg_diameter_mm = 24.0
volume_mm3 = math.pi*(avg_diameter_mm/2)**2 * height_mm * 0.55  # 0.55 fill / shape factor
volume_cm3 = volume_mm3/1000
mass_g = volume_cm3 * 1.24
print(f"Figurine: {height_mm:.0f} mm tall, ~{volume_cm3:.1f} cm3, ~{mass_g:.1f} g PLA")

# --- Spider bead ---
bead_d_mm = 0.8      # extruded powder bead diameter
bead_h_mm = 0.4      # layer height per bead pass
bead_vol_mm3 = math.pi*(bead_d_mm/2)**2 * bead_h_mm
bead_mass_g = bead_vol_mm3/1000 * 1.24
n_beads = volume_mm3 / bead_vol_mm3
print(f"Bead: {bead_d_mm} mm dia x {bead_h_mm} mm, {bead_vol_mm3:.3f} mm3, {bead_mass_g*1000:.2f} mg each, {n_beads:,.0f} beads total")

# --- Ultrasonic bond per bead ---
# Energy to heat bead interface to melt: only ~30% of bead mass needs to reach melt at joint
freq_khz = 35
weld_time_s = 0.15   # per bead, within 0.1-0.5s literature range
power_w = 25         # small sonotrode, per-bead
energy_per_bead_J = power_w * weld_time_s
# thermal check: energy needed to raise interface mass (30%) 25->180C
heat_needed_J = bead_mass_g * 0.30 * 1.8 * (180-25)
print(f"Ultrasonic: {freq_khz} kHz, {weld_time_s}s/bead, {energy_per_bead_J:.2f} J/bead delivered, ~{heat_needed_J:.3f} J needed at interface -> margin {energy_per_bead_J/heat_needed_J:.1f}x (rest lost to conduction / vibration)")

# --- Spider movement (drone-like control) ---
move_speed_mm_s = 300  # 0.3 m/s, conservative for a legged bot placing precisely
# path length: beads laid in rows, average travel between beads ~ bead diameter + reposition
travel_per_bead_mm = bead_d_mm * 1.5
move_time_s = travel_per_bead_mm / move_speed_mm_s
deposit_time_s = 0.05  # dispense powder bead
cycle_per_bead_s = weld_time_s + move_time_s + deposit_time_s
total_time_s = n_beads * cycle_per_bead_s
print(f"Cycle/bead: weld {weld_time_s}s + move {move_time_s:.3f}s + deposit {deposit_time_s}s = {cycle_per_bead_s:.3f}s")
print(f"SPIDER TOTAL: {total_time_s/60:.1f} min ({total_time_s:.0f}s), {n_beads/total_time_s:.1f} beads/s")

# --- Swarm: N spiders, split volume, + coordination overhead ---
for n in [1, 10, 100]:
    overhead = 1 + 0.02*(n-1)  # collision avoidance / reporting, capped in model
    if n==100: overhead = 1.15
    t = total_time_s / n * overhead
    print(f"Swarm x{n}: {t/60:.2f} min (overhead {overhead:.2f}x)")

# --- FDM comparison ---
# FDM: same volume, 0.4mm line, 0.2mm layer, 50 mm/s, extrusion ~4 mm3/s
fdm_rate_mm3_s = 0.4*0.2*50
fdm_time_s = volume_mm3 / fdm_rate_mm3_s
print(f"FDM (0.4mm nozzle, 50mm/s): {fdm_rate_mm3_s:.1f} mm3/s, {fdm_time_s/60:.1f} min")
print(f"Spider vs FDM (single): {total_time_s/fdm_time_s:.2f}x slower" if total_time_s>fdm_time_s else f"Spider vs FDM (single): {fdm_time_s/total_time_s:.2f}x faster")

# --- What if bead is bigger / weld faster? sensitivity ---
for bd, wt in [(0.8,0.15),(1.5,0.10),(2.0,0.08),(0.8,0.05)]:
    bv = math.pi*(bd/2)**2 * bead_h_mm
    nb = volume_mm3 / bv
    ct = wt + (bd*1.5)/move_speed_mm_s + 0.05
    print(f"  bead {bd}mm, weld {wt}s -> {nb*ct/60:.1f} min single, {nb*ct/10/60:.2f} min x10 swarm")

# --- Energy total ---
total_energy_kwh = n_beads * energy_per_bead_J / 3.6e6
print(f"Total ultrasonic energy: {n_beads*energy_per_bead_J/1000:.1f} kJ = {total_energy_kwh:.4f} kWh (bonding only, not locomotion)")
print(f"Bond estimate: ultrasonic plastic welds typically 70-90% of parent strength; no melt pool, no layer-line weakness in Z if beads overlap 30%")

with open("results.json","w") as f:
    json.dump({"volume_cm3":volume_cm3,"mass_g":mass_g,"n_beads":n_beads,"single_min":total_time_s/60,"fdm_min":fdm_time_s/60,"swarm10_min":total_time_s/10*1.18/60,"energy_kJ":n_beads*energy_per_bead_J/1000},f,indent=2)
