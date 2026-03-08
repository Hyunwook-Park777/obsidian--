# EGY_Strategies of H2-air mixture formation for suppressing BF, PI, and knk

Strategies of hydrogen-air mixture formation for suppressing backfire,

pre-ignition, and knock in full-load operations of hydrogen

heavy-duty engines

Hyunwook Park a,* , Junsun Lee a

, Seungmook Oh a

, Changup Kim a , Yunsub Park b
,
Dockoon Yoo b

a Department of Eco-friendly Mobility Power, Korea Institute of Machinery and Materials, Daejeon, 34103, Republic of Korea
b Future Power System Development Team, HD Hyundai Infracore, Incheon, 22502, Republic of Korea

ARTICLE INFO

Keywords:

Hydrogen engine
Backfire
Pre-ignition
Knock
Heavy duty

Mixture formation

ABSTRACT

This study integrated hydrogen spray visualization and multi-cylinder combustion diagnostics to establish
hydrogen-air mixture formation strategies that simultaneously suppress backfire, pre-ignition, and knock in fullload
operations of a hydrogen port-fuel injection, heavy-duty engine. Using the Schlieren imaging, the actual
injection duration of hydrogen spray according to hydrogen injection pressure was determined. Based on an
injection duration limit, only injection pressures ranging from 1.0 to 1.2 MPa could be utilized at the maximum
power, whereas all five injection pressure ranges were allowed at the maximum torque. In hydrogen engine
experiments, backfire occurred as an excess air ratio decreased. Backfire in a particular cylinder caused knock
and pre-ignition in the subsequent firing-order cylinders; therefore, the engine load was drastically reduced. The
backfire was suppressed by increasing the excess air ratio, but pre-ignition and knock occurred sequentially while
delaying the hydrogen start of injection (SOI). Pre-ignition occurring in one cylinder did not affect the combustion
processes in the other cylinders; therefore, the engine could be operated stably. Appropriately high
excess air ratios to suppress backfire, early hydrogen SOIs to suppress pre-ignition and knock, and low hydrogen
injection pressures within an actual injection duration limit were beneficial for achieving high full-load
performance.

1. Introduction

Technological changes in energy systems have been led by a reduction
in greenhouse gas emissions since the Paris Climate Agreement. In
road transportation, CO2 emission regulations previously limited to
passenger vehicles, have been expanded to heavy-duty vehicles. The
European Commission adopted CO2 emission standards for heavy-duty
vehicles for the first time in 2019. In 2023, the Commission proposed
stronger revisions to the CO2 standards [1]. To meet the stringent CO2
standards, it is essential to introduce zero-emission vehicles equipped
with the following power sources: electrification, hydrogen fuel cells,
and hydrogen internal combustion engines. Hydrogen internal combustion
engines in heavy-duty applications are advantageous over
lithium-ion batteries and hydrogen fuel cells in terms of price competitiveness
and technological maturity [2].

Hydrogen, which is a carbon-free fuel, is an attractive option for
spark-ignition engines because it does not generate carbon-based
products during combustion. Hydrogen has a wide flammability range,
which enables the implementation of lean combustion in internal
combustion engines [3]. Therefore, it is possible to simultaneously
improve thermal efficiency and reduce NOX emissions by employing
lean combustion technology in hydrogen engines. The high flame
propagation speed of hydrogen allows a hydrogen engine to approach a
theoretical constant-volume cycle owing to its narrow combustion
duration, which is favorable for achieving high thermal efficiency. [4].
The thermal efficiency of a hydrogen engine can also be increased by
implementing a high compression ratio owing to the high research octane
number of lean hydrogen-air mixture [5].

Despite these advantages, there are some technical issues associated
with hydrogen spark-ignition engines, such as power deficit and
abnormal combustion. Because hydrogen has a low density, a hydrogen

* Corresponding author. Department of Eco-friendly Mobility Power, Korea Institute of Machinery and Materials 156 Gajeongbuk-Ro, Yuseong-Gu, Daejeon, 34103,
Republic of Korea.

E-mail address: hwpark@kimm.re.kr (H. Park).

Contents lists available at ScienceDirect

Energy

journal homepage: www.elsevier.com/locate/energy

https://doi.org/10.1016/j.energy.2025.136343

Received 9 March 2025; Received in revised form 14 April 2025; Accepted 26 April 2025

Energy 326 (2025) 136343

Available online 29 April 2025

0360-5442/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/bync-nd/4.0/).
spark-ignition engine with port fuel injection (PFI) supply reduces the
volumetric efficiency, resulting in a low engine power output [6]. In this
situation, when the excess air ratio is increased to apply lean combustion
technology, power loss of the hydrogen engine cannot be avoided.
Verhelst et al. [7] indicated that the power loss caused by a lean
hydrogen-air mixture should be compensated by intake boosting.
Another important issue encountered in hydrogen spark-ignition engines
with a PFI supply is the occurrences of abnormal combustion such
as backfire, pre-ignition, and knock, which are the main topics of this
study. Table 1 lists the definitions, causes, and results of abnormal
combustion phenomena in hydrogen PFI engines.

Backfire is defined as the ignition of a hydrogen-air mixture in the
intake manifold during the intake stroke when a fresh fuel-air mixture is
introduced into the cylinder [8]. Backfire mainly occurs in hydrogen
engines with a PFI supply and is typically induced by hot spots in the
combustion chamber and high residual gas temperatures owing to the
low minimum ignition energy of hydrogen [9]. Backfire occurrence reduces
the volumetric efficiency of a port-injection hydrogen engine,
resulting in a power drop [10]. Additionally, port injectors, a throttle,
and various types of sensor equipment in the intake system can be
damaged by hydrogen combustion in the intake manifold. Therefore,
backfire acts as a barrier to improving the power performance of
hydrogen engines [11]. Numerous studies have been conducted to
suppress backfire in hydrogen PFI engines. These studies include strategies
for engine variables, such as intake valve opening control,

hydrogen injection parameters, and ignition timings, to suppress backfire.
Lee et al. [12] reported that backfire could be suppressed by a
proper delay in the opening of the intake valve in a single-cylinder
hydrogen PFI engine under low-load conditions. The late intake valve
opening reduced the residual gas temperature owing to heat loss and
expansion effects; however, it reduced the volumetric efficiency.
Therefore, a proper delay in the intake valve opening and
lean-combustion boosting technology were effective in avoiding backfire
while maintaining the power output. Dhyani et al. [13] suppressed
backfire occurrences in a multi-cylinder hydrogen PFI engine during
low-load operations by varying the hydrogen start of injection (SOI).
When the equivalence ratio was increased to 0.82 with a hydrogen SOI
at the top dead center (TDC), backfire occurred owing to the high residual
gas temperature. In this situation, because the hydrogen SOI was
delayed by 40 crank angle degree (CAD), backfire was completely
eliminated. Spark timing retardation was also effective in reducing the
probability of backfire. Xin et al. [14] pointed out that the accurate
detection of backfire and targeted action can extend the operating range
of hydrogen PFI engines. Backfire events were detected by combining
the locations and amplitudes of the peak pressures monitored by two
manifold absolute pressure sensors. They emphasized that injection and
ignition strategies should be adjusted as soon as backfire is detected.

Pre-ignition is defined as the ignition of a hydrogen-air mixture in
the combustion chamber during the compression stroke prior to spark
discharge [15]. Because backfire is a type of pre-ignition phenomenon,
the causes of pre-ignition are the same as those of backfire. The fundamental
difference between backfire and pre-ignition in hydrogen
spark-ignition engines is the timing at which they occur [13]. While
backfire occurs during the intake stroke when the intake valves are
opened, pre-ignition refers to the ignition of a fresh charge during the
compression stroke when the intake valves are closed. Since pre-ignition
advances the combustion phasing, it may lead to an increase in negative
compression work and a decrease in power output [16]. Pre-ignition also
leads to a rapid increase in pressure and temperature in the cylinder,
causing more hot spots and triggering another pre-ignition or knock.
While considerable research has focused on backfire in hydrogen PFI
engines, pre-ignition has been primarily addressed in hydrogen
direct-injection (DI) engines, which can avoid backfire by initiating
hydrogen injection after the intake valve close (IVC). Wang et al. [17]
investigated the boundary of hydrogen SOIs in a turbocharged DI
hydrogen engine. When hydrogen injection was completed before the
IVC, a large amount of hydrogen occupied the cylinder volume, reducing
fresh air induction. The decrease in air reduced the excess air ratio and
weakened the cylinder cooling, which caused the pre-ignition phenomenon.
They concluded that considering the limitation of
pre-ignition, hydrogen injection should be timed to occur after IVC. Bao
et al. [18] observed that a delay in hydrogen injection was effective in
mitigating pre-ignition by a long time for cooling before hydrogen injection.
Pre-ignition occurred even with hydrogen injection after IVC at
an engine speed of 2000 rpm. However, the pre-ignition was alleviated
when the hydrogen SOI was delayed by 20 CAD. They also emphasized
that pre-ignition tended to occur at engine speeds higher than 3000 rpm
owing to the high in-cylinder temperature.

Knock is defined as the spontaneous ignition of an unburned mixture
in the end-gas region ahead of the flame propagation by a spark plug
[19]. Knock is induced when the fuel-air mixture in the end-gas region is
compressed to sufficiently high pressures and temperatures [20]. Once
the autoignition of one or more local regions within the end-gas occurs,
the nonuniform nature of the pressure distribution causes pressure
waves to propagate across the combustion chamber [18]. The thermal
shock from high-pressure waves and the vibration of the engine may
leave several pits and scratches on engine parts, such as pistons, cylinder
liners, and valves. Li et al. [21] reported that the compression ratio and
intake temperature are the key parameters affecting the knock-limited
equivalence ratio in hydrogen PFI engines using a two-zone model
with a knock criterion. According to a simulation by Li et al. [22], a high

Nomenclature

aTDC after top dead center
CAD crank angle degree
DI direct injection

EOI end of injection

EVC exhaust valve close
HRR heat release rate

IMEP indicate mean effective pressure
IVC intake valve close

MAPO maximum amplitude of pressure oscillation
MFB50 mass fraction burned 50
PFI port fuel injection

SCR selective catalytic reduction
SOI start of injection
TDC top dead center

VGT variable geometry turbocharger

Table 1

Definitions, causes, and results of abnormal combustion in hydrogen PFI
engines.

Item Backfire Pre-ignition Knock
Definition Ignition of a

hydrogen-air

mixture in the

intake manifold

during intake stroke

Ignition of a

hydrogen-air mixture

in the cylinder during
compression stroke
prior to spark
discharge

Autoignition of endgas
ahead of the
propagating

turbulent flame

Causes Hot spots in the

cylinder or high
residual gas
temperature

Hot spots in the
cylinder or high
residual gas
temperature

Fuel-air mixture in
the end-gas

compressed at high
pressures and
temperatures
Results - Power drop by low
volumetric
efficiency

- Intake system and
fuel supply parts
damage

- Power drop by

negative compression
work

- Another pre-ignition
or knock

- Propagation of
pressure waves

across the chamber
- Piston, intake &

exhaust valves parts
damage

H. Park et al. Energy 326 (2025) 136343

2
compression ratio amplified the effect of the equivalence ratio on the

knock intensity of a hydrogen DI engine. For a compression ratio of 11
and an equivalence ratio of 0.47, the engine operated with low knock
intensity values, regardless of the ignition timing. However, the
low-knock operating points of ignition timing were narrow at a
compression ratio of 17.5, and even a low equivalence ratio of 0.3. Bao
et al. [18] discovered that a delay in the hydrogen SOI suppressed
pre-ignition occurrences, which increased the load of a hydrogen DI
engine by increasing the equivalence ratio. However, the increase in the

equivalence ratio resulted in knock, despite the breakthrough of
pre-ignition. Lai et al. [23] proposed a hydrogen injection that was
slightly retarded after the IVC to suppress the knock occurred in a
hydrogen DI engine. Hydrogen injections before the IVC led to poor
mixing homogeneity owing the interference of air flow. By contrast, a
significantly delayed hydrogen SOI after the IVC caused a higher

end-mixture equivalence ratio and an increase in the combustion temperature,
which increased the propensity for knock.

To summarize the articles reviewed above, while strategies for
hydrogen injection parameters and intake valve timing for preventing
backfire have been suggested in hydrogen PFI engines, no attempts have
been made to suppress pre-ignition and knock at high-load operations.
Strategies for hydrogen-air mixture formation to suppress pre-ignition
and knock have been addressed primarily in hydrogen DI engine.
However, in the high-load operation of hydrogen PFI engines, not only

backfire but also pre-ignition and knock occur. These abnormal combustion
phenomena act as barriers to achieving high-load expansion in

hydrogen PFI engines. Therefore, this study investigated strategies for

hydrogen and air mixture formation to simultaneously suppress backfire,
pre-ignition, and knock in the full-load operations of a six-cylinder,
heavy-duty engine equipped with a hydrogen PFI system. The strategies
included variables such as excess air ratio, hydrogen SOI, and hydrogen
injection pressure. In addition, while previous studies installed an incylinder
pressure sensor only in a specific cylinder for abnormal combustion
detection, in this study, in-cylinder pressure sensors were
installed in all six cylinders. This allows us to understand not only the
impact of abnormal combustion occurring in a particular cylinder on the
next cycle but also the interaction of abnormal combustion between
cylinders according to the firing order within the same cycle. Hydrogen
spray visualization was also performed in a constant-volume chamber to
better understand the process of supplying hydrogen to the combustion
chamber through port injection with a long injection period. The results
of hydrogen spray visualization and engine experiments would provide a

practical solution for achieving high performance and controlling
abnormal combustion phenomena in hydrogen PFI engines.

2. Experiments and methods

2.1. Hydrogen spray visualization experiment

Before the hydrogen PFI engine experiment, the hydrogen spray
injected from a solenoid-type port fuel injector was visualized using the
high-speed Schlieren imaging technique in a constant-volume chamber.
Fig. 1 shows a schematic of the hydrogen spray visualization. The
chamber had a volume of 1.39 L. A port fuel injector was installed on the
right side of the chamber. Hydrogen supplied by a high-pressure
hydrogen cylinder was delivered to the injector. The target injection
pressure was set by using a pressure regulator. The injector was driven
by a universal injector driver (ZB5016, Zenobalti). The hydrogen spray
from the injector was recorded using a high-speed camera (VEO410L,
Phantom). The images were recorded at a sampling rate of 17,000
frames per second with a resolution of 512 x 512 pixels. Two mirrors and
a tungsten-halogen lamp were used to obtain the images of the hydrogen
spray. The signals from the injector driver and the high-speed camera
were synchronized using a delay generator (DG535, Stanford). Through
the spray experiment, the actual start and end of the hydrogen injection
according to the current signal applied to the injector were obtained.

Table 2 lists the experimental conditions for hydrogen spray visualization.
The hydrogen purity was 99.9 %. The injection mass was
selected based on the hydrogen mass flow rates supplied to the engine

during the maximum torque and maximum power operations. The injection
pressure was varied from 0.8 to 1.2 MPa, considering the pressure
range applicable to the actual high-load operation of hydrogen PFI
engines. The ambient pressure was fixed as 0.3 MPa. Image processing
was conducted by the MATLAB after recording the Schlieren images to
obtain the macroscopic spray behavior of hydrogen. Details of the image
processing method followed the procedures in previous literature [24].

Fig. 1. Schematic of hydrogen spray visualization experiment.

Table 2

Experimental conditions of hydrogen spray visualization.

Item Specification
Hydrogen purity [%] 99.9

Injection pressure [MPa] 0.8–1.2
Ambient pressure [MPa] 0.3

H. Park et al. Energy 326 (2025) 136343

3
The spray tip penetration was defined as the maximum axial distance
from the hydrogen nozzle exit to the spray edge.

2.2. Hydrogen engine experiment

Hydrogen engine experiments were performed on an in-line, sixcylinder,
heavy-duty, spark-ignition engine. Table 3 lists the engine
specifications. The engine had a displacement volume of 11.1 L. The
firing orders of the cylinders was 1-5-3-6-2-4. Six port-fuel injectors
were mounted on each intake port to supply hydrogen to the cylinders
during the intake stroke. A variable geometry turbocharger (VGT) was
adopted as the boosting system for the hydrogen engine.

Fig. 2 shows a schematic of the hydrogen engine experiment.
Hydrogen supplied from high-pressure cylinders passed through pressure
regulators and a fuel rail, and was eventually delivered to six portfuel
injectors. Table 4 lists the properties of hydrogen used in this study.
The mass flow rates of the hydrogen were measured using a Coriolis flow
meter (CMFS015M, Emerson). Air boosted by the VGT system was
supplied to the intake manifold after cooling using an intercooler. The
mass flow rates of the air were measured using a thermal mass flow
meter (FMT700-P, ABB). Combustion of the hydrogen-air mixture supplied
to each cylinder was initiated using a spark plug. Six piezoelectric
pressure transducers (6054BRU, Kistler) were installed in all six cylinders
to obtain in-cylinder pressure traces. The in-cylinder pressure
measurements over 300 consecutive cycles were transmitted to a combustion
analyzer (X-ion, AVL) to analyze the combustion parameters of
the hydrogen PFI engine. The concentrations of the exhaust gases were
measured using a gas analyzer (AMA i60, AVL). The analyzer was
composed of different gas detectors, and the detailed measurement
principles are described in Ref. [25]. The concentration of the unburned
hydrogen was measured using a hydrogen gas analyzer (HyEVO,
HORIBA). The parameters of the hydrogen-air mixture formation, such
as boost pressure, excess air ratio, hydrogen SOI, hydrogen injection
pressure, and spark timing, were controlled using an engine control unit.
Table 5 lists the specifications of the measurement equipment used in
this study. Table 6 lists the uncertainties of the engine parameters. The
uncertainties were obtained using the analysis method provided in
Ref. [26].

Table 7 lists the experimental conditions for the strategies of
hydrogen-air mixture formation in the hydrogen heavy-duty engine. The
engine speeds were 1200 and 2000 rpm, which had the maximum torque
and power of the hydrogen engine, respectively. The engine was operated
under full-load conditions for both engine speeds. The coolant
temperature and intake temperature were maintained at 363 ± 2 K and
323 ± 2 K, respectively. An excess air ratio decreased from 2.3 until
backfire occurred. The excess air ratio was defined as Equation (1).

Excess air ratio =

(
m˙ air/
m˙ hydrogen)
actual (
m˙ air/
m˙ hydrogen)
stoichiometry

(1)

where m˙ air and m˙ hydrogen denote the mass flow rates of air and hydrogen,
respectively. The hydrogen SOI was delayed by 30 CAD from base case.
The base case was determined after the exhaust valve close (EVC) of the
hydrogen engine. It is known that the start and end of the hydrogen

injection should be located between the EVC and IVC to prevent backfire
in hydrogen PFI engines [6]. The hydrogen injection pressure was varied
from 0.8 to 1.2 MPa. The spark timings for the engine speeds of 1200 and
2000 rpm were fixed as − 11 and − 12 CAD after top dead center (aTDC),
respectively.

The experimental procedure for establishing strategies for hydrogenair
mixture formation in a hydrogen heavy-duty engine is as follows.
First, hydrogen spray was visualized in a constant-volume chamber to
determine the spray development and actual injection period according
to the hydrogen injection pressure. Second, through hydrogen engine
experiments, the backfire phenomenon occurring in the high-load
operation was analyzed, and strategies for excess air ratio to suppress
backfire were identified. Finally, pre-ignition and knock occurrences
according to hydrogen injection parameters, such as hydrogen SOI and
hydrogen injection pressure, were analyzed, and strategies for
hydrogen-air mixture formation to achieve high-load operation of the
hydrogen PFI engine were suggested. The maximum amplitude of
pressure oscillation (MAPO) was selected as an evaluation index for the
knock [27]. MAPO is defined as the maximum value of the high-pass
filtered cylinder pressure oscillations between the crank angles of − 30
and 90 CAD aTDC [28]. The knock was determined when the MAPO
value was greater than 0.2 MPa in any one of the six cylinders [29].

3. Results and discussion

3.1. Hydrogen spray visualization

Hydrogen spray was visualized using the Schlieren imaging technique
in a constant-volume chamber to determine the hydrogen spray
development and actual injection duration prior to the hydrogen engine
experiments. The hydrogen spray behavior during the development
phase is important in terms of the time required for hydrogen injected
from the intake port to reach the cylinder. Because a hydrogen PFI
supply with a long injection duration should be carried out during the
intake stroke, it is important to determine the actual injection duration
for preventing backfire in hydrogen PFI engines.

Fig. 3 shows the Schlieren images of the port-injection hydrogen
spray during the development phase, and the quantitative spray tip
penetration of the hydrogen spray is shown in Fig. 4. Although the initial
development proceeded similarly within the error range, the spray tip
penetration subsequently increased with hydrogen injection pressure. A
higher hydrogen injection pressure resulted in a higher spray momentum
[30]. Therefore, the time required to reach the visible window
limit (90.9 mm) at higher injection pressures was shorter than that at
lower injection pressures. The minimum time to reach the visible window
limit was 2.12 ms with an injection pressure of 1.2 MPa. When the
injection pressure was reduced to 0.8 MPa, the time to reach the limit
increased to 2.65 ms. Therefore, a higher hydrogen injection pressure
was advantageous for supplying hydrogen fuel into the combustion
chamber more quickly, considering the distance between the hydrogen
port injector and the intake valves in an actual hydrogen PFI engine.

Fig. 5 shows the Schlieren images of the port-injection hydrogen
spray at the end of injection (EOI) phase. While there was no significant
difference in the actual hydrogen SOI depending on the hydrogen injection
pressure, as shown in Fig. 4, EOI was achieved earlier with an
injection pressure of 1.2 MPa than with lower injection pressures. This is
because the injection amount was fixed; therefore, the time required to
deliver the same mass of hydrogen was lower for a higher injection
pressure. The actual injection duration was calculated to quantify the
time for which the port-injection hydrogen was supplied according to
the hydrogen injection pressure. The actual injection duration was
defined as the period between the start and end of the hydrogen spray, as
determined from the Schlieren images.

Fig. 6 shows the actual injection durations of port-injection hydrogen
in time (left) and CAD (right) units according to the hydrogen injection
pressure. As the hydrogen injection pressure increased, the actual

Table 3

Engine specifications.

Item Specification

Engine type (HX12) In-line, six-cylinder, heavy-duty, sparkignitionBore
× stroke [m] 0.123 × 0.155
Displacement [L] 11.1

Number of valves per cylinder [− ] 4 (2 intake and 2 exhaust)
Firing order 1-5-3-6-2-4

Hydrogen injection type Port fuel injection

Boosting system Variable geometry turbocharger

H. Park et al. Energy 326 (2025) 136343

4
injection duration decreased. For example, when the actual injection
duration was 13.65 ms at the injection pressure of 0.8 MPa, the duration
decreased to 10.24 ms at the injection pressure of 1.2 MPa. The timebased
actual injection durations were converted into engine crank

angle units to understand the port-injection hydrogen supply in the
actual hydrogen heavy-duty engine operation. In the full-load operation
of the hydrogen PFI engine, the hydrogen injection duration was very
wide owing to the low injection pressure; therefore, an injection duration
limit was selected. The injection duration limit was set to 150 CAD
considering the valve timings of the base hydrogen engine and the
control margin of the hydrogen SOI. A hydrogen SOI before the EVC
exposes the fresh hydrogen-air mixture to high-temperature residual
gas, resulting in backfire in hydrogen PFI engines [31]. When the

Fig. 2. Schematic of hydrogen engine experiment.

Table 4
Properties of hydrogen.

Item Specification

Purity [%] 99.9
Density at 273 K [kg/Nm3
] 0.089
Lower heating value [MJ/kg] 119.9
Autoignition temperature [K] 858
Minimum ignition energy [mJ] 0.02
Stoichiometric air-to-fuel ratio [− ] 34.3

Table 5

Specifications of measurement equipment.

Measured
parameters

Device Measurement
range

Linearity/
accuracy

Repeatability

Hydrogen
flow rate

CMFS015M
(Emerson)

0–30 kg/h ≤ ± 0.25 %
of MVb
≤ ± 0.2 % of
MVb
Air flow rate FMT700-P
(ABB)
0–2400 kg/h ≤ ± 1 % of
MVb
≤ ± 0.25 % of
MVb
In-cylinder
pressure
6054BRU
(Kistler)
0–30 MPa ≤ ± 0.3 %
of FSa
–

THC
CH4
NOX
CO
CO2
O2

AMA i60
(AVL)

0 - 5000 ppm
0 - 3000 ppm
0 - 5000 ppm
0 - 5000 ppm
0 - 5000 ppm
0 - 25 vol%

≤ ± 1 % of
FSa

≤ ± 0.5 % of
FSa

Hydrogen HyEVO
(HORIBA)

0 - 2000 ppm ≤ ± 1 % of
FSa

–

a FS: full scale.
b MV: measurement value.

Table 6

Uncertainties of engine parameters.

Parameters Data uncertainty [%]

Net indicated mean effective pressure ±0.8
In-cylinder pressure ±1.1
Heat release rate ±1.7
Maximum amplitude of pressure oscillation ±2.4
NOx emissions ±2.2

Table 7
Experimental conditions.

Item Value

Engine speed [revolutions/
minute]

1200 2000

Engine load [%] 100 % (maximum
torque)
100 % (maximum
power)
Coolant temperature [K] 363 ± 2
Intake temperature [K] 323 ± 2
Excess air ratio [− ] 2.3–2.0
Hydrogen start of injection [CAD
aTDC]
Base ~ Base + 30

Hydrogen injection pressure
[MPa]

0.8–1.2

Spark timing [CAD aTDC] − 11 − 12

H. Park et al. Energy 326 (2025) 136343

5
hydrogen SOI is too late, hydrogen is still delivering after the IVC,
resulting in backfire [6]. Despite the same injection duration in the time

resolution, the actual injection duration in the engine crank angle resolution
at the maximum power (2000 rpm and 100 % engine load) was
longer than that at the maximum torque (1200 rpm and 100 % engine
load) owing to the faster engine speed. Based on the injection duration
limit selected in this study, it was confirmed that all five injection
pressures could be utilized in the base hydrogen engine under the

maximum torque operation. However, only hydrogen injection pressures
in the range of 1.0–1.2 MPa could be applied under the maximum
power operation.

3.2. Backfire occurrence and strategies of excess air ratio

Based on the results of hydrogen spray visualization, engine experiments
were conducted in a hydrogen PFI engine under full-load conditions.
The excess air ratio was reduced from 2.3 to search for

conditions of backfire occurrences in the maximum torque and power
operations. Because the generation of boosting pressure in the VGT
equipped on the hydrogen engine was limited, an increase in the
maximum torque and power could be achieved by reducing the excess
air ratio. However, low excess air ratios contribute to high combustion
temperatures, leading to high residual gas temperatures at the start of
the intake process [13]. Therefore, the high-load expansion achieved by
reducing the excess air ratio in hydrogen PFI engines is limited by the
occurrence of backfire. The hydrogen injection pressure was selected as

1.2 MPa for both engine loads. Port-injection hydrogen must be provided
between the EVC and IVC of the hydrogen engine to prevent
backfire, and a high injection pressure has the advantage of supplying
the hydrogen mass in a short period of time [9].

Fig. 7 shows the net indicated mean effective pressure (IMEP) and
excess air ratio at which backfire occurred in the hydrogen PFI engine.
While the backfire occurred at an excess air ratio of approximately 2.0 at
the maximum power, backfire was observed at a relatively higher excess
air ratio at the maximum torque. This was due to a higher net IMEP of
2.0 MPa at the maximum torque than that at the maximum power (1.7
MPa net IMEP). A high IMEP indicates that a high hydrogen mass is
delivered to the combustion chamber per cycle, which increases the
combustion temperature. This increases the residual gas temperature
and the possibility of more hot spots inside the cylinder [6]. Therefore,
the backfire event was observed even at the high excess air ratio at the
maximum torque.

Figs. 8 and 9 show the pressure traces of the six cylinders for normal
combustion and backfire cycles, respectively, at the maximum torque.
The trend of the in-cylinder pressure traces at the maximum power was
the same. The firing order of the cylinders was 1-5-3-6-2-4. Although the
pressure traces of the six cylinders were similar during the normal
combustion cycle, they were not consistent during the backfire cycle.

For example, the backfire occurrence in cylinder 5 caused knock (cylinders
3, 6, and 4) and pre-ignition (cylinder 2) in the other cylinders in
the same cycle. The ignition of the fresh hydrogen-air mixture in the
intake manifold resulted in the peak in-cylinder pressure of cylinder 5
close to the value under the motored condition. The backfire of cylinder

5 increased the charge temperature in the intake manifold. Consequently,
the initial temperature of the fresh hydrogen-air mixture in the

Fig. 3. Schlieren images of port-injection hydrogen spray during development phase.

Fig. 4. Spray tip penetration of port-injection hydrogen spray during development
phase.

H. Park et al. Energy 326 (2025) 136343

6
subsequent firing-order cylinders also increased [32]. The high charge
temperature also reduced the volumetric efficiency of air in the subsequent
firing-order cylinders, which lowered the excess air ratio. Therefore,
the high initial temperature and low excess air ratio of the mixture
resulted in the knock and pre-ignition phenomena. While the peak
in-cylinder pressure was 11.5 MPa for cylinder 1 (normal combustion),
the peak pressure increased to 23.1 MPa for cylinder 3 (knock). The
occurrence of backfire, knock, and pre-ignition in the backfire cycle
reduced the engine load. Fig. 10 shows the average net IMEP of the six
cylinders over 250 consecutive cycles. Prior to the backfire, the average
net IMEP was approximately 2.0 MPa. The average net IMEP was
reduced to 1.6 MPa in the backfire cycle. Owing to the continued
occurrence of abnormal combustion phenomena, the net IMEP
decreased, and engine operation at the maximum torque was impossible.
In summary, the backfire occurrence in one cylinder caused
abnormal combustion phenomena in the subsequent firing-order cylinders,
resulting in engine shutdown owing to combustion instability. The
backfire events could be suppressed simply by increasing the excess air

ratio. However, in this case, some compromises were required regarding
the maximum torque and power.

3.3. Strategies of injection parameters for suppressing pre-ignition and
knock

In addition to backfire events, other abnormal combustion phenomena,
such as pre-ignition and knock, also occur during the full-load
operation of hydrogen PFI engines. This section investigates the strategies
of injection parameters for suppressing pre-ignition and knock. In
other words, abnormal combustion events according to the hydrogen
SOI and injection pressure were analyzed, and strategies were suggested.
Because backfire was a dangerous event that even resulted in engine
shutdown as found in the previous section, the excess air ratio increased
to 2.2 and 2.1 in the maximum torque and power operations, respectively,
for preventing backfire.

Figs. 11 and 12 show the average mass fraction burned 50 (MFB50)
and average net IMEP of the six cylinders according to the hydrogen SOI,

Fig. 5. Schlieren images of port-injection hydrogen spray at end of injection phase.

Fig. 6. Actual injection durations of port-injection hydrogen in time (left) and engine crank angle (right) units according to hydrogen injection pressure.

H. Park et al. Energy 326 (2025) 136343

7
respectively, at the maximum torque. The trends of combustion and
performance according to the hydrogen SOI were similar for the
maximum torque and power operations. Therefore, the results at the
maximum torque were presented. The MFB50 was defined as the crank
angle at which 50 % of the total heat release occurred [33]. As the
hydrogen SOI was delayed, the MFB50 advanced. The delay in the
hydrogen SOI reduced the hydrogen-air mixing period between the
hydrogen EOI and spark discharge, leading to the formation of a locally
rich area and thus the advanced MFB50. The average net IMEP increased
with the delay in the hydrogen SOI because the combustion phasing was

advanced to the optimal point for work conversion near the TDC [34].
No abnormal combustion events occurred when the hydrogen SOI was
delayed by 20 CAD from the base case. Although similar MFB50s were
observed until the hydrogen SOI was delayed by 10 CAD from the base,
further delays up to 20 CAD from the base led to significant MFB50

Fig. 7. Net indicated mean effective pressure and excess air ratio at which
backfire occurred.

Fig. 8. In-cylinder pressure traces of six cylinders for normal combustion cycle
at the maximum torque.

Fig. 9. In-cylinder pressure traces of six cylinders for backfire cycle at the
maximum torque.

Fig. 10. Average net indicated mean effective pressure of six cylinders over
250 consecutive cycles at the maximum torque.

Fig. 11. Average mass fraction burned 50 of six cylinders according to
hydrogen start of injection at the maximum torque.

Fig. 12. Average net indicated mean effective pressure of six cylinders according
to hydrogen start of injection at the maximum torque.

H. Park et al. Energy 326 (2025) 136343

8
advances. However, as the hydrogen SOI was delayed by 25 CAD from
the base, pre-ignition was observed along with a rapid MFB50 advance.
A further delay in the hydrogen SOI caused combustion knock. The
causes of pre-ignition and knock events can be inferred from the heat
release rate (HRR) and in-cylinder bulk temperature data. Fig. 13 shows
the average HRR (left) and in-cylinder bulk temperature (right) curves
of the six cylinders according to the hydrogen SOI. Similar to the trend in
the MFB50 results, the peak HRR increased slightly until the hydrogen

SOI was delayed by 10 CAD from the base, which increased the combustion
temperature slightly. However, with further delays in the
hydrogen SOI, the combustion phasing advanced and the peak HRR
increased significantly. Therefore, when the hydrogen SOI was delayed
by 25 CAD from the base, pre-ignition occurred because the high HRR
increased the combustion temperature, which induced a high residual
gas temperature and hot spots in the combustion chamber [35]. A
further delay in the hydrogen SOI resulted in an even higher peak HRR
and in-cylinder bulk temperature. As a result, the hydrogen-air mixture
in the end-gas region was compressed to sufficiently high pressures and
temperatures, which caused the knock. It is noted that pre-ignition was
also observed at the engine operating point where the knock occurred
[17].

The pre-ignition and knock phenomena caused by the delay in the
hydrogen SOI were analyzed at greater depths. Fig. 14 shows the incylinder
pressure (left) and HRR (right) curves of the six cylinders for
the pre-ignition cycle. A pre-ignition event was observed in cylinder 5 in

cycle 179; however, combustion proceeded normally in the other cylinders.
Unlike normal combustion, the heat release due to pre-ignition
occurred from − 25 CAD aTDC prior to the spark timing. Therefore,

the in-cylinder pressure increased drastically at a relatively earlier stage
than during the normal combustion. The pre-ignition also led to the
spontaneous ignition of the end-gas mixture. Therefore, while the

average peak in-cylinder pressure of the normal combustion cylinders
was 12.7 MPa, the peak pressure for the pre-ignition cylinder increased
to 17.6 MPa owing to the knock occurrence. The effects of pre-ignition
on the combustion and engine performance between the cylinders and
cycles were also analyzed. Figs. 15 and 16 show the MFB 50 and average
net IMEP of the six cylinders over 300 consecutive cycles with a 25 CAD
delay in the hydrogen SOI from the base, respectively. Only the MFB50
of the pre-ignition event (cycle 179) advanced to − 1.5 CAD aTDC,
whereas the MFB50 values of the other cycles were similar to those of
the normal combustion cylinders. Therefore, there was no significant
change in the average net IMEP even when pre-ignition occurred. In
summary, the pre-ignition occurring in a particular cylinder did not
affect the combustion processes in the subsequent firing-order cylinders;
therefore, the engine could be operated stably without significant net
IMEP fluctuations.

Fig. 17 shows the MAPO of the six cylinders according to the
hydrogen SOI. The MAPO values were low until the hydrogen SOI was
delayed by 20 CAD from the base. When the hydrogen SOI was delayed
by 25 CAD from the base, the MAPO values slightly increased. A further

delay in the hydrogen SOI resulted in a significant increase in the MAPO

values. For example, the MAPO values of all the cylinders except cylinder
3 exceeded 0.2 MPa with a 30 CAD delay in the hydrogen SOI from
the base. It is noted that the MAPO value of the knock accompanying
pre-ignition was higher than that of the combustion knock without preignition.
Fig. 18 shows the knock intensity of cylinder 5 excluding (left)
and including (right) the pre-ignition cycle over 300 consecutive cycles
with a 25 CAD delay in the hydrogen SOI from the base. While the knock
intensities were within 0.2 MPa in the absence of the pre-ignition event,
the peak knock intensity increased to 0.81 MPa in the pre-ignition cycle.
Fig. 19 shows the knock intensity of cylinder 5 over 300 consecutive
cycles with a 30 CAD delay in the hydrogen SOI from the base. As the
hydrogen SOI was delayed, the knock intensities increased overall with a
peak value of 0.62 MPa. Although not stored within 300 consecutive
cycles, pre-ignition and knock were observed. When knock occurs, more

intense combustion and heat release induce a high residual gas temperature
and hot spots in the cylinder, leading to pre-ignition [17]. The
high knock intensities caused by knock and pre-ignition can damage the
pistons and valves of hydrogen engines. Therefore, in the full-load
operation of hydrogen PFI engines, pre-ignition and knock should be
suppressed by properly advancing the hydrogen SOI.

Strategies for hydrogen injection pressure were also investigated.
Early hydrogen SOIs were adopted to suppress pre-ignition and knock
for the maximum torque and power operations. Based on the results of
hydrogen spray visualization as discussed in section 3.1, a wide range of
hydrogen injection pressure from 0.8 to 1.2 MPa was tested at the
maximum torque, whereas only the injection pressure of 1.0–1.2 MPa
was adopted at the maximum power.

Figs. 20 and 21 show the average MFB50 and net IMEP of the six
cylinders according to the hydrogen injection pressure at the maximum
torque and power, respectively. The hydrogen PFI engine operated
without any abnormal combustion events over the hydrogen injection
pressure range tested at the early hydrogen SOIs. The change in MFB50
due to variations in the hydrogen injection pressure was minimal at the
maximum torque. This is because the narrow injection duration in the
engine crank angle resolution, as shown in Fig. 6, provided sufficient
time for hydrogen-air mixing prior to spark discharge. Therefore, almost
no change was observed in the average net IMEP when the hydrogen
injection pressure was varied. However, at the maximum power, the
actual injection duration in the engine crank angle resolution was
considerably long owing to the high engine speed. Therefore, the delay
in the EOI with a decrease in the hydrogen injection pressure reduced

Fig. 13. Average heat release rate (left) and in-cylinder bulk temperature (right) curves of six cylinders according to hydrogen start of injection at the
maximum torque.

H. Park et al. Energy 326 (2025) 136343

9
the time for hydrogen-air mixing, resulting in the advancement of
MFB50. The average net IMEP also increased slightly with a decrease in
the injection pressure.

The HRR and in-cylinder bulk temperature showed similar trends to
the MFB50 results. Fig. 22 shows the average HRR (left) and in-cylinder
bulk temperature (right) curves of the six cylinders according to the

hydrogen injection pressure at the maximum torque. There was no significant
change in the HRR traces depending on the hydrogen injection
pressure, which resulted in similar peak in-cylinder bulk temperatures.
However, at the maximum power, small changes were observed in
combustion parameters. Fig. 23 shows the average HRR (left) and incylinder
bulk temperature (right) curves of the six cylinders according
to the hydrogen injection pressure at the maximum power. As hydrogen
injection pressure was reduced, the combustion phasing advanced and
the peak HRR increased slightly, which resulted in a high combustion
temperature [35]. Therefore, when developing an actual hydrogen PFI
engine that receives hydrogen from a high-pressure storage tank, a low
injection pressure is beneficial for increasing the utilization of hydrogen
stored in the high-pressure tank at the maximum torque. At the
maximum power, an appropriately low injection pressure should be
selected considering the increase in the actual injection duration with a
decrease in the injection pressure.

This study integrated hydrogen spray visualization and multicylinder
combustion diagnostics to establish hydrogen-air mixture formation
strategies that simultaneously suppress backfire, pre-ignition,
and knock in full-load operations of a hydrogen PFI heavy-duty engine.
Through appropriately high excess air ratios to suppress backfire,
early hydrogen SOIs to suppress pre-ignition and knock, and low
hydrogen injection pressures within an actual injection duration limit,
high engine loads of 1.95 MPa and 1.64 MPa net IMEPs were achieved at
the maximum torque and power, respectively. These values represent an
8.3 % increase at the maximum torque and a 21.5 % increase at the

Fig. 14. In-cylinder pressure (left) and heat release rate (right) curves of six cylinders for pre-ignition cycle at a hydrogen start of injection = Base + 25 CAD.

Fig. 15. Mass fraction burned 50 of six cylinders over 300 consecutive cycles at
a hydrogen start of injection = Base +25 CAD.

Fig. 16. Average net indicated mean effective pressure of six cylinders over
300 consecutive cycles at a hydrogen start of injection = Base +25 CAD.

Fig. 17. Maximum amplitude of pressure oscillation of six cylinders according
to hydrogen start of injection at the maximum torque.

H. Park et al. Energy 326 (2025) 136343

10
maximum power compared to a recent report for a hydrogen PFI heavyduty
engine in the same class [36].

4. Conclusions

Hydrogen PFI engines are emerging to meet the stringent CO2 standards
for heavy-duty applications. However, abnormal combustion,
such as backfire, pre-ignition, and knock, acts as a barrier to the
expansion of the high-load operation required in heavy-duty engines.
This study investigated strategies for hydrogen-air mixture formation to
suppress backfire, pre-ignition, and knock in full-load operations of a
hydrogen PFI engine. Unlike previous studies, in-cylinder pressure
sensors were installed in all the cylinders to determine the interactions
of abnormal combustion between the cylinders and cycles. Hydrogen
spray visualization was also performed to better understand the process
of supplying hydrogen to the cylinder through port injection. The main
conclusions of this study are as follows.

1) As the hydrogen injection pressure increased from 0.8 to 1.2 MPa,
the spray tip penetration during the development phase increased
owing to the high spray momentum. The actual injection duration
decreased with increasing injection pressure, which is advantageous
for supplying hydrogen to the cylinder in a short period. Based on an
injection duration limit of 150 CAD, all five injection pressures can
be utilized in an actual hydrogen PFI engine at the maximum torque.

Fig. 18. Knock intensity of cylinder 5 excluding (left) and including (right) pre-ignition cycle over 300 consecutive cycles at a hydrogen start of injection = Base +
25 CAD.

Fig. 19. Knock intensity of cylinder 5 over 300 consecutive cycles at a
hydrogen start of injection = Base +30 CAD.

Fig. 20. Average mass fraction burned 50 of six cylinders according to
hydrogen injection at the maximum torque and power.

Fig. 21. Average net indicated mean effective pressure of six cylinders according
to hydrogen injection pressure at the maximum torque and power.

H. Park et al. Energy 326 (2025) 136343

11
However, only injection pressures ranging from 1.0 to 1.2 MPa can
be applied at the maximum power.

2) Backfire occurred at an excess air ratio of approximately 2.1 at the

maximum torque, whereas the engine operated at lower excess air
ratios until backfire occurred at the maximum power. The backfire
occurrence in a particular cylinder caused knock and pre-ignition in
the subsequent firing-order cylinders. The engine was shut down
because the continued occurrence of abnormal combustion reduced
the net IMEP. The dangerous backfire phenomenon could be avoided
by increasing the excess air ratio; however, in this case, the
maximum torque and power had to be sacrificed to some extent.

3) Proper high excess air ratios were applied to suppress the backfire

occurrence; however, pre-ignition and knock occurred sequentially
as the hydrogen SOI was delayed by 25 and 30 CAD from the base,
respectively. Unlike the backfire phenomenon, the pre-ignition
occurring in a particular cylinder did not affect the combustion
processes in the other cylinders; therefore, the engine could be
operated stably without significant net IEMP fluctuations. However,
the knock accompanied by the pre-ignition event exhibited a higher
MAPO value than the knock cycle without pre-ignition. The MAPO
values of the five cylinders exceeded 0.2 MPa with a 30 CAD delay in
the hydrogen SOI from the base. Therefore, early hydrogen SOIs
were beneficial for pre-ignition and knock suppression.

4) When adopting early hydrogen SOIs, there were no significant
changes in the HRR and net IMEP with varying hydrogen injection

pressures at the maximum torque. However, as the injection pressure
was reduced from 1.2 to 1.0 MPa at the maximum power, the combustion
phasing advanced and the peak HRR increased slightly,
which resulted in a slightly increased net IMEP. Therefore, considering
the increases in the actual injection duration with a decrease in
the hydrogen injection pressure, an appropriately low injection
pressure should be selected for an actual hydrogen PFI engine to
increase the utilization rate of hydrogen stored in a high-pressure
storage tank.

Through the strategies for hydrogen-air mixture formation proposed
in this study, high engine loads of 1.95 MPa and 1.64 MPa net IMEPs
were achieved at the maximum torque and power, respectively. The
main findings from this study can provide a practical solution for controlling
abnormal combustion events and achieving high engine performance
in the development of an actual hydrogen PFI engine. The
future work is to increase the full-load performance of our hydrogen PFI
heavy-duty engine by 15 % through two-stage turbocharging. The
hydrogen PFI engine would be exposed to abnormal combustion beyond
an injection duration limit without increasing hydrogen injection pressure
under the full-load conditions. Therefore, intake mixture dilutions
such as exhaust gas recirculation and water injection will be also
implemented to achieve the full-load performance.

Fig. 22. Average heat release rate (left) and in-cylinder bulk temperature (right) curves of six cylinders according to hydrogen injection pressure at the
maximum torque.

Fig. 23. Average heat release rate (left) and in-cylinder bulk temperature (right) curves of six cylinders according to hydrogen injection pressure at the
maximum power.

H. Park et al. Energy 326 (2025) 136343

12
CRediT authorship contribution statement

Hyunwook Park: Writing – original draft, Investigation, Formal
analysis, Conceptualization. Junsun Lee: Resources, Investigation, Data
curation. Seungmook Oh: Supervision. Changup Kim: Visualization.
Yunsub Park: Writing – review & editing, Methodology. Dockoon Yoo:
Project administration, Funding acquisition.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Acknowledgement

This work was supported by the Technology Innovation Program
(20018148, 300 kW class zero-CO2 hydrogen combustion engine system
and storage supply system development for construction machinery and
commercial vehicles) funded by the Ministry of Trade Industry & Energy
(MOTIE, Korea)

Data availability

The data that has been used is confidential.

References

[1] Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE
COUNCIL amending regulation (EU) 2019/1242 as regards strengthening the CO2
emission performance standards for new heavy-duty vehicles and integrating
reporting obligations, and repealing regulation (EU) 2018/956. European
Commission; 2023. Available from: https://eur-lex.europa.eu/legal-content/EN/T
XT/?uri=celex%3A52023PC0088.

[2] Lago Sari R, Fogue Robles A, Monsalve Serrano J, Cleary D. Techno-economic
assessment of hydrogen as a fuel for internal combustion engines and proton
exchange membrane fuel cells on long haul applications. Energy Convers Manag
2024 Jul;311:118522. https://doi.org/10.1016/j.enconman.2024.118522.
[3] Duan X, Li Y, Liu J, Guo G, Fu J, Zhang Q, et al. Experimental study the effects of
various compression ratios and spark timing on performance and emission of a
lean-burn heavy-duty spark ignition engine fueled with methane gas and hydrogen
blends. Energy 2019 Feb;169:558–71. https://doi.org/10.1016/j.
energy.2018.12.029.

[4] Lhuillier C, Brequigny P, Contino F, Mounaïm-Rousselle C. Experimental study on
ammonia/hydrogen/air combustion in spark ignition engine conditions. Fuel 2020
Jun;269:117448. https://doi.org/10.1016/j.fuel.2020.117448.
[5] Zhang S wei, Sun B gang, Luo Q he, Bao L zhi, Li X yu, Leach F. Experimental
multiple parameters optimization of the injection strategies for a turbocharged
direct injection hydrogen engine to achieve highly efficient and clean performance.
Energy 2024 Dec;312:133592. https://doi.org/10.1016/j.energy.2024.133592.
[6] Gao J, Wang X, Song P, Tian G, Ma C. Review of the backfire occurrences and
control strategies for port hydrogen injection internal combustion engines. Fuel
2022 Jan;307:121553. https://doi.org/10.1016/j.fuel.2021.121553.
[7] Verhelst S, Maesschalck P, Rombaut N, Sierens R. Increasing the power output of
hydrogen internal combustion engines by means of supercharging and exhaust gas
recirculation. Int J Hydrogen Energy 2009 May;34(10):4406–12. https://doi.org/
10.1016/j.ijhydene.2009.03.037.

[8] Huynh TC, Kang JK, Noh KC, Lee JT, Caton JA. Controlling backfire for a
hydrogen-fueled engine using external mixture injection. J Eng Gas Turbines
Power 2008 Nov 1;130(6):062804. https://doi.org/10.1115/1.2940353.
[9] Khalid AH, Muhamad Said MF, Veza I, Abas MA, Roslan MF, Abubakar S, et al.
Hydrogen port fuel injection: review of fuel injection control strategies to mitigate
backfire in internal combustion engine fuelled with hydrogen. Int J Hydrogen
Energy 2024 May;66:571–81. https://doi.org/10.1016/j.ijhydene.2024.04.087.
[10] Navale SJ, Kulkarni RR, Thipse SS. An experimental study on performance,
emission and combustion parameters of hydrogen fueled spark ignition engine with
the timed manifold injection system. Int J Hydrogen Energy 2017 Mar;42(12):
8299–309. https://doi.org/10.1016/j.ijhydene.2017.01.059.
[11] Di´eguez PM, Urroz JC, S´
ainz D, Machin J, Arana M, Gandía LM. Characterization of
combustion anomalies in a hydrogen-fueled 1.4 L commercial spark-ignition
engine by means of in-cylinder pressure, block-engine vibration, and acoustic
measurements. Energy Convers Manag 2018 Sep;172:67–80. https://doi.org/
10.1016/j.enconman.2018.06.115.

[12] Lee J, Lee K, Lee J, Anh B. High power performance with zero NOx emission in a
hydrogen-fueled spark ignition engine by valve timing and lean boosting. Fuel
2014 Jul;128:381–9. https://doi.org/10.1016/j.fuel.2014.03.010.

[13] Dhyani V, Subramanian KA. Experimental investigation on effects of knocking on
backfire and its control in a hydrogen fueled spark ignition engine. Int J Hydrogen
Energy 2018 Apr;43(14):7169–78. https://doi.org/10.1016/j.
ijhydene.2018.02.125.

[14] Xin G, Ji C, Wang S, Meng H, Chang K, Yang J, et al. Monitoring of hydrogen-fueled
engine backfires using dual manifold absolute pressure sensors. Int J Hydrogen
Energy 2022 Mar;47(26):13134–42. https://doi.org/10.1016/j.
ijhydene.2022.02.042.

[15] Liang Z, Xie F, Guo Z, Wang Z, Dou H, Wang B, et al. Optimization and prediction
of a novel preignition in hydrogen direct injection engines through
experimentation and the random forest algorithms. Energy Convers Manag 2024
Aug;313:118602. https://doi.org/10.1016/j.enconman.2024.118602.
[16] Yang Z, Wang L, Zhang Q, Meng Y, Pei P. Research on optimum method to
eliminate backfire of hydrogen internal combustion engines based on combining
postponing ignition timing with water injection of intake manifold. Int J Hydrogen
Energy 2012 Sep;37(17):12868–78. https://doi.org/10.1016/j.
ijhydene.2012.05.082.

[17] Wang K da, fu Zhang Z, Sun B gang, Zhang S wei, Lai F yu, Ma N, et al.
Experimental investigation of the working boundary limited by abnormal
combustion and the combustion characteristics of a turbocharged direct injection
hydrogen engine. Energy Convers Manag 2024 Jan;299:117861. https://doi.org/
10.1016/j.enconman.2023.117861.

[18] Bao L zhi, Sun B gang, he Luo Q, cheng Li J, Qian D chao, yang Ma H, et al.
Development of a turbocharged direct-injection hydrogen engine to achieve clean,
efficient, and high-power performance. Fuel 2022 Sep;324:124713. https://doi.
org/10.1016/j.fuel.2022.124713.

[19] yu Li X, Sun B gang, Zhang S wei, Bao L zhi, he Luo Q, Leach F, et al. Investigations
of combustion characteristics and mechanism of backfire-induced super-knock in a
turbocharged hydrogen engine. Energy 2024 Dec;312:133453. https://doi.org/
10.1016/j.energy.2024.133453.

[20] Manzoor MU, Yosri M, Talei M, Poursadegh F, Yang Y, Brear M. Normal and
knocking combustion of hydrogen: a numerical study. Fuel 2023 Jul;344:128093.
https://doi.org/10.1016/j.fuel.2023.128093.

[21] Li H. Knock in spark ignition hydrogen engines. Int J Hydrogen Energy 2004 Jul;29
(8):859–65. https://doi.org/10.1016/j.ijhydene.2003.09.013.
[22] Li Y, Gao W, Zhang P, Fu Z, Cao X. Influence of the equivalence ratio on the knock
and performance of a hydrogen direct injection internal combustion engine under
different compression ratios. Int J Hydrogen Energy 2021 Mar;46(21):11982–93.
https://doi.org/10.1016/j.ijhydene.2021.01.031.

[23] Lai FY, Sun BG, Wang X, Zhang DS, Luo QH, Bao LZ. Research on the inducing
factors and characteristics of knock combustion in a DI hydrogen internal
combustion engine in the process of improving performance and thermal
efficiency. Int J Hydrogen Energy 2023 Mar;48(20):7488–98. https://doi.org/
10.1016/j.ijhydene.2022.11.091.

[24] Ki Y, Kim JJ, Lee SY, Hwang J, Bae C. Measurement of hydrogen jet equivalence
ratio using laser induced breakdown spectroscopy. SAE Tech Pap 2024. https://
doi.org/10.4271/2024-01-2623. 2024-01-2623).

[25] Park H, Lee J, Jamsran N, Oh S, Kim C, Lee Y, et al. Comparative assessment of
stoichiometric and lean combustion modes in boosted spark-ignition engine fueled
with syngas. Energy Convers Manag 2021 Jul;239:114224. https://doi.org/
10.1016/j.enconman.2021.114224.

[26] Chen Z, Zhang T, Wang X, Chen H, Geng L, Zhang T. A comparative study of
combustion performance and emissions of dual-fuel engines fueled with natural
gas/methanol and natural gas/gasoline. Energy 2021 Dec;237:121586. https://doi.
org/10.1016/j.energy.2021.121586.

[27] Sun J, Zhang X, Tang Q, Wang Y, Li Y. Knock recognition of knock sensor signal
based on wavelet transform and variational mode decomposition algorithm.
Energy Convers Manag 2023 Jul;287:117062. https://doi.org/10.1016/j.
enconman.2023.117062.

[28] Maurya RK, Maurya L, Luby. Reciprocating engine combustion diagnostics. Cham,
Switzerland: Springer International Publishing; 2019.

[29] Liu S, Lin Z, Zhang H, Lei N, Qi Y, Wang Z. Impact of ammonia addition on knock
resistance and combustion performance in a gasoline engine with high
compression ratio. Energy 2023 Jan;262:125458. https://doi.org/10.1016/j.
energy.2022.125458.

[30] Pham Q, Chang M, Kalwar A, Agarwal AK, Park S, Choi B, et al. Macroscopic spray
characteristics and internal structure studies of natural gas injection. Energy 2023
Jan;263:126055. https://doi.org/10.1016/j.energy.2022.126055.
[31] Hong M, Zhang J, Li X, Ouyang M. Effect of injection timing on backfire of port
injection hydrogen engine. SAE Tech Pap 2008. https://doi.org/10.4271/2008-01-
1788. 2008-01-1788).

[32] Luo Q he, Sun B gang. Inducing factors and frequency of combustion knock in
hydrogen internal combustion engines. Int J Hydrogen Energy 2016 Sep;41(36):
16296–305. https://doi.org/10.1016/j.ijhydene.2016.05.257.
[33] Park H, Shim E, Bae C. Improvement of combustion and emissions with exhaust gas
recirculation in a natural gas-diesel dual-fuel premixed charge compression
ignition engine at low load operations. Fuel 2019 Jan;235:763–74. https://doi.
org/10.1016/j.fuel.2018.08.045.

[34] Park H, Shim E, Lee J, Oh S, Kim C, Lee Y, et al. Comparative evaluation of
conventional dual fuel, early pilot, and reactivity-controlled compression ignition

H. Park et al. Energy 326 (2025) 136343

13
modes in a natural gas-diesel dual-fuel engine. Energy 2023 Apr;268:126769.
https://doi.org/10.1016/j.energy.2023.126769.
[35] Saxena S, Bedoya ID. Fundamental phenomena affecting low temperature
combustion and HCCI engines, high load limits and strategies for extending these
limits. Prog Energy Combust Sci 2013 Oct;39(5):457–88. https://doi.org/10.1016/
j.pecs.2013.05.002.

[36] Briggs T, Williams R. Zero impact engines: a demonstration of H2-ICE technologies
for zero-CO2 and near-zero Nox in the North American class 8 heavy-duty truck
market. In: 45th international Vienna motor symposium; 2024. https://doi.org/
10.62626/ws3g-faaf.

H. Park et al. Energy 326 (2025) 136343

14