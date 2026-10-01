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
from data import C, d, EPS


def normal_form(C, d):
    """Повертає (C_new, d_new) з нулями на діагоналі."""
    # TODO (Данік)
    raise NotImplementedError


def matrix_norms(C):
    """Повертає (norm1, norm2, norm3)."""
    # TODO (Данік)
    raise NotImplementedError


def stop_tolerance(q, eps):
    """Повертає поріг зупинки ітерацій."""
    # TODO (Данік)
    raise NotImplementedError


def prepare(C, d, eps):
    """Повертає (C_new, d_new, q, tol)."""
    # TODO (Данік): викликати normal_form, matrix_norms, stop_tolerance
    raise NotImplementedError


if __name__ == "__main__":
    prepare(C, d, EPS)
