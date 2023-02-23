import random

answer = [random.randint(0,9) for i in range(4)]
guess = []
counter = 0

def get_guess():
    try:
        guess = [int(i) for i in input("Введите 4-х значное число: ")]
        if len(guess) != 4:
            raise RuntimeError
    except ValueError:
        print("Не число!")
        return get_guess()
    except RuntimeError:
        print("Не 4-х значное число!")
        return get_guess()
    else:
        return guess

def check_guess(answer, guess):
    bulls = 0
    cows = 0
    for i in answer:
        if i in guess:
            bulls += 1
    for i, j in enumerate(answer):
        if j == guess[i]:
            cows += 1
    return bulls, cows


while guess != answer:
    counter += 1
    guess = get_guess()
    if guess == answer:
        break
    else:
        bulls, cows = check_guess(answer, guess)
        print(f"Цифр числа угадано, Быки: {bulls}")
        print(f"Цифр числа угадано на нужном месте, Коровы: {cows}")
print("Угадали число: ", end="")
for i in answer:
    print(i, end="")
print(f" Попыток: {counter}")
    
