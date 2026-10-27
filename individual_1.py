n = int(input())

if n % 10 == 1 and n != 11:
    print(f"Мы успешно сдали {n} экзамен")
elif n % 10 in (2, 3, 4) and n not in (12, 13, 14):
    print(f"Мы успешно сдали {n} экзамена")
else:
    print(f"Мы успешно сдали {n} экзаменов")
