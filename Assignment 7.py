ASSIGNMENT NO 7 - APPLICATION OF PYTHON IN THE FIELD OF FOUNDATION ENGINEERING


Q-1

#To Determine the bearing capacity of soil with water table
BulkDensity =float(input("Enter the value of Bulk Density of soil:"))
SatDensity = float(input("Enter the value of Saturated Density of soil:")) WaterDensity = float(input("Enter the unit Weight of Water:"))
Df= float(input("Enter the value of depth of footing:"))
Dw = float(input("Enter the value of water table above footing level:"))
Dw1= float(input("Enter the value of Water table below the level of footing:")) B= float(input("Enter the value of width of footing:"))
Nq= float(input("Enter the vaiue of Nq:"))
N= float(input("Enter the value of N ganna (N):")) SubDensity=float(input())
print("Submerged Weight of soil is:", SubDensity)
#The bearing capacity of soil when water table is at ground print("CASE A")
qu=(SubDensity*Df*Nq)+(0.5*0.8*B*SubDensity*N)
print("The value of ultimate bearing capacity of soil is:", qu) #Approximate calculation of Bearing capacity of soil is.
Rw= 0.5+0.5*(Dw/B)
print("The value of Rw is:", Rw) Rw1=0.5+0.5*(Dw1/8)
print("The value of Rw1 is:", Rw1)
qu=(BulkDensity*Df*Nq*Rw) + (0.5*0.8*8*BulkDensity*N*Rw1)
print("The value ultimate bearing capacity of soil is:", qu) # Case B
print("CASE B")
qu=(BulkDensity*Df*Nq)+(0.5*0.8*8*SubDensity)
print("The value of ultimate bearing capacity is:", qu)
Dw = float(input("Enter the value of water table above footing level:"))
Dw1 = float(input("Enter the value of Water table below the level of footing:")) print("The approximate value of ultimate bearing capacity is: ")
Rw=0.5+0.5*(Dw/B)
print("The value of Rw is:", Rw) Rw1= 0.5 + 0.5* (Dw1/8)
print("The value of Rw1 is:", Rw1)
qu=(BulkDensity*Df*Nq*Rw)+(0.5*0.8*8*BulkDensity*Rw1)
print("The approximate value of ultimate hearing capacity is: ", qu) # Case C
print("CASE C")
x = float(input("Enter the value of depth of water below footing:"))
qu=(BulkDensity*Df*Nq)+(0.5*0.8*((BulkDensity*x)+(SubDensity*(B-x)))*N) print("The value of ultimate bearing capacity is:", qu)
Dw = float(input("Enter the value of water table above footing level:"))
Dw1= float(input("Enter the value of Water table below the level of footing:")) print("The approximate value of ultimate bearing capacity is:")
Rw= 8.5+ 8.5*(Dw/B)
print("The value of Rw is:", Rw) Rw1 = 0.5 + 0.5*(Dw1/8)
print("The value of Rwl is: ", Rw1)
qu= (BulkDensity*Df*Nq*Rw)+(0.5*0.8*8*BulkDensity*N*Rw1) print("the value of ultimate bearing capaciy is:", qu)

    Enter the value of Bulk Density of soil:18
Enter the value of Saturated Density of soil:20 Enter the unit Weight of Water:10
Enter the value of depth of footing:2
Enter the value of water table above footing level:0
Enter the value of Water table below the level of footing:0 Enter the value of width of footing:3
Enter the vaiue of Nq:33
Enter the value of N ganna (N):34 10
Submerged Weight of soil is: 10.0 CASE A
The value of ultimate bearing capacity of soil is: 1068.0 The value of Rw is: 0.5
The value of Rw1 is: 0.5
The value ultimate bearing capacity of soil is: 1573.2 CASE B
The value of ultimate bearing capacity is: 1220.0
Enter the value of water table above footing level:3
Enter the value of Water table below the level of footing:0 The approximate value of ultimate bearing capacity is:
The value of Rw is: 1.0 The value of Rw1 is: 0.5
The approximate value of ultimate hearing capacity is: 1216.8 CASE C
Enter the value of depth of water below footing:1
The value of ultimate bearing capacity is: 1704.8000000000002
 
Enter the value of water table above footing level:3
Enter the value of Water table below the level of footing:1 The approximate value of ultimate bearing capacity is:
The value of Rw is: 17.0
The value of Rwl is: 0.5625
the value of ultimate bearing capaciy is: 21297.6

Q-2

Enter the value of UCS of soil:75
Enter the value of dimension of pile:0.45 Enter the length of pile:15
Enter the value of adhesion factor:0.8 The value of Nc: 9
the Base area of footing is: 0.2025
The value of chohesion of soil is: 37.5 'Qpu: 68.34375
Qf: 810.0
the value of load carring capacity of pile is (Qu): 878.34375

Q-3

 

Enter the value of Bulk Density of soil:18
Enter the value of Saturated Density of soil:20 Enter the unit Weight of Water:10
Enter the value of depth of footing:2
Enter the value of width of footing:3 Enter the value of Ng:33
Enter the value of N gamma (N):34
Submerged Weight of soil is: 10.0
Number of data values of Water table above footing level: 3 Number of data values of Water table below footing level: 3
Enter the value of water table above footing level measured w.r.t. ground (Dw) : 0
The value of Rw is: 0.5
Enter the value of water table above footing level measured w.r.t. ground (Dw) :
 
1
The value of Rw is: 0.6666666666666666
Enter the value of water table above footing level measured w.r.t. ground (Dw) : 2
The value of Rw is: 0.8333333333333333
Enter the value of water table above footing level measured w.r.t. ground (Dw1): 0
The value of Rw1 is: 0.5
'qu: 1357.1999999999998 kN/m^2
Enter the value of water table above footing level measured w.r.t. ground (Dw1): 0
The value of Rw1 is: 0.5
'qu: 1357.1999999999998 kN/m^2
Enter the value of water table above footing level measured w.r.t. ground (Dw1): 1
The value of Rw1 is: 0.6666666666666666 'qu: 1479.6 kN/m^2
