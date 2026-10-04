"""
Матричний метод: x = A^-1 * b.
Хто робить: Степан

Що зробити:
  1) дописати до A одиничну матрицю E: (A | E);
  2) перетвореннями рядків (з вибором головного елемента) звести ліву частину до E —
     справа вийде A^-1;
  3) надрукувати A^-1 і обчислити x = A^-1 * b.
"""
from data import A, b
from utils import copy_matrix, print_matrix, print_vector, check_solution


def inverse_matrix(A):
    """Знаходить A^-1 методом Гаусса-Жордана з вибором головного елемента."""
    n = len(A)
    M = copy_matrix(A)
    # одинична матриця E
    E = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for k in range(n):
        # вибір головного елемента у стовпці k (як у методі Гаусса)
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        if M[p][k] == 0:
            raise ValueError("det(A) = 0: оберненої матриці не існує")
        M[k], M[p] = M[p], M[k]
        E[k], E[p] = E[p], E[k]

        # ділимо рядок на головний елемент — на діагоналі з'являється 1
        pivot = M[k][k]
        M[k] = [t / pivot for t in M[k]]
        E[k] = [t / pivot for t in E[k]]

        # обнуляємо стовпець k у ВСІХ інших рядках (і вище, і нижче)
        for i in range(n):
            if i != k:
                factor = M[i][k]
                M[i] = [M[i][j] - factor * M[k][j] for j in range(n)]
                E[i] = [E[i][j] - factor * E[k][j] for j in range(n)]

    return E


def multiply(Minv, b):
    """Множення матриці на вектор: (A^-1 * b)_i = Σ_j A^-1[i][j] * b[j]."""
    n = len(Minv)
    return [sum(Minv[i][j] * b[j] for j in range(n)) for i in range(n)]


def matrix_method(A, b):
    """Розв'язує Ax = b за формулою x = A^-1 * b. Повертає список x."""
    A_inv = inverse_matrix(A)
    print_matrix(A_inv, "Обернена матриця A^-1:", digits=6)

    x = multiply(A_inv, b)
    print("x = A^-1 * b")
    return x


if __name__ == "__main__":
    print("МАТРИЧНИЙ МЕТОД\n")
    x = matrix_method(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
