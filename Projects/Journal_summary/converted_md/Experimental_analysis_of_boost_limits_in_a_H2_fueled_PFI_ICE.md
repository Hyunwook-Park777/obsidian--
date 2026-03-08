# Experimental analysis of boost limits in a H2 fueled PFI ICE

Journal of Physics:

Conference Series

PAPER • OPEN ACCESS

Experimental analysis of boost limits in a hydrogen
fueled PFI internal combustion engine

To cite this article: S Frigo et al 2023 J. Phys.: Conf. Ser. 2648 012073

View the article online for updates and enhancements.

You may also like
Cognitive reflection test and the polarizing
force-identification questions in the FCI
Allan L Alinea
-

A HIGH-RESOLUTION VACUUM
ULTRAVIOLET LASER
PHOTOIONIZATION AND
PHOTOELECTRON STUDY OF THE CO
ATOM
Huang Huang, Hailing Wang, Zhihong Luo
et al.

-

Mixing the Solar Wind Proton and Electron
Scales. Theory and 2D-PIC Simulations of
Firehose Instability
R. A. López, A. Micera, M. Lazar et al.
-

This content was downloaded from IP address 119.203.250.11 on 01/03/2026 at 06:51
Content from this work may be used under the terms of theCreative Commons Attribution 3.0 licence. Any further distribution
of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
Published under licence by IOP Publishing Ltd

ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

1

Experimental analysis of boost limits in a hydrogen fueled PFI

internal combustion engine

S Frigo1
, D Bonini1

, S De Regibus2
, L Sguaitamatti2
1 Department of Energy, System, Territory and Construction Engineering (DESTEC) –
University of Pisa – Italy

2 Ecomotive Solutions – Serralunga di Crea (AL) - Italy

stefano.frigo@unipi.it

Abstract. In recent years we have witnessed a renewed interest in the use of hydrogen as a fuel
for the land transportation sector, not only for the decarbonisation of the propulsion system but
also, above all, as an energy vector for accumulating excess energy deriving from the use of
intermittent renewable sources such as wind and photovoltaics.

The present study shows the results of an ongoing research aimed at fine-tuning ready-to-market
strategies for the use of hydrogen in ICEs. Starting from a turbocharged engine fueled by natural
gas and utilized on light commercial vehicles, a low-cost indirect hydrogen injection system
(PFI) was implemented, combined with appropriate injection strategies and boost pressure
analysis, this last assuming a fundamental aspect in recovering engine performance that
inevitably deteriorates with the use of diluted mixtures.

It is found that the adoption of an air/hydrogen lambda value (λ) ≈ 2.5 allows the utilization of
high boost ratios without knocking and backfire and with the possibility of reaching performance
similar to the original natural gas fueled engine, with a higher efficiency (> 39 %) and with low
NOx emissions (< 200 ppm).

1. Introduction

In recent years we have witnessed a renewed interest in the use of hydrogen as a fuel, as testified by the
numerous articles available in the scientific literature and well described in recent review papers [1-8],
not only for the decarbonisation of the energy system but also, above all, as an energy vector for
accumulating excess energy deriving from the use of intermittent renewable sources such as wind and
photovoltaics.

Considering the transportation sector, the utilisation of hydrogen as fuel for light vehicles (cars)
appears improbable since these last are projected towards electrification (batteries), especially in Europe
where, starting from 2035, only cars with electric propulsion are forecasted to be sold. On the contrary,
for commercial vehicles (trucks) the horizon is not yet so defined, and for their decarbonisation several
solutions are being evaluated, such as the use of biofuels or hydrogen. In particular, the use of hydrogen
to fuel light commercial vehicles, mainly utilized for the distribution of goods in urban or immediately
extra-urban areas, appears particularly interesting not only because it can concretely contribute to
decrease the pollution in the urban centers, but also because such vehicles are characterized by a
moderate daily mileage (usually < 200 km) and therefore requiring a moderate volume on board to
accommodate the hydrogen tank which is, as known, the main problem connected to the use of hydrogen
as fuel for vehicles [9].
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

2

For land transportation, hydrogen can be used both in ICEs and in fuel cells, even if the diffusion of
this last technology still appears far away for large-scale applications, mainly due to the high costs
associated [10, 11]. The use of hydrogen in spark ignited engines, on the other hand, appears more
promising and in addition to the well-known advantages related to the absence of CO2 emissions in the
exhaust, there is the possibility of operating the load control by dosing fuel only thanks to hydrogen
reactivity and wide flammability range, leading to a drastic reduction of pumping losses therefore
increasing the efficiency.

But it is also known there are not only advantages. It is not the purpose of this work to investigate
again into the various problems and to give a detailed description of the various solutions, which, as
previously mentioned, is widely carried out in the recent scientific literature. It is however appropriate
to recall the main ones, such as the loss of power (compared to the use of liquid fuels, due to the low
hydrogen energy density), the possibility of backfiring in the intake manifold due to its high reactivity
(mainly when an indirect injection strategy, PFI, is adopted), or the onset of detonation due to its low
activation energy. In addition, high NOx emission levels can be observed when near stoichiometric
mixtures are employed. Table 1 summarizes the main characteristics of hydrogen compared with those
of the main fuels for ICEs [3, 4, 8].

A hydrogen direct injection (DI) system can be used to solve many of the aforementioned problems
[1, 4, 12, 13, 14]. However, hydrogen DI systems are still at the prototype level and, owing to the high
residual pressure required for injection, do not allow to utilize at maximum the amount of hydrogen
stored on board thus further lowering the vehicle's range, unless an auxiliary compressor is adopted
which in any case absorbs energy and further complicates the system.

PFI systems are certainly less expensive than DI systems and are available on the market, since they
basically represent an evolution of those applied for methane injection. In addition, if combined with
supercharging and the use of suitably injection strategies and diluted mixtures, they can solve the
problems of low power and backfire in the intake manifolds with a low tendency to knock and NOx
emission levels [15, 16, 17].

The present study shows the first results of an ongoing research which sees the collaboration of the
University of Pisa with the staff of the company Ecomotive Solutions (Serralunga di Crea - AL- Italy)
and aimed at fine-tuning ready-to-market strategies for the use of hydrogen in internal combustion
engines. Starting from a turbocharged PFI engine fueled by natural gas and used on light commercial
vehicles, a low-cost indirect hydrogen injection system has been implemented, combined with
appropriate injection strategies and boost pressure control, this last assuming a fundamental aspect in
recovering engine performance that inevitably deteriorates with the use of diluted mixtures.

The first results with hydrogen fueling, obtained without any particular engine optimization, with the
sole exception of the replacement of the intake manifold and turbocharger unit, have shown how it is
possible to conveniently transform methane-fueled production engines into hydrogen fueled units by
applying consolidated (commercial) technologies, obtain performance comparable to that of the original
engine, with even higher efficiency peak.

2. Experimental engine setup

One of the targets of the present project was to verify the possibility to implement a hydrogen injection
system in a commercial engine, typically adopted in light commercial vehicles, making as few
modifications as possible. An IVECO NEF 60 engine, designed to be fueled with natural gas, was chosen
and whose characteristics are reported in Table 2. The engine was connected to a Borghi & Saveri eddy
current brake, with rpm/torque controller, as shown in Figure 1.

The hydrogen feeding line, i.e. pipes, electro-valves, flow meter, pressure regulators etc., was
realized utilizing appropriate commercial components. With a view to making the least possible number
of modifications to the engine and therefore adopting simple hydrogen injection strategies, it was
decided to implement an indirect hydrogen injection system, hence maintaining the same injection
configuration (PFI) of the baseline engine. For the hydrogen injection a special injector model, derived
from one normally used for the indirect injection of natural gas, was selected.
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

3

Table 1 – Comparison of fuels characteristics
Properties Hydrogen Methane Gasoline Diesel
Carbon content (mass%) 0 75 84 86
Lower Heating Value (MJ/kg) 120 46 44 42.5
Density (kg/m3
) [@ 0°C, 1 bar] 0.089 0.72 730-780 830
Vol. Energy Content (MJ/m3
) [@ 0°C, 1 bar] 10.7 33 33 x 103 35 x 103

Boiling Point (K) 20 111 298-488 453-633
Auto-Ignition Temperature (K) 858 813 ⁓ 623 ⁓ 523
Minimum Ignition Energy in air (mJ)
[at 1 bar, stoichiometric] 0.02 0.29 0.24 0.24
Stoichiometric air/fuel ratio 34 17.2 ⁓ 14.7 ⁓ 14.5
Laminar flame speed in air (m/s)
[1 bar, 25 °C, stoichiometric] 1.85 0.38 0.37-0.43 0.37-0.43
Flammability limits in air (vol%) 4-76 5.3-15 1-7.6 0.6-5.5
Adiabatic flame temperature (K)
[1 bar, 25 °C, stoichiometric] 2480 2214 2580 ⁓ 2300
Quenching distance (mm)
[1 bar, 25 °C, stoichiometric] 0.64 2.1 ⁓ 2
Octane number [(R+M)/2] 130+ 120+ 87-95

Cetane number 13-17 40-55

Tab. 2 – Experimental engine characteristics
Engine model IVECO NEF60
Thermodynamic cycle Otto cycle

Max power 150 kW @ 2500 rpm
Max torque 750 Nm @ 1400 rpm
n. of cylinders 6 in line
Displacement 5880 cm3
Volumetric compression ration 11.3
n. of valves per cylinder 2

Air intake turbocharged
Fuel injection system PFI multipoint
Cooling system Water cooled

One of the few changes made to the engine involved the intake manifold. The original one was
replaced with a custom made one (Figure 12) which allows to locate the hydrogen injectors, connected
to a common feeding line (common rail), close to the intake valves. This location, together with proper
injection timing, helps to mitigate the problems of backfiring since reduces the accumulation of
hydrogen in the intake manifold. In particular, the timing of the hydrogen injection has been set so that
the injector always closes before the intake valve closes, in order to avoid hydrogen accumulations near
the intake valve, which could give rise to backfires in the following cycle. The dosing of the quantity of
injected hydrogen therefore takes place by anticipating the opening of the injector with respect to the
intake valve closing. However, the new intake manifold has been equipped with a safety valve to prevent
overpressure in the event of backfire problems. A customized electronic control unit has been adopted
for the control of all the operating engine parameters.

Another target of the project was to analyze the possibility to increase as possible the boost pressure
to obtain an adequate engine power utilizing diluted mixtures, these last necessary to avoid backfiring
problems which can occur owing to the adoption of a PFI strategy. Preliminary tests have evidenced the
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

4

impossibility of achieving adequate boost ratios with the original fixed geometry turbocharger when the
dilution of the air/hydrogen mixture increases. As better highlighted in the following paragraph, this can
be attributed to the decrease in the enthalpy of the exhaust gases as the dilution of the mixture increases
[18, 19, 20]. To solve such problem, it was decided to replace the original turbocharger with a new unit
equipped with variable geometry turbine (VGT) produced by BorgWarner and shown in Figure 3. The
possibility of using a VGT is also due to the charge dilution strategy adopted which reduces the exhaust
temperature and therefore allows the variable geometry system to operate in safety. In addition, an
appropriate crankcase ventilation system was also implemented.

Fig. 1 – The experimental engine on the test bench.

Fig. 2 – The new intake manifold

Fig. 3 – The new turbocharger with variable geometry turbine.
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

5

The indicating cycle acquisition for engine combustion analysis was possible thanks to the
application of an AVL ZI45 spark plug with integrated piezo-electric pressure sensor, an AVL shaft
encoder and an AVL Indimodul (model 622) data acquisition system. To monitor the pressure in the
intake and exhaust manifold, two Kistler piezo-resistive absolute pressure sensor (model 4045A5) have
been used and connected to the Indimodul. Several exhaust gas K-type thermocouples were located at
the engine exhaust and intake to verify the steady state conditions occurrence for each different test
condition. Once the engine was stabilized in a particular operating condition, data were collected and
analyzed to provide averaged values. Finally, for exhaust gas analysis, basically consisting only on NOx
emission, an AVL DiTEST GAS 1000 was employed. A sketch of the engine and the equipment used
in the test room are shown in Figure 4.

Fig. 4 – Sketch of the engine and the experimental equipment.

3. Experimental activity and resuslts

3.1. Analysis of boost limits

SI engines with indirect hydrogen injection (PFI) suffer, as known, from the problem of backfire in the
intake manifolds, especially with mixtures close to stoichiometric. In fact, a series of preliminary tests
confirmed that this problem becomes particularly serious with the use of mixtures characterized by a
lambda (λ) value < 2, this last being the mixture mass fraction defined as [20]:

 =
(

ℎ)

(

ℎ)
ℎ
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

6

It was therefore decided to continue the experimentation using λ values >2.

At this point, however, it is equally known that the dilution of the mixture leads to a drastic reduction
in engine performance. The only way to recover performance is to increase the boost pressure. But high
boost ratios have the limit of engine knock with low λ values, while as the dilution increases the limit
lies in the impossibility of obtaining adequate boost levels due to the low enthalpy of the exhaust gases.
A long experimental campaign was therefore dedicated to defining a correct engine operating range, in
order to verify, at different engine speeds, the maximum value of the boost ratio changing the mixture
dilution (λ). For each operating condition, the spark advance (SA) was adjusted in order to obtain the
maximum brake torque (MBT).

Boost regulation has been possible thanks to the adoption of the VGT which allows to adjust the
effective stator cross sectional area at the entrance of the radial turbine. This adjustment leads to exploit
at maximum the residual enthalpy of the exhaust gases even with the adoption of very diluted mixtures,
thing not possible with the original fixed geometry turbine. In fact, from the first fundamental relation
of turbo-compressor at steady state [18, 20], and reported below:

2
1

= {1 +

̇
̇

∙



∙

3
1

∙  ∙ [1 − (

4
3

)

−1

]}

−1

we know that the energy developed by the turbine, and therefore the boost ratio obtainable from the
compressor (p2/p1, where p1 is the ambient pressure and p2 the one after the compressor), increases
increasing the turbine inlet temperature (T3), therefore at the engine outlet, and the expansion ratio across
the turbine itself (p3/p4), where p4 is the ambient pressure equal to p1. With the VGT, by regulating the
stator cross sectional area at the turbine inlet, it is possible to raise the p3 which allows, on the one hand,
to increase the T3 as the gas expansion ratio at the engine outlet decreases, on the other hand to increase
the pressure expansion ratio across the turbine. The other quantities that appears in the equation are ṁT
(mass flow rate across the turbine), ṁC (mass flow rate across the compressor), cpT (gas specific heat at
constant pressure across the turbine, cpC (gas specific heat at constant pressure across the compressor),
k is the ratio of specific heats and finally ηTC is the total turbo-compressor efficiency. The subscripts T
and C stand for Turbine and Compressor, respectively.

The graphs of Figure 5 show the boost limits as λ varies at 1400, 2000 and 2500 rpm. As a whole,
the maximum boost ratios are obtained with a λ value of approximately 2.5, with a pick of 2.6 bar at
2000 rpm, while for lower λ values the boost increasing, however possible, leads to the onset of
detonation (knock limit). Beyond λ = 2.5 the boost value is instead limited, as aforementioned, by the
low enthalpy of the exhaust gases which prevent the expansion turbine from adequately "pushing" the
compressor (turbine limit). This aspect is confirmed by the trend of the exhaust temperatures which
decrease as the dilution of the mixture increases [21, 22], as shown in Figure 6 for various engine speeds
and at the corresponding maximum boost pressure adoptable. Intake air temperatures (after intercooler)
ranged from 35 °C to 45 °C degrees at maximum boost pressure, with an ambient temperature of about
18°C.
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

7

Fig. 5 – Boost limits at different rpm varying λ.

Fig. 6 - Exhaust temperature at full load of the hydrogen fueled engine at different λ values and rpm.
The dilution of the air/hydrogen mixture gives also benefits on the reduction of nitrogen oxides
(NOx) [20, 23]. The graph in the Figure 7 shows how, at various engine speeds and with the maximum
boost pressure adoptable, NOx emission is close to zero with lambda > 3, but also with lambda ≈ 2.5
the levels are very low (< 200 ppm).

300
350
400
450
500
550
600

1.5 2.0 2.5 3.0 3.5 4.0

exhaust temperature [°C]

λ

1400 2000 2500
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

8

Fig. 7 - NOx emissions at full load of the hydrogen fueled engine at different λ values and rpm.

3.2. Analysis of engine performance

As highlighted in the previous paragraph, the use of air/hydrogen mixtures characterized by lambda
values around 2.5 allows, on the one hand, to use the highest boost ratios without incurring backfire or
knocking problems, and, on the other, to obtain low NOx emissions.

Figure 8 and 9 show, respectively, the trend of engine power and torque at full load (maximum boost
pressure) as the rpm varies, using a lambda equal to 2.5. These trends are compared with those of the
original natural gas-powered engine which uses mixtures around the stoichiometric. It can be seen that
the hydrogen engine performance is of great importance, comparable to that of the original engine,
especially at higher rpm where the loss of power/torque can be quantified at around 10%. At low rotation
speeds, the impossibility of reaching adequate levels of supercharging justifies the greater difference in
performance with the original one.

Fig. 8 - Maximum hydrogen engine power with λ = 2.5 compared with that of the natural gas fueled
engine under stoichiometric conditions

0
200
400
600
800
1000
1200
1400
1600

1.5 2.0 2.5 3.0 3.5 4.0

NOx emissions [ppm]

λ

1400
2000
2500

20
40
60
80
100
120
140
160

500 1000 1500 2000 2500 3000

Power [kW]

rpm

natural gas hydrogen
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

9

Fig. 9 - Maximum hydrogen engine torque with λ = 2.5 compared with that of the natural gas fueled
engine under stoichiometric conditions

The use of diluted mixtures, in addition to obvious benefits from the point of view of NOx emissions,
also makes it possible to increase the engine efficiency thanks to the lower combustion temperatures
which lead to a decrease in thermal loss through the cylinder walls and reduce gaseous dissociation [20].
The figure 10 shows the comparison between the efficiency trend of the hydrogen fueled engine (always
at maximum load with lambda 2.5) with the original natural gas fueled one. It can be seen how the
hydrogen engine presents higher values on average, with a peak efficiency close to 40% around 2000
rpm.

Fig. 10 - Maximum hydrogen engine efficiency with λ = 2.5 compared with that of the natural gas
fueled engine under stoichiometric conditions

200
300
400
500
600
700
800

500 1000 1500 2000 2500 3000

Torque [Nm]

rpm

natural gas hydrogen

34
35
36
37
38
39
40

500 1000 1500 2000 2500 3000

efficiency [%]

rpm

natural gas hydrogen
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

10

4. Combustion analysis

The in-cylinder pressure signal was acquired and properly used to analyze the engine combustion
behavior. Once the engine was stabilized in one operating condition, 100 cycle were acquired and
averaged to calculate several combustions related parameters, such as the MFB10, MFB50 and MFB90
that are the crank angle (CA°) at which, respectively, 10%, 50% and 90% of the fuel mass is burned per
cycle, and the COVimep, that is the coefficient of variation of the inlet mean effective pressure [20].

As previously mentioned, at each engine speed and for each value of λ, the maximum boost was
sought, consequently adjusting the ignition advance in order to obtain the Maximum Brake Torque
(MBT). In these conditions the pressure peak in the cylinder always falls between 10° and 13° ATDC,
as reported in the graphs of Figure 11 which shows results at 2000 rpm and different λ values.

Fig. 11 - In cylinder pressure curves at 2000 rpm and different λ values.

As λ increases, at the same rpm, also the ignition advance for MBT increases since the mixtures
become less reactive. Table 3 shows these values at 2000 rpm, together with the location of the pressure
peak and value and also with the corresponding value for MFB10, MFB50 and MFB90, while Table 4
shows the same values at λ = 2.5 and different rpm. The analysis of MFB values confirms the high flame
speed of hydrogen, which allows the combustion reactions to be completed in less than 30 CA° even in
the presence of highly diluted mixtures, against an average of 40-50 CA° for the combustion of natural
gas in stoichiometric conditions.

As reported in Figure 12, the flame propagation speed of hydrogen allows for regular combustion
even with high λ values and consequently to obtain an always adequate regularity of combustion with
COVimep ranging from about 1% or less with lambda = 2, up to about 2 % with lambda equal to 3.5.
After this value some misfiring problems started to appear, which inevitably increase the COVimep
values.

0

20

40

60

80

100

120

-200 -150 -100 -50 0 50 100 150 200 cylinder pressure [bar]

CA [°]

λ = 2 λ = 2.2 λ = 2.5 λ = 3
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

11

Tab. 3 - Engine setting and combustion parameters of the hydrogen fueled engine at 2000 rpm.
λ = 2 λ = 2.3 λ = 2.5 λ = 3 λ = 3.5
Ignition advances (°) BTDC [for
MBT]
10 10.5 13.5 14.4 15.7

Location of pressure peak (°) ATDC 13 13.3 12.2 12.7 13.1
Pressure peak (bar) 98.4 100.3 107 69.2 64.3
MFB10 (°) ATDC 1.8 2.4 0.9 2.9 3.5
MFB50 (°) ATDC 8.6 9.8 8.6 12.2 13.1
MFB90 (°) ATDC 20.1 22.7 21.9 29.1 31.2

Tab. 4 - Engine setting and combustion parameters of the hydrogen fueled engine at λ = 2.5
1400 rpm 2000 rpm 2500 rpm
Ignition advances (°) BTDC [for
MBT]
10.3 13.5 13.9

Location of pressure peak (°) ATDC 12.9 12.2 12.3
Pressure peak (bar) 90 107 96
MFB10 (°) ATDC 2.2 0.9 0.9
MFB50 (°) ATDC 9.7 8.6 8.9
MFB90 (°) ATDC 22.8 21.9 23

Fig. 12 – COVimep at different rpm varying lambda.

5. Conclusions

The present study analyzed the possibility of converting to hydrogen a commercial 4-strokes PFI
turbocharged engine originally fed with natural gas and designed to be applied in light commercial
vehicle. The hydrogen conversion has been implemented by applying minimal modifications to the
original engine architecture (replacement of the intake manifold) with the only major replacement being
the turbocharger. The experimentation analyzed the engine performance at different rpm, air/hydrogen

0
0.5
1
1.5
2
2.5
3
3.5

1.5 2 2.5 3 3.5 4 4.5

COV imep

λ

1400 rpm
2000 rpm
2500 rpm
ATI-2023

Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

12

ratio (λ) and boost pressures. In particular, the maximum boost pressure has been analysed in depth in
order to define the correct engine operating range.

Engine calibration adopting a λ value equal to 2.5 has highlighted the possibility of reaching very
high engine efficiency (> 39 %), with low NOx emissions (< 200 ppm) and with a limited performance
loss (< 10%) compared to the original methane fueled engine.

These first results, obtained without any particular engine optimization, with the exception of the
turbocharger replacement, demonstrates how it is possible, by exploiting established technologies and
adopting appropriate hydrogen injection strategies and boost pressures, to bring hydrogen-fueled
engines to the market in a short time.

Future research activities, supported by a numerical simulation activity, will be focused on improving
the engine calibration and the air/hydrogen mixing process in order to reduce backfire and detonation
problems even with the use of slightly diluted air/hydrogen mixtures, always in presence of indirect
injection systems.

Bibliography

1. Verhelst S, “Recent progress in the use of hydrogen as a fuel for internal combustion engines”,
International Journal of Hydrogen Energy 39 (2014), 1071-1085.
2. Sharma S, Ghoshal S, “Hydrogen the future transportation fuel: From production to
applications”, Renewable and Sustainable Energy Reviews 43 (2015), 1151-1158.
3. Hosseini SE, Butler B, “An overview of development and challenges in hydrogen powered
vehicles”, International Journal of Green Energy (2020), 17:1, 13-37.
4. Stepien ZA, “A Comprehensive Overview of Hydrogen-Fueled Internal Combustion Engines:
Achievements and Future Challenges”, Energies 2021, 14, 6504.
5. Editorial, “The role of hydrogen for future internal combustion engines”, International J of
Engine Research 2022, Vol. 23(4) 529–540, @ IMechE 2022.
6. Wróbel K, Wróbel J, Tokarz W, Lach J, Podsadn KI, Czerwi´nski A, “Hydrogen Internal
Combustion Engine Vehicles: A Review”, Energies 2022, 15, 8937.
7. Shinde BJ, Karunamurthy K, “Recent progress in hydrogen fueled internal combustion engine
(H2ICE) – A comprehensive outlook”, Materials Today: Proceedings 51 (2022), 1568-1579.
8. Sun Z, Hong J, Zhang T, Sun B, Yang B, Lu L, Li L, Wu K, “Hydrogen engine operation
strategies: Recent progress, industrialization challenges, and perspectives”, International
Journal of Hydrogen Energy 48 (2023), 366-392.

9. Faye O, Szpunar J, Eduok U, “A critical review on the current technologies for the generation,
storage, and transportation of hydrogen”, International Journal of Hydrogen Energy 47 (2022),
13771-13802.

10. Pramuanjaroenkij A, Kakac S¸ “The fuel cell electric vehicles: The highlight review”,
International Journal of Hydrogen Energy 48 (2023), 9401-9425.
11. Aminudin MA, Kamarudin SK, Lim BH, Majilan EH, Masdar MS, Shaari N, “An overview:
Current progress on hydrogen fuel cell vehicles”, International Journal of Hydrogen Energy 48
(2023), 4371-4388.

12. Yip HL, Srna A, Yin Yuen AC, Kook S, Taylor RA, Yeoh GH, Medwell PR, Chan QN, “A
Review of Hydrogen Direct Injection for Internal Combustion Engines: Towards Carbon-Free
Combustion”, Appl. Sci. 2019, 9, 4842.

13. Oikawa M, Kojiya Y, Sato R, Goma K, Takagi Y, Mihara Y, “Effect of supercharging on
improving thermal efficiency and modifying combustion characteristics in lean-burn directinjection
near zero-emission hydrogen engines”, International Journal of Hydrogen Energy 47
(2022), 1319-1327.

14. Lai F, Sun B, Wang X, Zhang D, Luo Q, Bao L, “Research on the inducing factors and
characteristics of knock combustion in a DI hydrogen internal combustion engine in the process
ATI-2023
Journal of Physics: Conference Series 2648 (2023) 012073

IOP Publishing
doi:10.1088/1742-6596/2648/1/012073

13

of improving performance and thermal efficiency”, International Journal of Hydrogen Energy
48 (2023), 7488-7498.

15. Nagalingam B, Dubel M, Schmillen K, “Performance of the Supercharged Spark Ignition
Hydrogen Engine”, SAE Technical Paper 831688, 1983.
16. Verhelst S, Maesschalck P, Rombaut N, Sierens R, “Increasing the power output of hydrogen
internal combustion engines by means of supercharging and exhaust gas recirculation”,
International Journal of Hydrogen Energy 34 (2009), 4406-4412.
17. Gao J, Wang X, Song P, Tian G, Ma C, “Review of the backfire occurrences and control
strategies for port hydrogen injection internal combustion engines”, FUEL 307 (2022), 121553.
18. Hiereth H, Prenninger P, “Charging the Internal Combustion Engine”, Springer-Verlag WienNewYork,
2007.

19. Feneley AJ, Pesiridisa A, Andwari AM, “Variable Geometry Turbocharger Technologies for
Exhaust Energy Recovery and Boosting”, Renewable and Sustainable Energy Reviews 71
(2017), 959-975.

20. Heywood JB, “Internal Combustion Engine Fundamentals”, 2nd Edition. New York: McGrawHill
Education; 2018.

21. Sterlepper S, Fischer M, Claßen J, Huth V, Pischinger S, “Concepts for Hydrogen Internal
Combustion Engines and Their Implications on the Exhaust Gas Aftertreatment System”,
Energies 2021, 14, 8166.

22. Park C, Kim Y, Oh S, Oh J, Choi Y, Bae HK, Lee SW, Lee K, “Effect of fuel injection timing
and injection pressure on performance in a hydrogen direct injection engine”, International
Journal of Hydrogen Energy 47 (2022), 21552-21564.
23. Bao L, Sun B, Luo Q, “Experimental investigation of the achieving methods and the working
characteristics of a near-zero NOx emission turbocharged direct-injection hydrogen engine”,
FUEL 319 (2022), 123746.