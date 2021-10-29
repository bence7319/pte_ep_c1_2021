python = "python"
print("A python szó 1. kerektere:", python[0])
print("A python szó utolsó kerektere:", python[len(python)-1], python[-1])
print("A python szó 5x:", python*5)

str2 = "hallgató"
str3 = "Hiába a hegynyi anyag, a hallgató gyorsan halad."
print(str2 in str3)
print(python in str3)
print(python not in str3)
print(str3[0:5])
print(python + str2)
print(python, str2)
print(python, str2, sep=" & ")

str4 = "HALLGATÓ"
print(str4 in str3)
print(str4 > str2)
print("\\ \' \"")
print("New\nline")
