import random

list_1 = [random.randint(0, 100) for _ in range(5)]
list_2 = [random.randint(0, 100) for _ in range(5)]

list_all = []
list_all.extend(list_1)
list_all.extend(list_2)

list_unique = []
for i in list_all:
    if i not in list_unique:
        list_unique.append(i)

list_common = [i for i in list_1 if i in list_2]

list_maxmin = [max(list_all), min(list_all)]

print(list_1, list_2)
print(list_all)
print(list_unique)
print(list_common)
print(list_maxmin)