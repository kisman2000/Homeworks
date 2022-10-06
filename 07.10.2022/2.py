height = int(input("Height: "))
upperValueOfADay = int(input("Upper value of a day: "))
lowerValueOfADay = int(input("Lower value of a day: "))

print("")

valueOfADay = upperValueOfADay - lowerValueOfADay

days = height // valueOfADay

print("Days:", days)
