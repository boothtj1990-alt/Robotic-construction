"""
Spider matter-compiler v3 - CIRCUIT BOARD, MODELLED ESTIMATE, not a physical test.
Adds: swappable battery packs, swappable tail segments per material,
spool feed vs powder hopper comparison.

Board: 100 x 80 x 1.6 mm PCB, like an Arduino-sized board.
 - Substrate: plastic/glass-epoxy analogue (PLA in sim, 1.6mm thick, web/sparse core)
 - Traces: copper, 0.2mm wide x 0.035mm thick (1oz copper), total trace length ~2.5 m
 - Pads/vias: 80 pads, copper
 - No components placed in this run (placement is a separate gripper job)

Tail segments (interchangeable, click-in at abdomen, like a tool changer):
 - PLASTIC tail: 35 kHz, 25W, 0.8mm line, powder hopper OR spool
 - COPPER tail: 20 kHz, 60W metal ultrasonic, 0.2mm wire, spool only (powder copper oxidises / clogs)
   Copper metal ultrasonic welding: no melt, 20-25 kHz, higher power, needs clean wire.
   Copper heat: Cp 0.385, melt 1085C but we do NOT melt - solid-state, interface ~300C.
 - Swap time: 30s at tool station (spider walks to station, clicks tail off/on)
 - Battery swap: 20s at charging station, 100Wh pack, spider carries 1 spare? No - station swap.

Feed comparison:
 - POWDER hopper: 15g plastic, refill 60s at station, powder flow can clog / oxidise for metals
 - SPOOL: 50g filament/wire on abdominal spool, swap spool 45s, continuous feed, no clog,
   but spool adds mass + inertia at tail, slows turning slightly (-10% lay speed)
"""
import math, json

# --- Board ---
board_w, board_h, board_t = 100, 80, 1.6
substrate_vol_mm3 = board_w*board_h*board_t
# web core: shell top/bottom 0.3mm each + 20% infill core
shell_vol = board_w*board_h*0.6
core_vol = board_w*board_h*(board_t-0.6)*0.20
substrate_web_vol = shell_vol + core_vol
print(f"PCB {board_w}x{board_h}x{board_t}mm")
print(f" Substrate solid {substrate_vol_mm3/1000:.1f} cm3 -> web {substrate_web_vol/1000:.1f} cm3, {substrate_web_vol/1000*1.24:.1f} g plastic")

trace_len_m = 2.5
trace_w_mm, trace_t_mm = 0.2, 0.035
trace_vol_mm3 = trace_len_m*1000 * trace_w_mm * trace_t_mm
trace_mass_g = trace_vol_mm3/1000 * 8.96
print(f" Copper traces: {trace_len_m} m, {trace_w_mm}mm wide, {trace_vol_mm3:.1f} mm3, {trace_mass_g:.2f} g Cu")
print(f" Pads: 80x 1mm dia x 0.035mm = {80*math.pi*0.5**2*0.035:.1f} mm3, {80*math.pi*0.5**2*0.035/1000*8.96:.2f} g")

# --- Plastic substrate, tail nozzle, continuous ---
line_w, line_h = 1.0, 0.4  # wider line for substrate, faster
line_area = line_w*line_h
path_mm_plastic = substrate_web_vol / line_area
print(f"\nPLASTIC tail: {line_w}x{line_h}mm line, path {path_mm_plastic/1000:.1f} m")
for speed in [80, 100]:
    t = path_mm_plastic/speed/60*1.2  # 20% overhead turns/climb
    print(f"  at {speed} mm/s: {t:.1f} min")

# --- Copper traces, 20 kHz metal ultrasonic ---
# Copper wire laid as 0.2mm line, speed limited by metal ultrasonic power
# Interface heat: Cu Cp 0.385, interface mass 30%, to 300C (solid-state, not melt)
cu_line_mass_per_mm_g = trace_w_mm*trace_t_mm*1*8.96/1000
heat_cu_per_mm = cu_line_mass_per_mm_g*0.30*0.385*(300-25)
print(f"\nCOPPER tail: wire {trace_w_mm}mm, heat needed {heat_cu_per_mm:.5f} J/mm")
for p in [60]:
    # metal ultrasonic coupling ~10% (worse than plastic)
    max_speed = p*0.10 / heat_cu_per_mm
    print(f"  {p}W sonotrode, 10% coupling -> max {max_speed:.0f} mm/s")
    # use 60 mm/s conservative
    t_cu = trace_len_m*1000/60/60
    print(f"  traces at 60 mm/s: {t_cu:.1f} min pure, {t_cu*1.3:.1f} min with overhead")
    # pads: spot weld 0.2s each
    t_pads = 80*0.2/60
    print(f"  pads 80x 0.2s spot: {t_pads:.2f} min")

# --- Feed: powder vs spool, plastic ---
print("\n--- FEED: powder hopper vs spool (plastic substrate) ---")
# Powder: 15g hopper, need 8.0g plastic, so 1 fill, no refill. But powder flow rate limit?
# Spool: 50g spool, 1 spool, continuous.
# Both do the job for plastic, difference is reliability / speed penalty.
# Spool adds ~150g at tail, -10% lay speed (turning inertia), powder hopper is centred, no penalty.
for feed, speed, refill_min in [("powder 15g hopper", 80, 0), ("spool 50g", 72, 0)]:
    t = path_mm_plastic/speed/60*1.2 + refill_min
    print(f"  {feed}: {t:.1f} min, mass carried {15 if 'powder' in feed else 50}g, refill swaps 0")
print("  Verdict plastic: POWDER wins - lighter, no speed penalty, 8g < 15g capacity, no refill needed.")
print("  Powder risk: clogging if powder is damp / fine <20um, needs dry hopper + vibrator.")
print("\n--- FEED: copper ---")
print("  Powder copper: REJECTED in sim - oxidises in hopper, clogs nozzle, oxide layer kills ultrasonic bond.")
print("  Spool copper wire: WINS - clean wire, continuous, 2.8g needed, one 50g spool does ~17 boards.")
print("  So: plastic = powder, copper = spool. Mixed spider needs BOTH feed types, or two spiders.")

# --- Swaps: battery + tail ---
print("\n--- SWAPS ---")
# Single spider doing whole board: plastic tail first, then swap to copper tail
t_plastic = path_mm_plastic/80/60*1.2
t_copper = trace_len_m*1000/60/60*1.3 + 80*0.2/60
tail_swap_min = 0.5
total_single = t_plastic + tail_swap_min + t_copper
print(f"Single spider, 1 tail swap (30s): plastic {t_plastic:.1f} + swap {tail_swap_min} + copper {t_copper:.1f} = {total_single:.1f} min")
print(f" Battery: total power plastic 55W, copper 30W walk + 60W sonotrode = 90W")
energy_wh = t_plastic/60*55 + t_copper/60*90
print(f" Energy used: {energy_wh:.1f} Wh of 100Wh pack - NO battery swap needed for 1 board")
print(f" Battery swaps needed: 0 for 1 board, 1 swap after ~{100/energy_wh:.1f} boards")
print(f" Battery swap cost when it happens: 20s at station + ~30s walk = ~0.8 min")
# Swarm: 2 spiders, one plastic, one copper, no tail swap, parallel (copper waits for substrate top layer)
t_swarm2 = max(t_plastic, t_copper) + 0.5  # 0.5 min handover / coordination
print(f"\nSwarm x2 (plastic spider + copper spider, no tail swap): {t_swarm2:.1f} min")
print(f"  Copper spider idles {t_plastic-t_copper:.1f} min while substrate is laid, then works.")
# Swarm x10: 5 plastic + 5 copper, split board into zones
t_swarm10 = total_single/5 * 1.2  # rough, 5-way split, 20% coordination
print(f"Swarm x10 (5+5, zone split): ~{t_swarm10:.1f} min")
# Compare to conventional PCB fab: prototype PCB 24-48h turnaround, or CNC mill ~30-60 min
print(f"\nConventional: CNC-milled prototype PCB ~30-60 min, fab house 24-48h. Spider single: {total_single:.1f} min, swarm x2: {t_swarm2:.1f} min")

with open("results3.json","w") as f:
    json.dump({"plastic_min":t_plastic,"copper_min":t_copper,"single_total_min":total_single,"swarm2_min":t_swarm2,"energy_wh":energy_wh},f,indent=2)
