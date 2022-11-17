from math import sin, pi

a = float(input("Type here X coordinate:"))
b = float(input("Type here Y coordinate:"))



# checking the first zone
# вот тут данная проверка немного сломанная

if(
    b < a**2 # checking y = x**2 function
    and
    b > 2 - a**2 # checking y = 2 - x function
) :
    print("The point(",a,";",b,") is in the first zone!")
else :
    print("The point(",a,";",b,") is not in the first zone!")


# checking the second zone

if(
    a < 0 # checking collision with Y axis
    and
    b > a**2 # checking y = x**2 function
    and
    b < 2 - a # checking y = 2 - x function
    and
    b > 4 - a**2 # checking y = 4 - x**2
) :
    print("The point(",a,";",b,") is in the second zone!")
else :
    print("The point(",a,";",b,") is not in the second zone!")


# checking the third zone

if(
    a > 0 # checking collision with Y axis
    and
    b > 4 - a**2 # checking y = 4 - x**2 function
    and
    b > a**2 # checking y = x**2
) :
    print("The point(",a,";",b,") is in the third zone!")
else :
    print("The point(",a,";",b,") is not in the third zone!")


# checking the fourth zone

if(
    b > 0 # checking collision with X axis
    and
    b < a**2 # checking y = x**2 function
    and
    b < 2 - a # checking y = 2 - x function
) :
    print("The point(",a,";",b,") is in the fourth zone!")
else :
    print("The point(",a,";",b,") is not in the fourth zone!")

