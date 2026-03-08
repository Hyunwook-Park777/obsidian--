# ECM_Expansion of low-load operating range by mixture stratification

Contents lists available at ScienceDirect

Energy Conversion and Management

journal homepage: www.elsevier.com/locate/enconman

Expansion of low-load operating range by mixture stratification in a natural

gas-diesel dual-fuel premixed charge compression ignition engine

Hyunwook Park, Euijoon Shim, Choongsik Bae⁎

Department of Mechanical Engineering, KAIST (Korea Advanced Institute of Science and Technology), Republic of Korea

ARTICLE INFO

Keywords:
Duel fuel
PCCI

Natural gas
Diesel fuel
Low load

Mixture stratification

ABSTRACT

Dual-fuel premixed charge compression ignition (DF-PCCI) combustion can achieve low nitrogen oxides (NOX)
and particulate matter (PM) emissions for wide ranges of engine operations. However, the deterioration in
thermal efficiency, and hydrocarbon (HC) and carbon monoxide (CO) emissions at low loads were recognized as
the barriers for expanding the low-load operating range. In this study, the causes of the barriers were investigated
and a mixture preparation strategy was suggested for overcoming the barriers in a natural gas (NG)-
diesel DF-PCCI engine. Combustion and energy balance analysis was conducted to evaluate the strategy. Baseline
DF-PCCI was determined by combinations of diesel start of injection (SOI) and NG substitution ratio (SR) at low
loads from 0.3 to 0.6 MPa indicated mean effective pressure (IMEP). An increase in the homogeneity of a fuel-air
mixture in the baseline DF-PCCI effectively reduced the NOX and PM emissions but increased the HC and CO
emissions in each low-load operation. As the engine load was decreased, the formation of an overly-lean mixture
intensified the effects of the mixture homogeneity. Therefore, the thermal efficiency, and HC and CO emissions
deteriorated at 0.3 MPa IMEP. A mixture stratification strategy was established to increase the local equivalence
ratio and reactivity of the fuel-air mixture. The strategy was realized by a retarded diesel SOI, a lower NG SR,
and a higher exhaust gas recirculation rate. The strategy increased the degree of constant volume combustion by
enhancing the combustion performance. The enhanced combustion reduced the combustion loss, and thus,
improved the thermal efficiency. The HC and CO emissions also decreased mainly due to the improved combustion
and the reduced mass flow rates of the NG.

1. Introduction

Diesel engines have been widely used as power sources in transportation
because of their high thermal efficiency and torque. However,
as standards for carbon dioxide (CO2) and other harmful emissions are
stringent in transportation, there is a demand for improved efficiency
and reduced exhaust emissions in diesel engines. In particular, the reduction
in nitrogen oxides (NOX) and particulate matter (PM) emissions
from the diesel engines is an issue of growing importance. Currently,
diesel engines should be equipped with after-treatment devices to meet
the EURO VI emission legislation. Although the after-treatment devices
are attractive tools for reducing the NOX and PM emissions, their

implementation increases vehicle cost and deteriorates the fuel
economy [1]. Therefore, reducing emissions through in-cylinder combustion
technology is also required to ease the burden of after-treatment
systems.

For conventional diesel combustion (CDC), NOX is generated at the
boundary of the diffusion flame, which is characterized by a stoichiometric
fuel-air mixture and high temperature [2]. The PM is formed in
regions with high equivalence ratios and high temperatures. In an attempt
to reduce the NOX and PM emissions from the CDC, diesel-based
in-cylinder combustion concepts, such as homogeneous charge compression
ignition (HCCI), premixed charge compression ignition (PCCI),
and low temperature combustion (LTC), have been developed. These

https://doi.org/10.1016/j.enconman.2019.04.085

Received 24 February 2019; Received in revised form 25 April 2019; Accepted 27 April 2019

Abbreviations: aTDC, after top dead center; CAD, crank angle degree; CDC, conventional diesel combustion; CO, carbon monoxide; CO2, carbon dioxide; COV,
coefficient of variation; DF-PCCI, dual-fuel premixed charge compression ignition; DOCV, degree of constant volume; EGR, exhaust gas recirculation; HC, hydrocarbon;
HCCI, homogeneous charge compression ignition; HRR, heat release rate; IMEP, indicated mean effective pressure; ITE, indicated thermal efficiency; LHV,
lower heating value; LTC, low temperature combustion; MPRR, maximum pressure rise rate; NG, natural gas; NOX, nitrogen oxides; PCCI, premixed charge compression
ignition; PPC, partially premixed combustion; PM, particulate matter; SOI, start of injection; SR, substitution ratio; TDC, top dead center; THC, total
hydrocarbon

⁎ Corresponding author at: Department of Mechanical Engineering, KAIST (Korea Advanced Institute of Science and Technology), 291 Daehak-ro, Yuseong-gu,
Daejeon 34141, Republic of Korea.

E-mail address: csbae@kaist.ac.kr (C. Bae).

Energy Conversion and Management 194 (2019) 186–198

0196-8904/ © 2019 Elsevier Ltd. All rights reserved.

T
concepts reduced the NOX and PM emissions simultaneously due to the
reduction in combustion temperature of premixed fuel-air charges [3].
Fuel conversion efficiency was improved in these combustion concepts

mainly through the optimized thermodynamic cycles and the reduction
in heat losses [4]. However, there have been some challenges in commercializing
the combustion concepts. The combustion phasing control
was limited because chemical kinetics dominated the auto-ignition of

the premixed fuel-air mixture [5]. The operating range was confined to
low loads because the rapid volumetric combustion of the premixed
mixture resulted in high levels of in-cylinder pressure and maximum
pressure rise rate (MPRR) during high-load operations [6]. Gasolinebased
in-cylinder combustion concepts, such as gasoline HCCI and gasoline
partially premixed combustion (PPC), were suggested to address
the limited high-load operating range in the diesel-based combustion

concept. Gasoline is beneficial for fuel-air mixing because of its high
volatility and high resistance of auto-ignition [7]. Therefore, a higher
engine load was achieved in the gasoline PPC than in the diesel-based
in-cylinder combustion [8]. However, combustion instability, and excessive
hydrocarbon (HC) and carbon monoxide (CO) emissions were
drawbacks in low-load operations of the gasoline PPC [9]. The sparkassisted
combustion concept [10] and negative valve overlap [11] were
effective in lessening these drawbacks, but the NOX emissions reached
unacceptable levels. When only one fuel was applied to the in-cylinder

combustion concept, the engine operation was limited to specific ranges
[12].

Dual-fuel premixed charge compression ignition (DF-PCCI) concepts
blend two fuels having different reactivity in the combustion chamber
[13]. In the DF-PCCI concepts, the equivalence ratio and reactivity of a
fuel-air charge were controlled by modulating the fuel start-of-injection

(SOI) timing and the blending ratio between the two fuels [14]. While
single-fuel in-cylinder combustion concepts stratified the equivalence

ratio alone to achieve the high-load operations [15], fuel reactivity, in
addition to the equivalence ratio, stratification was employed for expanding
the high-load operating range in the DF-PCCI concepts [16].
The reactivity stratification led to the staged auto-ignition of the highreactivity
fuel and the low-reactivity fuel, which reduced the peak heat
release rate (HRR) and MPRR [17]. The reactivity and equivalence ratio
stratification in the DF-PCCI concept also led to an improvement in the
combustion phasing control [18]. Previous studies have shown that
simultaneous reduction in NOX and PM emissions can be achieved in
gasoline-diesel DF-PCCI engines at wide ranges of engine speeds and
loads [19–21]. A combination of diesel SOI and a blending ratio,
without exhaust gas recirculation (EGR), achieved low NOX and PM
emissions at low loads [19]. An advanced diesel SOI, a higher gasoline
portion, and a higher EGR rate were implemented as the load was increased
in order to reduce the high in-cylinder pressure and MPRR [20].
Although the engine was operated at a wider range of engine speeds
and loads in gasoline-diesel DF-PCCI concepts than in single-fuel incylinder
combustion concepts, the full-load operation was limited [21].
Miller cycle strategies [22] and a late diesel SOI [23] effectively reduced
the peak in-cylinder pressure and MPRR at the full-load operation,
but the NOX levels increased. The engine operation at low loads
also exposed shortcomings in the gasoline-diesel DF-PCCI concepts. The
thermal efficiency and HC and CO emissions deteriorated substantially

more in the DF-PCCI concept than in diesel CDC [24] and diesel LTC
[25].

Natural gas (NG) is considered as an alternative to conventional
petroleum because the low-carbon fuel can potentially lead to a reduction
in CO2 emissions in transportation [26]. The NG in the DF-PCCI
combustion concept is an attractive option because its high octane
number can be an advantage in expanding the high-load operating

range. Walker et al. [27] used experimental methods to evaluate the
potential for expanding the high-load limit in NG-diesel DF-PCCI mode.
A comparative analysis between gasoline-diesel and NG-diesel DF-PCCI

modes was conducted in a single-cylinder, heavy-duty engine by imposing
a constraint of MPRR. A lower peak HRR and wider combustion

duration led to the achievement of a higher load operation in the NGdiesel
DF-PCCI mode than in the gasoline-diesel DF-PCCI mode. The
combustion behavior was due to its lower reactivity than that of gasoline.
Nieman et al. [28] simulated an NG-diesel DF-PCCI engine at
broad ranges of engine operations using computational fluid dynamics
(CFD) software with the CHEMKIN. A larger reactivity difference of NG
and diesel than that of gasoline and diesel allowed the engine operation

up to 23 bar indicated mean effective pressure (IMEP) with low NOX
and PM emissions. However, the authors also pointed out that the low

reactivity of NG can be a disadvantage at low loads. Although low NOX
and PM emissions were achieved with diesel SOI and the blending ratio
of NG and diesel at the load range from 4 to 13.5 bar IMEP, the combustion
mode suffered from the deterioration in gross indicated efficiency,
and HC and CO emissions at 4 bar IMEP. Doosje et al. [29]
explored the potential for expansion to low-load operating range in the
DF-PCCI concept fueled with NG and diesel. As the engine load was
decreased, low NOX and PM emissions were retained. However, the fuel
consumption increased sharply at the lowest load investigated mainly
because of the increased losses in friction and combustion. Ansari et al.
[30] used empirical models to compare NG-diesel DF-PCCI mode to
CDC in a four-cylinder, light-duty engine. The models were created
based on a regression analysis of experimental data to assess the operational
cost and emissions of the two combustion modes. The DFPCCI
mode was more suitable than the CDC mode for the medium- to
high-load operations, mainly due to the superior fuel economy, and low
NOX and PM emissions. But the CDC was the optimal combustion mode
at low loads because the DF-PCCI mode led to a deterioration in fuel
consumption, low exhaust gas temperature, and high HC and CO
emissions. Hutter et al. [31] analyzed the factors that reached the lowload
limit in an NG-diesel DF-PCCI engine. Although the DF-PCCI mode
has the advantage of having lower CO2 emissions than CDC mode
owing to the low carbon-to-hydrogen ratio of NG, the advantage disappeared
as the engine load was decreased to the low-load limit. HC
emissions also increased sharply. Throttling effectively reduced the HC
emissions by increasing the equivalence ratio of the fuel-air charge.
However, the CO2 emissions increased due to the pumping loss in the
throttled operation. Li et al. [32] performed experimental investigations
in a six-cylinder NG-diesel DF-PCCI engine at 5.5 bar brake mean
effective pressure (BMEP). In the premixed DF-PCCI combustion mode,
which was realized by advancing the diesel SOI, there was higher
thermal efficiency and lower HC emissions than in conventional diffusive
dual-fuel combustion. In the DF-PCCI combustion mode, an advanced
diesel SOI, a large EGR rate, and a moderate equivalence ratio

were favorable for increasing thermal efficiency and reducing HC
emissions. Gharehghani et al. [33] compared NG-biodiesel DF-PCCI
combustion to NG-diesel DF-PCCI combustion in a single-cylinder engine
at low loads. In both combustion modes, as the engine load was

decreased, the HC and CO emissions increased. Superior thermal efficiency
and emissions were achieved in the NG-biodiesel DF-PCCI mode
than in the NG-diesel DF-PCCI mode because the higher oxygen content
and cetane number in biodiesel improved the combustion quality and
thus reduced the combustion loss.

Substantial studies have pointed out the barriers arising from lowload
operations of DF-PCCI engines, namely, the deterioration in
thermal efficiency, and HC and CO emissions. NG has lower reactivity
than gasoline, and although this intensified the barriers at the low
loads, very few studies addressed the causes and solutions for the
barriers in NG-diesel DF-PCCI combustion mode. Therefore, the objective
of this study is to investigate the causes of the barriers to the expansion
of the low-load operating range in an NG-diesel DF-PCCI engine
and to suggest a strategy for overcoming the barriers in terms of
fuel-air mixture preparation. The experimental study was conducted in
a heavy-duty compression-ignition engine. The engine was operated in
the DF-PCCI mode fueled with NG and diesel over a low-load range
from 0.3 to 0.6 MPa IMEP. Combustion and energy balance was analyzed
to find the causes of the barriers and to evaluate the mixture

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

187
preparation strategy. A wide range of diesel SOI and the blending ratio
of the two fuels was applied over the low loads to identify the barriers
to the expansion of the low-load operating range and their causes. In
response to the identified causes, a mixture preparation strategy was
established and evaluated in terms of performance and emissions.
Diesel SOI, a blending ratio of the NG and diesel, and an EGR rate were
used to determine the optimization of the mixture preparation at each
load.

2. Experimental setup and conditions

2.1. Experimental setup

A six-cylinder, heavy-duty, compression-ignition engine was modified
to a single-cylinder engine for the experimental investigation with
NG-diesel DF-PCCI combustion. The specifications of the engine and
diesel injector are given in Tables 1 and 2, respectively. The engine was
equipped with a common-rail, direct-injection system consisting of a
high-pressure pump, a common-rail, and a solenoid-type injector. A
cooled-EGR system, consisting of an EGR valve and an EGR cooler, was
also installed. The EGR cooler was used to reduce the gas temperature
in the downstream of the EGR system and to fix the air temperature at
the intake port. The EGR rate in this study was obtained by measuring
the concentrations of CO2 in the exhaust gas and the intake air. The
definition of the EGR rate is shown in Eq. (1).

= −
− EGR rate ×
CO CO
CO CO [%] 100 intake ambient
exhaust ambient
2, 2,
2, 2, (1)

Tables 3 and 4 presents the properties of the diesel and NG implemented
in this investigation, respectively. The previous study of the
authors contains a detailed description of the fuels [34]. The experimental
setup is illustrated in Fig. 1. The NG used as a low-reactivity fuel
was introduced into the cylinder during the intake stroke to form a
well-mixed NG-air mixture. An NG mass flow controller (Bronkhorst, F202AV)
and an air mass flow meter (Bronkhorst, F-106AI) were used to
record the mass flow rates of the NG and air, respectively. The diesel
used as a high-reactivity fuel was injected directly into the combustion
chamber during the compression stroke, and it acted as an ignition
source. A fuel consumption meter (AVL, 733S) was used to record the
mass flow rate of the diesel. A piezoresistive type pressure sensor

(Kistler, 4045A5) and a piezoelectric type pressure sensor (Kistler,
6052C) were implemented to measure the intake and in-cylinder
pressure, respectively. An exhaust gas analyzer (Horiba, Mexa-7100
DEGR) was used to determine the engine-out emissions, including NOX,
total HC (THC), CO, CO2, and O2. The NOX and THC concentrations in
the exhaust gas were measured by chemiluminescence detection and
flame ionization detection methods, respectively. A non-dispersive infrared
method was used to measure the CO and CO2 concentrations.
Magneto-pneumatic detection was used to measure the O2 concentration.
A smoke meter (AVL, 415S) was used to determine the engine-out
smoke emissions. The specifications of measurement equipment are
presented in Table 5. A combustion analyzer (NI, cROI-9024) was used
to record and process the measured values at a sampling rate of 0.2
crank angle degree (CAD). The pulse for each 0.2 CAD was generated by
an optical rotary encoder (Autonics, E40S) installed on the crankshaft.
In this study, the NG substitution ratio (SR) was defined to represent
the in-cylinder blending ratio between the NG and diesel. The NG SR
was calculated based on the mass flow rate and lower heating value
(LHV) of each fuel, as shown in Equation (2).

= +
NG SR ×
m LHV
m LHV m LHV [%] ̇
̇ ̇ 100 NG NG
NG NG Diesel Diesel (2)

where ṁ
NG and ṁ
Diesel are the mass flow rates of the NG and diesel,
respectively. LHVNG and LHVDiesel are the LHVs of the NG and diesel,
respectively. The equivalence ratio of the DF-PCCI concept was calculated
by Equation (3) [35].

− = + Equivalence ratio m AFR m AFR
m [ ] ̇ ̇
̇
NG NG Diesel Diesel
air (3)

where ṁ
air is the mass flow rate of the air. AFRNG and AFRDiesel are the
stoichiometric air-to-fuel ratios of the NG and diesel, respectively.

2.2. Analysis of combustion and energy balance

In this study, an analysis of combustion and energy balance was
conducted to understand the combustion phenomena occurring in the

Table 1

Engine specifications.

Item Specification

Engine type Single-cylinder, compression-ignition, directinjection,
naturally aspirated, heavy-duty
Combustion chamber shape Re-entrant bowl
Displacement [L] 0.981
Bore [mm] 100
Stroke [mm] 125
Compression ratio [-] 17.4

Fuel injection equipment Common-rail direct-injection system
EGR system Cooled-EGR

Table 2

Diesel injector specifications.

Item Specification

Injector type Solenoid injector
Number of holes 8
Nozzle hole diameter [mm] 0.146
Injection angle [o
] 146
Hydraulic flow rate (HFR*
) [cm3
/30 s] 460
Minimum injection quantity [mg/stroke] 2

* HFR: diesel fuel volume flowing through an injector nozzle over a specified
period of time

Table 3

Properties of diesel.

Item Value

Density at 293 K [kg/m3] 826
Cetane number [-] 52.1
Lower heating value [MJ/kg] 42.5
T10* (K) 508
T50* (K) 562
T90* (K) 616
Stoichiometric air-to-fuel ratio 14.5

* T10, T50, T90: the temperature at which 10%, 50%, and
90% of fuel evaporates

Table 4

Properties of natural gas.

Item Value

Methane (CH4) [%] 91.31
Ethane (C2H6) [%] 5.34
Propane (C3H8) [%] 2.17
I-Butane (i-C4H10) [%] 0.46
N-Butane (n-C4H10) [%] 0.48
I-Pentane (i-C5H10) [%] 0.016
N-Pentane (n-C5H10) [%] 0.002
Nitrogen (N2) [%] 0.222
Motor octane number (MON) [-] 124
Methane number (MN) [-] 81.7
Lower heating value (LHV) [MJ/Nm3
] 38.5
Gas density [kg/Nm3
] 0.829
Stoichiometric air-to-fuel ratio 16.9

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

188
DF-PCCI engine and, thus, to assess the efficiency of the energy conversion
in the engine.

The measured pressure traces were used to acquire the net HRR
[36]. The in-cylinder pressure profile for the HRR analysis was acquired
through ensemble averaging the pressure data of 100 consecutive cycles
for each set of experimental conditions. A smoothing equation was
applied to the in-cylinder pressure profile because the first derivative of
pressure with respect to CAD was noisy [37]. The smoothing seems to
offer a logical compromise between tracking meaningful pressure signal
information and avoiding the noisy derivative term [38]. Combustion
parameters, such as CA10, CA50, and CA90, were calculated to quantify
combustion phasing and combustion duration. The CA10, CA50, and

CA90 were defined as the crank angle where 10%, 50%, and 90% of the
total (cumulative) heat is released, respectively. CA50 represented the
combustion phasing, and the combustion duration was determined by
the difference between CA90 and CA10.

Degree of constant volume (DOCV) was used to quantify the heat
release characteristic of the DF-PCCI combustion. In order to obtain
high thermal efficiency in internal combustion engines, the heat is released
for a short combustion duration near the TDC [6,39]. The DOCV
is a quantification of the constant-volume combustion ratio in actual
engine combustion compared to the theoretical Otto cycle, as shown in
Eq. (4) [40].

= ∫ ⎧
⎨
⎩
− ⎡
⎣
⎢
+ ⎤
⎦
⎥
⎫
⎬
⎭
−
Degree of constant volume η Q
V V
V θ
dQ
dθ
dθ 1 1
( ) Otto
d c
1 γ

(4)

where ηOtto is the theoretical efficiency of Otto-cycle, and Q is the cumulative
heat release. Vd and Vc are the displacement and clearance
volume, respectively. dQ/dθ is the HRR.

The fuel energy in internal combustion engines consists of gross
indicated power, combustion loss, heat transfer loss, and exhaust loss
[19,41,42]. The gross indicated power is divided into net indicated
power and pumping loss [42]. Equations (5) and (6) were used to
calculate the indicated thermal efficiency (ITE) and combustion loss,
respectively. The previous study of the authors contains detailed descriptions
of the equations [34].

= +
ITE P
m LHV m LHV
3.6
̇
NG NG Diesel Diesel ̇ (5)

where P is the net indicated power [kW] and calculated through the
indicated work and the engine speed.

= +
+
Combustion loss m LHV m LHV
m LHV m LHV
̇ ̇
̇ ̇
CO CO THC Fuel
NG NG Diesel Diesel (6)

where ṁ
CO and ṁ
THC are the mass flow rates of the CO and THC, respectively.
The mass flow rates of THC and CO were determined by
multiplying the mass flow rate of exhaust gas by the mass fractions of

Fig. 1. Schematic diagram of engine setup [34]

Table 5

Specifications of measurement equipment.

Measured
parameters

Device Measurement
range

Linearity/
accuracy

Repeatability

CO HORIBA
MEXA-7100
DEGR

0–10 vol% ≤ ± 1% of
FS*
≤ ± 0.5% of
FS* CO2 0–16 vol%
NOX 0–10,000 ppm
THC 0–20,000 ppm
O2 0–25 vol%
PM AVL

Smoke Meter
415S
0–10 FSN – ≤ ± 0.005
FSN
≤3% of MV**
Diesel mass
flow rate
AVL
733S
0–150 kg/h ≤ ± 0.12%
of MV**
–

NG mass flow
rate

Bronkhorst
F-202AV

0.08–4 kg/h ≤ ± 0.5%
of MV**
≤ ± 0.1%
of FS*

≤ ± 0.2% of
MV**

Air mass flow
rate

Bronkhorst
F-106AI

5–125 kg/h ≤ ± 0.1%
of FS*
≤ ± 0.2% of
MV**
In-cylinder
pressure
Kistler
6056A
0–25 MPa ≤ ± 0.3%
of FS*
–

Intake pressure Kistler
4045A5

0–0.5 MPa ≤ ± 0.3%
of FS*

–

* FS: full scale
** MV: measurement value

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

189
THC and CO, respectively. The exhaust loss was calculated using the
measured exhaust gas temperature and intake temperature, as shown in
Eq. (7) [19].

= −
+
Exhaust loss mh T hT
m LHV m LHV
̇ [ ( ) ( )]
̇ ̇
exh exh exh int int
NG NG Diesel Diesel (7)

where ṁ
exh is the mass flow rate of the exhaust. hexh and hint are the
exhaust and intake enthalpies, respectively. The specific enthalpies
were acquired using the NIST reference fluid thermodynamic and
transport properties [43]. It was assumed that the exhaust consists only
of CO2, H2O, O2, N2, NO, HC, and CO. The heat transfer loss was calculated
by subtracting the gross indicated power, combustion loss, and
exhaust loss from the fuel energy [41,42].

2.3. Experimental conditions and procedure

Previous studies related to NG-diesel DF-PCCI combustion have
shown that NOX and PM emissions effectively reduced by modulating
diesel SOI and NG SR in low-load operations [28–31]. However, the
deterioration in thermal efficiency, and HC and CO emissions were
recognized as the barriers to the expansion of the low-load limit.

In this study, the causes of the barriers were analyzed, and a mixture
preparation strategy was proposed to overcome the barriers in an NGdiesel
DF-PCCI engine. Firstly, baseline DF-PCCI points were determined
by combinations of the diesel SOI and NG SR to find the
causes of the barriers. Combustion and energy balance were analyzed to
investigate the causes of the barriers. Then the mixture preparation
strategy was established based on the causes. The optimal points found
in the strategy were compared to the baseline DF-PCCI points in terms
of thermal efficiency and HC and CO emissions.

The experimental conditions for the investigation are shown in
Table 6. The engine speed was fixed as 1400 rpm. The engine load was
varied from 0.3 to 0.6 MPa net IMEP, which is a range of low-load

operations. Other parameters, such as intake pressure, intake temperature,
coolant temperature, and diesel injection pressure, were fixed.
The intake pressure was maintained at 0.1 MPa during the experiments.
In general, the increase of the intake pressure under low loads is considered
to be difficult due to the low enthalpy (the low exhaust gas
temperature and low flow rate) of the exhaust gas. The reduction of the
exhaust gas temperature due to the increase of boost pressure also leads
to low conversion efficiency of oxidation catalysts in low-load operations
of DF-PCCI engines. This fact can explain the validity of the
naturally aspirated conditions utilized in the current study. The coolant
temperature was controlled by the value at the outlet of the engine
block and head.

It should be noted that there were constraints during the experiment.
The NOX and PM emissions were set lower than the EURO VI
regulation (NOX less than 0.4 g/kWh, PM less than 0.01 g/kWh) because
DF-PCCI concepts were proposed to reduce the NOX and PM emissions
from CDC. The coefficient of variation (COV) of IMEP was kept at less
than 5% to maintain stable combustion. To prevent engine damage, the
MPRR was kept at less than 1 MPa/CAD [44,45]. Each set of the experimental
conditions was repeated three times, and the exhaust gas
emission and fuel mass flow rate measurements were taken again three
times. The coefficient of variation (standard deviation divided by the

mean value) for the emission and mass flow rate measurements were
less than 3% and 2%, respectively, demonstrating satisfactory repeatability
[46].

3. Results and discussion

3.1. Barriers for expanding low-load operating range

In this section, the baseline DF-PCCI points were selected to investigate
barriers and their causes in low-load operations of NG-diesel
DF-PCCI engines. The baseline DF-PCCI points were determined based
on high ITE, and the NOX and PM emissions below the constraints.

Therefore, CA50 was chosen as a control parameter to determine the
baseline DF-PCCI points at the low-load range from 0.3 to 0.6 MPa
IMEP. The CA50 is a crucial factor influencing the thermal efficiency
and emissions in internal combustion engines [6,39]. For example,
when the CA50 is located before TDC, the thermal efficiency is reduced
because of the negative work, and the high in-cylinder temperature
causes the NOX emissions to increase. Conversely, when the CA50 is
retarded well beyond an optimal location, the thermal efficiency is
reduced, and HC and CO emissions increase due to a reduction in the
combustion efficiency. In this paper, only the experimental results of
the thermal efficiency and emissions at 0.45 MPa IMEP were presented.
This is because the trends of the results were similar at the low-load
range from 0.3 to 0.6 MPa IMEP, although there were differences in
specific values.

Fig. 2 shows the NG SR and ITE according to the CA50 and diesel
SOI. Increasing the NG SR at the fixed diesel SOI caused the CA50 to be
retarded. As the diesel SOI was retarded toward TDC, the NG SR was
increased to keep the CA50 constant. In other words, the CA50 was
retarded by increasing the NG SR and advancing the diesel SOI. The
increase in the NG SR formed a well-premixed fuel-air mixture because
the fraction of the fuel introduced during the intake stroke increased
[14,47]. The mixing between the fuel and air was also increased by the
advance in the diesel SOI [14,17]. Therefore, the increase of the NG SR
and the advance of the diesel SOI caused the increase in the homogeneity
of the mixture and the reduction in its local reactivity, finally
retarding the CA50 [34]. There was an optimal ITE region consisting of
a combination of CA50 and diesel SOI at each low-load. Increasing the
engine load caused the CA50 location with the optimal ITE region to be
retarded. The optimal CA50 for the best ITE at 0.3 MPa IMEP was located
around −2 CAD after top dead center (aTDC). When CA50 was
located before TDC, the negative work generally reduced the thermal
efficiency [6,39]. However, retarding the CA50 after TDC at 0.3 MPa
IMEP caused the combustion efficiency to deteriorate abruptly, which
resulted in low ITE [34]. The optimal CA50 for the best ITE was located
around 2 and 4 CAD aTDC at 0.45 and 0.6 MPa IMEP, respectively.

Fig. 3 shows the NOX and PM emissions according to the CA50 and
diesel SOI at 0.45 MPa IMEP. The NOX and PM emissions were reduced
when the CA50 was retarded and the diesel SOI was advanced. The
advance in the diesel SOI increased the homogeneity of the mixture.
The retardation of the CA50 resulted from a higher NG SR. The higher
NG SR also increased the homogeneity of the mixture. Therefore, the
increase in the mixture homogeneity, which lowered the local reactivity
of the mixture, reduced the combustion temperature and, thus, NOX and
PM emissions. At all combinations of the CA50 and diesel SOI tested,
the PM emissions were below the constraints.

Fig. 4 shows the THC and CO emissions according to the CA50 and
diesel SOI at 0.45 MPa IMEP. The NG SR strongly affected THC emissions.
It is noted that the trend in THC emissions in Fig. 4 was similar to
that in the NG SR in Fig. 2. The higher THC emissions with the higher
NG SR were due to the low combustion temperature and the NG
trapped in the crevices during the compression stroke [34]. The CO
emissions increased when the CA50 was retarded and the diesel SOI
was advanced. The high CO emissions were due to the low combustion

temperature of the more homogeneous fuel-air mixture. The CO

Table 6

Experimental conditions.

Item Value

Engine load (net IMEP) [MPa] 0.3–0.6
Engine speed [rpm] 1400
Intake pressure [MPa] 0.1

Intake temperature [K] 298 ± 1
Coolant temperature [K] 353 ± 1
Diesel injection pressure [MPa] 100

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

190
emissions were more affected by the CA50 than by the diesel SOI. The
baseline DF-PCCI point at 0.45 MPa IMEP was selected as the CA50 of 2
CAD aTDC and the diesel SOI of −40 CAD aTDC because of the high
ITE, and the NOX and PM emissions below the constraints. The procedures
for selecting the baseline DF-PCCI points at 0.3 and 0.6 MPa IMEP
were the same for those at 0.45 MPa IMEP.

Table 7 shows the engine operating conditions for the selected
baseline DF-PCCI points over the low-load range from 0.3 to 0.6 MPa
IMEP. The optimal CA50, and low NOX and PM emissions were acquired
with the combination of diesel SOI and NG SR at each low-load
of the DF-PCCI engine. As the engine load was increased, an advancement
of diesel SOI and a higher NG SR should be applied to retard the
CA50 and to reduce the NOX emissions [19,28].

Fig. 5 shows the in-cylinder pressure and HRR for the baseline DFPCCI
points. The corresponding performance and emissions are shown
in Fig. 6. The optimal CA50 was retarded as the engine load was increased.
It is noted that although the best ITE was located around the
CA50 of 4 CAD aTDC at 0.6 MPa IMEP, the optimal CA50 was selected
as 6 CAD aTDC in order to reduce the NOX emissions below the constraint.
The combination of the diesel SOI and NG SR alone achieved
low NOX and PM emissions that met the constraints at all the low loads
investigated. However, the THC and CO emissions increased rapidly as
the engine load was decreased. In each low-load operation of the NGdiesel
DF-PCCI engine, the increase in the homogeneity of the mixture
contributed to reducing the NOX and PM emissions simultaneously, but
it also increased the THC and CO emissions, because the increase of the
mixture homogeneity reduced the combustion temperature [48]. In this
situation, as the engine load was decreased, an overly-lean fuel-air

mixture was formed. It is noted that the equivalence ratio of the mixture
was reduced from 0.5 at 0.6 MPa IMEP to 0.29 at 0.3 MPa IMEP, as
shown in Table 7. At the lowest engine load, the overly-lean mixture
caused the high THC and CO emissions by intensifying the effects of
increasing the mixture homogeneity. Unburned methane accounts for a
significant portion of THC emissions in NG-diesel dual fuel engines
[49]. The unburned methane emissions are formed in regions of the
overly-lean mixture where the combustion temperature is low [50].
High CO can be formed in the overly-lean mixture regions in the temperature
below 1450 K [50,51]. The CO was not oxidized to CO2 because
the combustion temperature was low. Therefore, there was an
abrupt increase in THC and CO emissions at 0.3 MPa IMEP.

As the engine load was decreased, the ITE also deteriorated significantly.
In order to determine the reason for the low ITE, an analysis
of energy balance was conducted. Fig. 7 shows the energy balance for
the baseline DF-PCCI points at the low-load range of 0.3 to 0.6 MPa
IMEP. As the engine load was decreased, the combustion and heat
transfer losses increased. However, the exhaust loss was reduced at the
lower engine load, which offset the increase in the heat transfer loss
[19]. The pumping loss was slightly reduced with decreasing the engine
load. Therefore, the higher combustion loss was considered as the main
cause of the low ITE. As the engine load was moved from 0.6 to 0.3 MPa
IMEP, the combustion loss increased from 3.8% to 8.7%. The high
combustion loss at 0.3 MPa IMEP was due to the low combustion
temperature of the overly-lean mixture, which had the equivalence
ratio of 0.29.

The barriers and their causes for expanding the low-load operating
range were investigated by selecting the baseline DF-PCCI points at the

Fig. 2. Natural gas substitution ratio (left) and indicated thermal efficiency (right) according to CA50 and diesel SOI timing at 0.45 MPa IMEP for determining the
baseline case.

Fig. 3. NOX (left) and PM (right) emissions according to CA50 and diesel SOI timing at 0.45 MPa IMEP for determining the baseline case.

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

191
low-load range from 0.3 to 0.6 MPa IMEP. The barriers were identified
as low ITE and high THC and CO emissions. The main cause of the
barriers can be summarized as the formation of the overly-lean mixture
at the lowest engine load. The overly-lean mixture increased the mixture
homogeneity and thus reduced the combustion temperature and

the combustion efficiency. Therefore, the ITE, and THC and CO emissions
deteriorated significantly.

3.2. Mixture stratification for overcoming barriers at low loads

In the previous section, the formation of the overly-lean mixture
was identified as the main cause of low ITE, and high THC and CO
emissions at 0.3 MPa in the NG-diesel DF-PCCI engine. Therefore, an
increase in the local equivalence ratio of the mixture can improve the
ITE, and the THC and CO emissions. A higher local equivalence ratio is
achieved by retarding the diesel SOI and reducing the NG SR in DFPCCI
concepts [34,47]. In other words, mixture stratification increases
the equivalence ratio and reactivity of the local mixture where the

Fig. 4. THC (left) and CO (right) emissions according to CA50 and diesel SOI timing at 0.45 MPa IMEP for determining the baseline case.

Table 7

Engine operating conditions for baseline DF-PCCI.

IMEP [MPa] 0.3 0.45 0.6
NG flow rate [kg/h] 0.39 0.66 0.91
Diesel flow rate [kg/h] 0.36 0.3 0.32
Air flow rate [kg/h] 40.6 40.4 40.3
Diesel SOI [CAD aTDC] −35 −40 −55
NG substitution [%] 54 71 76
EGR rate [%] 0 0 0
Equivalence ratio [-] 0.29 0.38 0.5

Fig. 5. In-cylinder pressure and heat release rate for baseline DF-PCCI over a
low-load range from 0.3 to 0.6 MPa IMEP.

Fig. 6. Performance and emissions for baseline DF-PCCI over a low-load range
from 0.3 to 0.6 MPa IMEP.

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

192
combustion initiates. In fact, THC and CO were reduced with the mixture
stratification, as shown in Fig. 4. However, although the mixture

stratification contributed to reducing THC and CO emissions, NOX
emissions increased, as shown in Fig. 3, and the CA50 was advanced
before TDC, as shown in Fig. 2. Therefore, cooled-EGR was implemented
with the mixture stratification to reduce the NOX emissions
and to retard the CA50.

Fig. 8 shows the HRR, CA50, and NOX emissions according to the
diesel SOI and EGR rate at 0.3 MPa IMEP. When the diesel SOI was
retarded from −35 to −25 CAD aTDC at NG SR of 50%, without the
implementation of the EGR rate, the CA50 was advanced and the peak
HRR was increased. The higher peak HRR resulted in higher NOX
emissions. In this situation, as the EGR rate of 40% was introduced, the
CA50 was retarded and the NOX emissions decreased because of the
intake dilution effect of the EGR [52]. As a result, after the introduction

of the EGR, the CA50 and NOX emissions had values similar to those in
the initial state. Fig. 9 shows the HRR, CA50, and NOX emissions according
to the NG SR and EGR rate at 0.3 MPa IMEP. When the NG SR
was reduced from 60% to 40% at diesel SOI of −30 CAD aTDC without
the EGR, the CA50 advanced, and the peak HRR increased. The effects

were similar to those of the retardation of the diesel SOI. When EGR
was introduced, the CA50 and NOX emissions returned to their initial
levels. In summary, although a retardation of diesel SOI and a lower NG
SR effectively reduced the THC and CO emissions, the CA50 advanced,

and the NOX emissions increased. However, the implementation of EGR
effectively offset the advanced CA50 and the increased NOX emissions
[53]. The effect of EGR rate on the CA50 and the NOX emissions in the
DF-PCCI engine was similar at the low loads investigated.

Table 8 shows the engine operating conditions for the mixture
stratification strategy at 0.3 MPa IMEP. The baseline DF-PCCI corresponds
to the selected point in the previous section. In the previous
study comparing diesel PCCI and gasoline-diesel DF-PCCI at an extremely
low load condition, the HC and CO emissions as well as the fuel
consumption were much lower in the diesel PCCI than in the DF-PCCI
[21]. Therefore, the diesel PCCI case was also tested at 0.3 MPa IMEP.
There was a gradual increase in the degree of mixture stratification
until it reached the baseline DF-PCCI, Strategy 1, Strategy 2, and diesel
PCCI. In other words, the diesel SOI was retarded from −35 at the
baseline DF-PCCI to −25 CAD aTDC at the Strategy 2. The NG SR was
reduced from 54% at the baseline DF-PCCI to 23% at the Strategy 2.
The EGR rate was increased from 0% at the baseline DF-PCCI to 50% at
the Strategy 2. A higher EGR rate was implemented in the diesel PCCI
(NG SR = 0%) than in the Strategy 2 of the DF-PCCI. Fig. 10 shows the
performance and emissions of the baseline DF-PCCI, Strategy 1,
Strategy 2, and diesel PCCI. The CA50 applied in the Strategy 2 and
diesel PCCI was more advanced than in the baseline DF-PCCI and
Strategy 1 to reduce the THC and CO emissions. As shown in Fig. 4, an
advanced CA50 effectively reduced the THC and CO emissions. Despite
the advanced CA50, the Strategy 2 and diesel PCCI had the NOX
emissions levels similar to those of the baseline DF-PCCI and Strategy 1,
owing to the higher EGR rate. Low NOX and PM emissions, which met
the constraints, were seen in all cases.

The ITE improved when the degree of mixture stratification was
increased. The higher ITE was due to the improvement in the combustion
performance. Fig. 11 shows the HRR and combustion parameters
according to the mixture stratification. Figs. 12 and 13 show the
pressure-volume curves and DOCV according to the mixture stratification,
respectively. As shown in Fig. 11, as the degree of mixture stratification
was increased in the DF-PCCI, the HRR profile peak grew
higher, its combustion duration became narrower. Although the local
reactivity of the mixture in the Strategy 2 was higher than those in the

Fig. 7. Energy balance for baseline DF-PCCI over a low-load range from 0.3 to
0.6 MPa IMEP.

Fig. 8. Heat release rate (left) and CA50 and NOX emissions (right) according to diesel SOI timing and EGR rate at 0.3 MPa IMEP.

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

193
baseline DF-PCCI, the combustion initiation was more retarded because
of the higher EGR rate. The higher reactivity in the Strategy 2 enhanced
the combustion, which resulted in the higher peak HRR and an earlier
end of the combustion. Therefore, the pressure in the Strategy 2 had
lower values than those in the baseline DF-PCCI before the combustion
initiation, mainly because of the thermal effect of EGR, and it increased
abruptly with the ignition of the higher mixture reactivity, as shown in
Fig. 12. This caused the DOCV to increase from 0.91 at the baseline DFPCCI
to 0.94 at the Strategy 2, as shown in Fig. 13. In other words, the
mixture stratification strategy caused the combustion to approach the
theoretical Otto-cycle by controlling the HRR [54]. Therefore, the ITE
increased in the DF-PCCI as the degree of mixture stratification was
increased at 0.3 MPa IMEP. The ITE was more improved in the diesel
PCCI than in the Strategy 2 of the DF-PCCI. The higher ITE was due to a
higher peak HRR and a narrower combustion duration, as shown in
Fig. 11.

The mixture stratification strategy also effectively reduced the THC
and CO emissions. The reduction in the THC and CO emissions was
mainly due to the enhanced combustion performance and the reduced
mass flow rate of NG. The increase in the degree of mixture stratification
increased the local reactivity of the mixture and thus enhanced the
combustion performance. Unburned NG was the main source of THC
emissions, and an increase of NG SR favored CO formation, as discussed
in the previous section. Therefore, the lower NG SR with the mixture
stratification strategy contributed to reducing the THC and CO formations.The
mixture stratification strategy was also implemented and assessed
at 0.45 and 0.6 MPa IMEP. The engine operating conditions for
DF-PCCI with mixture stratification at the low-load range from 0.3 to
0.6 MPa IMEP are shown in Table 9. A retardation of diesel SOI, a lower
NG SR, and a higher EGR rate were implemented in the mixture stratification
strategy than in the baseline DF-PCCI. As the engine load was
increased, the required EGR rate for realizing the mixture stratification
strategy was reduced mainly because of the higher equivalence ratio.

Fig. 14 shows the in-cylinder pressure and HRR for the DF-PCCI
with mixture stratification. The corresponding performance and emissions
are compared to those of the baseline DF-PCCI in Fig. 15. The NOX
and PM emissions were below the constraints in the baseline DF-PCCI
and DF-PCCI with mixture stratification. An advanced CA50 was applied
to the DF-PCCI with mixture stratification in order to reduce the
THC and CO emissions. The THC and CO emissions were reduced with a
higher degree of mixture stratification at the low loads. The principles
of reducing the THC and CO emissions were explained by the enhanced
combustion performance and the reduced mass flow rate of NG, as
discussed in the previous paragraph. The reduction in the THC and CO
emissions by the mixture stratification was greater at the lowest load.

Fig. 9. Heat release rate (left) and CA50 and NOX emissions (right) according to natural gas substitution ratio and EGR rate at 0.3 MPa IMEP.

Table 8

Engine operating conditions at 0.3 MPa IMEP for evaluating a mixture stratification
strategy.

net IMEP [MPa] baseline Strategy 1 Strategy 2 Diesel PCCI

NG flow rate [kg/h] 0.39 0.26 0.16 0

Diesel flow rate [kg/h] 0.36 0.47 0.57 0.73
Air flow rate [kg/h] 40.6 24.3 20.3 17.7

Diesel SOI [CAD aTDC] −35 −30 −25 −25
NG substitution [%] 54 38 23 0

EGR rate [%] 0 40 50 57

Equivalence ratio [-] 0.29 0.46 0.54 0.60

Fig. 10. Performance and emissions according to mixture stratification at
0.3 MPa IMEP.

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

194
The DF-PCCI with mixture stratification reduced the THC and CO
emissions by about 43% and 50% at 0.3 MPa IMEP, respectively,
compared to the baseline DF-PCCI.

The ITE was also improved by the mixture stratification strategy at
the low loads investigated. The ITE improvement was also maximized
at the lowest load. A more specific analysis of the ITE is shown in
Fig. 16, which depicts the energy balance for the baseline DF-PCCI and
DF-PCCI with mixture stratification at the low loads. Despite the higher
heat transfer losses, the DF-PCCI with mixture stratification had lower
exhaust and combustion losses than the baseline DF-PCCI. The reduction
in the exhaust losses was due to more efficient work conversion, as
shown in Fig. 12. Enhanced combustion performance, reduced mass
flow rates of NG, and advanced CA50 all account for the reduction in
the combustion losses. The enhanced combustion performance and
advanced CA50 effectively reduced the combustion losses but increased
the heat transfer losses. The main contributor to the improvement in the
ITE at the low loads was the reduction in the combustion losses. Although
the reduction in the combustion losses was higher than the increase
in the ITE, the contribution of the combustion losses was partially
offset by the increase in the heat transfer losses. The higher
improvement in the ITE at the lowest load was due to the higher reduction
in the combustion loss.

Diesel PCCI was implemented at 0.45 MPa IMEP because it effectively
improved the ITE at 0.3 MPa IMEP. Fig. 17 shows the energy
balance for the DF-PCCI with mixture stratification and diesel PCCI at
0.3 and 0.45 MPa IMEP. The application of the diesel PCCI at 0.6 MPa

IMEP was limited by requiring excessive EGR rates in this study. Although
the diesel PCCI was effective in improving the ITE at 0.3 MPa
IMEP, the ITE became worse in the diesel PCCI than in the DF-PCCI at
0.45 MPa IMEP. While the combustion efficiency gain due to the application
of the diesel PCCI was higher than the increase in the heat
transfer loss at 0.3 MPa IMEP, the gain did not exceed the increase in

Fig. 11. Heat release rate (left) and combustion parameters (right) according to mixture stratification at 0.3 MPa IMEP.

Fig. 12. Pressure-volume curves according to mixture stratification at 0.3 MPa IMEP.

Fig. 13. Degree of constant volume according to mixture stratification at
0.3 MPa IMEP.

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

195
the heat transfer losses at 0.45 MPa IMEP.

Fig. 18 shows the THC and CO emissions for the DF-PCCI with
mixture stratification and diesel PCCI at 0.3 and 0.45 MPa IMEP. The
diesel PCCI effectively reduced the THC and CO emissions compared to
the DF-PCCI at 0.3 MPa IMEP, because of the enhanced combustion and
the absence of NG, as already explained above. However, the CO
emissions were higher in the diesel PCCI than in the DF-PCCI at
0.45 MPa because of the excessive EGR rate [55].

4. Summary and conclusions

In dual-fuel premixed charge compression ignition (DF-PCCI) engines,
the deterioration in thermal efficiency, and hydrocarbon (HC)
and carbon monoxide (CO) emissions at low loads are known as the
barriers for expanding the low-load operating range. In this study, the
causes of the barriers were investigated and a mixture preparation
strategy for overcoming the barriers was proposed and evaluated for the
effectiveness in expanding the low-load limit. The experimental study
was conducted in a natural gas (NG)-diesel DF-PCCI engine at a lowload
range from 0.3 to 0.6 MPa indicated mean effective pressure
(IMEP).

Baseline DF-PCCI was determined by combinations of diesel start of
injection (SOI) and NG substitution ratio (SR). An increase in the
homogeneity of a fuel–air mixture effectively reduced the NOX and PM

emissions but increased the HC and CO emissions at each low load
condition. As the engine load was decreased, the formation of an
overly-lean mixture increased the mixture homogeneity further and
thus aggravated the HC and CO emissions substantially. The indicated
thermal efficiency (ITE) also deteriorated because the overly-lean
mixture increased the combustion loss.

A mixture stratification strategy was established to increase the
local equivalence ratio and reactivity of the fuel-air mixture at the low
loads. The mixture stratification was realized by a retarded diesel SOI, a
lower NG SR, and a higher EGR rate. The mixture stratification allowed
the combustion to approach the theoretical Otto-cycle by enhancing the
combustion performance, and thus the ITE was improved. The HC and
CO emissions also effectively decreased mainly due to the enhanced
combustion and the reduced mass flow rates of NG. The DF-PCCI with
the mixture stratification improved the ITE by 6.5% and reduced the
HC and CO emissions by 43% and 50%, respectively, at 0.3 MPa IMEP
compared to the baseline DF-PCCI.

Diesel PCCI was also implemented at the low loads in an attempt to
improve the ITE, and HC and CO emissions. Although the diesel PCCI
was effective in improving the ITE at 0.3 MPa IMEP, the ITE became
worse than that of the DF-PCCI at 0.45 MPa IMEP. The diesel PCCI had
lower HC and CO emissions compared to the DF-PCCI at 0.3 MPa IMEP.
However, the CO emissions were higher than that of the DF-PCCI at
0.45 MPa IMEP.

Acknowledgement

The authors would like to appreciate the Global-Top Project
(Development of Advanced Combustion Technology for Global Top Low

Table 9

Engine operating conditions for DF-PCCI with mixture stratification.

net IMEP [MPa] 0.3 0.45 0.6

NG flow rate [kg/h] 0.16 0.54 0.82
Diesel flow rate [kg/h] 0.57 0.43 0.41
Air flow rate [kg/h] 20.3 27.9 27.7

Diesel SOI [CAD aTDC] −25 −35 −40
NG substitution [%] 23 58 69
EGR rate [%] 50 30 30

Equivalence ratio [-] 0.54 0.55 0.71

Fig. 14. In-cylinder pressure and heat release rate for DF-PCCI with mixture
stratification over a low-load range from 0.3 to 0.6 MPa IMEP.

Fig. 15. Performance and emissions for baseline DF-PCCI and DF-PCCI with
mixture stratification over a load range from 0.3 to 0.6 MPa IMEP.

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

196
Emission Vehicle (2016002070001)) of the Ministry of Environment
(MOE) of Korea for financial support by the Center for Environmentally
Friendly Vehicle (CEFV). The authors would also like to thank Zenobalti

Co. for their technical support.

References

[1] Yao M, Zheng Z, Liu H. Progress and recent trends in homogeneous charge compression
ignition (HCCI) engines. Prog. Energy Combust. Sci. 2009;35(5):398–437.
https://doi.org/10.1016/j.pecs.2009.05.001.
[2] Zhao H. HCCI and CAI engines for the automotive industry. Elsevier; 2007.
[3] Gan S, Ng HK, Pang KM. Homogeneous charge compression ignition (HCCI) combustion:
implementation and effects on pollutants in direct injection diesel engines.
Appl. Energy 2011;88(3):559–67. https://doi.org/10.1016/j.apenergy.2010.09.
005.

[4] Agarwal AK, Singh AP, Maurya RK. Evolution, challenges and path forward for low
temperature combustion engines. Prog. Energy Combust. Sci. 2017;61:1–56.
https://doi.org/10.1016/j.pecs.2017.02.001.
[5] Bendu H, Murugan S. Homogeneous charge compression ignition (HCCI) combustion:
Mixture preparation and control strategies in diesel engines. Renew. Sustain.
Energy Rev. 2014 Oct;1(38):732–46. https://doi.org/10.1016/j.rser.2014.07.019.
[6] Saxena S, Bedoya ID. Fundamental phenomena affecting low temperature combustion
and HCCI engines, high load limits and strategies for extending these limits.
Prog. Energy Combust. Sci. 2013;39(5):457–88. https://doi.org/10.1016/j.pecs.
2013.05.002.

[7] Manente V, Johansson B, Cannella W. Gasoline partially premixed combustion, the
future of internal combustion engines? Int. J. Engine Res. 2011;12(3):194–208.
https://doi.org/10.1177/1468087411402441.
[8] Manente V, Johansson B, Tunestal P. Partially premixed combustion at high load
using gasoline and ethanol, a comparison with diesel. SAE Tech. Pap. 2009–01-
0944. https://doi.org/10.4271/2009-01-0944.
[9] Lundgren MO, Wang Z, Matamis A, Andersson O, Richter M, Tuner M, et al. Effects
of Post-Injections Strategies on UHC and CO at Gasoline PPC Conditions in a HeavyDuty
Optical Engine. SAE Tech. Pap. 2017–01-0753. https://doi.org/10.4271/
2017-01-0753.

[10] Benajes J, Molina S, García A, Monsalve-Serrano J, Durrett R. Performance and
engine-out emissions evaluation of the double injection strategy applied to the
gasoline partially premixed compression ignition spark assisted combustion concept.
Appl. Energy 2014;134:90–101. https://doi.org/10.1016/j.apenergy.2014.08.
008.

[11] Borgqvist P, Tunestal P, Johansson B. Comparison of negative valve overlap (NVO)
and rebreathing valve strategies on a gasoline PPC engine at low load and idle
operating conditions. SAE Int. J. Engines (2013–01-0902) 2013;6(1):366–78.
https://doi.org/10.4271/2013-01-0902.
[12] Bessonette PW, Schleyer CH, Duffy KP, Hardy WL, Liechty MP. Effects of fuel
property changes on heavy-duty HCCI combustion. SAE Tech. Pap. 2007–01-0191.
https://doi.org/10.4271/2007-01-0191.
[13] Reitz RD, Duraisamy G. Review of high efficiency and clean reactivity controlled
compression ignition (RCCI) combustion in internal combustion engines. Prog.
Energy Combust. Sci. 2015;46:12–71. https://doi.org/10.1016/j.pecs.2014.05.003.

Fig. 16. Energy balance for baseline DF-PCCI and DF-PCCI with mixture stratification
over a load range from 0.3 to 0.6 MPa IMEP.

Fig. 17. Energy balance for DF-PCCI with mixture stratification and diesel PCCI
at 0.3 and 0.45 MPa IMEP (diesel PCCI at 0.45 MPa: diesel SOI of −25 CAD
aTDC, EGR rate of 65%).

Fig. 18. THC and CO emissions for DF-PCCI with mixture stratification and
diesel PCCI at 0.3 and 0.45 MPa IMEP (diesel PCCI at 0.45 MPa: diesel SOI of
−25 CAD aTDC, EGR rate of 65%).

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

197
[14] Benajes J, Molina S, García A, Monsalve-Serrano J. Effects of direct injection timing
and blending ratio on RCCI combustion with different low reactivity fuels. Energy
Convers. Manage. 2015;99:193–209. https://doi.org/10.1016/j.enconman.2015.
04.046.

[15] Paykani A, Kakaee AH, Rahnama P, Reitz RD. Progress and recent trends in reactivity-controlled
compression ignition engines. Int. J. Engine Res.
2016;17(5):481–524. https://doi.org/10.1177/1468087415593013.
[16] Inagaki K, Fuyuto T, Nishikawa K, Nakakita K, Sakata I. Dual-fuel PCI combustion
controlled by in-cylinder stratification of ignitability. SAE Tech. Pap. 2006–01-
0028. https://doi.org/10.4271/2006-01-0028.

[17] Tang Q, Liu H, Li M, Geng C, Yao M. Multiple optical diagnostics on effect of fuel
stratification degree on reactivity controlled compression ignition. Fuel
2017;202:688–98. https://doi.org/10.1016/j.fuel.2017.04.136.

[18] Kavuri C, Paz J, Kokjohn SL. A comparison of Reactivity Controlled Compression
Ignition (RCCI) and Gasoline Compression Ignition (GCI) strategies at high load,
low speed conditions. Energy Convers. Manage. 2016;127:324–41. https://doi.org/
10.1016/j.enconman.2016.09.026.

[19] Kokjohn SL, Hanson RM, Splitter DA, Reitz RD. Fuel reactivity controlled compression
ignition (RCCI): a pathway to controlled high-efficiency clean combustion.
Int. J. Engine Res. 2011;12(3):209–26. https://doi.org/10.1177/
1468087411401548.

[20] Benajes J, Pastor JV, García A, Monsalve-Serrano J. The potential of RCCI concept
to meet EURO VI NOx limitation and ultra-low soot emissions in a heavy-duty
engine over the whole engine map. Fuel 2015;159:952–61. https://doi.org/10.
1016/j.fuel.2015.07.064.

[21] Wang Y, Zhu Z, Yao M, Li T, Zhang W, Zheng Z. An investigation into the RCCI
engine operation under low load and its achievable operational range at different
engine speeds. Energy Convers. Manage. 2016;124:399–413. https://doi.org/10.
1016/j.enconman.2016.07.026.

[22] Molina S, García A, Pastor JM, Belarte E, Balloul I. Operating range extension of
RCCI combustion concept from low to full load in a heavy-duty engine. Appl.
Energy 2015;143:211–27. https://doi.org/10.1016/j.apenergy.2015.01.035.
[23] Benajes J, García A, Monsalve-Serrano J, Boronat V. Achieving clean and efficient
engine operation up to full load by combining optimized RCCI and dual-fuel dieselgasoline
combustion strategies. Energy Convers. Manage. 2017;136:142–51.
https://doi.org/10.1016/j.enconman.2017.01.010.

[24] García A, Monsalve-Serrano J, Roso VR, Martins ME. Evaluating the emissions and
performance of two dual-mode RCCI combustion strategies under the World
Harmonized Vehicle Cycle (WHVC). Energy Convers. Manage. 2017;149:263–74.
https://doi.org/10.1016/j.enconman.2017.07.034.

[25] Wang Y, Yao M, Li T, Zhang W, Zheng Z. A parametric study for enabling reactivity
controlled compression ignition (RCCI) operation in diesel engines at various engine
loads. Appl. Energy 2016;175:389–402. https://doi.org/10.1016/j.apenergy.
2016.04.095.

[26] Kalsi SS, Subramanian KA. Experimental investigations of effects of EGR on performance
and emissions characteristics of CNG fueled reactivity controlled compression
ignition (RCCI) engine. Energy Convers. Manage. 2016;130:91–105.
https://doi.org/10.1016/j.enconman.2016.10.044.

[27] Walker NR, Wissink ML, DelVescovo DA, Reitz RD. Natural gas for high load dualfuel
reactivity controlled compression ignition in heavy-duty engines. J. Energy
Res. Technol. 2015;137(4):042202https://doi.org/10.1115/icef2014-5620.
[28] Nieman DE, Dempsey AB, Reitz RD. Heavy-duty RCCI operation using natural gas
and diesel. SAE Int J Engines (2012–01-0379) 2012(5):270–85. https://doi.org/10.
4271/2012-01-0379.

[29] Doosje E, Willems F, Baert R. Experimental demonstration of RCCI in heavy-duty
engines using diesel and natural gas. SAE Tech. Pap. 2014–01-1318. https://doi.
org/10.4271/2014-01-1318.

[30] Ansari E, Shahbakhti M, Naber J. Optimization of performance and operational cost
for a dual mode diesel-natural gas RCCI and diesel combustion engine. Appl. Energy
2018;231:549–61. https://doi.org/10.1016/j.apenergy.2018.09.040.
[31] Hutter R, Ritzmann J, Elbert P, Onder C. Low-load limit in a diesel-ignited gas
engine. Energies 2017;10(10):1450. https://doi.org/10.3390/en10101450.
[32] Li W, Liu Z, Wang Z. Experimental and theoretical analysis of the combustion
process at low loads of a diesel natural gas dual-fuel engine. Energy
2016;94:728–41. https://doi.org/10.1016/j.energy.2015.11.052.
[33] Gharehghani A, Hosseini R, Mirsalim M, Jazayeri SA, Yusaf T. An experimental
study on reactivity controlled compression ignition engine fueled with biodiesel/
natural gas. Energy 2015;89:558–67. https://doi.org/10.1016/j.energy.2015.06.
014.

[34] Park H, Shim E, Bae C. Improvement of combustion and emissions with exhaust gas
recirculation in a natural gas-diesel dual-fuel premixed charge compression ignition
engine at low load operations. Fuel 2019;235:763–74. https://doi.org/10.1016/j.
fuel.2018.08.045.

[35] Zheng J, Wang J, Zhao Z, Wang D, Huang Z. Effect of equivalence ratio on

combustion and emissions of a dual-fuel natural gas engine ignited with diesel.
Appl. Therm. Eng. 2019;146:738–51. https://doi.org/10.1016/j.applthermaleng.
2018.10.045.

[36] Heywood JB. Internal combustion engine fundamentals. New York: Mcgraw-hill;
1988.

[37] Stone R. Introduction to internal combustion engines. London: Macmillan; 1999. p.
543–4.

[38] Rakopoulos DC, Rakopoulos CD, Kyritsis DC. Butanol or DEE blends with either
straight vegetable oil or biodiesel excluding fossil fuel: comparative effects on diesel
engine combustion attributes, cyclic variability and regulated emissions trade-off.
Energy 2016;115:314–25. https://doi.org/10.1016/j.energy.2016.09.022.
[39] Park H, Kim J, Bae C. Effects of Hydrogen Ratio and EGR on Combustion and
Emissions in a Hydrogen/Diesel Dual-Fuel PCCI Engine. SAE Tech. Pap. 2015–01-
1815. https://doi.org/10.4271/2015-01-1815.

[40] Shudo T, Nabetani S, Nakajima Y. Analysis of the degree of constant volume and
cooling loss in a spark ignition engine fuelled with hydrogen. Int. J. Engine Res.
2001;2(1):81–92. https://doi.org/10.1243/1468087011545361.
[41] Benajes J, Molina S, García A, Monsalve-Serrano J. Effects of low reactivity fuel
characteristics and blending ratio on low load RCCI (reactivity controlled compression
ignition) performance and emissions in a heavy-duty diesel engine. Energy
2015;90:1261–71. https://doi.org/10.1016/j.energy.2015.06.088.
[42] Manente V, Johansson B, Tunestal P, Cannella W. Effects of different type of gasoline
fuels on heavy duty partially premixed combustion. SAE Int J Engines
(2009–01-2668) 2010;2(2):71–88. https://doi.org/10.4271/2009-01-2668.
[43] E.W. Lemmon, M.L. Huber, M.O. McLinden, NIST reference fluid thermodynamic
and transport properties–REFPROP, 2002.

[44] Benajes J, García A, Monsalve-Serrano J, Villalta D. Exploring the limits of the
reactivity controlled compression ignition combustion concept in a light-duty diesel
engine and the influence of the direct-injected fuel properties. Energy Convers.
Manage. 2018;157:277–87. https://doi.org/10.1016/j.enconman.2017.12.028.
[45] Bhaduri S, Contino F, Jeanmart H, Breuer E. The effects of biomass syngas composition,
moisture, tar loading and operating conditions on the combustion of a tartolerant
HCCI (Homogeneous Charge Compression Ignition) engine. Energy
2015;87:289–302. https://doi.org/10.1016/j.energy.2015.04.076.
[46] Rakopoulos CD, Rakopoulos DC, Kosmadakis GM, Papagiannakis RG. Experimental
comparative assessment of butanol or ethanol diesel-fuel extenders impact on
combustion features, cyclic irregularity, and regulated emissions balance in heavyduty
diesel engine. Energy 2019;174:1145–57. https://doi.org/10.1016/j.energy.
2019.03.063.

[47] Roberts G, Rousselle CM, Musculus M, Wissink M, Curran S, Eagle E. RCCI combustion
regime transitions in a single-cylinder optical engine and a multi-cylinder
metal engine. SAE Int J Engines (2017–24-0088) 2017;10(5):2392–413. https://
doi.org/10.4271/2017-24-0088.

[48] Papagiannakis RG, Krishnan SR, Rakopoulos DC, Srinivasan KK, Rakopoulos CD. A
combined experimental and theoretical study of diesel fuel injection timing and
gaseous fuel/diesel mass ratio effects on the performance and emissions of natural
gas-diesel HDDI engine operating at various loads. Fuel 2017;202:675–87. https://
doi.org/10.1016/j.fuel.2017.05.012.

[49] Liu J, Yang F, Wang H, Ouyang M, Hao S. Effects of pilot fuel quantity on the
emissions characteristics of a CNG/diesel dual fuel engine with optimized pilot
injection timing. Appl. Energy 2013;110:201–6. https://doi.org/10.1016/j.
apenergy.2013.03.024.

[50] Liu J, Zhang X, Wang T, Zhang J, Wang H. Experimental and numerical study of the
pollution formation in a diesel/CNG dual fuel engine. Fuel 2015;159:418–29.
https://doi.org/10.1016/j.fuel.2015.07.003.

[51] Wei L, Geng P. A review on natural gas/diesel dual fuel combustion, emissions and
performance. Fuel Process. Technol. 2016;142:264–78. https://doi.org/10.1016/j.
fuproc.2015.09.018.

[52] Divekar PS, Chen X, Tjong J, Zheng M. Energy efficiency impact of EGR on organizing
clean combustion in diesel engines. Energy Convers. Manage.
2016;112:369–81. https://doi.org/10.1016/j.enconman.2016.01.042.
[53] Uchida N, Okamoto T, Watanabe H. A new concept of actively controlled rate of
diesel combustion for improving brake thermal efficiency of diesel engines: Part
1—verification of the concept. Int. J. Engine Res. 2018;19(4):474–87. https://doi.
org/10.1177/1468087417720332.

[54] Rakopoulos CD, Rakopoulos DC, Mavropoulos GC, Kosmadakis GM. Investigating
the EGR rate and temperature impact on diesel engine combustion and emissions
under various injection timings and loads by comprehensive two-zone modeling.
Energy 2018;157:990–1014. https://doi.org/10.1016/j.energy.2018.05.178.
[55] Chen Z, Wu Z, Liu J, Lee C. Combustion and emissions characteristics of high nbutanol/diesel
ratio blend in a heavy-duty diesel engine and EGR impact. Energy
Convers. Manage. 2014;78:787–95. https://doi.org/10.1016/j.enconman.2013.11.
037.

H. Park, et al. Energy Conversion and Management 194 (2019) 186–198

198