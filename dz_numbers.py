import itertools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
options = ["+", "-", None]

for i in itertools.product(options, repeat = 8):
    copy = [i for i in numbers]
    for count, j in enumerate(i):
        copy.insert(count * 2 + 1, j)
    equation = ""
    for i in copy:
        if i != None:
            equation += str(i)
    result = eval(equation)
    if result == 100:
        equation_list = []
        for i in equation:
            if i == "+" or i == "-":
                equation_list.append(" ")
                equation_list.append(i)
                equation_list.append(" ")
            else:
                equation_list.append(i)
        print(f"{''.join(str(x) for x in equation_list)} = {result}")
