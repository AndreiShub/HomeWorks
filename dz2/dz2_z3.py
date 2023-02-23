exit = 1
price = [5, 10 , 15, 20 , 25, 30]
print("1 - Первый оператор")
print("2 - Второй оператор")
print("3 - Третий оператор")
print("4 - Четвертый оператор")
print("5 - Пятый оператор")
print("6 - Шестой оператор")
while exit:
    try:
        op_1 = int(input("Выберите 1 оператора:\n"))
    except ValueError:
        continue
    if op_1 not in [1, 2, 3, 4, 5, 6]:
        continue
    else:
        while exit:
            try:
                op_2 = int(input("Выберите 2 оператора:\n"))
            except ValueError:
                continue
            if op_2 not in [1, 2, 3, 4, 5, 6]:
                continue
            elif op_1 == op_2:
                print("Звонок бесплатный")
                exit = 0
            else:
                print(f"Звонок стоит {price[op_1 - 1] + price[op_2 - 1]} рублей в минуту")
                exit = 0
