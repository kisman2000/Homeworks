secondsRaw = int(input("Seconds: "))

print("")

hours = secondsRaw // (60 * 60)
minutes = (secondsRaw - (hours * 60 * 60)) // 60
seconds = secondsRaw % 60

print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)
