"""
Метод Зейделя.
Хто робить: Данік

Що зробити:
  те саме, що Якобі, але при обчисленні x_i(k) одразу беремо вже знайдені
  на цьому кроці x_1(k), ..., x_{i-1}(k).
"""
from data import C, d, EPS
from normal_form import prepare


def seidel(C, d, tol, maxiter=1000):
    """Повертає (x, кількість ітерацій). Друкує таблицю: k | x1..x4 | max|Δ|."""
    raise NotImplementedError


if __name__ == "__main__":
    C_new, d_new, q, tol = prepare(C, d, EPS)
    x, k = seidel(C_new, d_new, tol)
    print("x =", [round(v, 4) for v in x], " ітерацій:", k)
