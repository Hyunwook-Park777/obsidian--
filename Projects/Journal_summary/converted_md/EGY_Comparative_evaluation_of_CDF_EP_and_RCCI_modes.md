# EGY_Comparative evaluation of CDF, EP, and RCCI modes

Energy 268 (2023) 126769

Available online 18 January 2023

0360-5442/© 2023 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/bync/4.0/).Comparative
evaluation of conventional dual fuel, early pilot, and

reactivity-controlled compression ignition modes in a natural gas-diesel

dual-fuel engine

Hyunwook Park a,*
, Euijoon Shim b
, Junsun Lee a
, Seungmook Oh a,c
, Changup Kim a
,
Yonggyu Lee a,c
, Kernyong Kang a

a Department of Mobility Power Research, Korea Institute of Machinery and Materials, Daejeon, 34103, Republic of Korea
b Department of e-Powerpack, Hyundai Doosan Infracore, Incheon, 22502, Republic of Korea

c Environment Energy Machinery, University of Science and Technology, Daejeon, 34113, Republic of Korea

ARTICLE INFO

Keywords:
Dual fuel
RCCI

Pilot injection
Natural gas

Thermal efficiency
Methane emissions

ABSTRACT

Conventional dual fuel (CDF), early pilot (E-Pilot), and reactivity-controlled compression-ignition (RCCI) were
compared in a natural gas-diesel dual-fuel engine. The CDF mode was the most suitable for high-load operations
based on its effective combustion phasing control. Furthermore, a high brake thermal efficiency (BTE) of 42.8%
was achieved. However, the BTE deteriorated to 38.8% under low-load condition because of the high combustion
loss of 5.1%. This high combustion loss was reduced to 3.5% and 3.3% in the E-Pilot and RCCI modes,
respectively. The RCCI mode also had the lowest heat transfer loss, which achieved the highest BTE of 41.4%.
However, the direction of combustion phasing control based on the diesel injection showed opposite trends to
that of the CDF mode, and the engine operation was limited to the low loads. The E-Pilot mode covered mediumload
operations, and its combustion phasing control was similar to that of the CDF mode. The E-Pilot mode
resulted in a higher BTE of 43.1% under the medium-load condition than the CDF mode. The following strategy
could be a solution considering smooth mode transitions and effective emissions reduction: E-Pilot mode for the
low-to-mid load operations and CDF mode for the high load operations.

1. Introduction

Efforts to minimize carbon dioxide (CO2) emissions are actively
underway in various sectors because of the increasing global interest in
greenhouse gas (GHG) emissions. In the transport sector, existing CO2
regulations for passenger vehicles are becoming more stringent, and
new targets are being introduced for heavy-duty vehicles and ships. In
2018, the International Maritime Organization adopted a strategy to
reduce GHG emissions from international shipping [1]. Based on this
strategy, the total annual GHG emissions from international shipping
need to be reduced by 50% at minimum until the year of 2050,
compared to those of 2008. The first CO2 emission standards for new
heavy-duty vehicles in the European Union were established in 2019
[2]. The average CO2 emissions from the selected heavy-duty categories
should be reduced by 30% until the year of 2030, relative to the EU
average CO2 emissions of 2019.

Unlike passenger vehicles, the application of lithium-ion batteries as
the power sources for heavy-duty vehicles and ships is difficult because
of their low-energy density [3]. Dual-fuel engines could be technically
viable solutions for addressing the CO2 regulations in heavy-duty vehicles
and ships [4]. Dual-fuel combustion is a technique using two fuels to
control the in-cylinder reactivity prior to combustion [5]. In the
commercialization stage, natural gas (NG) is selected as a fuel for
dual-fuel engines because of its low carbon-to-hydrogen ratio. The CO2
emissions of the dual-fuel engines can be reduced by up to 20%
compared to those of the diesel engines when the ratio of NG in dual-fuel
engines is increased; the benefit of the reduced emissions can be
expanded further using biogas [6]. The NG-diesel dual-fuel engines can
be flexibly operated for the diesel-only mode as well as the dual-fuel
mode based on the operating conditions [7,8]. In the dual-fuel engines
with the NG port injection, nitrogen oxides (NOX) and particulate matter
(PM) emissions could be effectively reduced by forming an NG-air premixed
charge, compared to using conventional diesel combustion [9].

* Corresponding author. Department of Mobility Power Research, Korea Institute of Machinery and Materials, 156 Gajeongbuk‒Ro, Yuseong‒Gu, Daejeon, 34103,
Republic of Korea.

E-mail address: hwpark@kimm.re.kr (H. Park).

Contents lists available at ScienceDirect

Energy

journal homepage: www.elsevier.com/locate/energy

https://doi.org/10.1016/j.energy.2023.126769

Received 24 July 2022; Received in revised form 10 December 2022; Accepted 18 January 2023
Energy 268 (2023) 126769

2

Conventional dual fuel (CDF) is a traditional dual-fuel approach
[10]. NG is supplied to the engine cylinder along with air during the
intake stroke to form a premixed charge, and diesel is injected into the
cylinder at the end of the compression stroke acting as an ignition source
[11]. The advantage of the CDF mode is that the combustion phasing can
be controlled with the diesel start of injection (SOI) [12]. The CDF mode
achieves engine loads equivalent to those of the diesel combustion [13].
The thermal efficiency can also be equally matched to or improved even
further than that of diesel-only combustion at high-load operations by
controlling the diesel SOI [14]. However, the CDF mode suffers from low
thermal efficiency and high hydrocarbon (HC) and carbon monoxide
(CO) emissions, particularly in low-load operations [15]. The overly
lean mixture in the CDF mode reduces the combustion temperature
under low-load conditions [16]. Yousefi et al. proposed an advanced
diesel SOI to reduce HC and CO emissions at low loads [17]. The early
diesel introduction into the combustion chamber provided more time for
the diesel to mix with the surrounding NG-air mixture, which enhanced
the flame propagation. Despite the reduction in HC and CO emissions,
NOX emissions increased because of the high combustion temperature.
Barba et al. reported that minimal HC emissions were achieved only

with high NOX emissions under the CDF mode [18]. A mixture stratification
strategy was established to overcome the barriers of the low-load
operations in the CDF mode [19]. The combination of an early diesel
SOI, a low NG substitution ratio, and a high exhaust gas recirculation
(EGR) rate simultaneously reduced HC, CO, and NOX emissions. You
et al. improved the thermal efficiency and HC and CO emissions in the
CDF mode at low loads through the EGR with appropriate intake
throttling [20]. Despite these efforts, the late diesel SOI of the CDF mode
results in the incomplete combustion of lean NG-air mixtures where the
diesel spray does not reach [21]. Nieman et al. reported combustion
losses higher than 6% for the total fuel energy in NG-diesel dual-fuel
engines under low-load conditions [10].

Reactivity-controlled compression ignition (RCCI) is a promising
dual-fuel technology that achieves high efficiency and low emissions
simultaneously [22]. In RCCI, the NG is supplied into the cylinder during
the intake stroke as with the CDF; however, diesel is injected relatively
early and premixed with the NG before its combustion initiation [10].
HC, CO, and NOX emissions in the RCCI mode can be reduced because of
the early diesel SOI. Park et al. reported that an advance in the diesel SOI
to the RCCI mode reduced HC and CO emissions [23]. Further, NOX

emissions were reduced in the RCCI mode because its long ignition delay
prevented high-temperature diffusion combustion [17,24]. Despite
these advantages, the RCCI mode presented some challenges, which
include combustion phasing control and the limitations in the operating
range. Combustion phasing is controlled by the injection quantities,
timings, and properties of two fuel because the autoignition of the
premixed fuel-air mixture is dominated by chemical kinetics in the RCCI

mode [25]. Indrajuana et al. reported that the limitation in the combustion
phasing control is more pronounced during transient operation
because of the different response times of the fast fuel injector drive and
slow dynamics of the intake manifold pressure [26]. Another major
challenge of the RCCI mode is that engine operation is confined to
low-to-medium load conditions [27]. Nieman et al. indicated that the
in-cylinder pressure and maximum pressure rise rate (MPRR) in the
RCCI mode increased rapidly with increasing engine load, which limits
its high-load operation [28]. Indrajuana et al. proposed that the
mode-switching from RCCI to CDF mode can be considered a viable
solution for high-load operation in real-world applications [29].

Early pilot (E-Pilot) is a hybrid dual-fuel technology that combines
the CDF and RCCI modes [2,28]. In the E-Pilot mode, the pilot injection
of diesel is introduced into the combustion chamber as early as the RCCI
diesel injection, and the main SOI of diesel is located close to top dead
center (TDC), which is similar to that in the CDF mode. Huang et al.
varied the pilot SOIs of diesel while maintaining a main SOI in an
NG-diesel dual-fuel engine [30]. The CH4 emissions significantly
decreased as the pilot SOI of diesel advanced to the E-Pilot regime
because of its enhanced flame propagation. In addition, MPRR was
alleviated as the ignition of the first pilot injection shortened the mixing
time of the main diesel injection and NG-air mixture. Park et al. applied
an E-Pilot strategy to dual-fuel engines fueled with NG and diesel at
high-load operations, wherein the RCCI operation was impossible [2].

It is necessary to combine the dual-fuel modes based on the target
application of dual-fuel engines considering the possibilities and challenges
of the dual-fuel modes listed above [28,31]. A comparison of the
dual-fuel modes should be performed to determine the mode that is most
beneficial for each operating point. However, only few studies have
attempted to compare the CDF, E-Pilot, and RCCI modes. Shim et al.
compared the CDF and RCCI modes in a single-cylinder engine under

low-load conditions [32]. The RCCI mode improved both thermal efficiency
and emissions compared to the CDF mode in the low-load operation
through the optimization of the diesel single injection and NG
ratio. Nieman et al. compared multiple combustion modes over a wide
range of engine loads for steady-state engine calibration in heavy-duty

engines [28]. Diesel-only combustion was selected for low-load operations
because dual-fuel modes exhibited high combustion losses. The
RCCI mode was selected for mid-load operations because of its high
thermal efficiency and low smoke and NOX emissions. The CDF mode
was implemented in high-load operations because the MPRR values

gained importance. The authors provide a good example of the applicability
of multiple dual-fuel modes; however, only scattered experimental
results were presented in the comparison of dual-fuel modes
because this study focused on the selection of the combustion mode for

the steady-state engine calibration. Therefore, it is difficult to understand
the operating strategy of each mode comprehensively because
detailed information on the variables is omitted.

Different dual-fuel modes were investigated separately to overcome
barriers to commercialization. Few studies have attempted to combine
the CDF, E-Pilot, and RCCI modes or some of these modes under limited
engine load conditions. This study conducted a comparative evaluation
of the NG-diesel dual-fuel modes (CDF, E-Pilot, and RCCI) in a multicylinder
heavy-duty engine under low-to-full load conditions. In
comparing the three combustion modes, this study introduced doubleinjection
strategies of the diesel to the CDF mode unlike previous
studies that implemented a late single injection [3,10,28]. Diesel double
injections can improve the thermal efficiency of the CDF mode through
the mixture formation optimization at low loads and through MPRR

Nomenclature

aTDC after top dead center
BMEP brake mean effective pressure
BTE : brake thermal efficiency
CAD crank angle degree

CDF conventional dual fuel
CO carbon monoxide
CO 2 carbon dioxide

ECU engine control unit
EGR exhaust gas recirculation
E‒Pilot early pilot

GHG greenhouse gas
HC hydrocarbon

HRR heat release rate

MPRR maximum pressure rise rate
NG natural gas

NO X : nitrogen oxides

PM particulate matter

RCCI reactivity‒controlled compression ignition
SOI start of injection
TDC top dead center

H. Park et al.
Energy 268 (2023) 126769

3

reduction at high loads [2,33]. Since diesel double injections are already
implemented in the E-Pilot and RCCI, the double-injection strategies for
the CDF introduced in this study are considered advantageous in
switching between the dual-fuel modes. The three dual-fuel modes were
comprehensively examined in terms of combustion phasing control,
thermal efficiency, the analysis of heat release and energy balance, and
exhaust gas emissions.

2. Experiments and methods

2.1. Experimental setup

A comparative evaluation of NG-diesel dual-fuel combustion modes
(CDF, E-Pilot, and RCCI) was conducted experimentally in a multicylinder,
heavy-duty engine with a displacement of 11.1 L. The engine
specifications are presented in Table 1. The properties of the NG and
diesel are listed in Tables 2 and 3, respectively.

Fig. 1 shows a schematic of the NG‒diesel dual-fuel engine experimental
setup. The NG was supplied to the intake port through six port
injectors with an injection pressure of 0.8 MPa. The NG injection mass
was measured by a mass flowmeter (CMFS025 M, Emerson). Diesel was
fed directly into the engine cylinder through a common‒rail system that
can handle diesel-injection pressures up to 180 MPa. The diesel injection
mass was measured with a mass flowmeter (735 S, AVL). Control parameters
for the diesel and NG injections including the injection timing,
injection duration, and fuel-injection pressure were varied using an NG
engine control unit (ECU) and a diesel ECU, respectively. The air mass
introduced into the engine cylinders was measured with a mass flowmeter
(FMT700‒P, ABB). The in-cylinder pressure was measured by a
piezoelectric pressure sensor (GU21D, AVL). The crank angle position
was obtained through a shaft encoder (ETU‒427, AVL) having a resolution
of 0.2 crank angle degree (CAD). The combustion parameters of
the dual-fuel modes were obtained using a combustion analyzer (X-ion,
AVL) based on the in-cylinder pressure measurement for 300 consecutive
cycles. The concentrations of exhaust gases were measured using an
exhaust gas analyzer (AMA i60, AVL). The analyzer was composed of
different gas detectors; the detailed measurement principles are
described in Ref. [34]. The extinction coefficients for the exhaust PM
values of the dual-fuel modes were measured using an opacimeter (439,
AVL). The conversion of the extinction coefficient into soot density
follows the correlation in Ref. [35]. The specific emissions of the exhaust
gases were calculated according to the method established by the United
Nations [36]. Table 4 presents the specifications of the measurement
equipment used in this study. Table 5 presents the uncertainties of the
engine parameters. The uncertainties were obtained using the analysis
method provided in Ref. [37].

2.2. Experimental method

Fig. 2 shows a schematic of the NG-diesel dual-fuel modes utilized in
this study. NG was supplied to the intake port during the intake stroke
for all three dual-fuel modes. The CDF mode is a traditional approach to
the dual-fuel combustion that utilizes delayed diesel SOIs. This study
adopted double-injection strategies for diesel unlike previous studies

that implemented a late single injection of diesel [10,28]. A small
amount of pilot injection immediately before the main injection was
effective in reducing the MPRR, and this enabled engine operations from
low to full load conditions. The RCCI is technology that can achieve high
efficiency and low emissions among dual-fuel modes. Diesel was injected
relatively early in the RCCI mode compared to the diesel injection of
the CDF mode during the compression stroke. The RCCI mode adopted
double-injection strategies for diesel to minimize the cylinder wall
wetting of the spray. Unfortunately, the RCCI mode was limited to
low-load operation because of its high MPRR unlike the CDF mode. The
E-Pilot is a hybridization of the CDF and RCCI modes; the first and
second diesel SOIs were similar to those of the RCCI and CDF modes,
respectively. It was possible to operate the engine in higher load conditions
than those in the RCCI mode by reducing the mass of the first
diesel injection in the E-Pilot mode. However, the high-load operation
was also limited in the E-Pilot mode with an increase in the engine load
because of its high MPRR.

Table 6 lists the experimental conditions for the comparison of the
dual-fuel combustion modes. The engine speed was selected as 1200
revolutions per minute, which had the maximum torque of the base
engine. The experimental investigation was performed for 0.6, 1.2, 1.8,
and 2.4 MPa brake mean effective pressures (BMEPs), which correspond
to the 25%, 50%, 75%, and 100% of the maximum engine load,
respectively. The coolant temperature was maintained at 363 ± 2 K, and
the oil temperature was maintained at different values depending on the
engine load; this value increased with the engine load. The NG substitution
rate varied from 80% to 30% as engine load increased from 0.6
MPa to 2.4 MPa BMEP; the operation window for the engine was narrow
because of knocking combustion or high MPRR at a higher NG substitution
rate. The NG substitution rate was defined as the energy content
of the NG divided by the total energy content of the NG and diesel which
are indicated in Equation (1).

NG substitution rate [%] = m˙ NGLHVNG
m˙ NGLHVNG + m˙ dieselLHVdiesel

× 100 (1)

where m˙ NG and m˙ diesel are the mass flow rates of the NG and diesel,
respectively. LHVNG and LHVdiesel are the lower heating values of the NG
and diesel, respectively. The specific values of the intake pressure, back
pressure, equivalence ratio of premixed NG-air mixture, and total
equivalence ratio according to the engine load and NG substitution rate
were also included in Table 6. The total equivalence ratio was calculated
through Equation (2) [19].

Table 1

Engine specifications.

Item Specification
Cylinder arrangement [¡] In‒line 6

Bore × stroke [m] 0.123 × 0.155
Displacement [L] 11.1

Compression ratio [− ] 16.6:1

Number of valves per cylinder [− ] 4 (2 intake and 2 exhaust)

Diesel injection system Common‒rail (Max. 180 MPa)
Natural gas injection system Port‒fuel injection (0.8 MPa)
Boosting system Wastegate turbocharger

Table 2

Properties of natural gas.

Item Specification

Composition [% by volume] Methane (CH4): 91.3
Ethane (C2H6): 5.3

Propane (C3H8): 2.2
Butane (C4H10): 1.0
Nitrogen (N2): 0.2
Motor octane number (MON) [− ] 124

Methane number (MN) [− ] 81.7
Lower heating value (LHV) [MJ/Nm3
] 38.5
Density at 273 K [kg/Nm3
] 0.788
Stoichiometric air‒to‒fuel ratio [− ] 16.9

Table 3

Properties of diesel.

Item Specification
Cetane number [− ] 52.1
Density at 273 K [kg/m3] 838

Lower heating value [MJ/kg] 42.6
Stoichiometric air‒to‒fuel ratio 14.5

H. Park et al.
Energy 268 (2023) 126769

4

Total equivalence ratio [ − ] = m˙ NGAFRNG + m˙ dieselAFRdiesel
m˙ air

(2)

where m˙ air is the mass flow rate of the air. AFRNG and AFRdiesel are the airto-fuel
ratios of the NG and diesel, respectively. The diesel injection
pressure increased with an increase in engine load. EGR technology was
excluded in this study to focus on the comparison of three different dualfuel
modes. Some benefits can be obtained with the introduction of EGR

in each dual-fuel mode. However, the performance change attributed to
the difference in the optimal EGR rate for each mode can harm the
comparison of the three combustion modes.

The experimental procedure to compare the dual-fuel modes in a
heavy-duty engine is as follows: First, the three dual-fuel modes were
compared at 0.6 MPa BMEP. Second, CDF and E-Pilot modes were
compared at 1.2 MPa BMEP because the high MPRR of the RCCI mode
restricted its operation. Finally, only CDF mode was operated at 1.8 and
2.4 MPa BMEP because the E-Pilot mode showed high MPRR values. The
MPRR limit was determined at 1.0 MPa/CAD to prevent engine damage
[2].

2.3. Analysis of energy balance

Energy balance was analyzed to examine the differences in the
thermal efficiencies of the three dual-fuel combustion modes. The fuel
power of the NG and diesel in dual-fuel modes is divided into the gross

Fig. 1. Schematic of natural gas‒diesel dual fuel engine setup.

Table 4

Specifications of measurement equipment.

Measured
parameters

Device Measurement
range

Linearity/
accuracy

Repeatability

Natural gas
flow rate

CMFS050 M
(Emerson)

0–60 kg/h ≤ ± 0.25%
of MV**
≤ ± 0.2% of
MV**
Diesel flow
rate
735 S (AVL) 0–125 kg/h ≤ ± 0.12%
of MV**
–

Air flow rate FMT700‒P
(ABB)

0–2400 kg/h ≤ ± 1% of
MV**
≤ ± 0.25% of
MV**
In‒cylinder
pressure
GU21D
(AVL)
0–25 MPa ≤ ± 0.11%
of FS*
–

THC
CH4
NOX
CO
CO2
O2

AMA i60
(AVL)

0–12,000 ppm
0–8000 ppm
0–6000 ppm
0–10 vol%
0–20 vol%
0–25 vol%

≤ ± 1% of
FS*

≤ ± 0.5% of
FS*

Extinction
coefficient

439 (AVL) 0–10 1/m ≤ ± 0.5%
of MV**

–

*FS: full scale, **MV: measurement value.

Table 5

Uncertainties of engine parameters.

Parameters Data uncertainty [%]
Brake thermal efficiency ±0.8
Combustion loss ±1.0
Exhaust loss ±1.0
Heat transfer loss ±1.3
NOX and CH4 emissions ±1.6
CO emissions ±1.5
PM emissions ±1.8

H. Park et al.
Energy 268 (2023) 126769

5

indicated power, combustion loss, exhaust loss, and heat transfer loss [2,
28]. The gross indicated power comprises the brake power, friction loss,
and pumping loss. Brake thermal efficiency (BTE) is defined as the brake
power divided by the fuel power [38]. The friction loss is determined by
subtracting the brake power from the net indicated power. The pumping
loss is determined by subtracting the net indicated power from the gross
indicated power. The combustion loss is defined as the power of
incomplete combustion products divided by the fuel power [2]. The
exhaust loss is defined as the power of the exhaust gas enthalpy divided
by the fuel power [34]. The heat transfer loss is determined by subtracting
the gross indicated power, combustion loss, and exhaust loss
from the fuel power [5]. The formulas for calculating the BTE, combustion
loss, and exhaust loss are presented in Equations (3)–(5). Specific
information on each term in these Equations is provided in Ref. [2].

BTE [%] = 3.6Pbrake
m˙ NGLHVNG + m˙ dieselLHVdiesel

× 100 (3)

Combustion loss = m˙ COLHVCO + m˙ CH4LHVNG + m˙ NMHCLHVdiesel
m˙ NGLHVNG + m˙ dieselLHVdiesel

(4)

Exhaust loss = m˙ exh[hexh(Texh) − hamb(Tamb)]
m˙ NGLHVNG + m˙ dieselLHVdiesel

(5)

3. Results and discussion

3.1. Comparison of CDF, E-Pilot, and RCCI modes at low loads

A comparative evaluation of CDF, E-Pilot, and RCCI modes was
conducted based on key engine performance and emissions data at 0.6
MPa BMEP. Table 7 lists the diesel injection parameters for the three
dual-fuel modes. The parameters were determined to achieve a high
thermal efficiency in each dual-fuel mode through preliminary
experiments.

Fig. 3 shows the CA50 and MPRR of the three dual-fuel modes with
variations in diesel main SOI. CA50 was selected as a combustion
parameter representing the combustion phasing of dual-fuel modes, and
was defined by the crank angle position of 50% mass fraction burned
[39]. CA50 was controlled in the same direction as the diesel SOI in the
CDF and E-Pilot modes, whereas the CA50 was delayed with an advance
in the diesel SOI in the RCCI mode. The heat release rate (HRR) curves of
the three dual-fuel modes with variations in diesel main SOI are presented
in Fig. 4. In the CDF mode, diesel was injected near TDC where
the ambient temperature was high; therefore, the injected diesel acted as
an ignition source and the combustion initiated [17]. In the RCCI mode,
the ignition delay increased significantly because of the early diesel SOI.
Diesel was premixed with the surrounding NG-air mixture during the
ignition delay. Therefore, the combustion initiated from locally rich and
highly reactive regions where the diesel was injected [23]. In this situation,
the local equivalence ratio and reactivity increased in the diesel
injection regions as the diesel SOI was retarded, and this advanced
CA50. In the E-Pilot mode, combustion did not occur with the diesel
pilot injection that had an SOI similar to that of the RCCI mode. The
CA50 moved in the same direction as the diesel SOI because the combustion
initiated with the main diesel injection. Although the direction
of combustion phasing control was the same for the CDF and E-Pilot
modes, the change in CA50 with respect to the diesel main SOI was
greater in the CDF mode than that of the E-Pilot mode. In both modes,
the combustion initiation with variations in the diesel main SOI was
similar. However, there was a difference in the HRR during the flame
propagation phase after the first peak HRR. In the CDF mode, the heat
release from the flame propagation of the NG-air premixed mixture
significantly delayed as the diesel main SOI was retarded. Nonetheless,
the difference in the heat release during the flame propagation phase
was not significant because the first injected diesel in the E-Pilot mode
was premixed with the NG-air mixture. For all dual-fuel modes, the
diesel SOIs were controlled such that the CA50s were not positioned
before TDC. This can help prevent the excessive MPRR caused by the
combination of piston compression and combustion. The MPRR was
higher than 1.0 MPa/CAD for the CDF mode when CA50 was advanced
before TDC.

Fig. 5 shows the BTE and combustion efficiency of the three dual-fuel
modes with variations in CA50. The BTE and combustion efficiency are
presented based on CA50 because the diesel main SOIs of the three
modes are significantly different, as shown in Fig. 3. In internal combustion
engines, CA50 is one of the most important factors that influences
the performance and emissions [19,39]. In all three dual-fuel

Fig. 2. Schematic of natural gas-diesel dual-fuel combustion modes.

Table 6

Experimental conditions.

Item Value
Engine speed [revolutions/
minute]

1200

Engine load (BMEP) [MPa] 0.6 1.2 1.8 2.4
Coolant temperature [K] 363 ± 2

Oil temperature [K] 367 ± 2 371 ± 2 372 ± 2 375 ± 2
Natural gas substitution rate
[%]
80 60 40 30

Intake pressure [kPa] 132 ± 2 166 ± 4 210 ± 4 256 ± 4
Back pressure [kPa] 102 ± 1 104 ± 1 108 ± 1 113 ± 1
Equivalence ratio (premixed
NG) [¡]
0.34 ±
0.01
0.34 ±
0.01
0.26 ±
0.01
0.22 ±
0.01
Equivalence ratio (total)
[¡]
0.41 ±
0.02
0.57 ±
0.01
0.65 ±
0.01
0.73 ±
0.01
Diesel injection pressure
[MPa]
80 90 100 110

Table 7

Diesel injection parameters for dual-fuel modes at 0.6 MPa BMEP.
Dual-fuel
modes
Pilot SOI [CAD
aTDC]
Main SOI [CAD
aTDC]
Main mass fraction
[%]
CDF − 29 ~ − 22 − 23 ~ − 16 85
E-Pilot − 56 ~ − 48 − 22 ~ − 14 40
RCCI − 84 ~ − 72 − 54 ~ − 42 40

H. Park et al.
Energy 268 (2023) 126769

6

modes, the BTEs increased as the CA50s were advanced, and showed
maximum values at CA50s near TDC. When CA50 was located before
TDC in internal combustion engines, it produced negative work, and
thus, reduced thermal efficiency [40]. When the CA50 was located
excessively delayed, it reduced combustion efficiency. Although the

negative work increased with advancing the CA50 near TDC, the combustion
efficiency significantly increased as shown in Fig. 5, resulting in
the BTE increase. In the low-load operation where the fuel power was
low, the increase in the combustion efficiency with respect to the CA50
advance was greater than the negative work effect. In the E-Pilot and
RCCI modes, the BTE slightly changed with variations in the CA50,
whereas the BTE significantly decreased with retarding the CA50 in the

CDF mode. In the E-Pilot and RCCI modes where some or all of diesel
was injected early, the overall combustion phasing slightly delayed and
the peak HRR values were similar with retarding the CA50. However, as
the CA50 was retarded, the heat release during the flame propagation
phase after the first peak HRR significantly delayed and the peak HRR
values decreased. Therefore, the BTE in the CDF mode was greatly
influenced by the CA50. For all given CA50s, BTE was the highest in the
order of RCCI, E-Pilot, and CDF. An analysis of energy losses indicated
the cause of the BTE trend. Fig. 6 shows the energy balance of the three
dual-fuel modes for each optimal BTE. The E-Pilot and RCCI modes
exhibited lower combustion losses than the CDF mode. The heat transfer
loss for the RCCI mode was lower than those of the CDF and E-Pilot
modes. In conclusion, the RCCI mode had the highest BTE because of its
lower combustion and heat transfer losses. The wide dispersion of diesel
increased the reactivity of the surrounding NG-air mixture because the
RCCI mode had early diesel SOIs, and this helped reduce the combustion
loss [17]. The early diesel SOIs also allowed diesel to be premixed with
the NG-air mixture, and therefore, the combustion temperature was
reduced because of the locally lean fuel-air mixture, which reduced the
heat transfer loss [41].

Figs. 7 and 8 show the HRR and pressure-volume traces of the three
dual-fuel modes for each optimal BTE. Two peak HRRs were distinguished
in the CDF and E-Pilot modes, whereas the RCCI mode exhibited
a bell-shaped HRR curve. The first peak HRR in the CDF and E-Pilot
modes corresponded to the autoignition of diesel and some entrained
premixed NG-air mixture combustion [42]. Subsequently, the flame
propagation of the premixed NG-air mixture constituted the second peak
HRR. In the RCCI mode, the combustion initiated with a small
low-temperature heat release and high-temperature heat release
occurred immediately because diesel was premixed with the NG-air
mixture. This bell-shaped HRR curve contributed to maintaining a
lower pressure trace before TDC and to allowing a pressure rise near
TDC in the pressure-volume trace. Therefore, the pressure-volume trace
was the closest to the theoretical constant-volume cycle among the three
dual-fuel modes; this is favorable for achieving a high BTE. The
pressure-volume trace of the E-Pilot mode was similar to that of the RCCI
mode because the first peak HRR of the E-Pilot mode was significantly

Fig. 3. CA50 and maximum pressure rise rate of dual-fuel modes with variations
in diesel main start of injection at 0.6 MPa BMEP.

Fig. 4. Heat release rate curves of dual-fuel modes with variations in diesel main start of injection at 0.6 MPa BMEP.

H. Park et al.
Energy 268 (2023) 126769

7

lower than that of the CDF mode. Only the diesel main was injected near
TDC in the E-Pilot mode although both the pilot and main diesel sprays
were injected near TDC in the CDF mode. Therefore, a reduction in the
diesel quantity injected near TDC and entrained premixed NG-air
mixture combustion resulted in the lower first peak HRR.

Fig. 9 shows the NOX and PM emissions of the three dual-fuel modes
with variations in CA50. For all given CA50s, the NOX and PM emissions
were effectively reduced in the E-Pilot and RCCI modes while the
emissions were high in the CDF mode. In the CDF mode, high levels of
NOX were formed in the high-temperature regions surrounding the
diesel sprays because the pilot and main were injected near TDC [17]. In
the RCCI mode, early diesel injections were significantly separated from
the combustion initiation. Therefore, the premixed fuel-air mixture
resulted in a low combustion temperature, and NOX formation was
mitigated effectively. The E-Pilot mode emitted intermediate levels of

NOX emissions between those of the RCCI and CDF modes. The PM
emissions were reduced in the E-Pilot and RCCI modes. The CDF mode
had locally rich and high-temperature regions of diesel sprays at the
combustion initiation [41]. However, the E-Pilot and RCCI modes
reduced the local equivalence ratio and combustion temperature, and
this led to lower PM emissions. Fig. 10 shows the CH4 and CO emissions
of the three dual-fuel modes with variations in CA50. The RCCI mode,
which had early diesel SOIs, recorded lower CH4 and CO emissions than
the CDF mode; this is because the wide distribution of diesel increased
the reactivity of the surrounding NG-air mixture [23]. The E-Pilot mode
could reduce CH4 and CO emissions to the same level as that of the RCCI
mode because the first diesel SOI was as early as that of the RCCI mode.

3.2. Comparison of CDF and E-Pilot modes at mid loads

Despite the superior efficiency and emissions of the RCCI mode at
0.6 MPa BMEP, engine operation was impossible at 1.2 MPa BMEP
because of the difficulty in controlling combustion phasing and the high
MPRR. Therefore, a comparative evaluation was conducted for the CDF
and E-Pilot modes. Table 8 lists the diesel injection parameters of the

Fig. 5. Brake thermal efficiency and combustion efficiency of dual-fuel modes
with variations in CA50 at 0.6 MPa BMEP.

Fig. 6. Energy balance of dual-fuel modes for each optimum at 0.6 MPa BMEP.

Fig. 7. Heat release rate curves of dual-fuel modes for each optimum at 0.6
MPa BMEP.

Fig. 8. Pressure–volume diagram of dual-fuel modes for each optimum at 0.6
MPa BMEP.

H. Park et al.
Energy 268 (2023) 126769

8

two dual-fuel modes. In the E-Pilot mode, the mass fraction of the diesel
pilot injection was reduced to 20% to avoid an excessive MPRR rise.
Fig. 11 shows the CA50 and MPRR of the CDF and E-Pilot modes with
variations in diesel main SOI. Combustion phasing was effectively
controlled by changing the diesel SOI in the two dual-fuel modes at 1.2
MPa BMEP, similar to the low-load operation. When the diesel SOI was
advanced, the combustion phasing also advanced. However,

advancements in the diesel SOI were limited by the high MPRR. It was
possible to advance combustion phasing near TDC in the E-Pilot mode
than in the CDF mode. The premixed NG-air in the squish area was
partially burned by the early injection of the diesel pilot [14]. The early
partial burning diluted the unburned end-gas in the subsequent main
combustion process in the E-Pilot mode, and therefore, the MPRR values
were lower than those in the CDF mode, even with the relatively
advanced CA50.

Fig. 12 shows the BTE and combustion efficiency of the CDF and EPilot
modes with variations in CA50. The BTE of the E-Pilot mode was
slightly higher than that of the CDF mode. The higher BTE was due to its
higher combustion efficiency from an early pilot injection and an
advanced CA50. The combustion performance was enhanced because
the early pilot injection of the diesel increased the reactivity of the
surrounding NG-air premixed mixture prior to the combustion initiation
[2]. Further, the E-Pilot mode allowed an advanced CA50, which

Fig. 9. Nitrogen oxides and particulate matter emissions of dual-fuel modes
with variations in CA50 at 0.6 MPa BMEP.

Fig. 10. Methane and carbon monoxide emissions of dual-fuel modes with
variations in CA50 at 0.6 MPa BMEP.

Table 8

Diesel injection parameters of dual-fuel modes at 1.2 MPa BMEP.
Dual-fuel
modes
Pilot SOI [CAD
aTDC]
Main SOI [CAD
aTDC]
Main mass fraction
[%]
CDF − 18 ~ − 15 − 12 ~ − 9 94
E-Pilot − 43 ~ − 39 − 8 ~ − 4 80

Fig. 11. CA50 and maximum pressure rise rate of CDF and E-Pilot modes with
variations in diesel main start of injection at 1.2 MPa BMEP.

Fig. 12. Brake thermal efficiency and combustion efficiency of CDF and E-Pilot
modes with variations in CA50 at 1.2 MPa BMEP.

H. Park et al.
Energy 268 (2023) 126769

9

contributed to an increase in the combustion efficiency. An energy
balance analysis was performed to closely compare the BTE of the two
dual-fuel modes. Fig. 13 shows the energy balance of the CDF and E-Pilot
modes for each optimal BTE. The E-Pilot mode had advantages in
combustion and exhaust losses compared to the CDF mode, but the
benefits were partially offset by its high heat transfer loss. The advanced
CA50 of the E-Pilot mode reduced the combustion and exhaust losses
[40]. However, the advanced CA50 caused greater heat transfer loss in
the E-Pilot mode. As the combustion took place in a smaller volume of
the engine cylinder in the E-Pilot mode, the surface area was small
which was advantageous for reducing heat transfer loss. However, the
heat was transferred to the engine head and piston top surface when the
in-cylinder temperature was high resulting in the higher heat transfer
loss. Therefore, it can be concluded that the reduction in combustion loss
contributed significantly to the improvement of the BTE in the E-Pilot
mode than that of the CDF mode. The combustion loss accounted for
4.6% of the fuel energy in the CDF mode, whereas the E-Pilot mode
recorded a combustion loss of 3.6%.

Figs. 14 and 15 show the HRR and pressure-volume traces of the CDF
and E-Pilot modes for each optimal BTE. The partial oxidation of the NGair
mixture caused by an early pilot of diesel allowed CA50 to advance
toward TDC in the E-Pilot mode [14]. The partial oxidation contributed
to reducing the peak HRR because it diluted the unburned NG-air
mixture. In addition, the early pilot and its long ignition delay in the
E-Pilot mode formed more homogeneous lean mixture than that of the
CDF mode reducing the peak HRR. Therefore, the HRR profile of the

E-Pilot mode resulted in the pressure-volume trace closer to the theoretical
constant-volume cycle than that of the CDF mode; this is favorable
for achieving a high BTE. The advanced CA50 induced a sharp rise
in the pressure near TDC.

Fig. 16 shows the NOX and PM emissions of the CDF and E-Pilot
modes with variations in CA50. There was no significant difference in
NOX emissions between the two modes; however, the NOX emissions
decreased slightly in the E-Pilot mode when comparing optimal BTE

cases. Although an advanced CA50 increased the combustion temperature,
the implementation of an early pilot and a late main contributed to
the formation of a locally leaner fuel-air mixture compared to that of the
late pilot and main injections [30]. Therefore, the NOX emissions were
reduced because of its lower combustion temperature. In addition, the
PM emissions were also slightly reduced in the E-Pilot mode for the same
reason. Fig. 17 shows the CH4 and CO emissions of the CDF and E-Pilot

modes with variations in CA50. The CH4 and CO emissions were reduced
in the E-Pilot mode than those in the CDF mode. Despite the small
amount of the diesel pilot, its early SOI enhanced flame propagation to
relatively distant regions by increasing the reactivity of the unburned
end-gas in the squish areas [14,30].

3.3. CDF mode at high loads

As the engine load was higher than 1.8 MPa BMEP, engine operation
with the E-Pilot mode was limited by its CA50 location before TDC and
high MPRR. Therefore, the CDF mode was selected as the high-load
operation. Combustion phasing was retarded in the CDF mode at highload
operations to suppress the MPRR. It is known that the thermal efficiency
can be achieved at a level equal to or higher than that of dieselonly
combustion under high-load conditions [28]. Table 9 summarizes
the diesel injection parameters of the CDF mode at 1.8 MPa and 2.4 MPa
BMEP. Pilot injection was used to suppress the high MPRR [2,14]. The
mass fractions of the pilot injection were minimized to achieve high
BTEs by preventing negative work attributed to the autoignition of the
diesel pilot injection and some entrained premixed NG-air mixture
Fig. 13. Energy balance of CDF and E-Pilot modes for each optimum at 1.2
MPa BMEP.

Fig. 14. Heat release rate curves of CDF and E-Pilot modes for each optimum at
1.2 MPa BMEP.

Fig. 15. Pressure–volume diagram of CDF and E-Pilot modes for each optimum
at 1.2 MPa BMEP.

H. Park et al.
Energy 268 (2023) 126769

10

combustion.

Fig. 18 shows the CA50 and MPRR of the CDF mode with variations
in diesel main SOI. Like in low and mid loads, combustion phasing was
controlled in the same direction as the diesel SOI at 1.8 MPa and 2.4 MPa
BMEP. The advance in CA50 using the diesel SOI was limited by the high

MPRR values. The CA50 advance was limited to 12 CAD aTDC at 2.4
MPa BMEP although the CA50 advanced to near TDC at 0.6 MPa BMEP.
Fig. 19 shows the BTE and combustion efficiency of the CDF mode
with variations in CA50. The BTE increased at both high loads when the
CA50 advanced. An advance in diesel SOI prolonged the ignition delay,
and it formed a more premixed NG-air and diesel mixture prior to the
combustion initiation [17]. Therefore, the advanced CA50 resulted in an
increase in the peak HRR and a reduction in the combustion duration;
these were favorable for achieving a high BTE. The BTE was higher at
1.8 MPa BMEP than at 2.4 MPa BMEP because of its more advanced
CA50. There was no significant difference in combustion efficiency between
the two engine loads. An energy balance analysis was performed
for both high-load operations. Fig. 20 shows the energy balance of the
CDF mode at 1.8 MPa and 2.4 MPa BMEP for each optimal BTE.
Although the proportion of mechanical loss was high at 1.8 MPa BMEP,
the exhaust loss accounted for a low proportion. The mechanical losses

Fig. 16. Nitrogen oxides and particulate matter emissions of CDF and E-Pilot
modes with variations in CA50 at 1.2 MPa BMEP.

Fig. 17. Methane and carbon monoxide emissions of CDF and E-Pilot modes
with variations in CA50 at 1.2 MPa BMEP.

Table 9

Diesel injection parameters of CDF mode at 1.8 MPa and 2.4 MPa BMEP.
Engine load Pilot SOI [CAD
aTDC]
Main SOI [CAD
aTDC]
Main mass fraction
[%]
1.8 MPa
BMEP
− 15 ~ − 12 − 9 ~ − 6 97

2.4 MPa
BMEP

− 12 ~ − 10 − 6 ~ − 4 98

Fig. 18. CA50 and maximum pressure rise rate of CDF mode with variations in
diesel main start of injection at 1.8 MPa and 2.4 MPa BMEP.

Fig. 19. Brake thermal efficiency and combustion efficiency of CDF mode with
variations in CA50 at 1.8 MPa and 2.4 MPa BMEP.

H. Park et al.
Energy 268 (2023) 126769

11

in internal combustion engines are mainly caused by friction and
auxiliary losses [43]. Since the mechanical loss value did not increase
significantly with the engine load, the proportion in total fuel power
decreased with increasing the engine load. The more advanced CA50
decreased the exhaust temperature, and this lowered the exhaust loss
[40]. It is noteworthy that the proportion of combustion loss in the CDF
mode under high-load conditions was as low as that in the RCCI mode at
low-load operation and that in the E-Pilot mode at mid-load operation.
Although the combustion loss accounted for 5.1% in the CDF mode at
0.6 MPa BMEP, the proportion was reduced to 3.6% at 2.4 MPa BMEP.
This is because the heat release attributed to sufficient fuel energy inputs
resulted in a high combustion temperature under high-load conditions
[28]. A high BTE of 42.8% at 1.8 MPa BMEP was reduced to 38.8% at
0.6 MPa BMEP because of the different combustion losses.

Figs. 21 and 22 show the HRR and pressure-volume traces of the CDF
mode at 1.8 MPa and 2.4 MPa BMEP for each optimal BTE. The highload
operations showed more retarded HRR curves than those of the
low and mid loads; therefore, an effective pressure increase was

impossible in the small cylinder volume, and the highest pressure was
achieved when the piston moved down. Among the high-load operations,
the more advanced HRR profile at 1.8 MPa BMEP resulted in its
pressure-volume trace closer to the theoretical constant-volume cycle
than that at 2.4 MPa BMEP, which had a higher BTE.

Fig. 23 shows the NOX and PM emissions of the CDF mode with
variations in CA50 at 1.8 MPa and 2.4 MPa BMEP. Under the two highload
conditions, NOX emissions were reduced with retarding CA50;
however, the CA50 retardation led to an increase in PM emissions and a
reduction in BTE. The PM formed in the CDF mode is oxidized before the
exhaust process. Since the combustion temperature decreased with the
CA50 retardation, the PM was not actively oxidized, and thus, the PM
emissions increased [38]. Therefore, it is important to consider the
trade-off relationship between the NOX and PM emissions or the NOX
emissions and BTE. Fig. 24 shows the CH4 and CO emissions of the CDF
mode with variations in CA50 at 1.8 MPa and 2.4 MPa BMEP. Under
high-load operations where fuel energy was sufficiently introduced, the
CH4 and CO emissions slightly decreased with an advance in the CA50. It

Fig. 20. Energy balance of CDF mode for each optimum at 1.8 MPa and 2.4
MPa BMEP.

Fig. 21. Heat release rate curves of CDF mode for each optimum at 1.8 MPa
and 2.4 MPa BMEP.

Fig. 22. Pressure–volume diagram of CDF mode for each optimum at 1.8 MPa
and 2.4 MPa BMEP.

Fig. 23. Nitrogen oxides and particulate matter emissions of CDF mode with
variations in CA50 at 1.8 MPa and 2.4 MPa BMEP.

H. Park et al.
Energy 268 (2023) 126769

12

is noteworthy that the CH4 and CO emissions in the CDF mode at high
loads were as low as those in the RCCI mode at low-load operation and
those in the E-Pilot mode at mid-load operation.

4. Summary and conclusion

Dual-fuel engines are considered power sources that could provide
short-to-medium term solutions for the CO2 regulations in heavy-duty
vehicles and ships. This study conducted a comparative evaluation of
NG-diesel dual-fuel modes (CDF, E-Pilot, and RCCI) in a six-cylinder
heavy-duty engine under low-to-full load conditions.

The CDF mode was found to be the most suitable for the high-load
operation of dual-fuel engines. The combustion phasing was
controlled in the same direction as the diesel SOI. The CDF mode
operated the engine up to the full load of 2.4 MPa BMEP. High BTEs of
42.8% and 41.6% were achieved at 1.8 MPa and 2.4 MPa BMEP,
respectively. However, the BTE was reduced to 38.8% at 0.6 MPa BMEP.
Although the combustion losses accounted for 3.6%–3.8% at high loads,
its low-load operation showed a combustion loss of 5.1%.

The high combustion loss in the CDF mode at low-load operation was
overcome by implementing the E-Pilot and RCCI modes. The high
combustion loss of the CDF mode decreased to 3.5% and 3.3% in the EPilot
and RCCI modes, respectively. The RCCI mode achieved the
highest BTE of 41.4% among the three dual-fuel modes at 0.6 MPa
BMEP. A bell-shaped HRR profile in the RCCI mode approached the
theoretical Otto cycle. However, the extension of the operating range to
1.2 MPa BMEP was limited in the RCCI mode because of its CA50
location before TDC and excessive MPRR.

Unlike the RCCI mode, the engine operation with the E-Pilot mode
was possible at 1.2 MPa BMEP. The direction of the combustion phasing
control based on the diesel SOI was also the same as that in the CDF
mode. In the E-Pilot mode, the BTE was improved to 43.1% at 1.2 MPa
BMEP owing to the lower combustion loss than that of the CDF mode.
In conclusion, it was impossible to cover the entire engine operating
range using only one dual-fuel mode. Therefore, it is desirable to
implement an optimal dual-fuel mode for each load operation: RCCI
mode at low loads, E-Pilot mode at mid loads, and CDF mode at high
loads. In this case, efforts need to be devoted to the conversion between
dual-fuel modes because the direction of combustion phasing control
based on the diesel SOI in the RCCI mode is opposite to those in the CDF
and E-Pilot modes. The following strategy could also be a solution for

dual-fuel engine applications where the transient operation is frequent:
E-Pilot mode at low-to-mid loads and CDF mode at high loads. This
approach provides the benefits of smooth mode transitions, high BTE,
and low emissions.

From the aspect of the results covered in this study, it is necessary to
expand the operating range of the RCCI and E-Pilot modes to maximize
the advantages of dual-fuel engines. Although not covered in this study,
EGR and valve train technologies could allow the expansion of the RCCI
and E-Pilot modes to low and high loads. Research on piston geometries
dedicated to the dual-fuel modes are also useful for developing clean and
efficient dual-fuel engines.

Cretid author statement

Hyunwook Park: Investigation, Formal analysis, Writing – original
draft. Euijoon Shim: Conceptualization. Junsun Lee: Investigation, Data
curation. Seungmook Oh: Supervision. Changup Kim: Methodology,
Resources. Yonggyu Lee: Writing – review & editing. Kernyong Kang:
Visualization.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Data availability

The data that has been used is confidential.

Acknowledgement

The authors would like to acknowledge the governmental project
grant (No. 20003640) of the Ministry of Trade, Industry and Energy of
the Republic of Korea.

References

[1] Elkafas AG, Khalil M, Shouman MR, Elgohary MM. Environmental protection and
energy efficiency improvement by using natural gas fuel in maritime

transportation. Environ Sci Pollut Control Ser 2021;28(43):60585–96. https://doi.
org/10.1007/s11356-021-14859-6.

[2] Park H, Shim E, Lee J, Oh S, Kim C, Lee Y, Kang K. Large–squish piston geometry
and early pilot injection for high efficiency and low methane emission in natural
gas–diesel dual fuel engine at high–load operations. Fuel 2022;308:122015.
https://doi.org/10.1016/j.fuel.2021.122015.

[3] García A, Monsalve-Serrano J, Martinez-Boggio S, Gaillard P, Poussin O, Amer AA.
Dual fuel combustion and hybrid electric powertrains as potential solution to
achieve 2025 emissions targets in medium duty trucks sector. Energy convers
manage 2020;224:113320. https://doi.org/10.1016/j.enconman.2020.113320.
[4] Mikulski M, Ramesh S, Bekdemir C. Reactivity Controlled Compression Ignition for
clean and efficient ship propulsion. Energy 2019;182:1173–92. https://doi.org/
10.1016/j.energy.2019.06.091.

[5] Liu J, Wu P, Ji Q, Sun P, Wang P, Meng Z, Ma H. Experimental study on effects of
pilot injection strategy on combustion and emission characteristics of diesel/
methanol dual-fuel engine under low load. Energy 2022;247:123464. https://doi.
org/10.1016/j.energy.2022.123464.

[6] Nelles M. New engines at volvo trucks. ATZheavy duty worldwide 2019;12(3):
12–7. https://doi.org/10.1007/s41321-019-0033-7.

[7] Ma B, Yao A, Yao C, Chen C, Qu G, Wang W, Ai Y. Multiple combustion modes
existing in the engine operating in diesel methanol dual fuel. Energy 2021;234:
121285. https://doi.org/10.1016/j.energy.2021.121285.

[8] Yu H, Wang W, Sheng D, Li H, Duan S. Performance of combustion process on
marine low speed two-stroke dual fuel engine at different fuel conditions: full
diesel/diesel ignited natural gas. Fuel 2022;310:122370. https://doi.org/10.1016/
j.fuel.2021.122370.

[9] Lee CF, Pang Y, Wu H, Nithyanandan K, Liu F. An optical investigation of

substitution rates on natural gas/diesel dual-fuel combustion in a diesel engine.
Appl Energy 2020;261:114455. https://doi.org/10.1016/j.apenergy.2019.114455.
[10] Nieman DE, Morris AP, Miwa JT, Denton BD. Methods of improving combustion
efficiency in a high-efficiency, lean burn dual-fuel heavy-duty engine. SAE Tech
Pap 2019-01-0032. https://doi.org/10.4271/2019-01-0032.

[11] Aksu C, Kawahara N, Tsuboi K, Kondo M, Tomita E. Extension of PREMIER

combustion operation range using split micro pilot fuel injection in a dual fuel

Fig. 24. Methane and carbon monoxide emissions of CDF mode with variations
in CA50 at 1.8 MPa and 2.4 MPa BMEP.

H. Park et al.
Energy 268 (2023) 126769

13

natural gas compression ignition engine: a performance-based and visual
investigation. Fuel 2016;185:243–53. https://doi.org/10.1016/j.fuel.2016.07.120.
[12] Pham Q, Park S, Agarwal AK, Park S. Review of dual-fuel combustion in the
compression-ignition engine: spray, combustion, and emission. Energy 2022:
123778. https://doi.org/10.1016/j.energy.2022.123778.
[13] Paykani A, Garcia A, Shahbakhti M, Rahnama P, Reitz RD. Reactivity controlled
compression ignition engine: pathways towards commercial viability. Appl Energy
2021;282:116174. https://doi.org/10.1016/j.apenergy.2020.116174.
[14] Yousefi A, Guo H, Birouk M. Split diesel injection effect on knocking of natural gas/
diesel dual-fuel engine at high load conditions. Appl Energy 2020;279:115828.
https://doi.org/10.1016/j.apenergy.2020.115828.

[15] Liu J, Liu Z, Wang L, Wang P, Sun P, Ma H, Wu P. Numerical simulation and
experimental investigation on pollutant emissions characteristics of PODE/
methanol dual-fuel combustion. Fuel Process Technol 2022;231:107228. https://
doi.org/10.1016/j.fuproc.2022.107228.

[16] Jatoth R, Gugulothu SK, kiran Sastry GR. Experimental study of using biodiesel and
low cetane alcohol as the pilot fuel on the performance and emission trade-off
study in the diesel/compressed natural gas dual fuel combustion mode. Energy
2021;225:120218. https://doi.org/10.1016/j.energy.2021.120218.
[17] Yousefi A, Birouk M, Guo H. An experimental and numerical study of the effect of
diesel injection timing on natural gas/diesel dual-fuel combustion at low load. Fuel
2017;203:642–57. https://doi.org/10.1016/j.fuel.2017.05.009.
[18] Barba C, Dyckmans J, Forster ¨ J, Schnekenburger T. Natural gas-diesel dual fuel for
commercial vehicle engines. Internationaler Motorenkongress. Wiesbaden:
Springer Vieweg; 2017. p. 391–407. https://doi.org/10.1007/978-3-658-17109-4_
23. 2017.

[19] Park H, Shim E, Bae C. Expansion of low-load operating range by mixture
stratification in a natural gas-diesel dual-fuel premixed charge compression
ignition engine. Energy Convers Manag 2019;194:186–98. https://doi.org/
10.1016/j.enconman.2019.04.085.

[20] You J, Liu Z, Wang Z, Wang D, Xu Y, Du G, Fu X. The exhausted gas recirculation
improved brake thermal efficiency and combustion characteristics under different
intake throttling conditions of a diesel/natural gas dual fuel engine at low loads.
Fuel 2020;266:117035. https://doi.org/10.1016/j.fuel.2020.117035.
[21] Wei L, Geng P. A review on natural gas/diesel dual fuel combustion, emissions and
performance. Fuel Process Technol 2016;142:264–78. https://doi.org/10.1016/j.
fuproc.2015.09.018.

[22] Zhang W, Chang S, Wu W, Dong L, Chen Z, Chen G. A diesel/natural gas dual fuel
mechanism constructed to reveal combustion and emission characteristics. Energy
2019;179:59–75. https://doi.org/10.1016/j.energy.2019.04.106.
[23] Park H, Shim E, Bae C. Improvement of combustion and emissions with exhaust gas
recirculation in a natural gas-diesel dual-fuel premixed charge compression
ignition engine at low load operations. Fuel 2019;235:763–74. https://doi.org/
10.1016/j.fuel.2018.08.045.

[24] Wissink ML, Curran SJ, Roberts G, Musculus MP, Mounaïm-Rousselle C. Isolating
the effects of reactivity stratification in reactivity-controlled compression ignition
with iso-octane and n-heptane on a light-duty multi-cylinder engine. Int J Engine
Res 2018;19(9):907–26. https://doi.org/10.1177/1468087417732898.
[25] Singh AP, Kumar V, Agarwal AK. Evaluation of comparative engine combustion,
performance and emission characteristics of low temperature combustion (PCCI
and RCCI) modes. Appl Energy 2020;278:115644. https://doi.org/10.1016/j.
apenergy.2020.115644.

[26] Indrajuana A, Bekdemir C, Luo X, Willems F. Robust multivariable feedback
control of natural gas-diesel RCCI combustion. IFAC-PapersOnLine 2016;49(11):
217–22. https://doi.org/10.1016/j.ifacol.2016.08.033.

[27] Hall C, Kassa M. Advances in combustion control for natural gas–diesel dual fuel
compression ignition engines in automotive applications: a review. Renew Sustain
Energy Rev 2021;148:111291. https://doi.org/10.1016/j.rser.2021.111291.

[28] Nieman DE, Morris AP, Neely GD, Matheaus AC, Miwa JT. Utilizing multiple
combustion modes to increase efficiency and achieve full load dual-fuel operation
in a heavy-duty engine. SAE Tech Pap 2019-01-1157. https://doi.org/10.4271/
2019-01-1157.

[29] Indrajuana A, Bekdemir C, Feru E, Willems F. Towards model-based control of
RCCI-CDF mode-switching in dual fuel engines. SAE Tech Pap 2018-01-0263.
https://doi.org/10.4271/2018-01-0263.

[30] Huang H, Zhu Z, Chen Y, Chen Y, Lv D, Zhu J, Ouyang T. Experimental and
numerical study of multiple injection effects on combustion and emission
characteristics of natural gas–diesel dual-fuel engine. Energy Convers Manag 2019;
183:84–96. https://doi.org/10.1016/j.enconman.2018.12.110.
[31] Benajes J, García A, Monsalve-Serrano J, Sari RL. Fuel consumption and engine-out
emissions estimations of a light-duty engine running in dual-mode RCCI/CDC with
different fuels and driving cycles. Energy 2018;157:19–30. https://doi.org/
10.1016/j.energy.2018.05.144.

[32] Shim E, Park H, Bae C. Comparisons of advanced combustion technologies (HCCI,
PCCI, and dual-fuel PCCI) on engine performance and emission characteristics in a
heavy-duty diesel engine. Fuel 2020;262:116436. https://doi.org/10.1016/j.
fuel.2019.116436.

[33] Wang L, Liu J, Ji Q, Sun P, Li J, Wei M, Liu S. Experimental study on the high load
extension of PODE/methanol RCCI combustion mode with optimized injection
strategy. Fuel 2022;314:122726. https://doi.org/10.1016/j.fuel.2021.122726.
[34] Park H, Lee J, Jamsran N, Oh S, Kim C, Lee Y, Kang K. Comparative assessment of
stoichiometric and lean combustion modes in boosted spark-ignition engine fueled
with syngas. Energy Convers Manag 2021;239:114224. https://doi.org/10.1016/j.
enconman.2021.114224.

[35] Dodd AE, Holubecki Z. The measurement of diesel exhaust smoke. Motor Industry
Research Association; 1965.

[36] Worldwide harmonized heavy duty emissions certification procedure – chapter 8.
Emissions measurement and calculation. United Nations; 2005.
[37] Chen Z, Zhang T, Wang X, Chen H, Geng L, Zhang T. A comparative study of
combustion performance and emissions of dual-fuel engines fueled with natural
gas/methanol and natural gas/gasoline. Energy 2021;237:121586. https://doi.
org/10.1016/j.energy.2021.121586.

[38] Heywood JB. Internal combustion engine fundamentals. McGraw-Hill Education;
2018.

[39] Jamsran N, Park H, Lee J, Oh S, Kim C, Lee Y, Kang K. Influence of syngas
composition on combustion and emissions in a homogeneous charge compression
ignition engine. Fuel 2021;306:121774. https://doi.org/10.1016/j.
fuel.2021.121774.

[40] Saxena S, Bedoya ID. Fundamental phenomena affecting low temperature
combustion and HCCI engines, high load limits and strategies for extending these
limits. Prog Energy Combust Sci 2013;39(5):457–88. https://doi.org/10.1016/j.
pecs.2013.05.002.

[41] Merts M, Derafshzan S, Hyvonen ¨ J, Richter M, Lundgren M, Verhelst S. An optical
investigation of dual fuel and RCCI pilot ignition in a medium speed engine. Fuel
Commun 2021;9:100037. https://doi.org/10.1016/j.jfueco.2021.100037.
[42] Ahmad Z, Kaario O, Qiang C, Vuorinen V, Larmi M. A parametric investigation of
diesel/methane dual-fuel combustion progression/stages in a heavy-duty optical
engine. Appl Energy 2019;251:113191. https://doi.org/10.1016/j.
apenergy.2019.04.187.

[43] Tormos B, Martín J, Carreno ˜ R, Ramírez L. A general model to evaluate mechanical
losses and auxiliary energy consumption in reciprocating internal combustion
engines. Tribol Int 2018;123:161–79. https://doi.org/10.1016/j.
triboint.2018.03.007.

H. Park et al.