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


def lu(A, b):
    """Розв'язує Ax = b. Друкує проміжні кроки, повертає список x = [x1, x2, x3, x4]."""
    # TODO : реалізуй метод. роби копію через copy_matrix(A),
    # щоб не мінялися вихідні дані з data.py.
    raise NotImplementedError


if __name__ == "__main__":
    x = lu(A, b)
    print_vector("x", x)
    check_solution(A, b, x)
