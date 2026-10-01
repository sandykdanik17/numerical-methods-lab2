"""
Спільні допоміжні функції, якими користуються всі методи.
"""


def copy_matrix(M):
    """Повертає копію матриці, щоб методи не змінювали вихідні дані з data.py."""
    return [list(map(float, row)) for row in M]


def print_matrix(M, title=None, aug=None, digits=4):
    """
    Друкує матрицю рядок за рядком.
    aug — стовпець правих частин: якщо його передати, друкується
          розширена матриця (A | b) з вертикальною рискою.
    """
    if title:
        print(title)
    for i, row in enumerate(M):
        line = "  ".join(f"{v:>10.{digits}f}" for v in row)
        if aug is not None:
            line += f"  | {aug[i]:>10.{digits}f}"
        print("  [" + line + " ]")
    print()


def print_vector(name, x, digits=6):
    """Друкує вектор у вигляді name = (x1; x2; ...)."""
    print(f"{name} = (" + "; ".join(f"{v:.{digits}f}" for v in x) + ")")


def check_solution(A, b, x):
    """
    Перевірка розв'язку: підставляємо x у кожне рівняння системи
    і дивимось, наскільки ліва частина відрізняється від правої.
    Повертає максимальну нев'язку max|Ax - b|.
    """
    n = len(A)
    residual = 0.0
    for i in range(n):
        left = sum(A[i][j] * x[j] for j in range(n))
        residual = max(residual, abs(left - b[i]))
    print(f"Перевірка: max|Ax - b| = {residual:.2e}\n")
    return residual
