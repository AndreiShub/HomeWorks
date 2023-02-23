try:
    x = int(input())
    y = int(input())
except ValueError:
    print("Invalid input")
else:    
    if x == y:
        print("Числа равны")
    else:
        print(max(x,y))

