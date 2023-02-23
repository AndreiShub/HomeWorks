def func():
    try:
        list = [int(x) for x in input("Введите три числа: ").split()]
        if len(list) > 3:
            return 1
    except ValueError:
        print("Числа должны быть целыми")
        return 1
    while True:
        try:
            op = int(input("1 - Максимальное\n2 - Минимальное\n3 - Среднеарифметическое\n"))
        except ValueError:
            continue
        if op == 1:
            print(max(list))
            break
        if op == 2:
            print(min(list))
            break
        if op == 3:
            print(sum(list) / len(list))
            break
        else:
            continue


while func():
    pass
