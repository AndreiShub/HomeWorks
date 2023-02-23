def podvig():
    str = input()
    new_str = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_str += str[i].lower()
        if i % 2 == 1:
            new_str += str[i].upper()
    print(new_str)
podvig()