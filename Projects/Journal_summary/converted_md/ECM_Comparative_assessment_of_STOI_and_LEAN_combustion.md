# ECM_Comparative assessment of STOI and LEAN combustion

Energy Conversion and Management 239 (2021) 114224

Available online 8 May 2021

0196-8904/© 2021 Elsevier Ltd. All rights reserved.

Comparative assessment of stoichiometric and lean combustion modes in

boosted spark-ignition engine fueled with syngas

Hyunwook Park a,*

, Junsun Lee b

, Narankhuu Jamsran a
, Seungmook Oh a,b
, Changup Kim a
,
Yonggyu Lee a,b
, Kernyong Kang a

a Department of Engine Research, Korea Institute of Machinery and Materials, Daejeon 34103, Republic of Korea

b Environment and Energy Mechanical Engineering, Korea University of Science and Technology, Daejeon 34113, Republic of Korea

ARTICLE INFO

Keywords:
Syngas

Hydrogen

Spark-ignition engine

Stoichiometric combustion
Lean combustion
Compression ratio

ABSTRACT

Synthesis gas (syngas) is considered an intermediate step between conventional carbon-based fuels and future
hydrogen-based fuels. Spark-ignition (SI) engines are suitable for converting the chemical energy of syngas for
small-scale electrical power generation. However, syngas-fueled SI engines have lower power outputs and
thermal efficiencies than SI engines fueled with conventional fuels such as gasoline and natural gas do. The
objective of this study was to compare the stoichiometric and lean combustion modes in a single-cylinder SI
engine to determine the optimal combustion mode for the development of a syngas engine generator with high
power and high efficiency. A high gross indicate power was achieved in the stoichiometric combustion mode by
increasing the intake pressure, owing to the increase in the volumetric efficiency and syngas fuel input. The gross
indicated thermal efficiency (ITE) improved as the compression ratio was increased from 10:1 to 17.1:1, owing to
the high peak heat release rate and short combustion duration. In the lean combustion mode, high gross ITEs
were achieved by increasing the excess air ratio to 2.5, but the additional increase led to low combustion efficiencies.
However, the gross indicated power decreased with an increase in the excess air ratio. The low gross
indicated power was increased through intake boosting. Based on a parametric study, the optimal compression
ratio for the stoichiometric combustion mode was selected to be 15:1. Pre-ignition occurred in the stoichiometric
combustion mode at a compression ratio of 17.1:1 and an intake pressure of 0.16 MPa. Engine operation with a
high compression ratio of 17.1:1 was possible in the lean combustion mode owing to the low combustion
temperature. The gross ITE in the lean combustion mode was 18.4% higher than that in the stoichiometric
combustion mode, mainly because of a significant reduction in the heat transfer loss. However, the gross indicated
power in the lean combustion mode was 25.6% lower than that in the stoichiometric combustion mode.

1. Introduction

With growing concerns regarding climate change due to the increase
in greenhouse gas emissions, interest in the use of low-carbon and
hydrogen (H2)-based fuels is increasing. Synthesis gas (syngas) is
considered an intermediate step in the transition from carbon-based
fuels to H2-based fuels [1]. Syngas is a fuel-gas mixture composed
mainly of H2 and carbon monoxide (CO). Syngas can be produced
directly through chemical processes such as steam methane reforming,
coal gasification, and biomass gasification, or obtained indirectly as a
by-product of these processes [2]. Various energy systems have been
developed to convert the chemical energy of syngas effectively into

electrical power [3]. Among these systems, an internal combustion engine
is a suitable option for producing heat and electricity simultaneously
[4]. Considering the recent increase in the demand for smallscale
distributed power generation, the combination of internal combustion
engine systems with gasification technology for syngas production
is regarded as a promising solution [5].

A compression-ignition (CI) engine is an obvious candidate for producing
electrical power because of its ability to burn syngas with various
fuel compositions [6]. Another merit of the CI engine is the use of a high
compression ratio, which ensures high thermal efficiency [7]. As it is
difficult to achieve autoignition of syngas in CI engines without intake
heating, dual-fuel combustion is normally adopted to ignite the syngas
[8]. In dual-fuel combustion, syngas is supplied with air during the

* Corresponding author at: Department of Engine Research, Korea Institute of Machinery and Materials, 156 Gajeongbuk-Ro, Yuseong-Gu, Daejeon 34103, Republic
of Korea.

E-mail address: hwpark@kimm.re.kr (H. Park).

Contents lists available at ScienceDirect

Energy Conversion and Management

journal homepage: www.elsevier.com/locate/enconman

https://doi.org/10.1016/j.enconman.2021.114224
Received 18 March 2021; Accepted 24 April 2021
Energy Conversion and Management 239 (2021) 114224

2

intake stroke, and diesel is injected into the syngas-air mixture during

the compression stroke to initiate syngas combustion. Dual-fuel combustion
is controlled by the diesel injection timing and the ratio of diesel
to syngas [9]. As syngas can be substituted for diesel fuel, dual-fuel
engines can reduce diesel consumption. Sahoo et al. conducted an
experimental study on a diesel-syngas dual-fuel engine with minor

modifications to the existing diesel engine design and operating parameters
[10]. Saving in diesel were assessed by varying the syngas
composition. As the H2 proportion increased in the syngas, the diesel
consumption decreased. A high diesel replacement of 72% was achieved
with only H2 at 80% engine load. The possibility of increasing the engine
thermal efficiency through dual-fuel combustion has also been reported
[11,12]. Rinaldini et al. experimentally investigated diesel-syngas dualfuel
combustion in a CI engine equipped with a common-rail injection
system [12]. The dual-fuel operation with syngas and diesel improved
the brake thermal efficiency compared with that under operation with
only diesel; the improvement was remarkable at higher loads. This can
be explained by the faster combustion in the dual-fuel mode during the
combustion-development stages, compared with that in the diesel mode.
Although the aforementioned diesel-syngas dual-fuel engines have

certain advantages, they also have some drawbacks. The syngas substitution
rate is limited to a certain level as additional syngas introduction
cannot simultaneously ensure high performance and low
emissions [1,13]. The fundamental problem with dual-fuel engines is

that diesel injection is necessary to initiate syngas combustion. However,
engine operation with only syngas is desirable considering the
growing demand for environmentally friendly electricity production
[14].

A homogeneous charge compression ignition (HCCI) engine is a
potentially viable energy system for electricity generation because it can
be operated using syngas alone. A high intake temperature, which is
usually achieved via gasifier heating or intake heating, and a high
compression ratio are required in an HCCI engine to ignite the syngas-air
mixture owing to the high autoignition temperature of this mixture [15].
HCCI engines are not only capable of 100% syngas operation but can
also be adapted for a wide range of fuel compositions [16]. However, it
is difficult to control the combustion timing in an HCCI engine, because

the combustion is controlled primarily by the chemical kinetics of syngas
[17]. Therefore, some concerns exist regarding the control of combustion
timing in response to variations in the syngas composition.
Power de-rating is also an important issue in HCCI engines [18]. Bhaduri

et al. assessed HCCI operation with syngas, which was obtained from a
two-stage downdraft gasifier, in a modified diesel engine [19]. Under

variations in the syngas composition reflecting the actual HCCI operation,
stable combustion was maintained by controlling the syngas flow
rate. The authors reported that an expensive and sophisticated incylinder
pressure sensor was required to control the combustion
phasing in the HCCI engine. However, the engine operation was
confined to low loads owing to the high pressure rise rate. Therefore,
high-load extension is required to commercialize HCCI engines for
electricity generation.

A spark-ignition (SI) engine is a technically viable solution for electricity
generation via syngas combustion, because it can compensate for
the aforementioned shortcomings of CI and HCCI engines. SI engines can
be operated with syngas alone because syngas combustion is controlled
by spark timings [20]. Commercial SI engines, such as gasoline and
natural gas engines, can be operated directly as syngas SI engines with

minimal modifications [21,22]. Raman et al. tested the load and efficiency
of an SI engine fueled with syngas obtained from fuel wood [21].
The fuel intake manifold and hydraulic governor of a natural gas SIbased
engine, which had a compression ratio of 12:1, were modified
for syngas operation. A maximum electrical power of 73 kW with an
overall efficiency of 21% was achieved by the syngas SI engine. The
authors also conducted SI engine operation with natural gas at high
loads. With the same compression ratio, the efficiency of the syngas
operation (21%) was lower than that of the natural gas operation (24%).
Indrawan et al. compared the overall efficiency and electrical power
achieved under natural gas and syngas operation in a two-cylinder SI
engine [22]. The efficiencies with syngas and natural gas were 21% and
23%, respectively, at an electrical power of 5 kW. While a maximum
load of 7 kW could be produced under natural gas operation, the syngas
engine generated a maximum load of 5 kW. A common finding with
regard to syngas SI engines is that they have lower power outputs and
thermal efficiencies than SI engines fueled with conventional fuels such
as gasoline and natural gas do.

Although SI engines are suitable for commercialization of syngas
engine generators through simple modifications, the development of a
dedicated engine design for syngas combustion is required to increase
the efficiency and power output. One common strategy for improving
the performance of SI engines is to increase the compression ratio [23].
As syngas has a high knock resistance, a high compression ratio can be

implemented in syngas SI engines [24]. Oh et al. experimentally investigated
the performance and emissions of a naturally aspirated SI engine
fueled with syngas over a wide range of compression ratios [25]. The
syngas composition was 70% H2, 15% CO, and 15% carbon dioxide
(CO2) by volume; thus, the fuel had a high proportion of H2. The gross
indicated thermal efficiency (ITE) increased from 46% to 51% with lean
combustion when the compression ratio was varied from 10:1 to 17:1.
However, the gross ITE decreased to 38% as the engine operation was
changed to stoichiometric combustion at the highest compression ratio
of 17:1, owing to the spark timing retardation for preventing backfire.
While the achievable maximum gross indicated mean effective pressure
(IMEP) increased with increasing compression ratio until a compression
ratio of 14:1, the additional increase in compression ratio reduced the
maximum gross IMEP. Another effective method to improve the thermal
efficiency of SI engines is lean combustion. As the low ignition energy
requirement of H2 in syngas can extend the lean flammability limit, lean
combustion with syngas enhances thermal efficiency [26]. Arroyo et al.
analyzed the combustion and performance of syngas operation in a
gasoline SI engine without any optimization of the syngas [27].
Although the thermal efficiencies increased under syngas operation with
lean combustion, the optimal excess air ratio for the thermal efficiency

was influenced by the syngas composition. The highest thermal efficiency
was achieved at an excess air ratio of 1.4 with syngas 2, which
was composed of 40% H2, 39% CO, 11% methane (CH4), and 10% CO2

by volume; however, the optimal excess air ratio was 1.2 with syngas 1,
which was composed of 23% H2, 23% CO, 26% CH4, and 28% CO2 by

Nomenclature

aTDC after top dead center
CAD crank angle degree
CH4 methane

CI compression ignition
CO carbon monoxide
CO2 carbon dioxide

ECU engine control unit
H2 Hydrogen

HCCI homogeneous charge compression ignition
IMEP indicated mean effective pressure

ISCO indicated specific carbon monoxide
ISNOX indicated specific nitrogen oxides
ITE indicated thermal efficiency
MBT maximum brake torque
NOX nitrogen oxides
O2 oxygen

rpm revolutions per minute
SI spark-ignition

THC total hydrocarbon

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

3

volume. Ran et al. compared ethanol, natural gas, and syngas as fuels for
lean combustion in a naturally aspirated SI engine [28]. Compared with
the ethanol and natural gas operations, the syngas operation had an
extended lean misfire limit; it also involved an excess air ratio of
1.3–4.0. Among those of the fuels tested, the ITE of syngas was the
highest, at 35%, at an excess air ratio of 2.0. Despite the high efficiency,
engine operation with syngas led to the lowest net IMEP owing to the
low volumetric efficiency under syngas operation and the lower heating
value of syngas.

While a dedicated engine design based on syngas properties can increase
efficiency and power output, most studies have investigated the
performance of syngas SI engines with minor modifications to existing
commercial engines. A high compression ratio and lean combustion can
be employed in syngas SI engines to improve their performance, because

syngas has a high knock resistance and low minimum energy requirement,
as mentioned earlier. Lean combustion is effective in improving
engine thermal efficiency owing to the high ratio of specific heats, but
the power output is reduced because of the reduction in fuel input into
the cylinder at a given intake pressure [25,27]. The objective of this
study was to compare the stoichiometric and lean combustion modes in
a boosted SI engine over various compression ratios, to determine the
optimal combustion mode for the development of a high-performance
syngas engine generator. To compensate for the low power output
associated with syngas engine operation, intake boosting, which has not
been considered in previous studies, was employed. SI engines fueled
with syngas have been operated under naturally aspirated conditions in
the literature [20–28]. In this study, optimal compression ratio, intake
manifold pressure, and excess air ratio for stoichiometric and lean
combustion modes were determined under boosted conditions. In
addition, an energy balance analysis was conducted at the optimum
engine operation of the two combustion modes to investigate the sources
of energy loss and their contributions.

2. Experiments and methods

2.1. Experimental setup

An experimental investigation was performed under stoichiometric
and lean combustion conditions in a single-cylinder SI engine that was
modified from a six-cylinder diesel engine. A diesel injector of the first
cylinder head was removed, and a spark plug (NGK, BKR6ES) was

installed on the diesel injector hole located at the center of the combustion
chamber. The other five cylinders were deactivated by drilling
holes in the pistons. The intake and exhaust manifolds of the base engine

were removed, and the intake and exhaust manifolds for syngas combustion
were manufactured and connected only to the first cylinder. The
detailed engine specifications are listed in Table 1. The bore and stroke
were 0.123 m and 0.155 m, respectively. The compression ratio was

varied from 13:1 to 17.1:1 by changing the combustion chamber geometry,
as shown in Fig. 1. Table 2 lists the properties of the syngas fuel
used in this study. The syngas was composed of 30% H2, 25% CO, and
45% CO2 by volume. The syngas composition was selected to reflect that
of the by-product generated during the Fisher-Tropsch process for coal

liquefaction.

A schematic diagram of the syngas engine setup is shown in Fig. 2.
Air was compressed using a compressor (EQ37, Nawootec, Republic of
Korea) and supplied to the intake manifold to increase the power output
of the syngas engine. The air flow was measured using a Coriolis flow
meter (CMFS050M, Emerson, United States). Syngas was obtained from
H2, CO, and CO2 containers and supplied to the intake manifold. The
quantities of H2, CO, and CO2 were measured using an H2 flow controller
(F-002AV, Bronkhorst, Netherlands), a CO flow controller (M3500V,
Line Tech, Republic of Korea), and a CO2 flow controller (M3500V, Line
Tech, Republic of Korea), respectively. The pressure of the syngas gas-air
mixture in the intake manifold was measured using an absolute pressure
sensor (MAP, Kefico, Republic of Korea). The in-cylinder pressure,
which varied with the syngas combustion, was measured using a
piezoelectric-type pressure transducer (6043A, Kistler, Switzerland).
The in-cylinder pressure was measured with a resolution of 0.2 crank
angle degree (CAD) using an angle encoder (ETU-427, AVL, Austria).
The pressure data was transferred to a combustion analyzer (619
Indimeter, AVL, Austria) to determine the parameters of the syngas
combustion. Combustion analysis was performed based on the pressure
data of 300 consecutive cycles for each set of tests. The engine-out
emissions were measured using a gas emission bench (AMA i60, AVL,

Austria), which was composed of several gas detectors. Total hydrocarbon
(THC) concentration was measured using a flame ionization
detector. Nitrogen oxides (NOX) concentration was measured using a
chemiluminescence detector. CO and CO2 concentrations were
measured using an infrared detector. Oxygen (O2) concentration was
measured using a paramagnetic detector. An engine control unit (ECU)
was used to monitor the sensors and control the spark timings during the
experiments. The specifications of the measurement equipment used in
this experiment are listed in Table 3.

2.2. Experimental method

Table 4 lists the experimental conditions used in this study. The
speed of the syngas engine was fixed at 1800 revolutions per minute
(rpm) to comply with the required electric power frequency of 60 Hz.
The coolant and oil temperatures were maintained at 353 ± 2 K and 358
± 3 K, respectively.

The experimental procedure for comparing the stoichiometric and
lean combustion modes is as follows. In the stoichiometric combustion
mode, the compression ratio was increased from 13:1 to 17.1:1 to
compensate for the lower thermal efficiency compared with that of the
lean combustion mode. The compression ratio of the base diesel engine
was 17.1:1. The highest compression ratio in the syngas SI engine was
selected as 17.1:1 to compare the performance of the diesel engine and
the syngas engine. The lower compression ratios of 15:1 and 13:1 were
selected to prevent knock and pre-ignition [23,25]. The intake pressure
was varied from 0.1 MPa to 0.16 MPa through the intake boosting to
increase the power output. In the lean combustion mode, the excess air
ratio was swept at intervals of 0.3 from 1.0 to 3.1 to maximize the
thermal efficiency. The excess air ratio was defined as the measured airto-fuel
ratio to the stoichiometric air-to-fuel ratio, as shown in Eq. (1):

Excess air ratio =

(

m˙ air/
m˙ Syngas)

( measured
m˙ air/
m˙ Syngas)

stoichiometry

(1)

where m˙ air and m˙ Syngas are the mass flow rates of air and syngas,
respectively. The intake pressure was also increased to 0.16 MPa to
compensate for the reduction in power output with increasing excess air
ratio. For each operating point, the spark timing was determined based
on the maximum brake torque (MBT) point. The optimal points of the
stoichiometric and lean combustion modes were selected based on the
performance and emission data obtained through the parametric studies

Table 1

Engine specifications.

Item Specification

Engine type Single-cylinder, heavy-duty, spark-ignition
Displacement [L] 1.84

Bore × stroke [m] 0.123 × 0.155

Compression ratio [− ] 13:1, 15:1, 17.1:1

Number of valves [− ] 2 (1 intake and 1 exhaust)
Intake valve opening [CAD aTDC] − 18
Intake valve closing [CAD aTDC] 214

Exhaust valve opening [CAD aTDC] − 226
Exhaust valve closing [CAD aTDC] 14

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

4

described above.

2.3. Analysis of energy balance

The energy balances for the stoichiometric and lean combustion
modes in the syngas SI engine were analyzed to compare the thermal
efficiencies and energy-loss sources of these modes comprehensively.
The chemical energy of the fuel in internal combustion engines comprises
the gross ITE, combustion loss, heat transfer loss, and exhaust loss
[29]. In this study, gross ITE was selected instead of net ITE to eliminate
the positive effects of the pumping work benefit caused by the intake
boost. The gross ITE was calculated using Eq. (2) [30]:

gross ITE = 3.6 × Pgross
m˙ Syngas × LHVSyngas

× 100 (2)

where Pgross is the gross indicated power of the syngas SI engine. The
gross indicated power is the power delivered to the piston during the
compression and expansion strokes. LHVSyngas is the lower heating value
of syngas. The combustion loss was calculated using Eq. (3) [31]:

Combustion loss = m˙ COLHVCO + m˙ H2LHVH2
m˙ SyngasLHVSyngas

(3)

where m˙ CO and m˙ H2 are the mass flow rates of CO and H2 in the engine
exhaust, respectively. The mass flow rate of H2 in the exhaust was
calculated based on the CO oxidation rate because of the absence of an
H2 analyzer. This calculation method was used because H2, CO, and CO2
were premixed in the chamber before being supplied to the engine
cylinder. LHVCO and LHVH2 are the lower heating values of CO and H2,
respectively. The exhaust loss was calculated using Eq. (4) [32]:

Exhaust loss = m˙ exh[hexh(Texh) − hamb(Tamb)]
m˙ SyngasLHVSyngas

(4)

where m˙ exh is the mass flow rate of the exhaust gas, and hexh and hamb
are the enthalpies at the exhaust gas temperature (Texh) and ambient
temperature (Tamb), respectively. The values of the enthalpies were
determined based on the National Institute of Standards and Technology
reference fluid thermodynamic and transport properties [33]. The
exhaust gas was assumed to be composed of H2, CO, CO2, O2, H2O, NO,
and N2. The heat transfer loss was calculated by subtracting the gross
ITE, combustion loss, and exhaust loss from the chemical energy of
syngas [32,34].

3. Results and discussion

3.1. Optimization of stoichiometric combustion

An SI engine fueled with syngas has a lower power output than one
fueled with conventional fuels, such as natural gas and gasoline, owing
to the low volumetric efficiency under syngas engine operation and the
low heating value of syngas. A large portion of the cylinder volume is
occupied by the syngas. To achieve a high power, it is more desirable to
operate a syngas SI engine under stoichiometric combustion than under
lean combustion. However, an important issue related to stoichiometric
combustion is the lower thermal efficiency compared with that under
lean combustion. Therefore, intake boosting and high compression ratios
were implemented in the stoichiometric operation to simultaneously
increase the volumetric efficiency and thermal efficiency. The
intake pressure was increased from 0.1 MPa to 0.16 MPa, and the
compression ratio was increased from 13:1 to 17.1:1. In this study, the
volumetric efficiency was defined as the mass flow rate of air into the
combustion chamber divided by the rate at which volume is displaced by
the piston, as shown in Eq. (5) [30].

Volumetric efficiency = 2 × m˙ air
ρair,intake × Vd × N × 100 (5)

where ρair,intake is the intake air density. The intake air density was
determined reflecting the air temperature in the intake manifold. Vd and
N are the engine displacement volume and engine rotational speed,
respectively.

Fig. 3 shows the gross indicated power under the stoichiometric
combustion according to the compression ratio and intake pressure. It
can be seen that pre-ignition occurred at a compression ratio of 17.1:1
and an intake pressure of 0.16 MPa. Knocking combustion is the spontaneous
autoignition of the unburned fuel–air mixture ahead of flame
propagation. Pre-ignition is a phenomenon in which the fuel–air mixture
is auto-ignited before the initiation of spark ignition. While knocking
combustion occurs after the spark-ignited flame propagation, preignition
is uncontrolled combustion that occurs before spark event
[30]. During the intake and compression strokes, pre-ignition can be
triggered by ignition sources such as hot spots in the intake manifold and
combustion chamber. The highest compression ratio and intake pressure
employed in this study produced a high ambient pressure and temperature
in the cylinder, which increased the possibility of pre-ignition
[35]. Therefore, spontaneous ignition of the syngas-air mixture
occurred before the spark was initiated.

As the intake pressure was increased, the gross indicated power
increased significantly. The high gross indicated power can be explained
by the increase in the volumetric efficiency and fuel input. Figs. 4 and 5
show the volumetric efficiency and fuel input under the stoichiometric
combustion according to the compression ratio and intake pressure. The
volumetric efficiency and fuel input increased with increasing intake
pressure for all compression ratios investigated. As the intake pressure

Fig. 1. Combustion chamber geometry.

Table 2

Syngas fuel properties.

Item Specification

Syngas composition by volume 30% H2, 25% CO, 45% CO2
Density @ 273 K [kg/m3
] 1.21
Lower heating value [MJ/Nm3
] 6.08

Stoichiometric air-to-fuel ratio [− ] 1.38

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

5

was increased from 0.1 MPa to 0.16 MPa at a compression ratio of 15:1,
the volumetric efficiency increased from 41.5% to 69.3%. The syngas
fuel input also increased from 31.5 m3
/h to 52.5 m3
/h. Therefore, the

gross indicated power increased from 20.6 kW to 34.7 kW. The gross
indicated power increased slightly as the compression ratio was
increased. Although the volumetric efficiency and fuel input remained
almost unchanged with increasing compression ratio, the thermal efficiency
improvement increased the gross indicated power. It can be
concluded that intake boosting is more effective for increasing the engine
power output compared to the increase in compression ratio.
Fig. 6(a) shows the gross ITE under the stoichiometric combustion
according to the compression ratio and intake pressure. The MBT spark
timing of the gross ITE is presented in Fig. 6(b). As the compression ratio
and intake pressure were increased, the MBT spark timing tended to be

Fig. 2. Schematic diagram of syngas engine setup.

Table 3
Specifications of measurement equipment.

Measured
parameters

Device Measurement
range

Linearity/
accuracy
Repeatability

THC AMA i60, AVL 0–20,000 ppm ≤± 1% of
FS*
≤± 0.5% of
NOX 0–5000 ppm FS*
CO 0–10 vol%
CO2 0–40 vol%
O2 0–25 vol%
Air flow rate CMFS050M,
Emerson
0–150 kg/h ≤± 0.25%
of MV**
≤± 0.2% of
MV**
H2 flow rate F-002AV,
Bronkhorst
0–20 m3
/h ≤± 0.5% of
MV**
≤± 0.2% of
MV**
CO flow rate M3500V, Line
Tech
0–24 m3
/h ≤± 1.0% of
FS*
≤± 0.25% of
MV**
CO2 flow
rate
M3500V, Line
Tech
0–30 m3
/h ≤± 1.0% of
FS*
≤± 0.25% of
MV**
In-cylinder
pressure
6043A, Kistler 0–25 MPa ≤± 0.5% of
FS*
–

*FS: full scale, **MV: measurement value.

Table 4
Experimental conditions.

Item Value
Engine speed [revolutions/minute] 1800
Coolant temperature [K] 353 ± 2
Oil temperature [K] 358 ± 3
Compression ratio [− ] 13:1, 15:1, 17.1:1
Intake pressure [MPa] 0.1–0.16 (0.2 sweep)
Excess air ratio [− ] 1.0–3.1 (0.3 sweep)
Spark timing [CAD aTDC] Corresponding to maximum brake torque

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

6

retarded. Whereas the increase in gross ITE with increasing intake
pressure was insignificant, an increase in compression ratio considerably
improved the gross ITE. It is known that for the ideal gas constantvolume
cycle, the engine thermal efficiency increases with increasing
compression ratio [30]. The increase in gross ITE can also be explained

via combustion analysis. Fig. 7 shows the heat release rate and combustion
parameters under the stoichiometric combustion according to
the compression ratio at an intake pressure of 1.0 MPa. In this study, the
start and end of combustion were defined as CA10 and CA90, respectively
[31]. CA10 and CA90 denote the crank angles where 10% and
90% of the total heat release occur, respectively. Although the fuel input
remained essentially constant with increasing compression ratio, the
peak heat release rate increased. The increase in compression ratio from
13:1 to 17.1:1 delayed the start of combustion but advanced the end of
combustion.

Under the compression ratio of 17.1:1, the combustion chamber had
a larger squish region and a smaller piston bowl than it did under the
other compression ratios, as shown in Fig. 1. This geometry led to
enhanced squish flow and turbulence [25]. As a result, the high-squish
flow with increasing compression ratio increased the combustion rate.
It can be concluded that the high peak heat release rate and short
combustion duration under the high compression ratio improved the
gross ITE. As the compression ratio was increased from 13:1 to 17.1:1 at
an intake pressure of 0.1 MPa, the gross ITE increased from 37.2% to
41.3%. Fig. 8 shows the heat release rate and combustion parameters
under the stoichiometric combustion according to the intake pressure at
a compression ratio of 13:1. The peak heat release rate increased with
increasing intake pressure, mainly because of the increase in the syngas
fuel input. However, the combustion duration remained almost unchanged
with increasing intake pressure, although it decreased with

Fig. 3. Gross indicated power under stoichiometric combustion versus
compression ratio and intake pressure.

Fig. 4. Volumetric efficiency under stoichiometric combustion versus
compression ratio and intake pressure.

Fig. 5. Fuel input under stoichiometric combustion versus compression ratio
and intake pressure.

Fig. 6. (a) Gross indicated thermal efficiency and (b) MBT spark timing under
stoichiometric combustion versus compression ratio and intake pressure.

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

7

increasing compression ratio. As the compression ratio was increased,
the increase in the unburned gas temperature due to piston compression
was significant [30]. However, the effect of increasing intake pressure
on the temperature rise of the unburned gas before spark event was
relatively small. The variations in the unburned gas temperature and
squish flow were smaller with increasing intake pressure than with
increasing compression ratio. Therefore, the increase in the intake
pressure did not have a significant effect on the combustion duration,
and the improvement in the gross ITE was minimal. Thus, for improving
the thermal efficiency of a syngas SI engine, increasing the compression
ratio is more desirable than intake boosting.

Figs. 9 and 10 show the NOX and CO emissions under stoichiometric

combustion according to the compression ratio and intake pressure,
respectively. As the compression ratio and intake pressure were
increased, the NOX emissions increased. The ambient pressure and
temperature before the initiation of combustion increased with

increasing compression ratio. Consequently, the peak combustion temperature
increased, resulting in high NOX emissions [23].

The increase in the intake pressure increased the ambient pressure
and temperature before combustion started, thereby increasing the
combustion temperature. The high intake pressure also increased the
syngas fuel input, as shown in Fig. 5. Therefore, more fuel chemical
energy was released as heat, which increased the maximum combustion

Fig. 7. Heat release rate (left) and combustion parameters (right) under stoichiometric combustion versus compression ratio at an intake pressure of 0.1 MPa.

Fig. 8. Heat release rate (left) and combustion parameters (right) under stoichiometric combustion versus intake pressure at a compression ratio of 13:1.

Fig. 9. Indicated specific nitrogen oxides (ISNOX) under stoichiometric combustion
versus compression ratio and intake pressure.

Fig. 10. Indicated specific carbon monoxide (ISCO) under stoichiometric
combustion versus compression ratio and intake pressure.

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

8

temperature and NOX emissions [36]. The CO emission increased as the
compression ratio and intake pressure were increased. Oxidation of CO
to CO2 is promoted at high combustion temperatures. The high

compression ratio and intake pressure increased the combustion temperature,
which contributed to a reduction in the CO emission. However,
as the compression ratio was increased from 13:1 to 17.1:1, the size of
the squish region increased, as shown in Fig. 1. Thus, a larger volume of
syngas could be quenched in the squish region [25]. Therefore, the CO
emission increased despite the high combustion temperature. Although
the high combustion temperature with increasing intake pressure could
contribute to the oxidization of CO in the cylinder, the high syngas fuel
input increased the CO emission. The syngas contained CO, unlike other
gaseous fuels such as natural gas and liquefied petroleum gas. Therefore,
the introduction of more CO during the intake stroke with increasing
intake pressure resulted in higher CO emission, despite the higher
combustion temperature. The THC emissions were negligible in the
syngas SI engine because the syngas contained no hydrocarbon species
[27,28].

3.2. Optimization of lean combustion

Lean combustion in an SI engine can significantly improve the
thermal efficiency compared with that under stoichiometric combustion.
Another advantage of lean combustion is the suppression of

abnormal combustion, such as knocking and pre-ignition [35]. However,
the engine power output under lean combustion is lower than that
under stoichiometric combustion. In this study, the excess air ratio was
varied from 1.0 to 3.1 to achieve lean combustion in the syngas engine
and thus improve the thermal efficiency. Since H2 in syngas has the
lowest ignition energy requirement compared to other fuels, such as
gasoline, ethanol, and natural gas, syngas SI engines can extend the lean
flammability limit [26]. The intake pressure was increased from 0.1 MPa
to 0.16 MPa to increase the engine power output.

Fig. 11 shows the gross indicated power under the lean combustion
according to the excess air ratio and intake pressure. Since no abnormal
combustion occurred under lean operation, the highest compression
ratio of 17.1:1 was employed to maintain a high thermal efficiency.
While pre-ignition occurred under stoichiometric operation at an intake
pressure of 0.16 MPa, under lean combustion, stable engine operation

without pre-ignition was observed owing to the low combustion temperature.
The gross indicated power decreased as the excess air ratio was
increased. This reduction can be determined based in the volumetric
efficiency and fuel input.

Figs. 12 and 13 show the volumetric efficiency and fuel input under
the lean combustion according to the excess air ratio and intake

pressure. As the excess air ratio was increased, the air input into the
cylinder increased, and the syngas fuel input decreased. Therefore, the
reduction in gross indicated power was due to a reduction in the
chemical energy and heat release from the syngas fuel. The low gross
indicated power under the lean combustion was offset by increasing the
intake pressure. As the intake pressure was increased from 0.1 MPa to
0.16 MPa at the excess air ratio of 2.2, the fuel input increased from 18.9
m3
/h to 33.0 m3
/h. Therefore, the gross indicated power increased from
14.6 kW to 25.8 kW.

Fig. 14(a) shows the gross ITE under the lean combustion according
to the excess air ratio and intake pressure. The MBT spark timing of the
gross ITE is presented in Fig. 14(b). As the excess air ratio was increased,
the spark timing had to be advanced to achieve the highest gross ITE.

While the MBT spark timings were similar with increasing intake pressure
at the excess air ratios of 1.0–1.9, they tended to be retarded when
the excess air ratio was greater than 2.2. As the excess air ratio was
increased, the gross ITE increased and then decreased after reaching its
maximum value. Under lean combustion, the engine thermal efficiency
is generally improved owing to the high ratios of specific heat and low

heat transfer losses in this mode [26]. However, the combustion efficiency
is reduced because of the low combustion temperature [37].
Fig. 15 shows the combustion efficiency under the lean combustion
according to the excess air ratio and intake pressure. As the excess air
ratio was increased, the combustion efficiency increased and reached a
peak value near the excess air ratio of 1.3, and then decreased. Although Fig. 11. Gross indicated power under lean combustion versus excess air ratio
and intake pressure at compression ratio of 17.1:1.

Fig. 12. Volumetric efficiency under lean combustion versus excess air ratio
and intake pressure at a compression ratio of 17.1:1.

Fig. 13. Fuel input under lean combustion versus excess air ratio and intake
pressure at a compression ratio of 17.1:1.

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

9

the low combustion temperature reduced the combustion efficiency
with an increase in the excess air ratio, the effect of a small amount of
excess O2 offset the effect of the reduction in combustion temperature
[28]. Hence, peak combustion efficiency was achieved near an excess air

ratio of 1.3. Until the gross ITE increased and reached its peak value with
increasing excess air ratio, the efficiency benefit of the lean combustion
outweighed the increase in the combustion loss. However, the high
combustion loss offset the benefit of lean combustion with an additional
increase in the excess air ratio. The influence of intake pressure on gross
ITE exhibited different trends depending on the excess air ratio. At low
excess air ratios, the change in gross ITE with increasing intake pressure
was insignificant. However, the gross ITE increased significantly with
increasing intake pressure at high excess air ratios. The gross ITE trends
are related to the combustion results. While the combustion efficiency
remained stagnant with increasing intake pressure at the excess air ratios
of 1.0–2.2, it increased when the excess air ratio was greater than
2.5.

Figs. 16 and 17 show the NOX emissions and peak bulk gas temperature
under the lean combustion according to the excess air ratio and
intake pressure. The peak bulk gas temperature was calculated by
assuming the fuel–air mixture in the cylinder as ideal gas [30]. The NOX

emissions decreased as the excess air ratio was increased. The NO formation
reaction is closely affected by combustion temperature, and
accelerates above 2000 K, which is well-known as the extended Zeldovich
mechanism [30]. The peak bulk gas temperature decreased significantly
as the excess air ratio was increased. Therefore, the low
combustion temperature at high excess air ratios reduced the NOX
emissions. The NOX emissions were less than 0.4 g/kWh when the excess
air ratio was greater than 2.2, regardless of the intake pressure.

Fig. 18 shows the CO emission under the lean combustion according
to the excess air ratio and intake pressure. As the excess air ratio was
increased, the CO emission decreased and reached a minimum value
near the excess air ratio of 1.3. The CO emission was low because of the
excess O2 and a sufficiently high combustion temperature.

3.3. Comparison of stoichiometric and lean combustion modes

The objective of this study was to compare the stoichiometric and
lean combustion modes in a single-cylinder syngas SI engine to determine
the optimal combustion mode for the development of a high-power
and high-efficiency engine generator. As mentioned in Section 3.1,
various compression ratios and intake pressures were employed under
stoichiometric combustion to increase the thermal efficiency and power
output. As explained in Section 3.2, various values of excess air ratio and
intake pressure were used to improve the thermal efficiency and power
output under lean combustion.

Table 5 summarizes the optimal values of the parameters for stoichiometric
and lean combustion. An intake pressure of 0.16 MPa
maximized the engine power output in both combustion modes. The

Fig. 14. (a) Gross indicated thermal efficiency and (b) MBT spark timing under
lean combustion versus excess air ratio and intake pressure at a compression
ratio of 17.1:1.

Fig. 15. Combustion efficiency under lean combustion versus excess air ratio
and intake pressure at a compression ratio of 17.1:1.

Fig. 16. Indicated specific nitrogen oxides (ISNOX) under lean combustion
versus excess air ratio and intake pressure at a compression ratio of 17.1:1.

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

10

optimal excess air ratio for lean combustion was 2.2. Although the
maximum gross ITE was achieved at the excess air ratio of 2.8, the gross
indicated power decreased significantly as the excess air ratio was
increased. In this study, the excess air ratio of 2.2 was selected because
the engine-out NOX emissions were below the value of the Stage V
emission standards for non-road engines. It is noted that the optimal
excess air ratio could be changed in consideration of the engine efficiency,
power, and exhaust emissions, depending on the purpose of the
engine application. The optimal compression ratios were determined to
be 15:1 under stoichiometric combustion and 17.1:1 under lean

combustion. Pre-ignition occurred in the stoichiometric combustion at a
compression ratio of 17.1:1 and an intake pressure of 0.16 MPa.
Therefore, the optimal compression ratio was reduced to 15:1 considering
pre-ignition and real-time changes in the composition of syngas
during actual operation of the engine generator. The gross ITE under
lean combustion was recorded as 46.3%, which was 18.4% higher than
that under stoichiometric combustion. An energy balance analysis was
conducted to investigate the sources of energy loss and their contributions.
Fig. 19 shows the energy balance for the stoichiometric and lean
combustion modes. The low heat transfer loss due to the low combustion
temperature in lean combustion was the main contributor to the
improvement in gross ITE. The exhaust loss in lean combustion was
slightly lower than that in stoichiometric combustion, which contributed
slightly to the improvement in gross ITE. However, the gross
indicated power in lean combustion was 25.8 kW, which was 25.6%
lower than that in stoichiometric combustion. At the intake pressure of
0.16 MPa, the syngas fuel input decreased under lean combustion owing
to the excess air introduced into the cylinder.

The volumetric efficiencies under the stoichiometric and lean combustion
modes were 69.3% and 95.8%, respectively. While the NOX
emissions were high in the stoichiometric combustion mode, the lean
combustion mode resulted in NOX emissions less than 0.4 g/kWh.
However, the high CO emission should be reduced using a CO oxidation
catalyst. Although the NOX and CO emissions were higher under stoichiometric
combustion than under lean combustion, the emissions can
be reduced effectively using an inexpensive three-way catalyst [30].

4. Conclusion

SI engines are advantageous for commercialization of syngas engine
generators with minimal changes in the existing engines. However,
previous studies have shown that syngas SI engines have lower power
outputs and thermal efficiencies than equivalent SI engines operating on
conventional fuels such as gasoline and natural gas do. Therefore, a
dedicated engine design for syngas combustion is required to address the
poor performance of syngas SI engines. The objective of this study was to
compare the stoichiometric and lean combustion modes in a singlecylinder
SI engine to determine the optimal combustion mode for the
development of a high-performance syngas engine generator.

High compression ratios and intake boosting were employed in the
stoichiometric combustion mode. A high gross indicated power was

Fig. 17. Peak bulk gas temperature under lean combustion versus excess air
ratio and intake pressure at a compression ratio of 17.1:1.

Fig. 18. Indicated specific carbon monoxide (ISCO) under lean combustion
versus excess air ratio and intake pressure at a compression ratio of 17.1:1.

Table 5

Comparison of stoichiometric and lean combustion at an intake pressure of 0.16
MPa.

Item Stoichiometric combustion Lean combustion
Excess air ratio [− ] 1.0 2.2

Compression ratio [− ] 15:1 17.1:1
MBT spark timing [CAD aTDC] − 20 − 24
Gross indicated efficiency [%] 39.1 46.3
Gross indicated power [kW] 34.7 25.8
Volumetric efficiency [%] 69.3 95.8
Fuel input [m3
/h] 52.5 33.0
ISNOX [g/kWh] 10.2 0.4
ISCO [g/kWh] 11.0 9.1

Fig. 19. Energy balance for stoichiometric and lean combustion modes at an
intake pressure of 0.16 MPa.

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

11

achieved by increasing the intake pressure owing to the increase in
volumetric efficiency and syngas fuel input. The gross indicated power
also increased slightly as the compression ratio was increased. The gross
ITE improved with increasing compression ratio owing to the high peak
heat release rate and short combustion duration.

Various excess air ratios and intake boosting were implemented in
the lean combustion mode. The peak gross ITEs were achieved near an
excess air ratio of 2.5. The gross ITE increased with an increase in excess
air ratio owing to high ratios of specific heat; however, the combustion
efficiency decreased significantly when the excess air ratio was greater
than 2.2. The gross indicated power decreased as the excess air ratio was
increased, owing to a drop in the chemical energy and heat release from
the syngas fuel. The low gross indicated power was increased through
intake boosting.

Optimal engine operating points were determined for the stoichiometric
and lean combustion modes to compare the performance and
emissions under these modes. The optimal compression ratio for stoichiometric
combustion was selected as 15:1 because of pre-ignition
occurring at a compression ratio 17.1:1 and an intake pressure of
0.16 MPa. However, the low combustion temperature under lean combustion
allowed the engine to operate at the compression ratio of 17.1:1.
The gross ITE under lean combustion was 18.4% higher than that under
stoichiometric combustion. An energy balance analysis revealed that a
significant reduction in heat transfer loss was the main contributor to the
high gross ITE under lean combustion. However, the gross indicated
power under lean combustion was 25.6% lower than that under stoichiometric
combustion. The NOX emissions were very low when the
excess air ratio was greater than 2.2.

In summary, stoichiometric operation using syngas is appropriate for
a high-power engine generator, whereas lean operation using syngas is
more suitable for a high-efficiency engine generator.

CRediT authorship contribution statement

Hyunwook Park: Conceptualization, Formal analysis, Writing -
original draft. Junsun Lee: Investigation, Data curation. Narankhuu
Jamsran: Investigation, Data curation. Seungmook Oh: Supervision.
Changup Kim: Methodology, Resources. Yonggyu Lee: Visualization.
Kernyong Kang: .

Declaration of Competing Interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Acknowledgements

The authors would like to acknowledge the Creative Allied Project
grant (No. CAP-16-06-KIER) of the National Research Council of Science
and Technology (NST) funded by the Ministry of Science and ICT of
Korea.

References

[1] Fiore M, Magi V, Viggiano A. Internal combustion engines powered by syngas: A
review. Appl Energy. 2020;276:115415. https://doi.org/10.1016/j.
apenergy.2020.115415.

[2] Liu K, Song C, Subramani V. Hydrogen and syngas production and purification
technologies. John Wiley & Sons 2010. https://doi.org/10.1002/9780470561256.
[3] Martinez S, Michaux G, Salagnac P, Bouvier JL. Micro-combined heat and power
systems (micro-CHP) based on renewable energy sources. Energy Convers Manage
2017;154:262–85. https://doi.org/10.1016/j.enconman.2017.10.035.
[4] Costa M, Di Blasio G, Prati MV, Costagliola MA, Cirillo D, La Villetta M, et al. Multiobjective
optimization of a syngas powered reciprocating engine equipping a
combined heat and power unit. Appl Energy 2020;275:115418. https://doi.org/
10.1016/j.apenergy.2020.115418.

[5] Wei L, Li X, Yang W, Dai Y, Wang C-H. Optimization of operation strategies of a
syngas-fueled engine in a distributed gasifier-generator system driven by

horticulture waste. Energy Convers Manage 2020;208:112580. https://doi.org/
10.1016/j.enconman.2020.112580.

[6] Roy MM, Tomita E, Kawahara N, Harada Y, Sakane A. Performance and emission
comparison of a supercharged dual-fuel engine fueled by producer gases with
varying hydrogen content. Int J Hydrogen Energy. 2009;34(18):7811–22. https://
doi.org/10.1016/j.ijhydene.2009.07.056.

[7] Sombatwong P, Thaiyasuit P, Pianthong K. Effect of pilot fuel quantity on the
performance and emission of a dual producer gas–diesel engine. Energy Procedia
2013;34:218–27. https://doi.org/10.1016/j.egypro.2013.06.750.
[8] Azimov U, Tomita E, Kawahara N, Harada Y. Effect of syngas composition on
combustion and exhaust emission characteristics in a pilot-ignited dual-fuel engine
operated in PREMIER combustion mode. Int J Hydrogen Energy 2011;36(18):
11985–96. https://doi.org/10.1016/j.ijhydene.2011.04.192.
[9] Rinaldini CA, Allesina G, Pedrazzi S, Mattarelli E, Tartarini P. Modeling and
optimization of industrial internal combustion engines running on Diesel/syngas
blends. Energy Convers Manage 2019;182:89–94. https://doi.org/10.1016/j.
enconman.2018.12.070.

[10] Sahoo BB, Sahoo N, Saha UK. Effect of H2: CO ratio in syngas on the performance
of a dual fuel diesel engine operation. Appl Therm Eng 2012;49:139–46. https://
doi.org/10.1016/j.applthermaleng.2011.08.021.

[11] Ramalingam S, Ezhumalai M, Govindasamy M. Syngas: Derived from biodiesel and
its influence on CI engine. Energy 2019;189:116189. https://doi.org/10.1016/j.
energy.2019.116189.

[12] Rinaldini CA, Allesina G, Pedrazzi S, Mattarelli E, Savioli T, Morselli N, et al.
Experimental investigation on a Common Rail Diesel engine partially fuelled by
syngas. Energy Convers Manage 2017;138:526–37. https://doi.org/10.1016/j.
enconman.2017.02.034.

[13] Dasappa S, Sridhar HV. Performance of a diesel engine in a dual fuel mode using
producer gas for electricity power generation. Int J Sustainable Energy 2013;32(3):
153–68. https://doi.org/10.1080/14786451.2011.605945.

[14] Kan X, Zhou D, Yang W, Zhai X, Wang CH. An investigation on utilization of biogas
and syngas produced from biomass waste in premixed spark ignition engine. Appl
Energy. 2018;212:210-22. https://doi.org/10.1016/j.apenergy.2017.12.037.
[15] Yamasaki Y, Kaneko S. Prediction of ignition and combustion development in an
HCCI engine fueled by syngas. SAE Tech Pap 2014–32-0002. https://doi.org/
10.4271/2014-32-0002.

[16] Wiemann S, Hegner R, Atakan B, Schulz C, Kaiser SA. Combined production of
power and syngas in an internal combustion engine–Experiments and simulations
in SI and HCCI mode. Fuel 2018;215:40–5. https://doi.org/10.1016/j.
fuel.2017.11.002.

[17] Przybyla G, Szlek A, Haggith D, Sobiesiak A. Fuelling of spark ignition and
homogenous charge compression ignition engines with low calorific value
producer gas. Energy 2016;116:1464–78. https://doi.org/10.1016/j.
energy.2016.06.036.

[18] Bhaduri S, Contino F, Jeanmart H, Breuer E. The effects of biomass syngas
composition, moisture, tar loading and operating conditions on the combustion of
a tar-tolerant HCCI (Homogeneous Charge Compression Ignition) engine. Energy
2015;87:289–302. https://doi.org/10.1016/j.energy.2015.04.076.
[19] Bhaduri S, Berger B, Pochet M, Jeanmart H, Contino F. HCCI engine operated with
unscrubbed biomass syngas. Fuel Process Technol 2017;157:52–8. https://doi.org/
10.1016/j.fuproc.2016.10.011.

[20] Enomoto H, Saito K. Effects of the hydrogen and methane fractions in biosyngas on
the stability of a small reciprocated internal combustion engine. Energy 2020;213:
118518. https://doi.org/10.1016/j.energy.2020.118518.
[21] Raman P, Ram NK. Performance analysis of an internal combustion engine
operated on producer gas, in comparison with the performance of the natural gas
and diesel engines. Energy 2013;63:317–33. https://doi.org/10.1016/j.
energy.2013.10.033.

[22] Indrawan N, Thapa S, Bhoi PR, Huhnke RL, Kumar A. Engine power generation and
emission performance of syngas generated from low-density biomass. Energy
Convers Manage 2017;148:593–603. https://doi.org/10.1016/j.
enconman.2017.05.066.

[23] Porpatham E, Ramesh A, Nagalingam B. Effect of compression ratio on the
performance and combustion of a biogas fuelled spark ignition engine. Fuel 2012;
95:247–56. https://doi.org/10.1016/j.fuel.2011.10.059.

[24] Bika AS, Franklin L, Kittelson DB. Engine knock and combustion characteristics of a
spark ignition engine operating with varying hydrogen and carbon monoxide
proportions. Int J Hydrogen Energy 2011;36(8):5143–52. https://doi.org/
10.1016/j.ijhydene.2011.01.039.

[25] Oh S, Kim C, Lee Y, Yoon S, Lee J, Kim J. Experimental investigation of the
hydrogen-rich offgas spark ignition engine under the various compression ratios.
Energy Convers Manage 2019;201:112136. https://doi.org/10.1016/j.
enconman.2019.112136.

[26] Ran Z, Hariharan D, Lawler B, Mamalis S. Experimental study of lean spark ignition
combustion using gasoline, ethanol, natural gas, and syngas. Fuel 2019;235:530–7.
https://doi.org/10.1016/j.fuel.2018.08.054.

[27] Arroyo J, Moreno F, Munoz ˜ M, Monn´e C, Bernal N. Combustion behavior of a spark
ignition engine fueled with synthetic gases derived from biogas. Fuel 2014;117:
50–8. https://doi.org/10.1016/j.fuel.2013.09.055.

[28] Ran Z, Hariharan D, Lawler B, Mamalis S. Exploring the potential of ethanol, CNG,
and syngas as fuels for lean spark-ignition combustion-An experimental study.
Energy 2020;191:116520. https://doi.org/10.1016/j.energy.2019.116520.
[29] Olmeda P, García A, Monsalve-Serrano J, Sari RL. Experimental investigation on
RCCI heat transfer in a light-duty diesel engine with different fuels: Comparison
versus conventional diesel combustion. Appl Therm Eng 2018;144:424–36.
https://doi.org/10.1016/j.applthermaleng.2018.08.082.

H. Park et al.
Energy Conversion and Management 239 (2021) 114224

12

[30] Heywood JB. Internal combustion engine fundamentals. New York: Mcgraw-hill;
1988.

[31] Park H, Shim E, Bae C. Improvement of combustion and emissions with exhaust gas
recirculation in a natural gas-diesel dual-fuel premixed charge compression
ignition engine at low load operations. Fuel 2019;235:763–74. https://doi.org/
10.1016/j.fuel.2018.08.045.
[32] Park H, Shim E, Bae C. Expansion of low-load operating range by mixture
stratification in a natural gas-diesel dual-fuel premixed charge compression
ignition engine. Energy Convers Manage 2019;194:186–98. https://doi.org/
10.1016/j.enconman.2019.04.085.
[33] Lemmon EW, Huber ML, McLinden MO. NIST reference fluid thermodynamic and
transport properties–REFPROP. NIST standard reference database 2002;23:v7.
[34] Dempsey AB, Walker NR, Reitz R. Effect of piston bowl geometry on dual fuel
reactivity controlled compression ignition (RCCI) in a light-duty engine operated

with gasoline/diesel and methanol/diesel. SAE Int J Engines 2013;6(1):78–100.
https://doi.org/10.4271/2013-01-0264.
[35] Wang Z, Liu H, Reitz RD. Knocking combustion in spark-ignition engines. Prog
Energy Combust Sci 2017;61:78–112. https://doi.org/10.1016/j.
pecs.2017.03.004.

[36] Ma F, Ding S, Wang Y, Wang Y, Wang J, Zhao S. Study on combustion behaviors
and cycle-by-cycle variations in a turbocharged lean burn natural gas SI engine
with hydrogen enrichment. Int J Hydrogen Energy 2008;33(23):7245–55. https://
doi.org/10.1016/j.ijhydene.2008.09.016.
[37] Yan B, Yao M, Mao B, Li Y, Qin Y. A comparative study on the fuel economy
improvement of a natural gas SI engine at the lean burn and the stoichiometric
operation both with EGR under the premise of meeting EU6 emission legislation.
SAE Tech Pap 2015–01-1958. https://doi.org/10.4271/2015-01-1958.

H. Park et al.