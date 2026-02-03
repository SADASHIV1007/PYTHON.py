lst = []   

n = int(input("Enter number : "))

for i in range(n):
    ch = input("Enter R/W/U/D: ")

    if ch == 'W':
        x = int(input("Enter number: "))
        lst.append(x)

    elif ch == 'R':
        print(lst)

    elif ch == 'U':
        p = int(input("Enter index: "))
        x = int(input("Enter new value: "))
        lst[p] = x

    elif ch == 'D':
        p = int(input("Enter index: "))
        lst.pop(p)

    else:
        print("Wrong choice")
