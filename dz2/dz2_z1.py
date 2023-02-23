def fizzBuzz():
    try:
        x = float(input())
    except ValueError:
        return "Ошибка: введите число от 1 до 100"
    if x < 1 or x > 100:
        return "Ошибка: введите число от 1 до 100"
    if x % 3 == 0 and x % 5 == 0:
        return "Fizz Buzz"
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    return x


print(fizzBuzz())