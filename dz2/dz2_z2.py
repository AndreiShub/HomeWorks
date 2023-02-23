try:
    x = float(input("Число:"))
    y = float(input("В степень от 0 до 7:"))
except Exception:
    exit()
if y < 0 or y > 7:
    exit()
print(x ** y)