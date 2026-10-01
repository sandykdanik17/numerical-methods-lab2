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


def matrix_method(A, b):
    """Розв'язує Ax = b. Друкує проміжні кроки, повертає список x = [x1, x2, x3, x4]."""
    # TODO Стьопа: реалізуй метод. роби копію через copy_matrix(A),
    # щоб не мінялися вихідні дані з data.py.
    raise NotImplementedError


if __name__ == "__main__":
    x = matrix_method(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
