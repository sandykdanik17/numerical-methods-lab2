"""
Метод LU-розкладу.
Хто робить: Саша

Що зробити:
  1) перевірити, що головні мінори Δ1..Δ4 не дорівнюють нулю;
  2) знайти L (нижньотрикутна, на діагоналі 1) і U (верхньотрикутна), A = L*U;
  3) розв'язати Ly = b (згори вниз), потім Ux = y (знизу вгору);
  4) надрукувати L, U, y.
"""
from data import A, b
from utils import copy_matrix, print_matrix, print_vector, check_solution


def det(M):
    """Визначник матриці (розклад за першим рядком)."""
    n = len(M)
    if n == 1:
        return M[0][0]
    total = 0.0
    for j in range(n):
        if M[0][j] == 0:
            continue
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        total += (-1) ** j * M[0][j] * det(minor)
    return total


def lu(A, b):
    """Розв'язує Ax = b. Друкує проміжні кроки, повертає список x = [x1, x2, x3, x4]."""
    n = len(A)

    # копіюємо вхідні дані, щоб не міняти A з data.py
    M = copy_matrix(A)
    v = [float(vi) for vi in b]

    # 1) головні мінори D1..Dn мають бути ненульовими
    print("Головні мінори системи:")
    for k in range(1, n + 1):
        delta = det([row[:k] for row in M[:k]])
        print(f"  D{k} = {delta:.6f}")
        if abs(delta) < 1e-12:
            raise ValueError(f"Головний мінор D{k} = 0, LU-розклад неможливий")
    print()

    # 2) A = L*U (алгоритм Дулліта, без перестановок рядків)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1.0

    for k in range(n):
        # рядок k матриці U
        for j in range(k, n):
            U[k][j] = M[k][j] - sum(L[k][m] * U[m][j] for m in range(k))
        # стовпець k матриці L
        for i in range(k + 1, n):
            L[i][k] = (M[i][k] - sum(L[i][m] * U[m][k] for m in range(k))) / U[k][k]

    print_matrix(L, "Матриця L (нижньотрикутна, на діагоналі 1):")
    print_matrix(U, "Матриця U (верхньотрикутна):")

    # 3) Ly = b — прямий хід (згори вниз)
    y = [0.0] * n
    for i in range(n):
        y[i] = v[i] - sum(L[i][j] * y[j] for j in range(i))
    print_vector("y", y)
    print()

    #    Ux = y — зворотний хід (знизу вгору)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return x


if __name__ == "__main__":
    x = lu(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
