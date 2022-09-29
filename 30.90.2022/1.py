a = int(input("Рубли: "))
b = int(input("Копейки: "))

print("")

c = int(input("Сколько: "))

print("")
print("")

d = a * c
f = b * c

e = f % 100
g = f // 100

d = d + g

print("К оплате ", d, " рублей ", e, " копеек") 
