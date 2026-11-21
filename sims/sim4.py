"""
Spider matter-compiler v4 - FULL PCB ASSEMBLY, MODELLED ESTIMATE.
Adds: Component Placement spider + Solder spider, working as PAIRS.

Board from v3: 100x80mm, substrate 4.0 min + copper 1.2 min = 5.7 min single, 4.5 min swarm x2.
Now add assembly:
 - 40 components: 20x 0805 resistors/caps (2mm), 10x SOT-23 / small ICs, 5x connectors, 4x larger caps, 1x MCU (QFP, 32 pins)
 - Total solder joints: 20*2 + 10*3 + 5*4 + 4*2 + 32 = 130 joints

Placement spider:
 - Uses front pedipalps as grippers (real spiders use pedipalps to manipulate prey - copy that).
   Head = camera + control, pedipalps = pick-and-place, tail = idle / counterweight.
 - Pick-and-place cycle (real SMT machines: 0.1-0.5s/component, but a walking spider is slower):
   travel to feeder tape (avg 150mm at 200mm/s) + pick 0.5s + travel to board (150mm)
   + vision align 0.8s + place 0.5s = ~2.8s per small component, 5s for MCU (align pins)
 - Accuracy: vision-guided, ~0.05mm placement, needed for 0.5mm pitch QFP.

Solder spider:
 - Sole job: lay solder. Tail = solder spool + low-temp sonotrode / heated tip.
   Solder: Sn63/Pb37, melt 183C, or SAC305 217C. Use 183C in sim (lower power).
   Per joint: dispense paste/dot 0.3s + heat/bond 0.4s = 0.7s/joint.
   It follows BEHIND the placement spider, 1-2 components behind, so it never waits for a cold board.
   No reflow oven needed - local bond per joint, like a tiny soldering iron on legs.

Pairs:
 - A pair = 1 placer + 1 solderer, working in tandem on the same zone.
   Placer lays component, solderer seals it ~3 seconds later. No handover, no queue.
   If solderer falls behind, placer pauses (backpressure) - modelled as 10% sync overhead.
 - 2 pairs = 4 spiders, board split in 2 zones. 5 pairs = 10 spiders, 5 zones.
"""
import math, json

# --- Components ---
components = [
    ("0805 R/C", 20, 2.8, 2),   # name, count, place_time_s, joints
    ("SOT-23 / small IC", 10, 3.5, 3),
    ("connector", 5, 4.5, 4),
    ("large cap", 4, 4.0, 2),
    ("MCU QFP-32", 1, 8.0, 32),
]
total_place_s = sum(c*t for _,c,t,_ in components)
total_joints = sum(c*j for _,c,_,j in components)
n_comp = sum(c for _,c,_,_ in components)
print(f"Components: {n_comp}, joints: {total_joints}")
print(f" Placement pure: {total_place_s:.0f}s = {total_place_s/60:.1f} min")
print(f" Solder pure: {total_joints*0.7:.0f}s = {total_joints*0.7/60:.1f} min")

# --- Single pair, sequential in tandem ---
# Placer is bottleneck (slower than solderer), solderer follows, 10% sync overhead
pair_time_min = total_place_s/60 * 1.10
# solderer finishes last component ~0.7*2 joints after placer, negligible, add 0.2 min
pair_time_min += 0.2
print(f"\nSingle PAIR (placer + solderer, tandem): {pair_time_min:.1f} min assembly")
print(f"  Placer bottleneck: {total_place_s/60:.1f} min, solderer: {total_joints*0.7/60:.1f} min, solderer idles {(total_place_s-total_joints*0.7)/60:.1f} min waiting")

# --- Full board: fab + assembly ---
fab_single_min = 5.7
fab_swarm2_min = 4.5
print(f"\nFull board single-threaded (fab then 1 pair): {fab_single_min + pair_time_min:.1f} min")
print(f"Full board (fab swarm x2, then 1 pair): {fab_swarm2_min + pair_time_min:.1f} min")

# --- Multiple pairs ---
for pairs in [1,2,5]:
    # split components evenly, + coordination overhead
    overhead = 1 + 0.10 + 0.03*(pairs-1)
    t = pair_time_min / pairs * overhead if pairs>1 else pair_time_min
    # fab also parallel? keep fab at swarm x2 = 4.5 min, assembly is after fab, so total:
    total = fab_swarm2_min + t
    print(f"{pairs} pair(s) ({pairs*2} spiders assembly): assembly {t:.1f} min, full board {total:.1f} min")

# --- Power / battery for assembly spiders ---
# Placer: walk 30W + vision 10W = 40W. Solderer: walk 30W + solder tip 15W = 45W.
# Pair assembly ~2.5 min, energy ~3.5 Wh - no battery swap.
print(f"\nPower: placer 40W, solderer 45W, pair assembly {pair_time_min:.1f} min uses ~{pair_time_min/60*42:.1f} Wh - no swap")
print(f"  A 100Wh pack does ~{100/(pair_time_min/60*42):.0f} full assemblies before swap")

# --- What breaks? ---
print("\nBottlenecks, in order:")
print(" 1. Placement travel: feeder -> board is ~60% of place time. Fix: feeder tape ON the spider (small reel on back), or feeder station at board edge.")
print(" 2. MCU alignment: 8s for QFP-32, vision align is 40% of that. Fix: dedicated high-res camera on placer head.")
print(" 3. Solder is NOT the bottleneck: 0.7s/joint, solderer is idle ~40% of the time in a pair - it could serve 2 placers.")
print("  -> Optimal ratio is NOT 1:1. Sim says 2 placers : 1 solderer is balanced.")
# 2 placers : 1 solderer
t_2p1s = max(total_place_s/2, total_joints*0.7)/60*1.10 + 0.2
print(f"  2 placers : 1 solderer (3 spiders): assembly {t_2p1s:.1f} min, full board {fab_swarm2_min+t_2p1s:.1f} min - faster than 1 pair, fewer spiders than 2 pairs")

with open("results4.json","w") as f:
    json.dump({"components":n_comp,"joints":total_joints,"pair_min":pair_time_min,"full_single_pair_min":fab_single_min+pair_time_min,"full_2pairs_min":fab_swarm2_min+pair_time_min/2*1.13,"optimal_2p1s_min":t_2p1s},f,indent=2)
