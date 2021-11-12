number = 350
if number > 100:
    print("A szám nagyobb, mint 100.")
else:
    print("A szám nem nagyobb, mint 100")

if number % 2 == 0:
    print("Páros")
else:
    print("Páratlan")

number1 = 9
number2 = 3
if number1 % number2 == 0 or number2 % number1 == 0:
    print("Az egyik szám osztható a másikkal.")
else:
    print("Az egyik szám nem osztható a másikkal.")

radar = "radar"
if radar[0] == radar[-1]:
    print("Első utolsó ugyanaz")
else:
    print("Első utolsó nem ugyanaz")

a = -5
if a>0:
    print("Pozitív.")
elif a<0:
    print("Negatív.")
else:
    print("Nulla")

nums = [2, 1, 8]
nums.sort()
print(nums)

a = 3
b = 4
c = 5
if a+b>c and b+c>a and a+c>b:
    print("Szerkeszthető 3szög")
else:
    print("Nem szerkeszthető 3szög")

grade = 4
grades = ["Elégtelen", "Elégséges", "Közepes", "Jó", "Jeles"]
print(grades[grade-1])

szam = input()
if szam.isnumeric():
    szam = int(szam)
    print(szam*3)
else:
    print("Nem szám.")
"""if (type(szam)) == int:
    print(szam*3)
else:
    print("Nem szám")"""
