"""
Метод Зейделя.
Хто робить: Данік

Що зробити:
  те саме, що Якобі, але при обчисленні x_i(k) одразу беремо вже знайдені
  на цьому кроці x_1(k), ..., x_{i-1}(k).
"""
from data import C, d, EPS
from normal_form import prepare
from jacobi import print_row


def seidel(C, d, tol, maxiter=1000):
    """Повертає (x, кількість ітерацій) і друкує таблицю ітерацій."""
    n = len(d)
    x = [0.0] * n                     # початкове наближення x(0) = (0, 0, 0, 0)

    print(f"{'k':>3} | {'x1':>10} {'x2':>10} {'x3':>10} {'x4':>10} | max|Δ|")
    print_row(0, x, None, tol)

    for k in range(1, maxiter + 1):
        x_old = x[:]                  # потрібне лише для обчислення max|Δ|
        for i in range(n):
            # ГОЛОВНА ВІДМІННІСТЬ від Якобі: беремо x (вже частково оновлений),
            # а не x_old, тож x_1..x_{i-1} тут уже нові
            x[i] = d[i] + sum(C[i][j] * x[j] for j in range(n) if j != i)

        delta = max(abs(x[i] - x_old[i]) for i in range(n))
        print_row(k, x, delta, tol)
        if delta <= tol:
            print()
            return x, k

    raise RuntimeError("Метод не зійшовся за maxiter ітерацій")


if __name__ == "__main__":
    print("МЕТОД ЗЕЙДЕЛЯ\n")
    C_new, d_new, q, tol = prepare(C, d, EPS)
    x, k = seidel(C_new, d_new, tol)
    print("x =", [round(v, 4) for v in x], " ітерацій:", k)
