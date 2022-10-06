firstHours = int(input("First hours: "))
firstMins = int(input("First minutes: "))
firstSecs = int(input("First seconds: "))

print("")

secondHours = int(input("Second hours: "))
secondMins = int(input("Second minutes: "))
secondSecs = int(input("Second seconds: "))

print("")
print("")

hoursDifferentInHours = secondHours - firstHours
hoursDifferentInMins = hoursDifferentInHours * 60
hoursDifferentInSecs = hoursDifferentInMins * 60

minsDifferentInMins = abs(secondMins - firstMins)
minsDifferentInSecs = minsDifferentInMins * 60

if(firstMins > secondMins) :
    minsDifferentInSecs = -minsDifferentInSecs

secsDifferentInSecs = abs(secondSecs - firstSecs)

if(firstSecs > secondSecs) :
    secsDifferentInSecs = -secsDifferentInSecs
    
finalDifferent = hoursDifferentInSecs + minsDifferentInSecs + secsDifferentInSecs

print("The different is", finalDifferent)
