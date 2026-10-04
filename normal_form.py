"""
Підготовка системи завдання 2 до ітераційних методів.
Робить: Данік

Що зробити:
  1) normal_form: на діагоналі C стоять 0.14 і 0.05, а мають бути нулі.
     Переносимо c_ii*x_i вліво: (1 - c_ii)*x_i = ..., ділимо рядок і d_i на (1 - c_ii);
  2) matrix_norms: три норми C (за рядками, за стовпцями, евклідова);
  3) stop_tolerance: якщо q <= 0.5 -> eps, інакше (1 - q)/q * eps;
  4) prepare: усе разом, друкує систему і норми.
"""
import math

from data import C, d, EPS


def normal_form(C, d):
    """Повертає (C_new, d_new) — систему x = C_new*x + d_new з нулями на діагоналі."""
    n = len(C)
    C_new = [list(map(float, row)) for row in C]
    d_new = [float(t) for t in d]

    for i in range(n):
        c_ii = C_new[i][i]
        if c_ii != 0:
            print(f"Рядок {i + 1}: c{i + 1}{i + 1} = {c_ii} ≠ 0 -> "
                  f"(1 - {c_ii})·x{i + 1} = ...  -> ділимо рядок на {1 - c_ii:.2f}")
            C_new[i][i] = 0.0
            C_new[i] = [c / (1 - c_ii) for c in C_new[i]]
            d_new[i] /= (1 - c_ii)
    print()
    return C_new, d_new


def matrix_norms(C):
    """
    Три норми матриці C:
      ||C||1 — максимум сум модулів елементів РЯДКІВ;
      ||C||2 — максимум сум модулів елементів СТОВПЦІВ;
      ||C||3 — корінь із суми квадратів усіх елементів.
    """
    n = len(C)
    norm1 = max(sum(abs(C[i][j]) for j in range(n)) for i in range(n))
    norm2 = max(sum(abs(C[i][j]) for i in range(n)) for j in range(n))
    norm3 = math.sqrt(sum(C[i][j] ** 2 for i in range(n) for j in range(n)))
    return norm1, norm2, norm3


def stop_tolerance(q, eps):
    """
    Поріг зупинки ітерацій:
      q <= 0.5         ->  max|x(k) - x(k-1)| <= eps;
      0.5 < q < 1      ->  max|x(k) - x(k-1)| <= (1 - q)/q * eps.
    """
    return eps if q <= 0.5 else (1 - q) / q * eps


def print_system(C, d):
    """Друкує систему у вигляді x_i = ... ."""
    n = len(C)
    for i in range(n):
        terms = " ".join(f"{C[i][j]:+.5f}·x{j + 1}" for j in range(n) if j != i)
        print(f"   x{i + 1} = {terms} {d[i]:+.5f}")
    print()


def prepare(C, d, eps):
    """Повний цикл підготовки. Повертає (C_new, d_new, q, tol)."""
    C_new, d_new = normal_form(C, d)
    print("Нормальний вигляд системи:")
    print_system(C_new, d_new)

    n1, n2, n3 = matrix_norms(C_new)
    print(f"||C||1 = {n1:.4f}   ||C||2 = {n2:.4f}   ||C||3 = {n3:.4f}")
    # Беремо норму за рядками: саме з нею узгоджена умова зупинки max|Δ|
    q = n1
    if q >= 1:
        raise ValueError("q >= 1: достатня умова збіжності не виконується")
    tol = stop_tolerance(q, eps)
    print(f"q = ||C||1 = {q:.4f} < 1 -> методи збігаються")
    print(f"Умова зупинки: max|x(k) - x(k-1)| <= {tol:.3e}\n")
    return C_new, d_new, q, tol


if __name__ == "__main__":
    prepare(C, d, EPS)
