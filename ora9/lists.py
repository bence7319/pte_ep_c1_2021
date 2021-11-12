my_list = [1, 2.5, "alma", False]
print(len(my_list))
print(2 in my_list)
print(my_list.index(2.5))
try:
    print(my_list.index(2))
except ValueError:
    print("Nincs a listában.")
print(my_list[0])
print(my_list[-1])
print(my_list[0:2])
