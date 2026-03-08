# 2025-32. FEV-Aachen

Vienna
Motor
Symposium

2025

This paper has been presented and published on the occasion of the 46th International Vienna
Motor Symposium 2025.

All papers of this symposium are published in an anthology (ISBN 978-3-9504969-4-9) and can be
ordered from the Austrian Society of Automotive Engineers (https://vienna-motorsymposium.com,
email: info@oevk.at).

All rights reserved. It’s not allowed to reproduce any part of this document, in any form (printing,
photocopy, microfilm or another procedure) or to use electronic systems o duplicate or manipulate it,
without the explicit permission.

46th International Vienna Motor Symposium
14 - 16 May 2025

2025-32

Is 30 Bar Mean Effective Pressure the Limit for Spark Ignited
Commercial Hydrogen Engines?
Ist bei 30 bar Mitteldruck das Limit für fremdgezündete
Nutzfahrzeugwasserstoffmotoren erreicht

M. Thewes, L. Virnich, A. Dhongde, A. Boberic, FEV, Aachen;
P. Zimmer, S. Pischinger, Chair of Thermodynamics of Mobile Energy
Conversion Systems, RWTH Aachen University

2025-32

DOI: https://doi.org/10.62626/3ce4-qcpb

Abstract

The occurrence of uncontrolled combustion phenomena is the limiting factor for the
performance of hydrogen engines. Homogeneity of the air/fuel mixture, avoidance of hot
zones in the combustion chamber, appropriate layout of the ignition system and lubrication
oil formulation are decisive factors for avoiding combustion anomalies. To optimize all these
characteristics, a special engine design would be preferable, with maintaining a high level
of commonality with existing diesel engines being the key to market success.

Against this background, FEV has developed a combustion concept with the base diesel
engine and its flat cylinder head design that meets the requirements for high charge
movement with maximum communality.

The simulations carried out beforehand are compared with the test bench results acquired
afterwards for different cylinder head configurations, with a special focus on the pre-ignition
tendency. The improved cylinder head design in combination with an improved piston ring
design, a special engine oil formulation and an increased injection pressure enables a
significant increase in the possible performance level, achieving a mean effective pressure
level of 28 bar without and 30 bar with tolerably low pre ignition events.

Kurzfassung

Verbrennungsanomalien sind der begrenzende Faktor für die Leistungsdichte von
Wasserstoffmotoren. Gemischhomogenität, Vermeidung heißer Zonen im Brennraum,
geeignete Auslegung des Zündsystems und Schmierölformulierung sind die
entscheidenden Faktoren, um diese Grenze zu verschieben. Um all diese Eigenschaften zu
optimieren, wäre eine spezielle Motorkonstruktion wünschenswert, wobei eine hohe
Gleichteileanzahl mit den bestehenden Dieselmotoren der Schlüssel für den Markterfolg
sein wird.

Vor diesem Hintergrund hat FEV ein Brennverfahren entwickelt, das die Anforderungen an
eine hohe Ladungsbewegung bei maximaler Übereinstimmung mit dem Diesel-Basismotor
und seinem flachen Zylinderkopfdesign erfüllt. Die im Vorfeld durchgeführten Simulationen
werden mit den später durchgeführten Prüfstandsergebnissen für verschiedene
Zylinderkopfkonfigurationen unter besonderer Berücksichtigung der Vorentflammungsneigung
verglichen. Das verbesserte Zylinderkopfdesign in Kombination mit einem
optimierten Kolbenringdesign, einer speziellen Motorölzusammensetzung und erhöhtem
Einspritzdruck ermöglicht eine signifikante Steigerung des Leistungsniveaus auf ein
Mitteldruckniveau von 28 bar ohne und 30 bar mit geringem Auftreten von Vorzündungen.

46th International Vienna Motor Symposium 2025 1
Introduction & Motivation

Given the high technological maturity level of internal combustion engines (ICEs) and the
gravimetric energy density of hydrogen compared to batteries, there is a continuously
increasing interest in internal combustion engines powered by hydrogen as a
decarbonization solution for the on- and off-road market. These engines typically run as

mono-fuel engines on the principle of premixed combustion with spark ignition, which is
different from the diffusive combustion of the base diesel setup. Therefore, important
decisions must be made in the architecture strategy of combustion engines for operation
with hydrogen (see Figure 1).

Figure 1: Decisions regarding architecture strategy for alternative fuels

The biggest challenge in achieving performance parity with diesel engines is the occurrence
of uncontrolled combustion phenomena (pre-ignition and knocking) with fuels with low
required ignition energy like hydrogen. In this context, the homogeneity of the air/fuel
mixture, the turbulence to increase mixing and flame speeds and the avoidance of hot zones
in the combustion chamber are the key elements to shift the limit to higher power density.
The decision about the cylinder head & port design is crucial in achieving these objectives.
Moreover, the appropriate layout of the boosting system to achieve target charge dilution is
necessary. The ignition system and the lubrication oil formulation are also decisive factors
for avoiding combustion anomalies.

One of the other decisive decisions must be taken on the injection system. Port fuel injection
(PFI) systems are being utilized in series production engines for hydrogen since 2024 but if
highest power density is targeted, the drawback on volumetric efficiency needs to be
avoided. In 2025, the first H2 direct injection (DI) engines are announced to be installed in a
small fleet of trucks [1]. The direct injection of hydrogen eliminates the loss in volumetric
efficiency compared to PFI systems but creates a tough challenge of sufficient mixture
homogenization which needs to be tackled by tailored charge motion design. The most
effective way to improve mixture homogenization would be a pent roof cylinder head design

2 46th International Vienna Motor Symposium 2025
to significantly increase level of charge motion but requires a complete redesign of the
cylinder head.

Since the introduction of hydrogen powered internal combustion engines will ramp up
gradually during the next years, high communality with today`s diesel engines and the
capability to produce these engines on the same manufacturing line are key. Therefore, the
design of cylinder heads of hydrogen combustion engines and the mixture formation concept

is dominated by the degree of targeted communality with the base engine. Typically, this
layout and optimization is done using 3D CFD simulations, which model the in-cylinder flow
considering the intake and exhaust ports as well. Such simulations can also model the
hydrogen injection in combination with the combustion process. However, these simulations
can be cost and time intensive especially when they consider the direct injection and multiple
cylinder head concepts. Additionally, they require detailed inputs regarding the operation
and injection parameters.

FEV’s Charge Motion Design (CMD) process provides an effective solution to optimize the

head, port and combustion chamber design for hydrogen combustion while in parallel
considering potential benefits also for a multi-fuel concept during the initial development
stage. The CMD process accelerates the development and provides a cost-effective solution
by combining CFD simulations, benchmark data and fuel specific correlations to rank the
design variants and give first impressions of the combustion performance in the layout
phase. The evaluations can then be updated for the specific fuel and injection concept during
the detailing phase when the required inputs for 3D CFD simulations are available. This
paper describes the CMD process and highlights its application to evaluate different head
concepts for a heavy-duty engine to extend the current limitation to and beyond 30 bar mean
effective pressure level.

Base engine design

The charge motion design of a conventional commercial diesel engine aims to produce an
efficient and turbulent airflow that maximizes fuel-air mixing for better combustion. This
involves controlling swirl and the motion of the air through the combustion chamber. While

this principle evolved during the last decades, the requirement of spark-ignited combustions
systems, and in combination, the usage of directly injected gaseous fuels hasn´t been in
focus in the past for engines for commercial vehicle application. The level and orientation of
the charge motion in a hydrogen combustion engine are influenced by three variables: intake
port design, piston shape and injector positioning (spray cap orientation). To fulfil the
requirement of a high degree of communality with the base diesel engine, the scope for
optimizing these three parameters is limited. Therefore, the usage of the well-established
pent roof cylinder head design known from gasoline engines for decades is not possible in
many cases. In order to achieve a sufficient level of tumble charge motion, shrouds (small
plates with asymmetric cross section which sit above the intake seat ring) can be applied to
mask a certain area of the intake port and therefore guide the incoming charge air flow
towards the cylinder head and consequently create tumble based charge motion (see Figure
2). The usage of shrouds can be beneficial if the design of a dedicated tumble orientated
intake port is not possible. However, these shrouds result in a volumetric efficiency penalty
for a targeted tumble level compared to a dedicated tumble-focused port design, thus
reducing the air fuel ratio at full load or reducing the maximum load level.

46th International Vienna Motor Symposium 2025 3
Figure 2: FEVs filling port design with tumble shrouds for hydrogen commercial engine

To overcome these drawbacks, FEV has designed and optimized a dedicated tumble port
and implemented it into a state-of-the-art diesel engine cylinder head design maintaining the
degree of commonality in terms of machining processes (valve seat and valve guide cutting)
as shown in Figure 3.

Figure 3: FEVs tumble port design for hydrogen commercial engines

The manufacturing steps for injector and spark plug sleeve installation will need to be
individualized for diesel and hydrogen combustion engines. To tackle the challenging task
of port design under the given restrictive boundary conditions, FEV used the self-developed
Charge Motion Design (CMD) process, which is described in the following chapter.

Charge Motion Design (CMD) Process

4 46th International Vienna Motor Symposium 2025
The target of the Charge Motion Design (CMD) process is the optimization of flow-guiding
surfaces of the combustion system, injector layout, and combustion properties (see Figure
4) for premixed combustion concepts. This process strongly focuses on in-cylinder 3D-CFD
simulations to narrow down and rank the hardware variants to minimize the testing efforts.
These simulations are then post-processed with proprietary scripts that generate an array
of direct and analyzed variables considering the in-cylinder flow and turbulence. These are
then plotted into multiple correlation scatter-bands, which consider not only the port and
combustion chamber geometry dimensions, but also the charge motion and turbulence
parameters. These scatter-bands form an essential component of the CMD process and
allow the evaluation of a given design quickly and in relation to the benchmark based on
decades of engine development at FEV. Furthermore, the underlying database is used to
directly identify required geometry changes.

Figure 4: Charge motion design (CMD) process at FEV

For premixed combustion systems, a high tumble level is the preferred approach to enable
efficient and stable engine operation. The tumble from the inflow is converted into turbulent
kinetic energy close to the top dead center (TDC), which further supports the mixing process

and accelerates flame propagation. Thus, the target of the CMD process is not only to
generate a high initial charge motion from the combustion chamber and port layout, but also
to ensure good conservation of tumble motion and conversion into turbulent kinetic
energy (TKE).

Another optimization target within the CMD process during the detailing phase is the injector
layout. High-precision injector models have been developed at FEV and validated against
optical measurements for a variety of fuels, including gasoline, CNG, hydrogen, and
methanol [2, 3]. The target for the injector layout is the reduction of wall impingement and
the overall improvement of mixture homogeneity. For lean operation, the stratification within

the cylinder is of particular importance because NOX emissions must be minimized. The
interaction of the injection with the charge motion is modelled and optimized with CFD
simulations.

Since TKE and characteristic numbers for fuel homogeneity do not correlate directly with the
combustion properties, FEV has developed two models to predict the combustion
performance of the engine. The first model evaluates the burn delay (0-5 % mass fraction

burned) during the early stage of combustion [4]. The second model evaluates the 5-50 %

46th International Vienna Motor Symposium 2025 5
mass fraction burned by correlating burn duration with a turbulent characteristic number [5].
Fuel-specific parameters and flame speeds are implemented in both models. The
knowledge of the burn delay provides an evaluation of the conditions at the spark plug. It
can detect when the optimum is reached and whether it is sufficient for stable ignition. A
faster 5-50 % burn duration can be directly correlated to the efficiency of the engine or
leveraged to work with higher air/EGR rates. Thus, the optimization of these two stages of
combustion is necessary.

RANS CFD simulations were performed at a high load operating point (1600 rpm,
24 bar IMEP) with hydrogen direct injection for the SCE setup. The injector was modelled
considering the inner valve geometry and imposing the mass flow rate and needle motion.
The three hardware variants mentioned in the previous section (base ports, base ports with
tumble shrouds and dedicated tumble ports) were simulated and the optimum defined for
the shrouds and the tumble ports. A pot bowl was used for these simulations as this shape
is realizable in hardware in the base piston design while allowing sufficient space for the
piston cooling. The results of the gas exchange simulation are plotted in the charge motion
scatter-bands in Figure 5, where the shaded region shows the benchmark engines with
bore > 90 mm.

Figure 5: CMD Process scatter-bands based on results of the CFD simulations

6 46th International Vienna Motor Symposium 2025
In the first trade-off between flow coefficient and tumble, it can be observed that the flow
performance must be sacrificed to create tumble motion. Stationary CFD simulations were
performed to calculate the flow coefficients for the three concepts. The tumble ports
generate significantly higher tumble compared to the shrouds for a given drop in flow
coefficients. The base port design produces no charge motion during the gas exchange

process. The hydrogen injection only produces a weak cross tumble motion, which is not
supported by the pot bowl piston design. By inserting the tumble shrouds into the intake
port, the tumble peak is significantly increased during the intake valve event. However, this
tumble level quickly disappears during the compression stroke. The dedicated tumble ports
generate a tumble peak during the intake stroke twice higher than the shrouds.
Consequently, despite the pot bowl, some of the tumble motion is conserved into the
compression stroke. However, these flat roof concepts are still lower than other pent-roof
concepts in the benchmark, which produce higher tumble peaks and can better maintain the
tumble thanks to lens-shaped bowl designs. The turbulence generated during the
compression stroke through the destruction of the tumble, is directly proportional to the
second tumble peak as shown by the shaded plot. Only the flat head tumble port design has
a significant level of turbulence coming from the moderate second tumble peak.

The mixture distribution at TDC coming from the 3D CFD simulation with hydrogen injection
is shown in Figure 6. The normalized standard deviation of the equivalence ratio is chosen
to represent the homogeneity in the combustion chamber. At this load point (1600 rpm,
24 bar IMEP) with chosen injector configuration, only a small improvement can be observed
in the homogeneity by the introduction of the tumble shrouds. The optimized tumble ports
improve the homogeneity including the small volume in front of the injector. Consequently,
the tumble port design is chosen and will be manufactured for the next measurement
campaign.

Figure 6: Results of mixture formation CFD simulation

The burn duration correlations for 0 to 5 % and 5 to 50 % were run for the three concepts
and are plotted in Figure 7. The spark timing is varied in the post processing and plotted on
the X-axis and the total burn duration from spark timing to 50 % is plotted on the Y-axis.

46th International Vienna Motor Symposium 2025 7
Figure 7: CMD burn duration evaluation for chosen concepts.

A lower lying curve indicates a faster and stable combustion. In this regard, the tumble
shrouds already show an advantage over the base port design and the tumble ports are
even better.

Test bench setup and results

For the experimental investigations, a heavy-duty diesel single cylinder engine was modified
to a pre-mixed hydrogen combustion system. A pot bowl piston design has been chosen to
achieve a compression ratio of 10.6:1 with the flat cylinder head design of the base diesel
engine. The cylinder head was redesigned to implement the low-pressure direct injection of
hydrogen in a lateral position, enabling an injector swap without cylinder head disassembly
to ensure high flexibility in the selection of components. To fulfill the requirement of high
communality with the base diesel engine, the valve position is carried over. The base engine
intake ports provide maximum cylinder filling with a very low level of charge motion. To
increase the level of charge motion, tumble shrouds were implemented upstream the intake
valve seats.

During all measurements, the exhaust backpressure was controlled to be equal to the boost
pressure. Unless otherwise stated, a high-flow low-pressure injector at a rail pressure of
30 bar was used in all measurements. The intake air was dried to a relative humidity of
3 - 10 % depending on air mass flow. A summary of the engine specifications and further
boundary conditions for operation can be found in Table 1.

Description Unit Value

Bore x stroke mm 132 x 156
Displacement cm3 2135

Compression ratio - 10.6:1

Coolant / oil temperature °C 90 / 90
Temperature in intake runner °C 25

8 46th International Vienna Motor Symposium 2025
Injection pressure (DI) bar 30

Spark Plug - Cold heat range
Charge motion - None / Tumble

Injector - High Flow LPDI

Table 1: Engine characteristics and boundary conditions for operation

To reach high specific power, abnormal combustion must be avoided. For a DI engine, knock
and pre-ignition (PI) are the relevant phenomena, as backfire cannot occur with a start of
injection after intake valves close. The occurrence of abnormal combustion events is
depending on the ratio between required ignition energy of the mixture and the provided
energy during intake and compression stroke.

The energy supply can be controlled on the one hand by optimized hardware to minimize oil
transport to the combustion chamber and to avoid hotspots, but also by adapted boundary
conditions such as lower coolant, oil and intake air temperatures. The required ignition
energy of the mixture on the other hand is heavily dependent on gas composition, which can
globally be altered by air fuel ratio (AFR), exhaust gas recirculation (EGR) and water
injection. On a smaller scale, charge motion is relevant to avoid local rich zones and residual
gas pockets, as these zones are prone to cause abnormal combustion [6, 7, 8].

In the following diagrams, the pre-ignition frequency is displayed in the top left diagram,
average knock amplitude and the maximum knock amplitude are shown in the top right
graph. In the bottom left, the indicated specific NOx (ISNOx) emissions can be seen and
lastly the efficiency is plotted on the bottom right. The X-axis is either indicated mean
effective pressure (IMEP) or the center of combustion/point of 50 % heat release (α50) for
the spark advance variation.

In the following diagrams, the relevance of charge motion can be observed. At the lower
engine speed of 1200 1/min (see Figure 8), the tumble configuration (base port + shroud)
shows lower PI rates than the base configuration. At 1600 1/min (see Figure 9) the
achievable load without tumble increases as the charge motion (generated by the hydrogen
injection) gets more intense, and in parallel the cycle duration shortens. Consequently, the
time a given volume element is exposed to a hot surface area is reduced by a shortened
cycle duration and an increased transport speed within the combustion chamber.

46th International Vienna Motor Symposium 2025 9
Figure 8: Load sweep Base Port vs Tumble Shroud, high flow injector, 1200 1/min

The base configuration also shows significantly more frequent knock with high amplitudes
beyond 24 bar IMEP at 1200 1/min. The sudden increase in knock shows the challenging
operation close to the knock limit for hydrogen engines and the necessity to improve the
robustness against abnormal combustion. Knock is influenced by mixture homogeneity and
peak temperatures during combustion. At high PI rates, temperatures rise as the combustion
chamber heats up due to high peak pressures and temperatures, potentially causing more
knock, which in turn causes more pre-ignition, resulting in a self-propelled cycle of abnormal
combustion. Charge motion has the same effects for knock as for PI, because rich zones
are reduced, and increased velocities allow less time for energy transfer.

The improvement in mixture homogeneity causes lower NOx emissions for the tumble setup
with similar efficiency level. At high PI and knock frequencies, efficiency decreases because
combustion occurs before TDC in some cycles, resulting in higher compression and wall
heat losses.

10 46th International Vienna Motor Symposium 2025
Figure 9: Load sweep Base Port vs Shroud, high flow injector, 1600 1/min

Figure 10 shows the importance of an injector with a sufficient flow rate and the capability
to handle higher rail pressures. On the one hand, the achievable maximum load is reduced
with low pressure and flow rate as the injection duration is limited by the pressure ratio
between combustion chamber and injector nozzle. On the other hand, the mixture formation
suffers with a lower injection pressure, as the spray penetration decreases, the time for
mixture formation shortens and the interaction with charge motion is reduced. This leads not
only to slightly higher PI frequencies but also to significantly increased knock amplitudes
already at IMEP = 24 bar for the regular injector setup. As the duration of sub-critical flow
during injection increases compared to the high flow injector, leading to an increase in rich
zones, NOX emissions also increase more. Furthermore, the freedom in operation strategies
increases with high flow injectors, as they cannot only operate at higher pressure to enable
stratified combustion for increased efficiency in part load operation, but also have short
injection durations at the start of compression to provide maximum time for mixture
formation.

46th International Vienna Motor Symposium 2025 11
Figure 10: Load sweep regular vs high flow injector, Tumble shrouds, n = 1600 1/min

For hydrogen combustion, the window of ideal spark timing is significantly limited by
abnormal combustion. To mitigate knock in a gasoline engine, the retardation of spark timing
is a sufficient countermeasure. For hydrogen, however, the retardation is limited by the

occurrence of higher PI rates. Advancing spark timing to improve efficiency by taking
advantage of the fast combustion speed of hydrogen is limited by a sudden increase in
knock frequency and amplitude. In Figure 11 a variation of spark timing with higher and
lower intake temperatures are compared showing that the occurrence of knocking
combustion is more direct dependent on temperature than pre-ignition. With retardation of
the spark timing. the PI frequency increases. This is caused by two effects. Firstly, there is
more time to initiate pre-ignition. For this engine, the start of PI is usually around 8-
10 °CA bTDC. As spark timing is usually more advanced, the combustion is faster than most
of the potential PI events. With retardation, the ratio of cycles that show pre-ignition
increases. The second effect is an increasing residual gas temperature with potentially
higher hydrogen concentration. Furthermore, the exhaust gas temperature rises and leads
to higher surface temperatures promoting energy transfer from wall to gas. The exact
influence of residual gas composition and temperature are planned to be investigated
further.

12 46th International Vienna Motor Symposium 2025
Figure 11: Ignition variation, high vs low intake temperature, 1600 1/min
This variation of intake air temperature shows the potential of improved charge air cooling
to reduce anomalous combustion. To increase the required ignition energy, it is also possible
to raise the water content in the intake air. Investigations with a humidity simulation will be
conducted in the future. Additionally, it is possible to add water injection into the intake
runner to take advantage of the water’s evaporation enthalpy to reduce the temperatures
inside of the cylinder.

The addition of high-pressure external exhaust gas recirculation is also possible but is less
desirable as water can condense in the EGR cooler and intake runner, so measures must
be taken to direct the water flow into the cylinder and to separate it when the engine is shut
down. In previous studies, NOX in the exhaust gas was found to promote knock in gasoline
engines, an effect that requires further investigations for hydrogen engines. [9,10]

To determine the effect of combustion anomalies on engine health, an endurance run with
over 1,000,000 engine cycles has been conducted. The engine was operated in high load
conditions at rated speed to maximize the strain on the engine. Three different spark timings
were investigated, representing a center of combustion of 8 °CA, 12 °CA and 20 °CA aTDC.
The focus was set on the latter two timings to maximize pre-ignition occurrence. The
histograms of the peak pressure and knock amplitude are displayed in Figure 12.

As expected, the highest average peak pressure happens at the earliest ignition timing, but
maximum peak pressures over 230 bar mostly occur at later ignition timings due to preignition.
Therefore, the ignition angle needs to be controlled in a way to minimize excessive
stress on the engine. A large number of pre-ignition events resulted in high knock amplitudes
even at late ignition angles.

TIR = 40 °C
TIR = 25 °C

0
1
2
3
4

H2 SCE (2.13l) n = 1600 1/min IMEP = 20 bar
Lateral DI TIR = 25/40 °C = 2.4
IGN Variation = 10.6 SOE = 170 °CAbTDC

0
2
4
6
8

50 / °CAaTDC
0 2 4 6 8 10 12 14 16 18

0
1
2
3
4

MAX

AVG

41
42
43
44
45

50 / °CAaTDC
0 2 4 6 8 10 12 14 16 18

0

30
60
90

120

46th International Vienna Motor Symposium 2025 13
Figure 12: Histogram of peak pressures and knock amplitudes in three operating points
over 1,000,000 cycles

In total, more than 1,700 engine cycles exhibited knock amplitudes above 10 bar while
around double the amount displayed amplitudes between 5 and 10 bar (not shown in
diagram). This excessive strain on the engine did not result in any damage to the cylinder
head or piston. Extrapolating the number of pre-ignition events with a PI rate of 0.5 % to the
engine lifetime (1,200,000 km @ 80km/h, 15000h, 1% full load) would result in a total
number of pre-ignitions of 27,000. This number of pre-ignitions is 16 times higher than tested
up to now. However, the next durability run is planned to demonstrate a permissible preignition
rate of 0.5 % over engine lifetime.

Conclusions and Outlook

For a pre-mixed hydrogen combustion system, which is dominated by its tendency towards
pre-ignition and knocking combustion, achieving diesel-like power levels on a heavy-duty
engine is a great challenge. To achieve maximum performance, mixture formation and
turbulence in the combustion chamber must be optimized.

FEVs Charge Motion Design (CMD) process combines the usage of CFD simulations and
benchmark scatterbands to evaluate and optimize the cylinder head concept designs. Burn
delay and burn duration correlations for different fuels based on a single turbulent
characteristic number enable predicting the performance of the layout. Special attention is
paid to the propagation of hydrogen flames due to their strong wrinkling. Tumble shrouds

14 46th International Vienna Motor Symposium 2025
and tumble ports, which showed better homogeneity and faster and stable combustion were
defined and optimized using the CMD process.

By introducing tumble motion into the combustion chamber, the dwell time of hydrogen near
local ignition sources is reduced. This, in combination with an improved mixture
homogeneity, leads to a significant decrease in pre-ignition occurrence, which enables
stable operation at maximum loads of 30 bar IMEP. Further improvement of the mixture
homogeneity was achieved by using a high flow injector. The increased flow rate gives the
mixture more time to homogenize, resulting in an overall improvement in engine
performance and emissions. Aside from the load, the spark timing also heavily influences
abnormal combustion phenomena. At an intake air temperature of 40 °C, centers of
combustion before 8 °CA aTDC are not feasible due to knock. Late ignition timings,
however, increase the pre-ignition frequency, so the stable operating range is narrow. This
was emphasized during an endurance run at high load with over 1,000,000 recorded engine
cycles. The most critical conditions were recorded at late ignition timings with a high number
of cycles with high peak cylinder pressures and knock amplitudes.

With dedicated and optimized hardware, loads even higher than 30 bar IMEP are
achievable. An optimized tumble motion combined with a high flow injector can improve
mixture formation, which is key for reducing abnormal combustion. FEV has designed and
optimized such a cylinder head concept with the CMD process, which is planned to be tested
on a single cylinder engine in the near future. In addition, an efficient charge air cooling
system is required to minimize knock occurrence and maximize filling. Finally, the oil
formulation and the oil transport into the combustion chamber need to be optimized for
hydrogen operation.

Acknowledgements

The authors would like to thank Dr. Max Mally and Mr. Josef Beuel from FEV Europe GmbH
for their contributions to this work as well as Hoerbiger AG for supporting with injection
equipment.

References

1. P. Albrecht, “Hydrogen Powertrain Solutions for HD-Trucking”, Aachener Kolloqium,
2024.

2. I. Singh, A. Güdden, A. Raut, A. Dhongde, A. Emran, V. Sharma & S. Wagh,
“Experimental and Numerical Investigation of a Single-Cylinder Methanol Port-Fuel Injected
Spark Ignition Engine for Heavy-Duty Applications”, SAE Technical Paper 2024-26-0072,
2024.

3. A. Dhongde, P. Recker, H. Sankhla, L. Virnich, “Advanced Simulation Methodologies
for Hydrogen Combustion Engines”, ATZheavy duty worldwide, 14(4), 46-51, 2021.

4. M. Budde, “Untersuchung zyklischer Schwankungen der Entflammung an der
Klopfgrenze von magerbetriebenen Ottomotoren”, Dissertation RWTH Aachen, 2012.

5. W. Wiese, S. Pischinger, P. Adomeit, J. Ewald, "Prediction of Combustion Delay and
Duration of Homogeneous Charge Gasoline Engines based on in-Cylinder Flow Simulation",
SAE Technical Paper, 2009-01-1796, 2009.

46th International Vienna Motor Symposium 2025 15
6. Meske, R., Zimmer, P., Virnich, L., et al.: Component and Combustion Optimization
of a Hydrogen Internal Combustion Engine to Reach High Specific Power for Heavy-Duty
Applications, JSAE Kyoto, 2023
7. Boberic, A. et al.: Measures to achieve high specific power with a heavy-duty H2
internal combustion engine: A numerical and experimental analysis, 31. Aachen Colloquium
Sustainable Mobility, 2022
8. Güdden, A., Zimmer, P. et. al.: Performance improvement of direct injection H2-ICE
with flat cylinder heads, 13. Dessauer Gasmotoren-Konferenz, 2024
9. Mally, M.: Experimentelle und numerische Untersuchung von gekühlter
Abgasrückführung an der Volllast eines aufgeladenen Ottomotors, Dissertation, RWTH
Aachen, 2021
10. Kawabata, Y., Sakonji, T., and Amano, T., "The Effect of NOx on Knock in Sparkignition
Engines," SAE Technical Paper 1999-01-0572, 1999, https://doi.org/10.4271/1999-
01-0572.

16 46th International Vienna Motor Symposium 2025