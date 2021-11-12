number = 0
isNumber = False
while not isNumber:
    try:
        number = int(input("Kérek egy egész számot: "))
        isNumber = True
    except ValueError:
        print("Nem egy egész szám")

if number % 2 == 0:
    print("Páros.")
else:
    print("Páratlan.")

i = 1
while i < 5:
    print(i)
    i += 1
for j in [1, 2, 3, 4, 5]:
    print(j)
for k in range(100):
    print(k, end=" ")
