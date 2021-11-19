my_list = [1, 2, 3]

my_list.append([4, 5, 6])
print(my_list)

my_list.extend([7, 8, 9])
print(my_list)

my_list.insert(3, "szilva")
print(my_list)

del(my_list[3])
print(my_list)

my_list = [3, 6, 3, 8, 1, 4, 11, 0]

my_list_copy = my_list.copy()
my_list2 = my_list
print("my_list", my_list)
print("my_list2", my_list2)
print("my_list_copy", my_list_copy)

my_list.sort()
print("my_list", my_list)
print("my_list2", my_list2)
print("my_list_copy", my_list_copy)

print("Sort reverse")
my_list.sort(reverse=True)
print("my_list", my_list)
print("my_list2", my_list2)
print("my_list_copy", my_list_copy)

print("Reverse method")
my_list_copy.reverse()
print("my_list", my_list)
print("my_list2", my_list2)
print("my_list_copy", my_list_copy)

my_list_copy2 = sorted(my_list_copy)
print("my_list_copy", my_list_copy)
print("my_list_copy2", my_list_copy2)
