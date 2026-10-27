a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if a1 == 0 and b1 == 0:
    print("Первое уравнение не задает прямую")
elif a2 == 0 and b2 == 0:
    print("Второе уравнение не задает прямую")
else:
    D = a1 * b2 - a2 * b1
    if D != 0:
        x = (b1 * c2 - b2 * c1) / D
        y = (a2 * c1 - a1 * c2) / D
        print(f"x = {x}, y = {y}")
    else:
        if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            print("Прямые совпадают")
        else:
            print("Прямые параллельны")
