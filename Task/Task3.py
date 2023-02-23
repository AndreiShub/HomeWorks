try:
    x = int(input())
    y = int(input())
except ValueError:
    print("Invalid input")
else: 
    print(str(x / y) + " километров в час")