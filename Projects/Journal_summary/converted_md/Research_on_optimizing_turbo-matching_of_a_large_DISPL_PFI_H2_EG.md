# Research on optimizing turbo-matching of a large DISPL PFI H2 EG

Research on optimizing turbo-matching of a largedisplacement
PFI hydrogen engine to achieve highpower
performance

Feng-yu Lai a
, Bai-gang Sun a,b

, Gang Xiao c
, Qing-he Luo a,b
,
Ling-zhi Bao a,*

a School of Mechanical Engineering, Beijing Institute of Technology, Beijing 100081, China
b Beijing Institute of Technology Chongqing Innovation Center, Chongqing, 401121, China
c Guangxi Yuchai Machinery Co., Ltd., Guangxi 537005, China

highlights

 The CNG engine turbine is not suited to H2ICE due to the low reduced mass flow rate.
 The method considers exhaust components and temperature to reach desired power.
 The max power is improved from 93.0 kW to 128.9 kW with the optimized turbine.
 The output torque is reduced by 15.6% at 1200 rpm due to poor intake pressure.
 The feature of turbocharging of H2ICE is discussed with some potential solutions.

article info
Article history:
Received 11 April 2023
Received in revised form
30 May 2023
Accepted 9 June 2023
Available online 30 June 2023

Keywords:

Turbocharger-matching
Turbine selection

Hydrogen internal combustion
engines

Exhaust gas component
Power performance

abstract

The output power of hydrogen engines is restricted due to the low volume energy density
of hydrogen and lean burn, thus a turbocharger is necessary to boost the power intensity,
especially for large-displacement hydrogen engines. However, turbine selection for
hydrogen engines is complex comparing gasoline engines because of the different exhaust
components and low exhaust temperature. In this research, the turbocharger-matching of
a 5.13 L hydrogen engine is studied, and the results show the original turbine, whose
maximum reduced mass flow is 0.00966 (kg/s)$K^0.5/kPa, cannot achieve the desired power
performance at high speeds. The reduced mass flow rate can be calculated, taking into
account the effect that exhausts composition and temperature. The accuracy of the
method is validated using data from a 2.3 L turbocharged H2ICE at various engine speeds
and throttle openings, and the error between the measured and calculated expansion ratio
is less than 5% mostly. At last, a well-matching turbine for high engine speeds of the 5.13 L
hydrogen engine to meet the desired power of 120 kW, whose maximum reduced mass
flow is extended to 0.0156 (kg/s)$K^0.5/kPa, is selected according to the method, and the
maximum power reaches 128.9 kW with a maximum torque of 662.6 N m, improving by
38.7% and 7.7% respectively comparing with the original turbine. However, the output
torque reduces by 15.6% at 1200 rpm. The reduced mass flow rate varies significantly in
comparison to the turbines that are well suited for low and high engine speeds

* Corresponding author. School of Mechanical Engineering, Beijing Institute of Technology, Beijing 100081, China.
E-mail addresses: xiaogang@yuchai.com (G. Xiao), 783572692@bit.edu.cn (L.-z. Bao).

Available online at www.sciencedirect.com

ScienceDirect

journal homepage: www.elsevier.com/locate/he

international journal of hydrogen energy 48 (2023) 38508 e38520

https://doi.org/10.1016/j.ijhydene.2023.06.104

0360-3199/© 2023 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.
respectively, thus the Variable Geometry Turbine may be the solution for both low and
high speeds simultaneously for hydrogen engines.

© 2023 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.

Introduction

Due to the lack of fossil fuels and the global greenhouse
impact, researchers are motivated to study and develop
alternative fuels such as hydrogen and ammonia. Hydrogen is
appealing as a prospective energy carrier. Hydrogen internal
combustion engines (H2ICEs) and hydrogen fuel cells (HFCs)
are known as the two main ways to utilize hydrogen energy,

while H2ICEs have a higher power density and high efficiency
at part load [1e3] compared with HFCs. Many benefits of using
hydrogen as a fuel in ICEs include reduced CO2 emissions,
rapid combustion velocity, low ignition energy, and high
thermal efficiency [1,4].

Nevertheless, owing to hydrogen's low volume energy
density and lean burn, which aims to produce almost nearzero
NOx emissions [5], H2ICEs have significantly less power
than gasoline engines. There are two main types of H2ICEs
mostly being investigated, port fuel injection (PFI) and direct
injection (DI). PFI H2ICEs are more easily and cheaply transformed
from gasoline engines than DI H2ICEs [6]. However,
the increase in power is limited by anomalous combustion
(preignition, backfire, and so on) [7,8]. According to the study
of Karagoz et al. [ € 9], the lower low heat value in volume than
that of gasoline, as well as backfire, restricts power output
increase. Although DI H2ICEs are more difficult to implement
due to the complexity of injector lubrication and cooling, as
well as the large cycle variation [10], DI can increase air flow
and DI has been found an effective way to boost power output
and lower NOx emissions [11]. However, there is still a power
performance disparity between H2ICEs and gasoline engines.
Supercharging and turbocharging are adopted by researchers
to increase the power intensity of H2ICEs, and the results
indicate that they are beneficial to improving power output
and thermal efficiency. Gu¨ rbu¨ z et al. [12] conducted supercharging
tests on a 0.476 L hydrogen engine with an external
supercharging air blower. The results demonstrated a 38%
increase in indicated power and a 16.5% rise in fuel consumption
respectively when the equivalence ratio is 0.6,
proving the potential to improve the performance of the
turbocharged H2ICE. Besides, the researchers [13] revealed
that intake-air temperature has obvious effects on the flame
development angle and volumetric efficiency. Ford reviewed
the development process of a 6.8 L supercharged V-10 H2ICE
[14], and power performance was comparable to or better than
that of target CNG or gasoline engines. Nakajima et al. [15]
demonstrated that turbocharging boosted brake thermal efficiency
by 2% at l (excess air ratio) about 2.5 for a PFI
1.3 L H2ICE. Lohse-Busch et al. [16] reported that a 170 N m
torque was available for a 2.3 L PFI H2ICE at 3000 rpm with a l
of 2 because supercharging improved volume efficiency.
Takagi et al. [17] found that supercharging increased IMEP of a
1 L one-cylinder DI H2ICE from 0.6 MPa to 0.85 MPa while
keeping l at 1.8. Furthermore, thermal efficiency was
improved to nearly 50%, which attributed to the reduced
proportion of the cooling loss due to the increased power
output. The poor improvement in power output at high engine
speeds caused by the energy consumption limits the implement
of superchargers, whereas turbochargers are more
common in automobiles because of the cheaper cost. The
results of Wallner et al. [18] and Obermair et al. [19] also
revealed turbocharging improved the indicated thermal

Nomenclature

H2ICE hydrogen internal combustion engine
HFC hydrogen fuel cell
PFI port fuel injection
DI direct injection

VGT variable geometry turbine
BTE brake thermal efficiency

BMEP break mean effective pressure

MBT minimum spark advance for best torque
m_ H hydrogen mass flow rate
m_ C air mass flow rate

m_ L air mass flow through the compressor
m_ reduced reduced mass flow rate of the turbine
m_ water cooling water mass flow rate

T1 assumed exhaust gas temperature

T2 theoretical turbine inlet temperature
Twaterin cooling water inlet temperature

Twaterout cooling water outlet temperature

TC air temperature after the intercooler
Pe desired power

h desired brake thermal efficiency
l excess air ratio

Hu hydrogen heat value

L0 stoichiometric air-fuel ratio
u mass fraction

hcooling the cooling to fuel power ratio
hTL turbocharger efficiency

Cp mix specific heat capacity at constant pressure of
the exhaust

Cp intake specific heat capacity at constant pressure of
the inlet air

Cv mix specific heat capacity at constant volume of
exhaust

Cp water specific heat capacity at constant pressure of
cooling water

pturbine discharge turbine discharge pressure
ppreturbine pre-turbine exhaust pressure

kT gas adiabatic index in the turbine
kL gas adiabatic index in the compressor

international journal of hydrogen energy 48 (2023) 38508 e38520 38509
efficiency of a 0.66 L DI H2ICE from 43% to 45.6% at 2000 rpm
with an IMEP of 0.8 MPa. Jilakara et al. [20] reported that the
power output of a 2.3 L turbocharged H2ICE reached 66.7 kW at
3600 rpm while a naturally aspirated CNG engine reached
52 kW. The research of Bao et al. [21] showed the power of a
matched turbocharged hydrogen engine increased by 123%,
and the torque increased by 195% comparing naturally aspirated
engine.

However, there are still some problems to be resolved in
turbocharging of H2ICE. First, the H2ICE turbo cannot sustain
the energy necessary to provide compressor required boosting
because of low exhaust temperature at low engine speeds [20].
Secondly, increased back pressure and pumping loss restrict
the enhancement of power output, particularly under high
engine speed condition [22]. According to the research of Lee
et al. [23], the back pressure of a turbocharged 2.4 L PFI H2ICE
reached 0.231 MPa while intake pressure was 0.132 MPa at
6000 rpm, and the torque of 84 N m was lower than that of

98 N m under naturally aspirated condition. Therefore,
choosing a well-matched turbocharger for H2ICE is significant
to boost the power output further. A more powerful
compressor with greater air mass flow rates and higherpressure
ratio is better suited for H2ICE [21], and Luo et al.

[24] suggested a method for selecting a compressor considering
the gas partial pressure of hydrogen in cylinders in
previous work. Meanwhile, there is still a necessity to select a
well-matched turbine. Bao et al. [21] stated that a small turbo
can provide sufficient power for turbocharging, however, the
reduction of turbine diameter causes a rise of exhaust pressure
especially at high speeds. Similar conclusions can be
summarized in other researches, but the turbocharging of

H2ICE is studied through exhaust pressure, and H2ICE turbine
have not been quantitatively analyzed with reduced mass
flow rates.

In this research, the turbocharger-matching of a 5.13 L
hydrogen engine is studied, and the results show the original
turbine cannot achieve the desired power performance at high
speeds. A method is proposed based on former researches in
order to select a turbine for a H2ICE taking the exhaust
component into consideration, and the reduced mass flow
rate can be calculated. Experimental data were used to validate
the accuracy of this method. Finally, a well-matching
turbine for high engine speeds of the large-displacement PFI
hydrogen engine to provide the desired power is selected according
to the method, and characteristics of the largedisplacement
PFI hydrogen engine turbocharger-matching
are concluded by comparing the data at low and high speeds.

Materials and methods

The engine test system and data acquisition system were
properly arranged and connected in order to obtain accurate
and precise experimental data. The 5.13 L 4-cylinder PFI
turbocharged hydrogen engine was transformed from a CNG
engine. The specifications of the large-displacement PFI
hydrogen engine are shown in Table 1 and the layout of the
experiment and data acquisition systems are shown in Fig. 1.

A CW250 eddy current dynamometer, an oil and water
temperature controller, air conditioning, and a ToCeiL20 N
hot-film air flow meter were all included in the test system.
The CW250 dynamometer has a maximum working capacity
of 250 kW and a maximum speed of 8000 rpm. The temperature
of the oil and cooling water in the engine were controlled

Table 1 e The specifications of the large-displacement PFI
engine.

Items Unit Values
Number of cylinders 4

Bore mm 110
Stroke mm 135

Displacement L 5.132
Number of valves 4

Compress ratio 12.5

EVO CA 47.7bBDC
EVC CA 9.4aTDC

IVO CA 2.4bTDC
IVC CA 15aBDC
Maximum power kW 176
Maximum torque N$m 900

Revolution of the engine rpm 600e2000

Fig. 1 e Layout of the 5.13 L PFI hydrogen engine experiment and data acquisition systems.

38510 international journal of hydrogen energy 48 (2023) 38508 e38520
by oil and water temperature controllers. The air mass flow
into the engine was measured with the ToCeiL20 N hot-film
air flow meter, and an Emerson CMF025 coriolis mass flow
meter was used to determine the hydrogen mass flow. The
Kibox combustion analyzer was used in the data acquisition
system, and the cylinder pressure and crankshaft angle signals
were recorded using a Kistler 6117B sensor and a Kistler
2613B sensor, respectively. The specifications of uncertainties
of the measured parameters are listed in Table 2. The engine
was warmed up before the testing to ensure that the oil and
cooling water reached 90 C and 80 C, respectively. The tests
were carried out while the engine was running at a constant
speed, with intervals of 500 rpm between 1500 and 4000 rpm.
The tests were carried out at the MBT (minimum spark
advance for best torque) in order to obtain comparable data,
and MBT tests were conducted by modifying the ignition
timing under different engine speed and load conditions. After
the hydrogen engine worked steadily at the current working
condition for 2 min, the average value of the test data of 200
cycles at this working condition was measured and recorded.
The uncertainty of tested results can be calculated according
to the principle of root-mean square method to obtain the
magnitude of the error given by Gaussian distribution [25], as
shown in Formula (1):

DR ¼

"vRvx1Dx12þvRvx2Dx22þ
…
vRvxnDxn2#1=2(1)where
DR is the uncertainty in the computed result; R is a
given function of the computed results; x1, x2, and xn are the
different measured parameters; Dx1, Dx2, Dxn are the corresponding
uncertainty of the different measured parameters.
The test engine was a 2.3 L four-cylinder PFI turbocharged
H2ICE, and its experiment data were used to confirm the
method's predicted results. The specifications of the experimental
hydrogen engine are shown in Table 3.

Results and discussion

Original turbocharger-matching of large-displacement PFI
hydrogen engine

The desired power performance is set at 600 N m @ 1200 rpm
with a maximum power of 120 kW at high speed. The experiments
are conducted with the original turbocharger which is
suited with the original CNG engine for preliminary performance
exploration. In order to achieve the desired torque, the
intake pressure increases to 0.312 MPa and the air flow reaches
448 kg/h. The results show the output torque can achieve
615 N m with a lambda of 2.12 and air flow rate of 448 kg/h at
1200 rpm. In addition, the expansion ratios surpass 3.0 when
H2ICE is operated at high load, and the maximum reaches
3.43. The power performance is acceptable at 1200 rpm.
However, the power is limited to 93 kW with a lambda of
1.77 at 1800 rpm, while the increasing hydrogen mass flow is
restricted by the knock phenomena and air mass flow has
reached its maximum at 498.6 kg/h. The reduced mass flow
rate of the turbine can be calculated and analyzed with the
efficiency map based on the pre-turbine exhaust pressure and
temperature with the hydrogen and air mass flow recorded.
Fig. 2 (a) shows the expansion ratios at 1200 rpm remain high,
and the reduced mass flow rate at 1800 rpm is higher than the
boundary data of the turbine efficiency map, which shows
poor matching and leads to restricted output power. A series
of experiments at speeds of 2000 rpm and 1600 rpm have been
carried out in an effort to increase the maximum power and
study the turbocharger matching at the current speed. The
results of Fig. 2 (a) and Fig. 2 (b) demonstrate that the reduced
mass flow rates at 2000 rpm are much higher than the
boundary data, but the BMEP at that speed is 10 bar which is
far below the desired power performance. On the other hand,
the output power at 1600 rpm is also tested as Fig. 2 (a) and
Fig. 2 (b) shown. The lower reduced mass flow rate is acceptable
for the original turbine when the hydrogen engine is
operated at medium and low loads, however, the reduced
mass flow rate is no longer within the turbine map when the
BMEP rises to 10.98 bar as the air flow grows. The findings of
these experiments show that the desired power performance
at high speed cannot be achieved with the original turbine,
requiring a well-matched turbine. Further research is aimed at
the selection of turbine at high speed.

Analysis of the method to select a well-matched turbine for
large-displacement PFI hydrogen engine

Commercial 1D codes are frequently used nowadays to match
gasoline engine turbochargers, while the simulations need
quantities of data especially cooling loss for H2ICE calibration.
Due to the smaller quenching distance and higher heat value
of hydrogen, some study on the heat transfer of hydrogen
engines indicates that the heat transfer model is distinct from
the uncalibrated Woschni model, which is typically chosen in
gasoline engine models [26]. Researchers found inaccurate
results when adopting unchanged models to hydrogen engines
[27], and that leads to inaccurate results of the preturbine
temperature. Thus, calibration for heat transfer of a

Table 2 e The uncertainties of the measured parameters.
Parameters Uncertainties Range

Speed ± 0.1% 0e10000 rpm
Torque ± 0.4% 0e1100 N m
Crank angel ± 0.02 CA

Pressure ± 0.8% 0e200 MPa
Air mass flow ± 1% Full Scale 0e450 kg/h
Hydrogen mass flow ± 0.1% Full Scale 0e6.5 kg/h

Table 3 e The specifications of test engine.

Items Unit Values
NO. of cylinders 4

Bore mm 90
Stroke mm 90

Displacement L 2.299
NO. of valves 4

Compress ratio 9.3

EVO CA 53.64bBDC

EVC CA 44.36aTDC
IVO CA 23.3bTDC
IVC CA 58aBDC

international journal of hydrogen energy 48 (2023) 38508 e38520 38511
hydrogen engine based on the abundant energy distribution
experiments results is necessary to ensure the accuracy of the
1D simulation and the turbocharger matching. On the other
hand, a generally well-matching turbine can only be chosen
after multiple computations of various turbochargers, as the
1D simulation is carried out depending on the map data input
of the turbocharger. The experiment results have been carried
out with the original turbocharger can serve as the basis for
selecting a well-matched turbine. The results above show that
the hydrogen engine's performance is significantly impacted
by the reduced mass flow rate. Thus, calculated reduced mass
flow rates at certain conditions can be a valuable reference for
selecting a turbine.

A calculation method for turbine selection is proposed
based on the calculation of Zinner et al. [28], and the reduced
mass flow rate can be achieved according to the calculated
turbine inlet temperature and the turbine expansion ratio.
The following are the steps of this calculation method, and
Fig. 3 shows the process of the calculation method.

1) The excess air ratio (l) is specified, and the flow rates of

hydrogen and air are calculated according to the designed
power and the brake thermal efficiency (BTE) of H2ICE.

2) The mass fraction u of each exhaust component is calculated
according to the chemical equation for the reaction
between hydrogen and air.

3) The specific heat capacity at a constant pressure of the

exhaust gas mixture (Cp_mix) is calculated by assuming the
exhaust gas temperature T1 and querying the Cp corresponding
to each exhaust gas component.

4) The theoretical value of the turbine inlet temperature T2 is

calculated according to the desired brake effective thermal
efficiency h expected at the design point of the H2ICE and
the cooling to fuel power ratio hcooling, an empirical
parameter, under the corresponding operating conditions.
The pre-turbine exhaust temperature can be determined
when T2 is equal to T1. The expansion ratio of the turbine
can be calculated according to the turbocharger efficiency,
the pre-turbine exhaust temperature, and the pressure
ratio of the compressor.

5) The pre-turbine exhaust pressure may be estimated using

the expansion ratio with the turbine discharge pressure,
which is related to the hydrogen engine's speed. The
calculated reduced mass flow rate is obtained according to
the parameters above.

Fig. 2 e (a) The 5.13 L hydrogen engine matching points in the original turbine efficiency map and (b) BMEP variation at
different conditions.

Fig. 3 e The process of the calculation method.

38512 international journal of hydrogen energy 48 (2023) 38508 e38520
According to the desired power and BTE of H2ICE, as well as
the specified excess air ratio, the air mass flow and hydrogen
mass flow can be determined by Formula (2) (3)

m_ H ¼ Pe  1000
Huh (2)

m_ C ¼ lL0m_ H (3)
where m_ H is the hydrogen flow rate, kg/s; Pe is the desired
power, kW; h is the brake thermal efficiency; Hu is the hydrogen
heat value, kJ/kg; m_ C is the air flow rate, kg/s; L0 is the theoretical
amount of air required for complete combustion per
kilogram of hydrogen; l is the specified excess air ratio;

Next, the mass fraction u of the exhaust composition after
the reaction can be calculated by Formula (4) (5) (6).

uH2O ¼ 2  18
2  18 þ ðl  1Þ  32 þ 3:71$l  28 (4)

uO2 ¼ ðl  1Þ  32
2  18 þ ðl  1Þ  32 þ 3:71$l  28 (5)

uN2 ¼ 3:71  l  28
2  18 þ ðl  1Þ  32 þ 3:71$l  28 (6)

where uH2O is the mass fraction water vapour; uO2 is the mass
fraction oxygen; uN2 is the mass fraction nitrogen;

According to the research [29], the specific heat capacity in
turbine affects the calculation of turbine. Thus, the specific
heat capacity at constant pressure of the exhaust gas mixture
(Cp_mix) is re-calculated by Formula (7). The exhaust gas
temperature T1 can be assumed, and the specific heat capacity
at constant pressure Cp for each exhaust gas component can
be searched (Temperature is the most important component
impacting Cp, and the pressure has a less impact on Cp. Hence
0.25 MPa is chosen as the appropriate pressure.).

Cp mix ¼ uH2OCp H2O þ uO2Cp O2 þ uN2Cp N2 (7)
where: Cp mix is the specific heat capacity for the exhaust gas
mixture, kJ/kg$K; Cp H2O is the specific heat capacity for water
vapour, kJ/kg$K; Cp O2 is the specific heat capacity for oxygen,
kJ/kg$K; Cp N2 is the specific heat capacity for nitrogen, kJ/kg$K.
The fourth part is the calculation to determine the preturbine
temperature and expansion ratio. The theoretical
value of the turbine inlet temperature T2 is calculated by
Formula (8), based on the desired effective thermal efficiency h
at the design point of the H2ICE, and the cooling to fuel power
ratio hcooling under the operating conditions, which is an
empirical parameter and needs to be set reasonably. At the
early development of the hydrogen engine, the certain value
of hcooling is based on the cooling data of the hydrogen engine
with similar displacement or, if available, preliminary experiments
under certain conditions.

T2 ¼



1  h  hcooling
Hu þ lL0Cp intakeTC
ð1 þ lL0ÞCp mix

(8)

where: hcooling is the cooling to fuel power ratio; Cp intake is the
specific heat capacity at constant pressure of the inlet air, kJ/
kg$K; and TC is the temperature of the air after the intercooler, K.

The temperature T1 is determined as the pre-turbine
exhaust temperature when the difference between the
assumed values T1 and calculated values T2 is within the
permissible error range. This method improves the accuracy
of the calculation of the pre-turbine exhaust temperature and
the turbine expansion ratio. Formula (9) can be obtained from
the research of Zinner et al. [28], and the pre-turbine exhaust
pressure can be obtained from Formula (10). At last, the turbine
reduced mass flow rate at certain condition can be
calculated by in Formula (11).

pT ¼ 1
n
1 þ ½1  ðpCÞ
kL1 kL
i
$m_ L
m_ T
$

Cp intake
Cp mix

$TC
T1
$ 1
hTLo kT kT1

(9)

ppreturbine ¼ pturbine discharge$pT (10)

m_ reduced ¼ ðm_ H þ m_ CÞ$ ffiffiffiffiffi
T1
p
ppreturbine

(11)

where: m_ L is the air flow through the compressor, kg/s; kL is
the gas adiabatic index in the compressor; m_ T is the gas flow
through the turbine, kg/s; kT is the gas adiabatic index in the
turbine, which is also can be determined by the calculated
Cp mix and Cv mix; pT is expansion ratio of the turbine; pC is
pressure ratio of the compressor; hTL is the efficiency of the
turbocharger; ppreturbine is the pre-turbine exhaust pressure,
MPa; pturbine discharge is the turbine discharge pressure, MPa;
m_ reduced is the reduced mass flow rate of the turbine, (kg/s)$
K^0.5/kPa;

Validation of the method with the experimental data

To verify the accuracy of this method for selecting a turbine
for the H2ICE, experimental data from a 2.3 L four-cylinder
turbocharged H2ICE at 2000 rpm, 2500 rpm, 3000 rpm, and
4000 rpm are utilized to compare with the calculated values.
The turbine inlet temperature, turbine inlet pressure and
turbine outlet pressure in the experimental data are measured
by the corresponding sensors. Formula (12), which incorporates
cooling water inlet and outlet temperatures, flow
rates, can be used to calculate the cooling to fuel power ratio
hcooling, and it can only be used to compute the cooling when
the required sensors are installed in order to validate the
measured and estimated turbine inlet temperature.

hcooling ¼ m_ water$ðTwaterout  Twaterin
$Cp water
m_ H$Hu

(12)

where: m_ water is the flow rate of cooling water, kg/s; Twaterout is
outlet temperature of cooling water, K; Twaterin is inlet temperature
of cooling water, K; Cp water is the specific heat capacity
at constant pressure of cooling water, kJ/kg$K.

As the hydrogen flow rate is much lower than the air flow
rate and the temperature of the injected hydrogen is about
300 K, the energy caused by the initial state of the hydrogen is
negligible and the effect of the hydrogen calorific value is
mainly considered. The results of turbine inlet temperature of
the H2ICE can be calculated by Formula (8) and (12). The
calculated and tested data of turbine inlet temperatures,

international journal of hydrogen energy 48 (2023) 38508 e38520 38513
when the equivalence ratio is 0.55 and the ignition timing is
set at MBT, are shown in Table 4.

The Error can be calculated by the formula followed:

Error ¼ Calculated Data  Measured Data
Measured Data (13)

According to Fig. 4 (a), the calculated values for the turbine
inlet temperature have an error margin of less than 5%
generally, which can be serve as the criterion in this method
[24]. At 3000 rpm, however, the maximum error 7.83% occurs.
This is most likely a result of measurement error, which led to
a greater hcooling being calculated. When the throttle opening
grows, the hcooling reduces, as shown by the findings in Fig. 4 (b).
Because the varied throttle openings at each operational
condition, as at 2000 rpm, are not significant, the hcooling should
not fluctuate significantly. However, the hcooling fluctuates
significantly for a few conditions where the error of predicted

temperature is substantial, thus it is critical to set the hcooling

accurately for each condition. Fig. 5 illustrates the comparison
between the calculated expansion ratio and the measured
expansion ratio at different speeds and throttle openings. The
results reveal that as the throttle opening increases, the
increasing airflow causes the expansion ratio to rise as well.
As a result, as the compressor's pressure ratio rises, a greater
expansion ratio may be achieved. However, the error in the
expansion ratio calculation is substantially lower than that in
the temperature calculation when comparing the results of
Figs. 4 and 5. The hydrogen engine is operated at low load and
has a low compressor pressure ratio, resulting in a reduction
in the expansion ratio error transmitted by the temperature
error.

Additionally, the experiments data of the 5.13 L H2ICE are
also utilized to confirm the applicability of different displacements.
According to Fig. 6 (a), the error between

Table 4 e The calculated and measured data of turbine inlet temperatures (Kelvin).
Throttle 4000 rpm 3000 rpm

Calculated Measured |Error|/% Calculated Measured |Error|/%
40% 943.1 931.15 1.28

38% 934.8 936.55 0.19 889.1 882.2 0.79
36% 957.7 945.15 1.33 880.0 884.2 0.47
34% 948.8 941.75 0.75 854.4 875.8 2.44
32% 964.6 941.75 2.43 865.2 880.6 1.74
30% 970.8 939.15 3.38 861.3 878.6 1.96
28% 965.3 941.55 2.52 842.6 877.2 3.94
26% 965.2 935.35 3.19 846.3 878.8 3.69
24% 888.1 923.35 3.81 806.3 874.8 7.83
2500 rpm 2000 rpm

Throttle Calculated Measured |Error|/% Calculated Measured |Error|/%
36% 884.9 881.2 0.42 827.9 826.2 0.21
34% 861.2 890.2 3.26 819.6 827.0 0.88
32% 868.4 887.2 2.11 811.3 823.2 1.44
30% 855.5 884.4 3.26 806.9 821.6 1.78
28% 868.3 886.0 1.99 805.6 825.2 2.37
26% 838.8 884.4 5.15 802.0 817.2 1.85
24% 843.5 878.2 3.94 799.0 818.0 2.32

(a) Variation in error of turbine inlet

temperature at different engine speeds

(b) Variation in at different engine
speeds

Limited range
of error

8.28%

3.38%

2.17%

average 0.5%
per condition

Fig. 4 e Variation in hcooling and the error of turbine inlet temperature at different engine speeds.

38514 international journal of hydrogen energy 48 (2023) 38508 e38520
measured and calculated expansion ratio is generally within
5%, and overly wide waste gate opening can cause the inaccuracy.
The difference between the calculated and measured
reduced mass flow rate is shown in Fig. 6 (b), and the error is
acceptable.

Optimized turbocharger-matching of large-displacement PFI
hydrogen engine

In order to achieve the desired power at 1800 rpm, the results
of the method described above serve as a guide in the turbine

(a) 4000rpm (b) 3000rpm

(c) 2500rpm (d) 2000rpm
Fig. 5 e Comparison between the measured and calculated expansion ratio at different engine speeds.

(a) Expansion ratio (b) Reduced mass flow rate
Fig. 6 e Comparison between the measured and calculated (a) expansion ratio and (b) reduced mass flow rate at 1200 rpm.

international journal of hydrogen energy 48 (2023) 38508 e38520 38515
selection process. According to experiments already conducted
on the hydrogen engine with the original turbine and
required sensors for the temperatures, the value of hcooling can
be determined. Fig. 7 shows that the hcooling at 1200 rpm with
high load is 0.21 on average, and a greater engine speed causes
a reduction in the hcooling. Thus, the hcooling at 1200 rpm with
1.5 MPa of BMEP is set at 0.20 preliminarily, which needs to be
verified according to the results at certain condition. The other
parameters are set respectively according to results from
previous experiments on the 5.13 L hydrogen engine: the
desired power ¼ 120 kW; the lambda ¼ 1.8; compressor pressure
ratio ¼ 2.7; brake thermal efficiency ¼ 0.38; air temperature
after cooler ¼ 35 C, turbocharger efficiency ¼ 0.48;
turbine discharge pressure ¼ 0.12 MPa due to the high backpressure
at high speed.

The turbine inlet temperature and expansion ratio can be
calculated as 874.7 K and 2.953 respectively, using the method
in Fig. 3 and the formulas above. Furthermore, the reduced
mass flow rate are calculated as 0.01417 (kg/s)$K^0.5/kPa. The
reduced mass flow rate used as a selection criterion for turbine
selection. Finally, an optimized turbine whose maximum

reduced mass flow rate is extended to 0.0156 (kg/s)$K^0.5/kPa
is selected. The optimized turbocharger is installed on the
hydrogen engine and a series of experiments are conducted at
1800 rpm. As the results shown in Fig. 8 (a) and (b), the output
power reached 121 kW with a lambda of 1.73 when experiments
were conducted with the selected turbine, indicating

the performance has been improved further, and the reduced
mass flow rate is 0.01394 (kg/s)$K^0.5/kPa. The difference between
the calculated and experiment results comes from the

waste gate leading to a lower pre-turbine exhaust pressure.
The experiment air mass flow is only 548 kg/h much lower
than the calculated air mass flow of 601 kg/h due to a lower
lambda and lower volumetric efficiency. In addition, Fig. 7 illustrates
that the hcooling at 1800 rpm is around 0.2 when BMEP
is about 1.5 MPa, which is close to the preset value in previous
calculation. In order to explore the maximum power of the
hydrogen engine, the experiments at 2000 rpm are carried out.
The matching points show the expansion ratio and the and

reduced mass flow rate increase further at high load, and the

power reaches 128.9 kW at 2000 rpm @ 1.71 of the lambda
which shows a well-matching. However, further output power
is restricted by knock of the hydrogen engine. As shown in
Fig. 8(c), the maximum pressure reaches 17.6 MPa 3 cycles
after a typical cycle with a maximum pressure of 10.9 MPa due
to a sequence of knock occurrences. Additionally, as the cycles
go, the rate of heat release increases significantly and the
start of combustion is advanced according to Fig. 8(d). The
knock must be avoided since it increases friction and cooling
loss and can possibly damage H2ICE components.

The following tests results in Fig. 8 (a) and (e) demonstrate
the turbocharger matching at other speeds. The hydrogen
engine can achieve better power performance at 1400 rpm and
1600 rpm. As compared to the original turbine, the maximum
BMEP of 1400 rpm and 1600 rpm are significantly improved,
reaching 1.624 MPa and 1.591 MPa respectively. The maximum
torque is increased to 662.6 N m at 1400 rpm, and the power is
improved to 109 kW at 1600 rpm. On the contrary, the huge
mass flow turbine results in lower rotor speed and intake
pressure at 1200 rpm where a great torque requirement exists.
The expansion ratio remains 1.75, and the torque reaches

517 N m at 1200 rpm @ 1.87 of the lambda, which is a respectable
performance but still falls short of the desired torque. The
results at 1000 rpm also show a poor matching where the
maximum BMEP is only 0.92 MPa. In contrast, the maximum
power and torque are improved by 38.7% and 7.7% respectively,
however, the maximum torque with the optimized turbine is
achieved at 1400 rpm. The torque at 1200 rpm decreases by

15.6%. The performance limitations with the optimized turbine
and the original turbine are listed in Table 5.

Furthermore, the exhaust pressures with the original and
optimized turbine respectively are contrasted at 1200 rpm and
2000 rpm. The exhaust pressures of the optimized turbine are
typically lower than those of the original turbine. As Fig. 9 (a)
shows, the exhaust pressure of the original turbine at

1200 rpm grows from 0.197 MPa to 0.262 MPa with the rising
BMEP, while that of the optimized turbine increases from
0.138 MPa to 0.196 MPa, which is generally lower. The reason is

that the intake pressure of the optimized turbine is low, and
more hydrogen is needed to maintain the same BMEP, which
indicates a poor charging capacity at low speeds. According to
Fig. 9 (b), at 2000 rpm, the exhaust pressure of the original
turbine increases from 0.280 MPae0.320 MPa, and that of the
optimized turbine rises from 0.208 MPa to 0.303 MPa. As the
BMEP grows, the exhaust pressure difference narrows because
the lambda of the original turbine falls obviously to increase
the BMEP, which reduces air flow. In contrast, the exhaust
pressure of the optimized turbine grows continuously.
Excessive exhaust pressure leads to higher pumping loss
especially at high speeds. The intake pressure of the optimized
turbine reaches the maximum of 0.250 MPa with a
BMEP of 1 MPa @ a lambda of 2.15, while that of the original
turbine is only 0.22 MPa with a low lambda of 1.69. In contrast,
the higher intake pressure brings more air flow and improves
the power performance with a higher lambda. Therefore, for
the exhaust pressure and the intake pressure at high speed,
the optimized turbine is the superior option. According to the
analysis, well-matched turbines should have a balanced
exhaust pressure and intake pressure at various speeds.

Fig. 7 e The variation of hcooling with BMEP @ 1200 rpm and
1800 rpm.

38516 international journal of hydrogen energy 48 (2023) 38508 e38520
Fig. 8 e (a) The 5.13 L hydrogen engine matching points at different speeds in the optimized turbine efficiency map.

Table 5 e The performance limitations with the optimized turbine and the original turbine.
Performance limitations Optimized turbine Original turbine
Most efficient operating range of the engine 1200 rpme1400 rpm @ 1.1 MPae1.5 MPa of BMEP 1200 rpm@ 1.1 MPae1.3 MPa of BMEP
The continuous operating range of the engine 800 rpme2000 rpm 800 rpme2000 rpm
The maximum power or torque 128.9 kW @ 2000 rpm
662.6 N m @ 1400 rpm
93.0 kW @ 1800 rpm
615.0 N m @ 1200 rpm

The lowest fuel consumption range 71.73 g/kWh @ 1400 rpm/1.32 MPa of BMEP 74.21 g/kWh @ 1200 rpm/1.13 MPa of BMEP
The optimum turbocharger efficiency 47.9% @ 1400 rpm/1.32 MPa of BMEP 43.7% @ 1400 rpm/1.13 MPa of BMEP

international journal of hydrogen energy 48 (2023) 38508 e38520 38517
The maximum reduced mass flow rate increases by 61.5%
compared the optimized turbine with the original turbine,
and the well-matched reduced mass flow rate increases from
0.00904 (kg/s)$K^0.5/kPa at 1200 rpm to 0.01425 (kg/s)$K^0.5/
kPa at 2000 rpm, which is a great range for typical waste gate
turbocharger. Thus, for a hydrogen engine to reach high

power performance at both low and high engine speeds,
especially the hydrogen engines whose speed vary significantly,
a turbocharger with a wider range of the reduced
mass flow rate, like VGT (Variable geometry turbine) is very
necessary. The wider flow rate range of VGT provides more
potential with H2ICE to adjust the exhaust pressure and
intake pressure. The performance of turbocharged H2ICE
with VGT and the adjustment will be studied in future
researches.

Conclusion

This study presents the process of the optimization of a largedisplacement
PFI hydrogen engine turbocharger matching for
better performance, and a calculation method of turbine selection
for turbocharged H2ICEs is utilized. The turbine inlet
temperature and expansion ratio are calculated by considering
the exhaust components, and the reduced mass flow
rate can serve as the reference for turbine selection. Finally,
the performance of the large-displacement PFI hydrogen engine
is improved significantly. The following conclusions are
reached.

1. The desired torque of 615 N m can be achieved at 1200 rpm
with the original turbine. However, the original turbine
performs poorly at high speeds due to the low reduced
mass flow rate of the turbine, whose maximum is 0.0966
(kg/s)$K^0.5/kPa. A modified turbocharger is necessary
because of the high air-fuel ratio and the lean burn of
hydrogen.

2. The reduced mass flow rate of turbine can be calculated to

select a well-matched turbine for H2ICE. Due to different
exhaust components and temperatures, the Cp of the

exhaust gas from H2ICEs is very different from that of
typical gasoline engines. The experiment data of the 2.3 L
and 5.13 L turbocharged H2ICE is used to validate the
calculation method at various engine speeds and throttle
openings, and the method is applicable for 5.13 L H2ICE
according to the validation. The error of calculated and
measured data can be less than 5% mostly.

3. The optimized turbocharger is selected according to the

calculated reduced mass flow rate for the 5.13 L PFI
hydrogen engine. The power performance at 1800 rpm is
improved from to 93 kWe121 kW. The maximum power is
extended to 128.9 kW at 2000 rpm, which is increased by
38.7%. In addition, the maximum torque is increased to
662.6 N m with at 1400 rpm, which is increased by 7.7%
compared with the maximum torque with original turbine.
However, the power performance is reduced by 15.6% at
1200 rpm, and the torque at 1200 rpm decreases to 518 N m.
According to analysis, the well-matched turbine should be
balanced the exhaust pressure and intake pressure at
different speeds.

4. The maximum reduced mass flow rate of the optimized
turbine increases by 61.5% comparing with the original
turbine, and the variations of the reduced mass flow rates
between low and high engine speeds vary significantly
from 0.00904 (kg/s)$K^0.5/kPa at 1200 rpm to 0.01425 (kg/s)$

K^0.5/kPa at 2000 rpm. Thus the VGT (Variable geometry
turbine), which provides a wide flow rate range, may be a

better option for hydrogen engines to accommodate
different engine speeds. The VGT is a key factor for H2ICEs
to achieve high power at different speeds. The characteristics
of turbocharged H2ICE with VGT and the adjustment
will be studied in future research.

Declaration of competing interest

The authors declare that they have no known competing
financial interests or personal relationships that could have
appeared to influence the work reported in this paper.

(a) 1200rpm (b) 2000rpm

Fig. 9 e The exhaust pressures and intake pressures of the original turbine and the optimized turbine at (a) 1200 rpm and (b)
2000 rpm.

38518 international journal of hydrogen energy 48 (2023) 38508 e38520
Acknowledgement

This study was supported by the National Natural Science
Foundation of China (Grant No.:52206228) and Beijing Institute
of Technology Research Fund Program for Young Scholars (2
2050205-XSQD- 202103007). This work is supported by the
China Zhongguancun Science park Management Committee
(202120339223).

references

[1] Verhelst S. Recent progress in the use of hydrogen as a fuel
for internal combustion engines. Int J Hydrogen Energy
2014;39:1071e85. https://doi.org/10.1016/
j.ijhydene.2013.10.102.

[2] Iwasaki H, Shirakura H, Ito A. A study on suppressing
abnormal combustion and improving the output of hydrogen
fueled internal combustion engines for commercial vehicles.
2011. https://doi.org/10.4271/2011-01-0674. 2011-01e0674.
[3] Keller J, Lutz A. Hydrogen fueled engines in hybrid vehicles.
2001. https://doi.org/10.4271/2001-01-0546. 2001-01e0546.
[4] Verhelst S, Wallner T. Hydrogen-fueled internal combustion
engines. Prog Energy Combust Sci 2009;35:490e527. https://
doi.org/10.1016/j.pecs.2009.08.001.

[5] Bao L, Sun B, Luo Q. Optimal control strategy of the
turbocharged direct-injection hydrogen engine to achieve
near-zero emissions with large power and high brake
thermal efficiency. Fuel 2022;325:124913. https://doi.org/
10.1016/j.fuel.2022.124913.

[6] Dennis PA, Dingli RJ, Abbasi Atibeh P, Watson HC, Brear MJ,
Voice G. Performance of a port fuel injected, spark ignition
engine optimised for hydrogen fuel. 2012. https://doi.org/
10.4271/2012-01-0654. 2012-01e0654.

[7] Wang L, Yang Z, Huang Y, Liu D, Duan J, Guo S, et al. The
effect of hydrogen injection parameters on the quality of
hydrogeneair mixture formation for a PFI hydrogen internal
combustion engine. Int J Hydrogen Energy 2017;42:23832e45.
https://doi.org/10.1016/j.ijhydene.2017.04.086.
[8] Reichel TG, Paschereit CO. Interaction mechanisms of fuel
momentum with flashback limits in lean-premixed
combustion of hydrogen. Int J Hydrogen Energy
2017;42:4518e29. https://doi.org/10.1016/
j.ijhydene.2016.11.018.

[9] Karagoz Y, Balcı € O, K € oten H. Investigation of hydrogen usage €
on combustion characteristics and emissions of a spark
ignition engine. Int J Hydrogen Energy 2019;44:14243e56.
https://doi.org/10.1016/j.ijhydene.2019.01.147.
[10] Luo Q, Sun B. Effect of the Miller cycle on the performance of
turbocharged hydrogen internal combustion engines. Energy
Convers Manag 2016;123:209e17. https://doi.org/10.1016/
j.enconman.2016.06.039.

[11] Lee J, Lee K, Lee J, Anh B. High power performance with zero
NOx emission in a hydrogen-fueled spark ignition engine by
valve timing and lean boosting. Fuel 2014;128:381e9. https://
doi.org/10.1016/j.fuel.2014.03.010.
[12] Gu¨ rbu¨ z H, Akc¸ay _
IH. Evaluating the effects of boosting

intake-air pressure on the performance and environmentaleconomic
indicators in a hydrogen-fueled SI engine. Int J
Hydrogen Energy 2021;46:28801e10. https://doi.org/10.1016/
j.ijhydene.2021.06.099.

[13] Gu¨ rbu¨ z H. Optimization of combustion and performance
parameters by intake-charge conditions in a small-scale aircooled
hydrogen fuelled SI engine suitable for use in pistonprop
aircraft. AEAT 2021;93:448e56. https://doi.org/10.1108/
AEAT-09-2020-0193.

[14] Natkin RJ, Denlinger AR, Younkins MA, Weimer AZ,

Hashemi S, Vaught AT. Ford 6.8L hydrogen IC engine for the
E-450 shuttle van. 2007. https://doi.org/10.4271/2007-01-4096.
2007-01e4096.

[15] Nakajima Y, Yamane K, Shudo T, Hiruma M, Takagi Y.
Research and development of a hydrogen-fueled engine for
hybrid electric vehicles. 2000. https://doi.org/10.4271/2000-
01-0993. 2000-2001e0993.

[16] Lohse-Busch H, Wallner T, Shidore N. Efficiency-optimized
operating strategy of a supercharged hydrogen-powered
four-cylinder engine for hybrid environments. 2007. https://
doi.org/10.4271/2007-01-2046. 2007-01e2046.
[17] Takagi Y, Oikawa M, Sato R, Kojiya Y, Mihara Y. Near-zero
emissions with high thermal efficiency realized by
optimizing jet plume location relative to combustion
chamber wall, jet geometry and injection timing in a directinjection
hydrogen engine. Int J Hydrogen Energy
2019;44:9456e65. https://doi.org/10.1016/
j.ijhydene.2019.02.058.

[18] Wallner T, Matthias NS, Scarcelli R. Influence of injection
strategy in a high-efficiency hydrogen direct injection
engine. SAE Int J Fuels Lubr 2011;5:289e300. https://doi.org/
10.4271/2011-01-2001.

[19] Obermair H, Scarcelli R, Wallner T. Efficiency improved
combustion system for hydrogen direct injection operation.
2010. https://doi.org/10.4271/2010-01-2170. 2010-01e2170.
[20] Jilakara S, Vaithianathan JV, Natarajan S, Ramakrishnan VR,
Subash G, Abraham M, et al. An experimental study of
turbocharged hydrogen fuelled internal combustion engine.
SAE Int J Engines 2015;8:314e25. https://doi.org/10.4271/2015-
26-0051.

[21] Bao L, Sun B, Luo Q, Li J, Qian D, Ma H, et al. Development of a
turbocharged direct-injection hydrogen engine to achieve
clean, efficient, and high-power performance. Fuel
2022;324:124713. https://doi.org/10.1016/j.fuel.2022.124713.
[22] Nguyen D, Choi Y, Park C, Kim Y, Lee J. Effect of supercharger
system on power enhancement of hydrogen-fueled sparkignition
engine under low-load condition. Int J Hydrogen
Energy 2021;46:6928e36. https://doi.org/10.1016/
j.ijhydene.2020.11.144.

[23] Lee J, Park C, Kim Y, Choi Y, Bae J, Lim B. Effect of
turbocharger on performance and thermal efficiency of
hydrogen-fueled spark ignition engine. Int J Hydrogen Energy
2019;44:4350e60. https://doi.org/10.1016/
j.ijhydene.2018.12.113.

[24] Luo Q, Sun B, Wang X. A general selection method for the
compressor of the hydrogen internal combustion engine
with turbocharger. 2017. https://doi.org/10.4271/2017-01-
1025. 2017-01e1025.

[25] Gu¨ rbu¨ z H. An investigation on effect of in-cylinder swirl flow
on performance, combustion and cyclic variations in
hydrogen fuelled spark ignition engine. J Energy Inst 2014:10.
[26] Michl J, Neumann J, Rottengruber H, Wensing M. Derivation
and validation of a heat transfer model in a hydrogen
combustion engine. Appl Therm Eng 2016;98:502e12. https://
doi.org/10.1016/j.applthermaleng.2015.12.062.
[27] Demuynck J, De Paepe M, Huisseune H, Sierens R,

Vancoillie J, Verhelst S. On the applicability of empirical heat
transfer models for hydrogen combustion engines. Int J
Hydrogen Energy 2011;36:975e84. https://doi.org/10.1016/
j.ijhydene.2010.10.059.

[28] Pucher H, Zinner K. Zusammenwirken von Lader und Motor.
Aufladung von Verbrennungsmotoren: grundlagen,

international journal of hydrogen energy 48 (2023) 38508 e38520 38519
Berechnungen, Ausfu¨hrungen. Berlin, Heidelberg: Springer
Berlin Heidelberg; 2012. p. 67e111. https://doi.org/10.1007/
978-3-642-28990-3_7.
[29] Payri F, Serrano JR, Fajardo P, Reyes-Belmonte MA, GozalboBelles
R. A physically based methodology to extrapolate

performance maps of radial turbines. Energy Convers Manag
2012;55:149e63. https://doi.org/10.1016/
j.enconman.2011.11.003.

38520 international journal of hydrogen energy 48 (2023) 38508 e38520