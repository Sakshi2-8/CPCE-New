ASSIGNMENT NO 4 - APPLICATION OF PYTHON IN FIELD OF CONCRETE TECHNOLOGY


Q-1

fck = float(input(" Enter the value of characteristic compressive strength:")) # Experimental Determinations
Gca = float(input ("Enter the value of specific gravity of CA:")) Gfa = float(input("Enter the value of specific gravity of FA:"))
Gc = float(input("Enter the value of specific gravity of Cement:")) Water_Density = float(input("Enter the value of Water Density:"))
AGG_Size = float(input("Enter the nominal Size of Aggregate:")) Nature_of_AGG = input("Nature of Aggregates:")
Slump = float(input("Enter the value of workability of concrete:")) Admixture = input("Type of Admixture:")
Exposure_Condition = input("Exposure Condition:") Concreting = input("Type of Concreting:")
Zone = int(input("Zone:")) # Target Mean Strength
sigma = {10:3.5,15:3.5,20: 4,25:4,30: 5,35: 5,40: 5,45: 5,50: 5,55: 5}
ft=fck+sigma[fck]*1.65
print("Target Mean Strength:",ft,"MPa") # Maximum free Water Cement Ratio
# Reference IS 456: 2000 Table 5 if(Concreting == "Plain"):
WC_ratio = {"Mild" : 0.6,"Moderate" :0.6,"Severe" :0.5,"Very Severe" :0.45, "Extreme":0.4}
else:
WC_ratio ={"Mild": 0.55,"Moderate":0.5,"Severe" :0.45,"Very Severe" :0.45, "Extreme":0.4}
print("W/C Ratio:",WC_ratio[Exposure_Condition] ) WC_ratio = WC_ratio[Exposure_Condition]
# Minimum Cement Content
if(Concreting == "plain"):
Min_Cement_Content = {"Mild":220,"Moderate": 240,"Severe": 250,
"Very Severe": 260,"Extreme": 280}
else:
Min_Cement_Content = {"Mild":300,"Moderate": 300,"Severe": 320,
"Very Severe": 340,"Extreme": 360}
print("Minmum Cement Content:", Min_Cement_Content[Exposure_Condition],"kg/m^3") # Water Content
Water_Content={10:208,20:186,40:165}
Water_Content = Water_Content[AGG_Size] if (Slump == 75):
Water_Content = Water_Content + Water_Content*0.03 elif (Slump == 100):
Water_Content = Water_Content + Water_Content*0.06 elif (Slump == 125):
Water_Content = Water_Content + Water_Content*0.09 elif (Slump == 150):
Water_Content = Water_Content + Water_Content*0.12 elif (Slump == 175):
Water_Content = Water_Content + Water_Content*0.15 elif (Slump == 200):
Water_Content = Water_Content + Water_Content*0.18 if (Nature_of_AGG == "Sub-Angular"):
Water_Content = Water_Content - 10 elif (Nature_of_AGG == "Gravel"):
Water_Content = Water_Content - 20 elif (Nature_of_AGG == "Round"):
Water_Content = Water_Content - 25 if (Admixture == "Plastisizer"):
Water_Content = Water_Content-(0.1*Water_Content) elif (Admixture=="Super-plastisizer"):
Water_Content = Water_Content-(0.2*Water_Content) print("Water Content:", Water_Content, "kg/m^3") # Cement Content
Cement_Content = Water_Content/WC_ratio
print("CementContent:", Cement_Content, "kg/m^3")
print("As Per IS 456:2000, Maximum allowed Cement Content is 450 kg/m^3")

if (Cement_Content< 450):
Cement_Content = Cement_Content else:
Cement_Content = 450

if Cement_Content< 450: print("Safe")
 
 
 

      Enter the value of characteristic compressive strength:40 Enter the value of specific gravity of CA:74
Enter the value of specific gravity of FA:74
Enter the value of specific gravity of Cement:3.15 Enter the value of Water Density:1000
Enter the nominal Size of Aggregate:20
Nature of Aggregates:Sub-Angular
Enter the value of workability of concrete:100 Type of Admixture:Super-Plastisizer
Exposure Condition:Severe
Type of Concreting:Reinforced Zone:1
Target Mean Strength: 48.25 MPa W/C Ratio: 0.45
Minmum Cement Content: 320 kg/m^3 Water Content: 187.16 kg/m^3
CementContent: 415.9111111111111 kg/m^3
As Per IS 456:2000, Maximum allowed Cement Content is 450 kg/m^3 Safe
Volume of Cemnet: 0.1320352733686067 m^3
Volume of Water: 0.18716 m^3
Volume of Course Aggregates and Fine Aggregates: 0.6808047266313932 m^3 Course Aggregate fraction: 0.606
Volume of Course Aggregate: 0.4125676643386243 m^3 Volume of Fine Aggregate: 0.26823706229276895 m^3
Mass of Course Aggregates: 30530.007161058198 Kg/m^3
Mass of Fine Aggregates: 19849.542609664903 kg/m^3 Weight Batching
1.0 : 47.72544440237875 : 73.40512514680589 : 0.45
Volume Batching:
1.0 : 2.0315560792904463 : 3.1246776244924126 : 1.4174999999999998
