"""
Метод Крамера.
Робить: Степан

Що зробити:
  1) написати функцію determinant(M) для визначника (розклад за першим рядком);
  2) обчислити Δ = det(A) і перевірити, що Δ ≠ 0;
  3) для кожного j замінити j-й стовпець A на b і обчислити Δj;
  4) xj = Δj / Δ. Надрукувати всі Δj.
"""
from data import A, b
from utils import print_matrix, print_vector, check_solution


def determinant(M):
    """
    Обчислює визначник розкладом за першим рядком (теорема Лапласа):
        det(M) = Σ (-1)^j * M[0][j] * det(мінор без 0-го рядка і j-го стовпця)
    Для матриці 4x4 це швидко і відповідає тому, як рахують вручну.
    """
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    result = 0
    for j in range(n):
        # мінор: викреслюємо 0-й рядок і j-й стовпець
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        result += (-1) ** j * M[0][j] * determinant(minor)
    return result


def cramer(A, b):
    """Розв'язує Ax = b методом Крамера. Повертає список x."""
    n = len(A)

    # Крок 1. Головний визначник
    delta = determinant(A)
    print(f"Головний визначник: Δ = det(A) = {delta:g}")
    if delta == 0:
        raise ValueError("Δ = 0: метод Крамера застосувати не можна")
    print("Δ ≠ 0, отже система має єдиний розв'язок\n")

    # Допоміжні визначники Δ_j і невідомі x_j
    x = []
    for j in range(n):
        # копія A, у якій j-й стовпець замінено на b
        A_j = [row[:] for row in A]
        for i in range(n):
            A_j[i][j] = b[i]
        delta_j = determinant(A_j)
        print_matrix(A_j, f"Матриця для Δ{j + 1} (стовпець {j + 1} замінено на b):", digits=0)
        print(f"Δ{j + 1} = {delta_j:g},   x{j + 1} = Δ{j + 1} / Δ = {delta_j:g} / {delta:g} = {delta_j / delta:g}\n")
        x.append(delta_j / delta)

    return x


if __name__ == "__main__":
    print("МЕТОД КРАМЕРА\n")
    x = cramer(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
