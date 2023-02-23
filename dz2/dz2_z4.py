def calc(n):
    if n < 500:
        return n * 0.03 + 200
    if n < 1000:
        return n * 0.05 + 200
    if n >= 1000:
        return n * 0.08 + 200


list = [int(x) for x in input("Введите числа: ").split()]
index = list.index(max(list))
result = [calc(e) for e in list]
result[index] += 200
for r in range(len(result)):
    print(f"{result[r]}$")


