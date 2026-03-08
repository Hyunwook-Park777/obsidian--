# The effect of different charging concepts on H2 fuelled ICEs

Fuel 343 (2023) 127983

Available online 2 March 2023

0016-2361/© 2023 Elsevier Ltd. All rights reserved.

Contents lists available at ScienceDirect

Fuel

journal homepage: www.elsevier.com/locate/fuel

Full length article

The effect of different charging concepts on hydrogen fuelled internal

combustion engines

Onur Barış ∗
, İlker Güler, Anıl Yaşgül

AVL Research and Engineering TR, 34885 Sancaktepe, Istanbul, Turkey

A R T I C L E I N F O

Keywords:
Hydrogen

Engine modelling
Boosting strategy
Lambda

A B S T R A C T

Hydrogen has been widely acknowledged as a potential fuel for internal combustion engines, owing to its
unique chemical properties, environmental friendliness, and the ability to be produced from a variety of
sources. The carbon-free nature of hydrogen is of particular significance as it is considered to be a key
contributor to achieving stringent emissions regulations. However, one of the challenges associated with
hydrogen as a fuel is the requirement for high air flow during combustion, which is necessary to meet the
stoichiometry of the combustion process. The failure to achieve this high air flow can result in elevated
emissions of Nitrogen Oxides (NOx), a phenomenon that is of concern for engine manufacturers.

Turbocharging increases the power and efficiency of internal combustion engines by forcing more air into
the combustion chamber. This can be particularly beneficial for hydrogen-fuelled engines as hydrogen has a
lower energy density compared to traditional fossil fuels. This study aims to establish the most efficient boosting
strategy for hydrogen-fuelled internal combustion engines with the goal of achieving a combination of fuel
economy, high power density, and low emissions of NOx. To achieve this objective, a model of a hydrogenfuelled
internal combustion engine, specifically tailored for heavy-duty vehicle applications and featuring a
direct injection system, has been developed. The validity of the model has been evaluated through a comparison
of the results obtained from the model with those obtained from dynamometer testing. The study employs a
model-based approach to examine a variety of charging concepts.

1. Introduction

From the beginning of the 21st century to the next two decades,
there has been a significant increase in world population, which indicated
a 26% rise as can be seen in [1]. This growth has also led to
a demand growth to energy. In order to supply this emerging energy
demand, the trend towards carbon-based fuels has resulted in a 39%
increase in total Greenhouse Gas (GHG) emissions [2]. Additionally,
it is posited that human actions are responsible for global warming,
specifically through the rise in GHGs like carbon dioxide in the atmosphere
[3]. Analysis of these increased items by sector reveals that
industrial usage, electricity and heat production, and transportation are
the primary contributors as shown in [2].

In order to decrease the impacts of global warming and ensure a
more sustainable environment, reduction of GHG emissions has become
a significant concern for the international community. To achieve
this goal and comply with strict emission regulations (EU Standard);
the automotive industry has also turned to alternative fuels such as
electricity, hydrogen, biofuels, ammonia, ether, and ester instead of

∗ Corresponding author.

E-mail addresses: Onur.Baris@avl.com (O. Barış), Ilker.Guler@avl.com (İ. Güler), Anil.Yasgul@avl.com (A. Yaşgül).

carbon-based fossil fuels [4–6]. Most scholars and engine manufacturers
have highlighted that hydrogen possesses unique physical and
chemical properties that make it a more suitable alternative fuel in
comparison to other options [7–10]. Even though the ideal reaction
of H2 and O2 only produces H2O without any conventional carbonbased
emissions (such as CO, CO2
, HC, and soot), the high combustion
temperature and the presence of nitrogen gas in the cylinder can lead
to the reaction N2 + O2→NOx. As a result, Hydrogen Fuelled Internal
Combustion Engines (H2ICEs) still have the issue of combustion
emissions, but these emissions are primarily limited to NOx, which is
comparatively simpler to manage than the emissions from other fuels
in internal combustion engines [11]. A comparison of the performance
of lean-burn without post-treatment, stoichiometric mixture conditions
with both Exhaust Gas Recirculation (EGR) and the post-treatment
system, revealed that the combination of lean-burn and a turbocharger
is the most efficacious method for achieving enhanced efficiency and
reduced NOx emissions [12].

Table 1 provides a comprehensive comparison of hydrogen, as a
candidate fuel to replace fossil fuels in the future, in relation to its

https://doi.org/10.1016/j.fuel.2023.127983

Received 6 December 2022; Received in revised form 25 January 2023; Accepted 23 February 2023
Fuel 343 (2023) 127983

2

O. Barış et al.

Table 1

Properties of hydrogen compared to gasoline and diesel.

Property Unit Gasoline Diesel Hydrogen
Density kg/m3 760 833 0.09
Lower heating value MJ/kg 43.5 42.5 120

Stoichiometric air demand kgair/kgfuel 14.7 14.5 34.3
Mixture calorific value PFI (mixture aspirated) MJ/m3 3.76 – 3.19
Mixture calorific value DI (air aspirated) MJ/m3 3.83 3.77 4.52
Minimum ignition energy mJ 0.24 0.24 0.02

Ignition limits Vol % 1.0–7.6 0.6–5.5 4-76

 0.4–1.4 0.5–1.3 0.2–10
Auto ignition temperature K ∼623 ∼523 858
Laminar flame speed cm/s 40–80 40–80 200

Quenching distance mm ∼2 – 0.64

Adiabatic flame temperature K 2580 ∼2300 2480
Carbon content % 84 86 0

combustion properties when compared to conventional fuels such as
diesel and gasoline, which are widely utilized in internal combustion
engines [13–15].

The alteration in the equivalence ratio had an impact on both the
combustion velocity and temperature [11]. Hydrogen has extremely
wide ignition limits compared to other conventional fuels which is very
well suited for lean operation [14]. Luo [16] divided the change in NOx
with equivalence ratio in PFI hydrogen fuel internal combustion engine
to four stages. At equivalence ratios less than 0.6, the combustion
temperature is the primary factor affecting NOx generation, and the
maximum combustion temperature is below 1600 K, which is not
sufficient to provide the necessary activation energy, resulting in NOx
concentrations of 200 ppm. As equivalence ratios increase to the range
of 0.6–0.88, the combustion temperature increases to 1800 K, and the
oxygen concentration becomes higher than 4%, creating suitable conditions
for NOx generation, leading to NOx concentrations of 7000 ppm
which exceed the typical production of NOx in traditional internal
combustion engines. As equivalence ratios reach the range of 0.88–
1.0, despite the high combustion temperature, NOx emissions rapidly
decline to 1000 ppm due to the decrease in oxygen concentration.
When the equivalence ratio is higher than 1, the mass concentration
of oxygen is close to 0, and the NOx emissions are minimal.

So, the most important factor triggering the formation of NOx emissions
is the high temperature reached in the cylinder [17]. Lean mixture
formation helps to reduce the combustion temperature thus near zero
NOx emission aim can be achieved on H2ICE [8]. Furthermore, one of
the key advantages of lean mixture is the improved overall efficiency
of the engine, as it eliminates the flow losses (pumping losses) [18].

At stoichiometric engine operation condition, hydrogen has the
higher flame speed. This results in a more isochoric, thus thermodynamically
more favourable combustion. On the other hand flame speed
reduces on the lean mixture condition as explained in [19].

With the highest auto-ignition temperature relative to the common
fuels, the resistance of hydrogen to knocking is expected to be
high [15]. This feature also proves that hydrogen fuel is more suitable
for use in spark ignition engines. However, since the minimum ignition
energy value is very low, there is a risk of pre-ignition caused by hot
spot if hydrogen fuel is used in spark ignition engines. Also, a nonplatinum
cold-rated spark plug should be used to avoid risks such as
pre-ignition and backfiring in SI engine [20].

Hydrogen, which is distinguished by its combustion characteristics
and carbon-free structure, is considered the most viable candidate for
the fuel of the future due to its various sources of production and its
environmentally friendly production methods [21].

However, on H2ICE, it is vital to determine the correct boosting
strategy to keep emissions within regulation limits. According to EURO
VI standard, NOX limit is given as 0.4 gr/kWh [22].

In this paper, conventional turbocharging concepts in the automotive
sector are considered for Hydrogen fuelled engine. The concepts
that are investigated are as follows:

1. Fixed Geometry Turbocharger (FGT)

2. Variable Geometry Turbocharger (VGT)
3. 2-stage Turbocharging (2-stage)

The FGT concept represents the most straightforward and practical
solution to implement on an engine. Regardless of whether engine runs
on hydrogen or conventional fossil fuels, single stage FGT which uses a
wastegate on turbine to control boost pressure by controlling exhaust
energy flow passing through the turbine wheel is the cheapest and
the simplest turbocharging option compared to single stage VGT and
2-stage turbocharging alternatives [23].

The VGT concept offers a greater degree of flexibility across the
entire engine speed range. At the turbine inlet, VGT utilizes racks whose
angle can be adjusted with an electronic actuator to control boost
pressure. Closing the racks basically creates a smaller turbine which has
higher efficiency at low mass flow rates. Moreover, a smaller turbine
results in higher turbine inlet pressures at low mass rates, enabling
higher energy extraction from exhaust gas by increasing expansion
ratio through the turbine. These two advantages of having a smaller
turbine are useful for low-end speed region and transient response of
the engine [24]. Consequently, VGT provides better performance for
wider operation ranges at the expense of complexity and cost due to
angle adjustable racks compared to FGT with wastegate option [25].

2-stage turbocharging is the most complex and costly one out of
these options. This concept is used when high air flow rates and
high boost pressures are required, like hydrogen engines with high
air requirements. It has a large turbocharger (LP stage) and a small
turbocharger (HP stage) to cover entire engine operating range. As
it is more efficient at high mass flow rate operating points, most of
the boost pressure demand is satisfied by LP stage at high-end speed
region. HP stage with a small turbocharger satisfies most of the boost
pressure demand at low-end speed region and is also beneficial for
transient response as explained above. HP stage can also be matched
as a VGT for better controllability at transient maneuvers. As a result,
2-stage turbocharging can cover a wider operation range with a better
transient response compared to single stage VGT [24,26]. However,
existence of LP turbine can force HP turbine to operate on low pressure
ratio and thereby on low efficiency. Therefore, higher pressure at HP
turbine inlet might be required to have the same boost pressure with
single stage VGT, which increases pumping losses and consequently
fuel consumption compared to single stage VGT option. In addition
to that, as it compresses the hot air compressed by LP compressor,
HP compressor outlet temperature is likely to exceed hardware limit.
To overcome this problem, usage of a titanium compressor or an
intercooler between LP and HP compressor is mandatory [26].

In addition to these, more advanced concepts such as e-turbo, eboost
or more advanced electrically assisted turbocharging systems can
be modelled. However, these types of concepts are not widely available
in the market. In addition, these all systems require higher voltage (48
V or higher), advanced electrical system and/or hybridization. For the
sake of system simplicity, these concepts are left out of the scope of this
paper, but these can be investigated as a next step if need arises.

Detailed comparison and conclusions of this study will be given in
the following parts of the paper but first the details of thermodynamic
model will be explained.
Fuel 343 (2023) 127983

3

O. Barış et al.

Fig. 1. Engine layout.

Table 2

Engine properties.

Properties Value

Engine displacement range 12–15L Class
Compression ratio range 9–12
No of cylinders 6

Configuration Inline

Firing order 1-5-3-6-2-4

EGR system High Pressure

AirPath Turbocharger with intercooler

2. Thermodynamic model

In this section, the important model details such as concepts that are
selected will be explained. The engine considered here is a heavy-duty
inline engine, which is in a displacement widely used in the industry.
Fig. 1 shows the schematic view of the engine.

Additionally, the engine properties are indicated in Table 2

Thermodynamical model consists of one-dimensional (1D) model
of the air path of the engine. Turbochargers are modelled using the
measured performance maps of compressor and turbine parts. Base 1D
model was validated with performance data from dynamometer and
model deviation was less than ±2% for all test points.

For heat transfer, a flow model is used which considers the squish,
swirl, and turbulence flow characteristics inside the cylinder. This
model calculates the convective heat transfer within the cylinder according
to the flow conditions. The details of this heat transfer model
can be found in [27]. A simplistic Finite Element Analysis (FEA) model
was used to calculate wall temperature inside the cylinder, where
cooling water and oil temperatures are given as boundary conditions.

For the investigation in this paper, low pressure direct injection
(LPDI) concept hydrogen engine with spark ignition (SI) is simulated.
Therefore, its compression ratio is lower compared to diesel, similar to
other heavy duty SI engines such as natural gas (NG) engines. There
are also other injection concepts available such as multi-port injection
(MPI) which is also spark ignited and high-pressure direct injection
(HPDI) with diesel pilot or HPDI hydrogen only (ignited with glow
plug or other support system). The reason why LPDI concept is selected
because of its best compromise between parameters such as cost, risk,
availability (of the injection system) and efficiency [28]. MPI concept
is the cheapest among these concepts and easiest to adapt [29]. The
injection system is relatively low pressure and less complex. One big
disadvantage of MPI is backfire as can be seen in [28]. It is also
stated in the same publication that the engine’s efficiency is lower
in comparison to other concepts. As a result of this lower efficiency,
the power density of the engine is also lower in comparison to other
concepts. The HPDI with diesel pilot concept is the most similar to
the diesel engine concept. The hydrogen is ignited with the means

Fig. 2. Typical NOx behaviour of a hydrogen DI engine vs. diesel.

of a diesel pilot injection. Like diesel; the concept benefits from high
compression ratio and therefore high thermal efficiency. However,
since there is diesel pilot injection, there is also some amount of CO2

emitted from the engine. Other downside of the engine is the more
complex and high pressure fuelling system required for both diesel
and hydrogen. Another disadvantage of this system is the high cost
related to its high-pressure injection system [28]. Hydrogen only HPDI
concept is generally considered to be troublesome and requires a lot
of further work as stated in [15,30]. Thus, it is excluded from further
consideration. In light of all the information available, it could be
deduced that the LPDI presents the best trade-off between all the factors
taken into account.

Hydrogen combustion has different emission characteristics compared
to diesel, as indicated in [31]. Hydrogen tends to have almost
0 engine-out NOx emission as excess air ratio () goes above 2.4.
Fig. 2 [31,32] clearly shows the behaviour of NOx emission as
changes and it is also stated in the paper explicitly. This will provide the
benefit of eliminating the need for a NOx conversion catalyst (such as a
selective reduction catalyst-SCR) entirely or using a smaller and simpler
one, which implies that the aftertreatment system (ATS) can be less
complex and more cost-effective. Therefore, it is chosen to investigate
full load performance at high lambda.

In comparison to the engines currently available on the market, this
value is exceptionally high and requires a significant amount of air.
Therefore, instead of pumping all air into the cylinder, a Cylinder Mass
Ratio (CMR) is defined and targeted to 2.4. This is done because EGR is
used in the model in all the turbocharging concepts mentioned above.
In comparison to , CMR is composed of both fresh air and EGR flow,
whereas  only includes fresh air. So, the CMR includes both air and
EGR divided by fuel mass and divided by stoichiometric air fuel ratio
(AFR) of hydrogen as shown below.

 =

  +
   ∗ 34.33

(1)

As stated in Ref. [33], high heat capacity of EGR will compensate
even better than air to lower in cylinder temperatures and therefore
also NOx emissions. It is clearly known that NOx is directly related with
high temperatures in cylinder as shown in [17]. In addition to these
facts, tests are also performed to prove that CMR has similar effect on
NOx emission as lambda and this behaviour is shown in Fig. 3.

Since the selected target mass ratio (CMR) is significantly higher
than typical diesel and gasoline engines, the question is whether there
is a sufficient turbocharger able to supply the air flow demand. It is
also the reason why different concepts are investigated in this paper
Fuel 343 (2023) 127983

4

O. Barış et al.

Fig. 3. NOx behaviour comparison including both Lambda and CMR.

in terms of their performance with such high mass ratio, as shown in
Fig. 3.

As the choice of the combustion model, SI Wiebe model that obtained
from the analyses of test results for each the engine speed and
torque is used. Wiebe model is a non-dimensional function to impose
burn rate or heat release rate. Wiebe function can be expressed as [34]:

b = 1 −

[−(

−0
 )

(+1)]

(2)

In the absence of correlated predictive combustion model, Wiebe
function is used for combustion modelling [35]. Since the combustion
process occurs within a homogeneous mixture with spark ignition, it is
well correlated using SI Wiebe function. In addition, limitations seen in
tests are considered when determining the combustion timing to avoid
abnormal combustion events due to hydrogens easy ignitability.

As mentioned earlier; EGR system is utilized. A high pressure EGR
system between exhaust and intake boost system is used, which is
one of the most common concepts. Also, the EGR is cooled because
hot EGR will drop the mass flow into the cylinder significantly at
high loads. EGR is also beneficial for abnormal combustion events as
investigated in [33]. In addition, some of the mass flow required for
low NOx is supplied using EGR system, which in turn lowers airflow
requirement from the turbocharger. So, the range of airflow required
from turbocharger will be lower and a smaller turbocharger can be
selected, which will be also beneficial for transient response.

3. Comparison of results

In this section, the comparison of steady state results between
different turbocharger concepts will be shown. The main focus of this
comparison is to investigate the performance of each turbocharging
concept, when targeting low engine-out NOx emissions. Due to this
target, the lambda must be lean, around 2.4, which results in a relatively
higher demand for air to reach the torque target. In this article,
each turbocharger concept is investigated in terms of their response to
this challenging air demand. Model results other than brake thermal
efficiency (BTE) (Fig. 7), cylinder mass ratio (Fig. 4) and overall TC
efficiency (Fig. 8) are plotted in normalized form.

As stated in the thermodynamic model section, this study has been
performed by trying to reach CMR target 2.4 and this target has been
achieved with all turbocharger concepts as can be seen below. In
addition to that, all related results can be seen comparatively between
concepts.

Fig. 4. CMR.

Fig. 5. BMEP.

Fig. 6. PMEP.

About Fig. 5, all turbocharger analysis results show same torque
output, therefore the graphs are on top of each other, and these cannot
be distinguished from each other. About Fig. 10, there is a dashed line
added at maximum compressor outlet temperature equals to 1, which
indicates the hardware limit. That is a critical value, since the analysis
results show that the engine operates close to the limit (see Figs. 4, 6–9
and 11–16).
Fuel 343 (2023) 127983

5

O. Barış et al.

Fig. 7. BTE.

Fig. 8. Overall turbocharger efficiency.

Fig. 9. Turbine inlet temperature.

Fig. 10. Compressor outlet temperature.

Fig. 11. Turbine inlet pressure.

From BTE point of view, VGT turbocharger has the best efficiency
in comparison to FGT and 2-stage configuration and this can be seen
in Fig. 7. This can be explained with the PMEP results especially at the

low-end-speed region shown in Fig. 6 . FGT has the worst PMEP, and

Fig. 12. Compressor outlet pressure.

Fig. 13. Compressor map of FGT.

Fig. 14. Compressor map of VGT.

2-stage TC configuration has a PMEP worse than VGT TC configuration
at the low-end-speed region. This is because of the size of high-pressure
turbocharger of 2-stage charging system is smaller than the size of VGT
system. A smaller turbine results in a higher-pressure ratio and higher
turbine inlet pressure, which increases pumping work during exhaust
stroke.

In addition to that, turbocharger limits are also important parameters
to look deeply whether the performance of turbocharger is able
to achieve targets at sea level and high-altitude level, too. As can be
seen, FGT is already at the limit even at the sea level (compressor

outlet temperature please see Fig. 10), because CMR 2.4 target is a hard
limit to provide boosted-air when the system has only the waste-gate to
satisfy the torque target. Other critical parameters such as turbine inlet
temperature and pressure are safely away from their limits, which can
be seen in Fig. 9 and Fig. 11, respectively. Similarly compressor outlet
pressure shown in Fig. 12 is also much lower than its limit. Their limits
Fuel 343 (2023) 127983

6

O. Barış et al.

Fig. 15. LP compressor map of 2-stage TC.

Fig. 16. HP compressor map of 2-stage TC.

are higher than the maximum of y-axis therefore it is not plotted in the
figures.

VGT turbocharger system is better in comparison to the system
with FGT charging, but this system is also close to the compressor
outlet temperature limit. This could make the VGT’s performance at
high altitude questionable. Compared to FGT; VGT has more margin at
higher engine speeds in compressor outlet temperature.

The system with 2-stage turbocharger can be the best option in
terms of the high-altitude performance because it has very good margin
to stay below the compressor outlet temperature limit in comparison
to the systems with FGT and VGT. This means, system with 2-stage
charging system can reach higher altitudes with same CMR levels
without derating. This is the biggest advantage of 2-stage according to
the analysis results.

Turbocharger speed is another important parameter and limit to
understand whether turbocharger performance is enough or not for
sea level and high altitude. Turbocharger maps are obtained from
turbocharger performance test rig. In these tests, turbocharger is tested
under certain conditions according to the reference condition and as
a result a performance map is obtained. It is a standard turbocharger

Table 3

Applications and possible use cases of different charging systems.

FGT VGT 2-stage
Genset X

Long haul X X
Construction X
Marine X X

Off-road X X

performance map consisting of the following parameters: pressure ratio,
mass flow, efficiency, and turbocharger speed. As can be seen from
compressor maps (Fig. 13, Fig. 14, Fig. 15, Fig. 16), all charging
concepts have margin to reach the turbocharger speed limit at sea level.
VGT has the less margin in terms of turbocharger speed amongst all
charging systems, and this means the system with VGT has the least
high-altitude potential in terms of turbocharger speed limit. However,
in order to have an idea about high altitude potential, turbocharger
speed limit and compressor outlet temperature should be considered
together.

Regarding turbocharger efficiencies, it can be said that VGT has
the highest efficiencies at most of the operation points. The system
with FGT is also close to these efficiency levels and low-pressure
turbocharger of 2-stage is also at same levels, where the high-pressure
turbocharger of 2-stage looks worse than the others. It is because the
low-pressure turbocharger is the more dominant one in terms of having
higher compression ratios and that is why the results are closer to the
center of low-pressure-charging compressor map. High-pressure stage
has lower efficiency because of the lower pressure ratio.

As for transient performance, VGT is expected to respond faster than
FGT turbocharger. However, having a smaller turbocharger on high
pressure side, 2-stage turbocharging concept is expected to have the
best transient response.

4. Conclusion

In this paper, different turbocharging systems are analyzed for
hydrogen engines with a very low engine-out NOx emission target. Here
instead of lambda, CMR is taken as a target to enable low NOx emission
with relaxed air charging requirement.

Following conclusion can be drawn about critical performance criteria:–
Full load target: All turbocharging concepts can achieve the target
full load at sea level thanks to the CMR and EGR strategy.

– NOx Emission: Low NOx emissions at steady state conditions are
secured by targeting a CMR of 2.4 thanks to the characteristics of
hydrogen combustion.

– Efficiency: VGT concept has the best brake thermal efficiency and
FGT has the lowest. 2-stage has efficiency close to VGT at higher engine
speeds. This is mostly related to pumping losses (PMEP). Low pressure
side of the 2-stage turbocharger is more efficient.

– Altitude margin: 2-stage has well enough margin compared to VGT
and FGT. FGT has almost no margin and VGT is limited at medium
speed in terms of compressor outlet temperature and turbocharger
speed. To conclude, 2 stage has the most margin, followed by VGT and
FGT, respectively.

From the conclusions drawn here, following applications can be
supported with different charging strategies as shown in Table 3.

As a next step, analyses for high altitude and transient load step can
be performed for all of the concepts to get a clear picture with solid
numbers.

CRediT authorship contribution statement

Onur Barış: Formal analysis, Conceptualization, Investigation,
Writing – original draft. İlker Güler: Data curation, Draft creation,
Supervising, Writing – review & editing. Anıl Yaşgül: Formal analysis,
Methodology, Visualization.
Fuel 343 (2023) 127983

7

O. Barış et al.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to
influence the work reported in this paper.
Data availability

The data that has been used is confidential.

Acknowledgment

The authors of this paper would like to thank to Abdullah Kılıçaslan
and Taha Küçük and Seher Jiani for their efforts.

References

[1] Population, total. URL https://data.worldbank.org/indicator/SP.POP.TOTL.
[2] Ritchie H, Roser M, Rosado P. Greenhouse gas emissions. 2020, URL https:
//ourworldindata.org/greenhouse-gas-emissions.

[3] Al-Ghussain L. Global warming: Review on driving forces and mitigation. Environ
Prog Sustain Energy 2019;38(1):13–21.

[4] Sandaka BP, Kumar J. Alternative vehicular fuels for environmental decarbonization:
a critical review of challenges in using electricity, hydrogen, and biofuels
as a sustainable vehicular fuel. Chem Eng J Adv 2023;100442.
[5] Novella R, Pastor J, Gomez-Soriano J, Bayona JS. Challenges and directions of
using ammonia as an alternative fuel for internal combustion engines. 2023.
[6] Hua Y. Ethers and esters as alternative fuels for internal combustion engine: A
review. Int J Engine Res 2023;24(1):178–216.

[7] Kahraman E, Ozcanlı SC, Ozerdem B. An experimental study on performance
and emission characteristics of a hydrogen fuelled spark ignition engine. Int J
Hydrogen Energy 2007;32(12):2066–72.

[8] White C, Steeper R, Lutz A. The hydrogen-fueled internal combustion engine: a
technical review. Int J Hydrogen Energy 2006;31(10):1292–305.
[9] Stockhausen WF, Natkin RJ, Kabat DM, Reams L, Tang X, Hashemi S,
Szwabowski SJ, Zanardelli VP. Ford P2000 hydrogen engine design and vehicle
development program. Tech. rep., SAE Technical Paper; 2002.
[10] Kiesgen G, Klüting M, Bock C, Fischer H. The new 12-cylinder hydrogen engine
in the 7 series: the H2 ICE age has begun. Tech. rep., SAE Technical Paper;
2006.

[11] Ma D-S, Sun Z. Progress on the studies about nox emission in PFI-H2ICE. Int J
Hydrogen Energy 2020;45(17):10580–91. http://dx.doi.org/10.1016/j.ijhydene.
2019.11.065.

[12] Verhelst S, Maesschalck P, Rombaut N, Sierens R. Increasing the power output
of hydrogen internal combustion engines by means of supercharging and exhaust
gas recirculation. Int J Hydrogen Energy 2009;34(10):4406–12.
[13] Pauer T, Weller H, Schünemann E, Eichlseder H, Grabner P, Schaffer K. H2 ICE
for future passenger cars and light commercial vehicles. In: Proceedings of the
41th international vienna motor symposium, Vienna, Austria. 2020, p. 22–4.
[14] Wallner T. Efficiency and emissions potential of hydrogen internal combustion
engine vehicles. 2011.

[15] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH, Medwell PR, Chan QN.
A review of hydrogen direct injection for internal combustion engines: towards
carbon-free combustion. Appl Sci 2019;9(22):4842.
[16] Duan J, Liu F, Sun B. An experimental study on the NOx emission characteristics
of PFI hydrogen internal combustion engine. Automot Eng 2014;36(10):1175–9.
[17] Heywood JB. Internal combustion engine fundamentals. McGraw-Hill Education;
2018.

[18] Rana KK, Natarajan S, Jilakara S. Potential of hydrogen fuelled IC engine to
achieve the future performance and emission norms. 2015.
[19] Wallner T. Development of combustion concepts for a hydrogen powered internal
combustion engine (Diss. Ph. D. Thesis), Graz University of Technology; 2004.
[20] Huyskens P, Van Oost S, Goemaere P, Bertels K, Pecqueur M. The technical
implementation of a retrofit hydrogen PFI system on a passenger car. Tech. rep.,
SAE Technical Paper; 2011.

[21] Holladay JD, Hu J, King DL, Wang Y. An overview of hydrogen production
technologies. Catal Today 2009;139(4):244–60.

[22] Krishnamoorthi M, Malayalamurthi R, He Z, Kandasamy S. A review on
low temperature combustion engines: Performance, combustion and emission
characteristics. Renew Sustain Energy Rev 2019;116:109404.
[23] Feneley AJ, Pesiridis A, Andwari AM. Variable geometry turbocharger technologies
for exhaust energy recovery and boosting-A Review. Renew Sustain Energy
Rev 2017;71:959–75.

[24] Dahham RY, Wei H, Pan J. Improving thermal efficiency of internal combustion
engines: Recent progress and remaining challenges. Energies 2022;15(17):6222.
[25] Cheong J, Cho S, Kim C. Effect of variable geometry turbocharger on HSDI diesel
engine. Tech. rep., SAE Technical Paper; 2000.

[26] Choi C, Kwon S, Cho S. Development of fuel consumption of passenger diesel
engine with 2 stage turbocharger. Tech. rep., SAE Technical paper; 2006.
[27] Morel T, Keribar R. A model for predicting spatially and time resolved convective
heat transfer in bowl-in-piston combustion chambers. SAE Trans 1985;77–93.
[28] Kufferath A, Schünemann E, Krüger M, Krüger M, Jianye S, Eichlseder H, Koch T.
H2 ICE Powertrains for future on-road mobility. In: Proceedings of the 42nd
international vienna motor symposium, Vienna, Austria. 2021, p. 29–30.
[29] Sommermann A, Hinrichsen F, Malischewski T, Hyna D, Karl C, Schmitt J,
McMackin M, Bec H. MAN H45 hydrogen engine: a robust and highly efficient
technology for CO2-neutral mobility. In: 18th symposium sustainable mobility,
transport and power generation. 2021.

[30] Boretti A. Hydrogen internal combustion engines to 2030. Int J Hydrogen Energy
2020;45(43):23692–703.

[31] Schutting E, Roiser SG, Eichlseder H, Lux S, Kleiber S. Hydrogen engine exhaust
aftertreatment. In: Proceedings of the international vienna motor symposium
2022. Österreichischer Verein für Kraftfahrzeugtechnik; 2022.
[32] Bekdemir C, Doosje E, Seykens X. H2-ICE technology options of the present and
the near future. Tech. rep., SAE Technical Paper; 2022.
[33] Verhelst S, De Landtsheere J, De Smet F, Billiouw C, Trenson A, Sierens R.
Effects of supercharging, EGR and variable valve timing on power and emissions
of hydrogen internal combustion engines. SAE Int J Engines 2009;1(1):647–56.
[34] Linemburg HdF, et al. Zero-dimensional model with a wiebe function and shifting
chemical equilibrium for spark ignited combustion engines. 2017.
[35] Raser B, Kapus P, Grabner P, Arnberger A, Heindl R, Egert M, Kunder N,
Weissbäck M, Fraidl G. High efficiency hydrogen internal combustion engine:
Carbon free powertrain for commercial vehicles and passenger cars. In: 2022
JSAE annual congress (Spring). 2022.