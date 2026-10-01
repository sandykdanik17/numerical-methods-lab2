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


def jacobi(C, d, tol, maxiter=1000):
    """Повертає (x, кількість ітерацій). Друкує таблицю: k | x1..x4 | max|Δ|."""
    raise NotImplementedError


if __name__ == "__main__":
    C_new, d_new, q, tol = prepare(C, d, EPS)
    x, k = jacobi(C_new, d_new, tol)
    print("x =", [round(v, 4) for v in x], " ітерацій:", k)
