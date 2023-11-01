ASSIGNMENT NO 10 - APPLICATION OF PYTHON IN THE FIELD OF DESIGN OF STEEL STRUCTURE


Q-1

# Design of tension member
Tu=float(input("Enter the value of ultimate tensile strength:")) fy=float(input("Enter the value of yield strength of steel:"))
fu= float(input("Enter the value of ultimate strength of steel:")) fub=float(input("Enter the value of ultimate strength of bolt:"))
Gamma_mo= float(input("Enter the value of partial factor of safety Garmma mo:")) Gamma_m1= float(input("Enter the value of partial factor of safety Garmma_m1:")) Gamma_mb= float(input("Enter the value of partial factor of safety Gamma_mb:")) print("Gross Area Required")
Agreq=1.1*Tu*1000/fy
print("The value of gross area required is:", 1.2*Agreq) #Selection of section
#Selecting ISA 100x65x8
Ag= float(input("Enter the value of gross area of steel is:")) Lcl= float(input("Enter the length of connected leg:"))
Lol= float(input("Enter the length of outstand leg:")) t= float(input("Entert the value of least thickness: "))
Ag= 1257
#Design of connections
d= float(input("Enter the value of diameter of bolt:")) do=d+2
print("The diameter of bolt hole is:", do) # As per IS code minimum pitch distance is pmin =2.5*d
print("The minimum pitch is:", pmin) #Edge distance as per IS 800 is
e=1.5*do
print("Enter the value of edge distance:", e)
nn=float(input("Number of shear planes with threaded intercepting the shear plane:")) ns= float(input("Number of shear plane without threads:"))
Anb=0.78*0.7854*d*d
print("threaded area of bolt is:", Anb)
Asb=0.7854*d*d
print("plane shank area of bolt is:", Asb)
Vdsb=(fub/(1.732*Gamma_mb)*(nn*Anb+ns*Asb)*10**-3) print("The value of Vdsb:", Vdsb)
kb1=e/(3*do)
print("Kb1:", kb1)
kb2=(pmin/(3*do))-0.25 print("Kb2:", kb2)
kb3=fub/fu
print("Kb3:", kb3) kb4 = 1
print("Kb4:", kb4)
kb= min(kb1,kb2,kb3,kb4) print("Kb:", kb)
Vdpb=(2.5*kb*d*t*fu*10**-3)/Gamma_mb print("Vdpb:", Vdpb)
Vd = min(Vdsb ,Vdpb) print("Vd:", Vd)
N=Tu/Vd
print("Number of bolts requird:", N)
N= float(input("Enter the value of number of bolts:")) # Check for strength
# Criteria 1 Yeilding of Gross Section Tdg=(Ag*fy*10-3)/Gamma_mo
print("The value of tensile strength due to yielding of gross section is:", Tdg) # Criteria 2 Rupture
Anc = (Lcl-(t/2)-do)*t
print("Net Area of Connecting leg is: (Anc):", Anc)
Ago=(Lol-(t/2))*t
print("Gross Area of outstand leg is: (Anc):", Ago)
Lc=(N-1)*pmin
print("Le:", Lc)
bs=(0.6*Lcl)+(Lol*t) print("bs:", bs)
Beta1=((fu/Gamma_m1)*(fy/Gamma_mo)) print("Beta:1", Beta1)
Beta2=(1.4-(0.076*(fy/fu)*(bs/Lc)*(Lol/t))) print("Beta:2", Beta2)
Beta=min(Beta1,Beta2) print("Beta:",Beta) print("Check 1")
if Beta>1.4:
print("Not Safe") else:
 
 
 

    Enter the value of ultimate tensile strength:225 Enter the value of yield strength of steel:250
Enter the value of ultimate strength of steel:410 Enter the value of ultimate strength of bolt:400
Enter the value of partial factor of safety Garmma mo:1.1 Enter the value of partial factor of safety Garmma_m1:1.25 Enter the value of partial factor of safety Gamma_mb:1.25 Gross Area Required
The value of gross area required is: 1188.0
Enter the value of gross area of steel is:1257 Enter the length of connected leg:100
Enter the length of outstand leg:65
Entert the value of least thickness: 8 Enter the value of diameter of bolt:20 The diameter of bolt hole is: 22.0
The minimum pitch is: 50.0
Enter the value of edge distance: 33.0
Number of shear planes with threaded intercepting the shear plane:1 Number of shear plane without threads:0
threaded area of bolt is: 245.0448
plane shank area of bolt is: 314.16
The value of Vdsb: 45.273866050808316 Kb1: 0.5
Kb2: 0.5075757575757576
Kb3: 0.975609756097561
Kb4: 1
Kb: 0.5
Vdpb: 65.6
Vd: 45.273866050808316
Number of bolts requird: 4.969754510195687 Enter the value of number of bolts:5
The value of tensile strength due to yielding of gross section is: 2856815.454545454 Net Area of Connecting leg is: (Anc): 592.0
Gross Area of outstand leg is: (Anc): 488.0
Le: 200.0
bs: 580.0
Beta:1 74545.45454545454
Beta:2 0.30807926829268273
Beta: 0.30807926829268273
Check 1 Safe
Check 2
Not Safe
'Tdn: 208927.19157427934
Avg: 1864.0
Avn: 2656.0
Atg: 480.0
Atn: 5280.0
Tb1: 246152.399439009
Tb2: 452794.5412555112
Tb 246152.399439009
Td 246152.399439009 SAFE
