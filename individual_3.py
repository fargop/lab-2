n = 10
while n < 100:
    s = (n // 10) + (n % 10)
    if s + s**2 == n:
        print(n)
    n += 1
