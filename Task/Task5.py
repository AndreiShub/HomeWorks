option = 5
aq_num = 3
fish_name = ""
counter_1 = 0
counter_2 = 0
aquarium_1 = ["Рыбка1", "Рыбка2", "Рыбка3"]
aquarium_2 = ["Рыбка4", "Рыбка5", "Рыбка6"]

print("Выберите действие:")
print("1 - Показать рыбок")
print("2 - Пересадить в другой аквариум")
print("3 - Покормить рыбок")
print("0 - Выход")
while option != 0:
    try:
        option = int(input())
    except ValueError:
        print("Ошибка: Введите число")
    if option == 0:
        print("Выход")
    if option == 1:
        try:
            aq_num = int(input("В каком аквариуме? (1 или 2): "))
        except ValueError:
            print("Ошибка: Введите число")
        else:
            if aq_num == 1:
                print(aquarium_1)
            elif aq_num == 2:
                print(aquarium_2)
            else:
                print("Нет такого аквариума")
    if option == 2:
        fish_name = input("Введите имя рыбки: ")
        if fish_name in aquarium_1:
            aquarium_1.remove(fish_name)
            aquarium_2.append(fish_name)
        elif fish_name in aquarium_2:
            aquarium_2.remove(fish_name)
            aquarium_1.append(fish_name)
        else:
            print("Нет такой рыбки")
    if option == 3:
        try:
            aq_num = int(input("В каком аквариуме? (1 или 2): "))
        except ValueError:
            print("Ошибка: Введите число")
        else:
            if aq_num == 1:
                counter_1 += 1
                counter_2 = 0
                if counter_1 == 3:
                    aquarium_2.pop()
                    print("Рыбка померла")
            elif aq_num == 2:
                counter_2 += 1
                counter_1 = 0
                if counter_2 == 3:
                    aquarium_1.pop()
                    print("Рыбка померла")
            else:
                print("Нет такого аквариума")
    if option < 0 or option > 3:
        print("Ошибка: Выберите действие")