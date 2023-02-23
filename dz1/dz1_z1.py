def func():
    try:
        x1, x2, x3 = [int(x) for x in input("Введите три числа: ").split()]
    except ValueError:
        print("Числа должны быть целыми")
        return 1
    while True:
        try:
            op = int(input("1 - Сложение\n2 - Умножение\n"))
        except ValueError:
            continue
        if op == 1:
            print(x1 + x2 + x3)
            break
        if op == 2:
            print(x1 * x2 * x3)
            break
        else:
            continue


while func():
    pass
