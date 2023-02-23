def func():
    try:
        x = float(input("Введите число метров: "))
    except ValueError:
        return 1
    while True:
        try:
            op = int(input("1 - В мили\n2 - В дюймы\n3 - В ярды\n"))
        except ValueError:
            continue
        if op == 1:
            print(x / 1609)
            break
        if op == 2:
            print(x * 39.37)
            break
        if op == 3:
            print(x * 1.094)
            break
        else:
            continue


while func():
    pass
