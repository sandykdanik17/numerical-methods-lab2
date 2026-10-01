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
    """Розв'язує Ax = b. Друкує проміжні кроки, повертає список x = [x1, x2, x3, x4]."""
    # TODO Тарас: реалізувати метод. Роби копію через copy_matrix(A),
    # щоб не змінювати вихідні дані з data.py.
    raise NotImplementedError


if __name__ == "__main__":
    x = gauss(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
