from math import sin, pi

a = float(input("Type here X coordinate:"))
b = float(input("Type here Y coordinate:"))

if(
    a**2 + b**2 > 4 # checking x**2 + y**2 = 4 function
    and
    b < a # checking y = x function
    and
    a < 2 # checking x = 2 function
) :
    print("The point(",a,";",b,") is in the zone!")
else :
    print("The point(",a,";",b,") is not in the zone!")
    
