x = input()

print(f"Цифры: {sum(i.isdigit() for i in x)}")
print(f"Буквы: {sum(i.isalpha() for i in x)}")