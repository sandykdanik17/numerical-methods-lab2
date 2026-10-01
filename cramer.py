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
from utils import copy_matrix, print_matrix, print_vector, check_solution


def cramer(A, b):
    """Розв'язує Ax = b. Друкує проміжні кроки, повертає список x = [x1, x2, x3, x4]."""
    # TODO (Тарас): реалізувати метод. Роби копію через copy_matrix(A),
    # шоб не міняти вихідні дані з data.py.
    raise NotImplementedError


if __name__ == "__main__":
    x = cramer(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
