"""
Spider matter-compiler v2 - MODELLED ESTIMATE, not a physical test.
Anatomy copied from a real spider, robotics kept to current limits:
 - Head/cephalothorax = sensors + control only: stereo camera, lidar, CPU. No extruder up front.
 - Tail/abdomen = spinneret nozzle + ultrasonic sonotrode, harmonic aimed rearward.
   Bonding happens AS the line is laid, continuous, no stop-start per bead.
 - 8 legs, alternating tetrapod gait (4 legs on ground at a time), low centre of gravity.
 - Feedstock: plastic powder in abdominal hopper, extruded as a continuous filament line.
 - Web logic: spider does NOT fill solid. It lays a shell + sparse radial/spiral infill,
   like a web - strong geometry, far less material than a solid FDM print.
"""
import math, json

# --- Real spider / robot constraints ---
# Real spiders: dragline silk ~3-5 um dia, tensile ~1 GPa. Robot scale-up: filament line 0.8mm.
# Legged robots (current): precise placement while walking ~50-100 mm/s, not 300 mm/s.
# Fast legged sprint is 1+ m/s but accuracy collapses. We use 80 mm/s laying speed.
# Ultrasonic plastic welding: 20-35 kHz, continuous sonotrode, 25W, amplitude 10-50 um.
# PLA: density 1.24, Cp 1.8 J/gK, melt 180C

height_mm = 40.0
avg_dia_mm = 24.0
# solid volume earlier: pi*r^2*h*0.55 = 10.0 cm3
solid_vol_mm3 = math.pi*(avg_dia_mm/2)**2 * height_mm * 0.55

# Web-infill: shell 1.2mm thick + 20% infill (radial + spiral, like a web)
shell_vol_mm3 = math.pi*((avg_dia_mm/2)**2 - (avg_dia_mm/2-1.2)**2) * height_mm
infill_vol_mm3 = (math.pi*(avg_dia_mm/2-1.2)**2 * height_mm) * 0.20
web_vol_mm3 = shell_vol_mm3 + infill_vol_mm3
print(f"Solid volume: {solid_vol_mm3/1000:.1f} cm3  |  Web (shell+20% infill): {web_vol_mm3/1000:.1f} cm3  ({web_vol_mm3/solid_vol_mm3*100:.0f}% of solid)")
print(f"Web mass: {web_vol_mm3/1000*1.24:.1f} g PLA - fits in a ~15g abdominal hopper with margin")

# --- Tail nozzle: continuous line ---
line_w_mm = 0.8
line_h_mm = 0.4
line_area_mm2 = line_w_mm * line_h_mm
for label, vol in [("solid", solid_vol_mm3), ("web", web_vol_mm3)]:
    path_m = (vol / line_area_mm2) / 1000
    print(f"\n{label}: path length {path_m:.1f} m of 0.8x0.4mm line")

# --- Continuous ultrasonic bonding at tail ---
# Energy per mm of line: heat only the interface strip (~30% of line mass) to 180C
line_mass_per_mm_g = line_area_mm2 * 1 * 1.24 / 1000  # per mm length, mm3->cm3
heat_per_mm_J = line_mass_per_mm_g * 0.30 * 1.8 * (180-25)
print(f"\nHeat needed at interface: {heat_per_mm_J:.4f} J/mm of line")
# At 80 mm/s, power needed if 100% efficient:
for speed in [50, 80, 120]:
    p_needed = heat_per_mm_J * speed
    print(f"  at {speed} mm/s laying speed: {p_needed:.2f} W ideal, ~{p_needed/0.15:.1f} W at 15% ultrasonic coupling efficiency (typical)")
# Sonotrode is 25W, so check max speed at 15% efficiency:
max_speed = 25 * 0.15 / heat_per_mm_J
print(f"  25W sonotrode, 15% coupling -> max continuous laying speed {max_speed:.0f} mm/s before bond gets cold")

# --- Build time, continuous ---
for speed in [50, 80, 120]:
    for label, vol in [("solid", solid_vol_mm3), ("web", web_vol_mm3)]:
        path_mm = vol / line_area_mm2
        t_min = path_mm / speed / 60
        # overhead: layer change / climb / reposition, spider must walk around object, turn, re-aim tail
        # real spider: ~20% overhead for repositioning, plus 10% for hopper refill check / sensor pause
        t_min_total = t_min * 1.30
        print(f"Speed {speed} mm/s, {label}: pure lay {t_min:.1f} min, +30% spider overhead = {t_min_total:.1f} min")

# --- Legs / locomotion physics check ---
# 1 kg spider-bot (500g body + 200g hopper/feed + 300g battery/sonotrode), 8 legs
# Walking power for legged robots ~ 20-40W at 0.1 m/s. Battery 100 Wh (drone-class) 
robot_mass_kg = 1.0
walk_power_w = 30
sonotrode_w = 25
total_power_w = walk_power_w + sonotrode_w
battery_wh = 100
runtime_h = battery_wh / total_power_w
print(f"\nPower: walk {walk_power_w}W + sonotrode {sonotrode_w}W = {total_power_w}W, 100Wh battery -> {runtime_h:.1f}h runtime, {runtime_h*60:.0f} min")
print(f"  Web figurine at 80mm/s takes ~{(web_vol_mm3/line_area_mm2)/80/60*1.3:.1f} min, uses {(web_vol_mm3/line_area_mm2)/80/60*1.3/60*total_power_w:.1f} Wh - one charge does ~{runtime_h/((web_vol_mm3/line_area_mm2)/80/60*1.3/60):.0f} figurines")
# Stability: 8 legs, tetrapod gait, 4 legs always down, centre of gravity ~15mm high, base ~80mm wide
# tip-over angle approx atan(40/15) = 69 deg - very stable vs biped (~10-15 deg)
print(f"Stability: 8-leg tetrapod, CoG ~15mm high, 80mm stance -> tip angle ~{math.degrees(math.atan(40/15)):.0f} deg, vs ~15 deg for a biped. It can climb / straddle the part while laying.")

# --- Swarm, web version, 80 mm/s ---
for n in [1, 10, 100]:
    t = (web_vol_mm3/line_area_mm2)/80/60*1.3 / n * (1+0.02*(n-1) if n<100 else 1.15)
    print(f"Swarm x{n} web figurine: {t:.2f} min")

# --- FDM comparison (from sim1) ---
print(f"\nFDM solid 40mm figurine: 41.5 min. Spider web version single: {(web_vol_mm3/line_area_mm2)/80/60*1.3:.1f} min")
print(f"Spider solid version single at 80mm/s: {(solid_vol_mm3/line_area_mm2)/80/60*1.3:.1f} min")

with open("results2.json","w") as f:
    json.dump({"web_vol_cm3":web_vol_mm3/1000,"web_single_min_80mms":(web_vol_mm3/line_area_mm2)/80/60*1.3,"solid_single_min_80mms":(solid_vol_mm3/line_area_mm2)/80/60*1.3,"max_lay_speed_mms":max_speed},f,indent=2)
