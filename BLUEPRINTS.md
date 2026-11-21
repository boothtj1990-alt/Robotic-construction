# Spider Matter-Compiler Blueprints

> Concept blueprints — Issue 1.0. Every figure is a modelled estimate from the simulations in `sims/` (sims 1–10), not a measurement from built hardware. Detailed enough to build a first prototype programme around — not fabrication-ready engineering drawings.

The full 14-page PDF blueprint pack is `spider-matter-compiler-blueprints.pdf` (see Releases / repo files once uploaded).

---

   M AT T E R - C O M P I L E R S WA R M • B L U E P R I N T PA C K • C O N C E P T I S S U E 1 . 0



   Spider Matter-Compiler
   Blueprints
   Every spider in the swarm — fab, placer, solderer,
   and the S / M / L size classes



One body plan does every job. The head thinks, the legs walk and climb, and the tail
does the work — and the tail swaps in 30 seconds. Change the tail segment, the feed,
and the blueprint file, and the same spider that laid a plastic figurine in the morning
lays copper traces, places components, or stacks a transformer core in the afternoon.
  BP-01 BASE FAB           BP-02 PLASTIC        BP-03 COPPER / METAL    BP-04 PLACER      BP-05 SOLDERER

  BP-06 S MICRO          BP-07 M MEDIUM         BP-08 L LARGE    BP-09 SPECIAL TAILS     BP-10 TRANSFORMER



WHAT IS IN THIS PACK
   Pages 2–3: the common platform and the master index — read these first.
   Pages 4–9: one blueprint sheet per spider type, with a labeled schematic, full spec table, feed system,
   power, and limits.
   Pages 10–11: special tails (steel, honing, grease) and the in-place transformer configuration.
   Pages 12–13: the support systems the swarm cannot work without — segment replacers, battery swap,
   charging, bulk feed, and the trailer layout.
   Page 14: interchangeability matrix and the honest limits of the whole design.


    Read this first — what these blueprints are: These are concept blueprints built from the matter-compiler
    simulations (sims 1–10). Every rate, mass, and power figure on these sheets is a modelled estimate from those
    simulations, not a measurement from a built machine. They are detailed enough to build a first prototype
    programme around and to brief an engineer — they are not fabrication-ready engineering drawings, and
    tolerances marked as targets still have to be proven on hardware.




Spider Matter-Compiler Blueprints • Issue 1.0                                                                  Page 1
C O M M O N P L AT F O R M


One body plan, copied from a real spider
The anatomy is not decoration. A real spider puts sensing and control at the front, manipulation in the
middle, and material production at the back — and that split is exactly what a matter compiler needs.




                                                       BODY / CHASSIS
                      HEAD                           battery + hopper + control              TAIL (TOOL)
                  camera + lidar + CPU                                                    swappable segment




             8 LEGS - alternating tetrapod gait, 4 feet down at all times



Figure 1 — Side schematic, base platform. Bonding happens at the tail, as the line is laid, so the head never has to look backwards
at its own work.



HEAD — CONTROL ONLY                                                 TAIL — THE TOOL
Stereo camera, lidar, and the control computer. No                  The abdomen carries the spinneret nozzle and the
extruder up front. The head aims the spider; the tail               ultrasonic sonotrode. Harmonic frequency is aimed
is aimed by body position, the way a real spider                    at the tail, bonding each line as it is laid —
aims its spinnerets.                                                continuous, no stop-start per bead. Tail segments
                                                                    click in and out at a replacer station in 30 seconds.
LEGS — DRONE-STYLE CONTROL
                                                                    WEB LOGIC — NEVER SOLID
Eight legs, alternating tetrapod gait: four feet on the
ground at all times. Centre of gravity about 15 mm                  The spider does not fill parts solid. It lays a shell
high on an 80 mm stance gives a tip-over angle                      plus sparse radial and spiral infill, like a web: about
near 69 degrees, against roughly 15 degrees for a                   20% infill behind a 1.2 mm shell. A 40 mm figurine
biped. The spider can climb, straddle the part it is                drops from 10.0 cm3 solid to about 6.4 cm3 web-
building, and work head-down.                                       built — strong geometry for far less material and
                                                                    time.



   Design rule that runs through every sheet: if a job can be done by swapping a tail, a feed, or a file, it is never
   done by building a different spider. New product = new blueprint download. New material = new tail segment.
   New scale = new size class.




Common platform                                                                                                               Page 2
MASTER INDEX


Six spider types, three size classes

 Sheet     Spider               Job                             Tail / tool                    Feed                 Base size

 BP-       Base Fab Spider      General fabrication platform    Any fab tail                   Powder or            M (1.0
 01                                                                                            spool                kg)

 BP-       Plastic Fab Spider   Substrates, housings,           Plastic tail, 35 kHz, 25 W     Powder hopper,       S/M/L
 02                             bodywork, figurines                                            15 g

 BP-       Copper / Metal       Traces, busbars, wiring,        Copper tail, 20 kHz, 60 W      Wire spool, 50       S/M/L
 03        Fab Spider           metal parts                                                    g

 BP-       Placer Spider        Pick and place components       Pedipalp grippers (tail =      Feeder tape /        S/M/L
 04                             and supplied parts              counterweight)                 parts tray

 BP-       Solderer Spider      Solder joints, following the    Solder tail, heated tip,       Solder spool         S/M
 05                             placer                          183 C

 BP-       S — Micro Spider     Panel internals, wiring,        Micro fab / wire / solder      Mini powder /        0.2 kg
 06                             transformer cores               tails                          spool                x500

 BP-       M — Medium           Bulk workforce: walls,          2–3 tails carried per          Powder + spool       1.0 kg
 07        Spider               fencing, busbars                spider                                              x1,200

 BP-       L — Large Spider     Heavy lift, steel gantry,       Heavy steel / lifting tail     Bulk powder          10 kg
 08                             formwork                                                       dock                 x300

 BP-       Special Tails        Steel, honing, grease for       Steel 80 W / honing /          Steel powder /       M/L
 09                             engines                         grease cartridge               grease

 BP-       Transformer          Build transformers in place,    Core stacker + winder          Sheet feed /         S-led
 10        Config.              mounts outward                  tails                          copper spool


SWARM COUNTS USED IN THE SIMULATIONS

 Job                                     Swarm       Make-up

 Figurine / PCB / assembly               2–10        Fab spiders + placer/solderer trios (2 placers : 1 solderer)

 Optimus-class robot / motorcycle        100         70 fab + 30 assembly (better split found: 85 fab / 15 assembly)

 Power relay station                     2,000       500 S + 1,200 M + 300 L = 4,300 kg total swarm mass



   Cost basis used throughout: about $2,000 per spider (drone-class body plus ultrasonic tail). A 100-spider
   swarm is therefore about $200,000; it breaks even only across a fleet of builds or many different products, never
   on a single unit.




Master index                                                                                                              Page 3
BLUEPRINT BP-01


Base Fab Spider — the 1 kg platform


        Leg span sized to straddle the part




                                                       TOP VIEW - 80 mm stance, 8 legs


                                                                                    Tail mount at rear



Figure 2 — Plan view. Legs are spaced so the spider can stand over its own work and lay material between its feet.


 Item                       Specification (modelled)

 Total mass                 1.0 kg — 500 g body/chassis, 200 g hopper/feed, 300 g battery + sonotrode

 Locomotion                 8 legs, alternating tetrapod gait; laying speed 80 mm/s (plastic), walking about 0.1 m/s at
                            precision

 Stability                  Centre of gravity ~15 mm high, 80 mm stance, tip-over angle ~69 degrees

 Head                       Stereo camera + lidar + control CPU; sensors and control only, no tooling

 Power                      Walk 30 W + plastic sonotrode 25 W = 55 W typical; copper work 90 W total

 Battery                    100 Wh swappable pack; ~1.8 h at 55 W; swap 20 s at station + ~30 s walk (about 0.8 min)

 Placement                  ~0.1–0.5 mm walking; needs vision + fine-adjust to reach the <0.05 mm some jobs demand
 accuracy

 Tail interface             Click-in segment, 30 s swap at a replacer station; electrical + feed coupling in the same mount


WHAT IT BUILDS
Web-built plastic parts (shell + 20% infill), PCB substrates, housings, brackets, and — with metal tails —
aluminium and steel parts at slower rates. A single base spider builds a web figurine in roughly 4 minutes
and a full PCB substrate in about 4 minutes; a swarm splits the same work by zones.


   Limit: precision is the wall, not power. Walking accuracy alone will not hold actuator mounts, cylinder bores, or
   fine-pitch parts — every precision job in this pack adds a vision fine-adjust step at the part.




BP-01 Base Fab Spider                                                                                                     Page 4
BLUEPRINT BP-02


Plastic Fab Spider — powder wins

 Item                        Specification (modelled)

 Tail segment                Plastic tail: ultrasonic sonotrode 35 kHz, 25 W, amplitude in the 10–50 micron range

 Line                        0.8 x 0.4 mm standard; 1.0 x 0.4 mm for fast substrate work

 Laying speed                80 mm/s continuous (25 W sonotrode ceiling is about 140 mm/s at 15% coupling
                             efficiency)

 Feed — powder               15 g abdominal hopper, centred mass, no speed penalty. A PCB substrate needs about 7.9
                             g, a figurine about 7–8 g — one fill per job

 Feed — spool (rejected      50 g spool works, but adds tail inertia and costs about 10% turning/laying speed (72 vs 80
 as primary)                 mm/s)

 Bond                        Interface-only heating to about 180 C for PLA-class plastic; only ~30% of line mass is
                             heated

 Power / energy              55 W total while laying; a PCB substrate uses about 5.4 Wh with copper work — ~18
                             boards per 100 Wh pack


POWDER HANDLING RULES
   Keep powder dry and above ~20 microns: damp or ultra-fine powder clogs the nozzle. The hopper
   needs a sealed lid and a small vibrator feed assist.
   Refill is 60 s at a feed station. At scale, spiders refill at bulk floor stations — they cannot carry a whole
   job. One Optimus needs 1,467 hopper refills across the swarm.
   Web logic applies to every plastic part: shell first, then radial/spiral infill at ~20%.

PROVEN JOBS IN THE SIMULATIONS
Figurines, PCB substrate (100 x 80 x 1.6 mm in ~4.0 min), Optimus housings (8 kg plastic), motorcycle
bodywork (7 kg), substation control-house walls (2,000 kg across the swarm).




BP-02 Plastic Fab Spider                                                                                              Page 5
BLUEPRINT BP-03


Copper / Metal Fab Spider — spool wins

 Item                     Specification (modelled)

 Tail segment             Copper/metal tail: ultrasonic metal welding 20 kHz, 60 W (steel work: 80 W class)

 Bond type                Solid-state — no melting. Interface reaches about 300 C, far below copper's 1,085 C melt point

 Line / wire              0.2 mm copper wire for traces; metal lines 0.3–0.5 mm2 section for structural work

 Laying speed             Copper 60 mm/s (precision-capped, not power-capped); aluminium 30 mm/s; steel 20 mm/s

 Feed — spool only        50 g clean wire spool. A PCB needs only 0.16 g of trace copper + pads (2.8 g with pads/waste in
                          sim accounting) — one spool does ~17 boards

 Feed — powder            Copper powder oxidises in the hopper, clogs the nozzle, and the oxide layer kills the ultrasonic
 (rejected)               bond. Never spec powder copper.

 Pads                     Spot weld 0.2 s per pad; 80 pads = ~0.27 min


PROVEN JOBS IN THE SIMULATIONS
PCB traces (2.5 m of 0.2 mm trace in ~1.2 min), Optimus wiring looms (3 kg copper), motorcycle wiring (2
kg), substation busbars and cable (1,500 kg spool copper across 2,000 spiders), and transformer windings
(BP-10).


   Mixed-material rule: a board needs both tails. Either one spider swaps tails once (plastic 4.0 min + 0.5 min
   swap + copper 1.2 min = 5.7 min total), or two dedicated spiders work together with no swap (4.5 min). At swarm
   scale, dedicated spiders win.




BP-03 Copper / Metal Fab Spider                                                                                        Page 6
BLUEPRINT BP-04


Placer Spider — pedipalps do the handling
Real spiders manipulate prey with their front pedipalps. The placer copies that directly: the head stays as
camera and control, the pedipalps become the grippers, and the tail is idle ballast and counterweight.




              PEDIPALP GRIPPERS                                                   Vision: head camera, 0.05 mm guided placement
              pick, hold, rotate, place




                                                                 Optional back-mounted feeder reel (cuts travel time)




Figure 3 — Placer configuration. No fab tail is fitted; grip force and vision replace it.


 Item                      Specification (modelled)

 Cycle — small             ~2.8 s: travel to feeder + pick 0.5 s + travel + vision align 0.8 s + place 0.5 s
 part

 Cycle — MCU               8.0 s; vision alignment is ~40% of that time
 QFP-32

 Accuracy                  ~0.05 mm vision-guided — the precision member of the swarm

 Power                     40 W (walk 30 W + vision 10 W)

 Loads                     Components to connectors on a PCB solo; supplied heavy parts in teams — 2 spiders per
                           Optimus actuator, 4 per motorcycle engine


BOTTLENECK AND FIX
Feeder-to-board travel is about 60% of place time. Fix in order: feeder station at the board edge, or a small
feeder tape reel carried on the placer's back. With that, a placer lays 40 PCB components (20x 0805, 10x
small ICs, 5x connectors, 4x large caps, 1x MCU) in about 2.3 minutes of pure placing.




BP-04 Placer Spider                                                                                                           Page 7
BLUEPRINT BP-05


Solderer Spider — one job, done fast

 Item                   Specification (modelled)

 Tail segment           Solder tail: spool feed + heated tip / low-temperature bond head

 Solder                 Sn63/Pb37, melt 183 C (SAC305 at 217 C is the lead-free alternative, at higher power)

 Per joint              0.7 s — dispense 0.3 s + heat/bond 0.4 s. Local bond per joint; no reflow oven

 Power                  45 W (walk 30 W + solder tip 15 W)

 Work pattern           Follows the placer 1–2 components behind, sealing each part about 3 s after it is placed


THE PAIR — AND WHY THE RATIO IS NOT 1:1
A placer + solderer pair assembles a 40-component, 130-joint board in about 2.7 minutes. But the solderer
is faster than the placer and idles about 40% of the time in a 1:1 pair. The balanced unit is a trio: 2 placers
feeding 1 solderer — 1.9 minutes of assembly, 6.4 minutes for a full board including fabrication, with fewer
spiders than two pairs.

 Assembly unit                                            Spiders           Assembly time                 Full board

 1 pair (1 placer + 1 solderer)                           2                 2.7 min                       7.2 min

 Trio (2 placers + 1 solderer)                            3                 1.9 min                       6.4 min

 2 pairs                                                  4                 ~1.5 min                      6.0 min

 5 pairs                                                  10                ~0.7 min                      5.2 min


Energy is trivial at this scale: a pair uses about 1.9 Wh per assembly, so a 100 Wh pack covers roughly 53
full assemblies before a swap.




BP-05 Solderer Spider                                                                                                  Page 8
BLUEPRINTS BP-06 / BP-07 / BP-08


Size classes — S, M, and L
Size variance is what makes the 2,000-spider substation swarm work. Without it, a uniform swarm cannot
both lift a transformer and fit inside a control panel. With it, each size does the job it fits.

                       S — Micro (BP-06)               M — Medium (BP-07)           L — Large (BP-08)

 Mass                  0.2 kg                          1.0 kg (the BP-01 base)      10 kg

 Count in 2,000        500                             1,200                        300
 swarm

 Battery               50 Wh                           100 Wh                       200 Wh (heavy-work spec)

 Runtime               ~4 h                            ~1.4–1.8 h fab               ~2 h at heavy work

 Average power         ~20 W                           ~60 W                        ~150 W

 Tails carried         Micro-solder / wire tail only   2–3 tails (plastic, steel,   Heavy steel / lifting tail
                                                       copper)

 Jobs                  Wiring, connectors, panel       General fab: walls,          Heavy lift, steel gantry, formwork;
                       internals, cable trenches,      fencing, busbar supports,    100 L spiders lift 50 kg each = a 5-
                       transformer core stacking       cable, most products         tonne transformer team

 Swaps over a          ~30 battery swaps each          Staggered, mid-range         ~61 battery swaps each
 substation build


SCALING RULES BETWEEN CLASSES
   Leg geometry, gait, head, and tail interface are identical in principle at every size — only dimensions,
   motor torque, battery, and tail power scale.
   Precision improves as size falls: S is the only class trusted with <0.05 mm lamination gaps and 0.2 mm
   wiring.
   Lift scales with team size, not individual size: heavy parts are always a team job with a shared lift
   controller.
   Feed scales with size: S carries mini feeds, M carries the standard 15 g hopper / 50 g spool, L docks at
   bulk stations rather than carrying bulk powder.




BP-06 / BP-07 / BP-08 Size Classes                                                                                 Page 9
BLUEPRINT BP-09


Special tails — steel, honing, and grease

 Tail                 Spec                                                    Used for

 Steel fab tail       Metal ultrasonic, 80 W class, 20 mm/s, 100% dense       Crankshafts, con-rods, valves, cams,
                      (no infill — strength parts must be solid), steel       cylinder liners, gantry steel
                      powder feed

 Aluminium fab        Metal ultrasonic, 60 W class, 30 mm/s, ~60% infill      Engine blocks and heads, Optimus frame
 tail                 with hollow passages where the design allows            (22 kg), bike frames and swingarms

 Honing /             Second-pass finishing tail, removes ~0.05 mm at 10      Cylinder bores (need <0.01 mm finish vs
 polishing tail       mm/s; adds ~40% time to any part it finishes            ~0.1 mm as-laid), crank journals, bearing
                                                                              seats

 Grease               Cartridge swap, not powder: 200 g cartridge,            Plain journal bearings — see below
 cartridge tail       dispenses 0.5 g per journal


PLAIN JOURNAL BEARINGS — NO BALL BEARINGS NEEDED
The printed-engine design deletes ball bearings entirely. Each bearing is a steel shell, a shaft, and a grease
film: clearance 0.02–0.05 mm, 9 journals per engine, 4.5 g of grease total, one cartridge per engine.


   The trade, stated plainly: a grease plain bearing overheats above about 7,000 RPM. A printed 998 cc engine is
   therefore capped near 120 hp at 7,000 RPM, against 200 hp at 13,500 RPM for the stock ball-bearing, forged-
   crank engine. Ultrasonic-printed steel is also not forged steel, so fatigue life is lower and the engine is derated. It
   is a working engine, not a race engine — and for a low-revving, air-cooled engine it is a much better fit.



PRINTED ENGINE BILL (PER ENGINE, SPIDER-MADE)

 Part                                         Material                            Mass

 Block + head                                 Aluminium powder                    28 kg

 Cylinder liners / sleeves                    Steel, honed                        6 kg

 Crankshaft + con-rods                        Steel, honed                        8 kg

 Valves + camshafts                           Steel, honed                        4 kg

 Pistons x4                                   Aluminium                           2 kg

 Gaskets / seals                              Plastic                             1 kg

 Total printed                                                                    49 kg (75% of engine)


Still supplied: spark plugs, injectors, ECU, clutch plates and similar precision parts, about 16 kg.




BP-09 Special Tails                                                                                                  Page 10
BLUEPRINT BP-10


Transformer configuration — built in place
No spider lifts a finished transformer in this configuration. The spiders start at the mounting joints on the
concrete pad and grow the transformer outward, so there is no crane limit and no size limit.

BUILD SEQUENCE (PER 5 MVA UNIT, ABOUT 5,000 KG)

 Step               Work                                                  Who                     Time (modelled)

 1. Mounts          Base and mounting joints, steel, bolted to the pad    M/L                     Included in
                                                                                                  tank/base work

 2. Core            Laminated silicon steel, 2,000 kg, 0.3 mm sheets,     S only (~200            135.0 h
                    gaps <0.05 mm                                         effective per unit)

 3. Windings        Copper, 1,000 kg, wound in place around the core      Max 4 spiders per       83.3 h
                    limbs, insulation paper between layers                unit

 4. Tank +          Steel tank 1,200 kg built around core and windings,   M / L (~200 per unit)   75.0 h
 radiators          sealing as it goes; radiators 400 kg

 5. Fill + fit      Insulating oil (1,500 L, trucked and pumped),         Crew / spiders assist   —
                    bushings, tap changer — all supplied


Per unit sequential total: 293.3 h. Three units in parallel across a 2,000-spider swarm bring the full
substation to 303.3 h — 12.6 days, against 5.1 days with supplied transformers.


   The serial bottleneck: winding cannot be parallelised. A coil is continuous, so only 4 spiders can wind one
   transformer at once — one per limb. That 83.3 h does not shrink no matter how many spiders you bring. Multi-
   feed winding heads or pre-wound sectional coils are the open design problem that would collapse it.



WHY BUILD IN PLACE ANYWAY
Supplied power transformers currently carry lead times averaging about 128 weeks. In-place building
trades 2.5x on-site time for skipping the entire order, manufacture, shipping, and crane queue: about 12.6
days from trailer arrival to a built station, transformers included. It also allows in-place repair — a failed
winding can be rebuilt without removing the transformer.




BP-10 Transformer Configuration                                                                                  Page 11
SUPPORT SYSTEMS


The swarm is only half the machine

SEGMENT REPLACER STATIONS (TOOL STATIONS)
Spiders do not carry every tail. They walk to a replacer station, click the old segment off, click the new one
on: 30 seconds per tail swap, 45 seconds for a spool change, 60 seconds for a powder refill. The
substation trailer carries 10 replacer stations (500 kg). At product scale, stations are zoned: fab zone,
assembly zone, and heavy zone each keep their own tail racks so no spider crosses the whole site to
change tools.

BATTERY SWAP AND CHARGING

 Class     Pack    Swap            Charging

 S         50      Station swap,   Substation trailer: 20 charging stations at 7 kW (1,000 kg). A 100-spider swarm
           Wh      staggered       doing a 1-hour Optimus build uses about 7 kWh — one 7 kW home station
                                   recharges it in about 1 hour. Swaps are always staggered; the swarm never stops
 M         100     20 s + ~30 s    as a whole.
           Wh      walk

 L         200     20 s + ~30 s
           Wh      walk


FEEDSTOCK LOGISTICS — THE REAL BOTTLENECK AT SCALE
     Plastic: powder, bulk hoppers at floor stations.
     Copper: spool wire only, at every scale.
     Steel / aluminium: powder, bulk docks — L spiders dock rather than carry.
     Grease / sealant: cartridges.
     Never spider-made: concrete (432,000 kg for a substation is truck-poured), transformer oil, battery
     cells, motors, and chips — supplied and placed.

Numbers that force this design: 33 kg of feedstock per Optimus is 1,467 hopper refills at 15 g; a printed-
engine motorcycle needs 84 kg; a substation needs 11,500 kg spider-made (26,500 kg with in-place
transformers). Onboard hoppers alone would stall every one of those jobs.




Support systems                                                                                                Page 12
DEPLOYMENT


Trailer layout — pull up, open up, let them go




              SPIDER RACKS                             REPLACERS x10                        DAY-1 FEEDSTOCK
              2,000 spiders                            + CHARGING x20                       3,000 kg
              4,300 kg                                 1,500 kg                             steel / plastic / copper




         53 ft trailer, ~20 t payload - total load ~8,800 kg. Bulk feedstock follows by separate truck.



Figure 4 — Substation deployment trailer. One trailer carries the swarm, its tool stations, its chargers, and its first day of material.


 Load                                                                     Mass

 Spiders (500 S + 1,200 M + 300 L)                                        4,300 kg

 Segment replacer stations x10                                            500 kg

 Charging stations x20                                                    1,000 kg

 Day-1 feedstock                                                          3,000 kg

 Total                                                                    ~8,800 kg — fits one 53 ft trailer


CONTROL — THE HIVE MIND
One swarm controller assigns zones, schedules tail and battery swaps so no zone ever empties, and
staggers refills so under 20% of spiders are off-task at any moment. Spiders work in zones with
coordination overhead modelled at 15–25% at swarm scale. If the controller goes down, spiders finish their
current line, park clear of the work, and wait — they never freelance a blueprint.




Trailer deployment                                                                                                                  Page 13
REFERENCE


Interchangeability — and the honest limits

WHAT SWAPS WITH WHAT

 Swap                         Time               Where              Notes

 Tail segment (any fab        30 s               Replacer station   Same mount and coupling on S / M / L, scaled
 tail)

 Battery pack                 20 s + ~30 s       Charging station   Packs are class-specific: 50 / 100 / 200 Wh
                              walk

 Powder hopper refill         60 s               Feed station       Plastic, aluminium, steel only — never copper

 Spool change                 45 s               Replacer station   Copper wire, solder, plastic filament

 Grease cartridge             30 s               Replacer station   One cartridge per printed engine

 Blueprint (product)          Download           Swarm              No retooling — this is the whole point of the
                                                 controller         design


LIMITS THAT NO BLUEPRINT IN THIS PACK REMOVES

     1. Precision: walking accuracy is 0.1–0.5 mm; precision jobs need vision fine-adjust, honing passes, or
         S-class spiders.
     2. Metal speed: steel at 20 mm/s and aluminium at 30 mm/s dominate every large build time — the
         Optimus frame and the substation gantry are both mostly waiting on metal.
     3. Serial jobs: transformer winding (4 spiders max) and engine placement (45 min, 4-spider team)
        have floors that swarm size cannot lower.
     4. Supplied core: motors, battery cells, chips, sensors, oil, and concrete are placed, never printed.
        Spider-made share ranges from 17.5% (sportbike, supplied engine) to 57% (Optimus) to 42% (bike,
        printed engine).
     5. Cost: at ~$2,000 per spider, a swarm pays only across many builds, many different products, or a
        site with no factory and no supply chain.
     6. Hands: 22-degree-of-freedom hands with 0.5 mm tendon parts sit below standard placement
        accuracy — they need a dedicated micro-placer or are supplied pre-assembled.


    End of pack. Sheets BP-01 to BP-10, plus support systems and deployment, cover every spider type used in
    simulations 1–10: figurines, circuit boards and assembly, Optimus-class robots, motorcycles with supplied and
    printed engines, and a trailer-deployed power relay station with in-place transformers.




Interchangeability + limits                                                                                         Page 14
