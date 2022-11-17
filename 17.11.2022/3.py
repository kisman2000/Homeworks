from math import sin, pi

a = float(input("Type here X coordinate: "))
b = float(input("Type here Y coordinate: "))



# checking the first zone

if(
    a**2 + b**2 < 1 # checking x**2 + y**2 = 1 function
    and
    b > abs(a) # checking y = -x and y = x functions
) :
    print("The point(",a,";",b,") is in the first zone!")
else :
    print("The point(",a,";",b,") is not in the first zone!")


# checking the second/third zone

if(
    b < 0 # checking collision with X axis
    and
    a**2 + b**2 < 1 # checking x**2 + y**2 = 1 function
    and
    b > -abs(a) # checking y = -x and y = x functions
) :
    zone = "second"

    if(a > 0) :
        zone = "third"
    
    print("The point(",a,";",b,") is in the ",zone," zone!")
else :
    print("The point(",a,";",b,") is not in the second and third zones!")


# checking the fourth zone

if(
    b < 0 # checking collision with X axis
    and
    a**2 + b**2 > 1 # checking x**2 + y**2 = 1 function
    and
    b < -abs(a) # checling collision with y = x and y = -x functions
) :
    print("The point(",a,";",b,") is in the fourth zone!")
else :
    print("The point(",a,";",b,") is not in the fourth zone!")
