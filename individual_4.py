import sys
import math

def main():
    try:
        x = float(input("Введите x: "))
    except ValueError:
        print("Ошибка ввода", file=sys.stderr)
        sys.exit(1)

    eps = 1e-10
    max_terms = 1000
    
    term = 1.0
    sum_val = term
    k = 0
    remainder_bound = abs(term)

    while remainder_bound > eps and k < max_terms:
        k += 1
        term *= -(x**2) / ((2 * k - 1) * (2 * k))
        sum_val += term
        remainder_bound = abs(term)

    print(f"{sum_val:.10f}")
    print(f"Количество включенных членов: {k + 1}")
    print(f"Оценка остатка: {remainder_bound:e}")

if __name__ == "__main__":
    main()
