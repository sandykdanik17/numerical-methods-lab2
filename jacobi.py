"""
Метод простої ітерації (Якобі).
Хто робить: Данік

Що зробити:
  1) x(0) = (0, 0, 0, 0);
  2) x_i(k) = d_i + Σ_{j≠i} c_ij * x_j(k-1) — нове рахуємо ЛИШЕ через попереднє;
  3) після кожного кроку max|x(k) - x(k-1)|, зупинка коли <= tol.
"""
from data import C, d, EPS
from normal_form import prepare


def print_row(k, x, delta, tol):
    """Один рядок таблиці ітерацій."""
    if delta is None:
        status = "---"
    else:
        status = f"{delta:.6f}" + ("  <= tol" if delta <= tol else "  > tol")
    print(f"{k:>3} | " + " ".join(f"{v:>10.6f}" for v in x) + f" | {status}")


def jacobi(C, d, tol, maxiter=1000):
    """Повертає (x, кількість ітерацій) і друкує таблицю ітерацій."""
    n = len(d)
    x = [0.0] * n                     # початкове наближення x(0) = (0, 0, 0, 0)

    print(f"{'k':>3} | {'x1':>10} {'x2':>10} {'x3':>10} {'x4':>10} | max|Δ|")
    print_row(0, x, None, tol)

    for k in range(1, maxiter + 1):
        x_old = x[:]                  # запам'ятовуємо попереднє наближення
        # нове наближення рахуємо тільки через x_old
        x = [d[i] + sum(C[i][j] * x_old[j] for j in range(n) if j != i) for i in range(n)]

        delta = max(abs(x[i] - x_old[i]) for i in range(n))
        print_row(k, x, delta, tol)
        if delta <= tol:
            print()
            return x, k

    raise RuntimeError("Метод не зійшовся за maxiter ітерацій")


if __name__ == "__main__":
    print("МЕТОД ПРОСТОЇ ІТЕРАЦІЇ (ЯКОБІ)\n")
    C_new, d_new, q, tol = prepare(C, d, EPS)
    x, k = jacobi(C_new, d_new, tol)
    print("x =", [round(v, 4) for v in x], " ітерацій:", k)
