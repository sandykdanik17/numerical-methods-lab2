"""
Метод Гаусса з вибором головного елемента у стовпці.
Хто робить: Тарас

Що зробити:
  1) для кожного стовпця k знайти найбільший за модулем елемент
     (від рядка k донизу) і переставити цей рядок на місце k;
  2) поділити рядок k на головний елемент, обнулити елементи під ним;
  3) друкувати розширену матрицю після кожного кроку (print_matrix(M, None, v));
  4) зворотний хід: знайти x4, x3, x2, x1.
"""
from data import A, b
from utils import copy_matrix, print_matrix, print_vector, check_solution


def gauss(A, b):
    """Розв'язує Ax = b методом Гаусса з вибором головного елемента. Повертає список x."""
    n = len(A)
    M = copy_matrix(A)          # робоча копія матриці
    v = [float(t) for t in b]   # робоча копія правих частин

    print_matrix(M, "Розширена матриця системи:", v)

    # Прямий хід
    for k in range(n):
        # 1) пошук головного елемента у стовпці k
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        print(f"Крок {k + 1}: головний елемент у стовпці {k + 1} — {M[p][k]:g} (рядок {p + 1})")
        if M[p][k] == 0:
            raise ValueError("Матриця вироджена: розв'язок не єдиний або не існує")

        # перестановка рядків, якщо головний елемент не на своєму місці
        if p != k:
            M[k], M[p] = M[p], M[k]
            v[k], v[p] = v[p], v[k]
            print(f"   міняємо місцями рядки {k + 1} і {p + 1}")

        # 2) ділимо головний рядок на головний елемент
        pivot = M[k][k]
        M[k] = [t / pivot for t in M[k]]
        v[k] /= pivot
        print(f"   ділимо рядок {k + 1} на {pivot:g}")

        # 3) обнуляємо елементи під головним (правило прямокутників)
        for i in range(k + 1, n):
            factor = M[i][k]
            M[i] = [M[i][j] - factor * M[k][j] for j in range(n)]
            v[i] -= factor * v[k]

        print_matrix(M, None, v)

    # Зворотний хід
    print("Зворотний хід:")
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = v[i] - sum(M[i][j] * x[j] for j in range(i + 1, n))
        print(f"   x{i + 1} = {x[i]:.6f}")
    print()

    return x


if __name__ == "__main__":
    print("МЕТОД ГАУССА З ВИБОРОМ ГОЛОВНОГО ЕЛЕМЕНТА\n")
    x = gauss(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
