try:
    fileobject = open("lorem.txt", "r")
    print(fileobject.read())
    fileobject.close()
except FileNotFoundError:
    print("Nem található fájl.")