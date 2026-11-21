# Spider Matter-Compiler Swarm

Open-source concept blueprints for a hive-mind swarm of spider-form matter compilers — robots that build things from powder feedstock using harmonic / ultrasonic bonding instead of heat.

One body plan does every job. The head thinks, the legs walk and climb, and the tail does the work — and the tail swaps in 30 seconds. Change the tail segment, the feed, and the blueprint file, and the same spider that laid a plastic figurine in the morning lays copper traces, places components, or stacks a transformer core in the afternoon.

## What is in this repo

- **`BLUEPRINTS.md`** — the full 14-page blueprint pack as text: the common platform, one sheet per spider type, special tails, the in-place transformer configuration, support systems, trailer deployment, and the honest limits.
- **`spider-matter-compiler-blueprints.pdf`** — the same pack as a formatted PDF (uploaded separately — see below).
- **`sims/`** — the Python simulations (sims 1–10) every figure in the blueprints is modelled from.

## The swarm

Three size classes, one platform:

| Class | Mass | Count in 2,000-swarm | Job |
|---|---|---|---|
| S — micro | 0.2 kg | 500 | Wiring, connectors, control-panel internals, cable trenches |
| M — medium | 1.0 kg | 1,200 | General fab — walls, fencing, busbars, circuit boards |
| L — large | 10 kg | 300 | Heavy lift, steel gantry, transformer placement (100× L = 5 t) |

Tail segments (30 s swap): plastic fab (35 kHz / 25 W), copper/metal fab (20 kHz / 60 W, solid-state ~300 °C), placer (pedipalp grippers), solderer (Sn63/Pb37 at 183 °C), steel, aluminium, honing, and a grease-cartridge plain journal bearing.

Feed: plastic and steel as powder, copper as spool wire (powder copper oxidises and clogs — rejected), grease as a cartridge swap, not powder.

## What the sims found

- **Plastic figurine:** single spider 5.4 min (web infill) vs 41.5 min FDM; swarm ×10, 0.64 min.
- **Circuit board:** fab + place + solder, 1 pair = 7.2 min; optimal 2 placers : 1 solderer = 6.4 min.
- **Optimus-class robot:** swarm ×100, 2.06 h; fleet of 10 pipelined, 21.8 h. Spiders make 57% of the mass; motors, battery cells and AI chips are supplied.
- **Sportbike (R1 class):** swarm ×100, 2.61 h/bike — worse value-add than a robot (17.5% spider-made), because the engine is supplied.
- **Printed engine:** Al block, steel cylinder liners, grease plain bearings instead of ball bearings — 6.70 h/bike, ~120 hp @ 7,000 RPM (vs 200 hp stock). Works, derated.
- **Power relay station, 2,000 spiders, trailer-deployed:** 5.1 days with supplied transformers; **12.6 days with transformers built in place** starting at the mounting joints and working out — slower on site, but it skips a real-world transformer lead time of ~128 weeks (nearly 2.5 years).

## Honest limits

These are concept blueprints. Every rate, mass and power figure is a modelled estimate from the sims, not a measurement from built hardware. They are detailed enough to build a first prototype programme around — they are not fabrication-ready engineering drawings, and tolerances marked as targets still have to be proven on hardware.

Known bottlenecks, from the sims:
- Precision is the wall, not power: actuator mounts, cylinder bores and QFP pins need <0.05 mm; a walking spider is ~0.1–0.5 mm without vision + fine-adjust.
- Metal is slow: Al at 30 mm/s, steel at 20 mm/s.
- Feedstock logistics: thousands of 15 g hopper refills per big build — bulk stations, not onboard hoppers.
- Transformer windings are serial: only 4 spiders per transformer can wind at once.
- Grease plain bearings cap a printed engine at ~7,000 RPM.

## License

MIT — see `LICENSE`. Build it, break it, improve it.
