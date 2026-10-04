
from data import A, b, C, d, EPS
from utils import check_solution
from cramer import cramer
from gauss import gauss
from matrix_method import matrix_method
from lu import lu
from normal_form import prepare
from jacobi import jacobi
from seidel import seidel

LINE = "=" * 75


def header(title):
    print(LINE + "\n" + title + "\n" + LINE)


def fmt_x(x, digits=4):
    # дуже малі числа показуємо як 0
    return "".join(f"{(0.0 if abs(v) < 1e-12 else v):>11.{digits}f}" for v in x)


def main():
    exact = {}
    for name, func in [("Крамера", cramer), ("Гаусса", gauss),
                       ("Матричний", matrix_method), ("LU-розкладу", lu)]:
        header(f"ЗАВДАННЯ 1. Метод {name}")
        x = func(A, b)
        check_solution(A, b, x)
        exact[name] = x

    header("ЗАВДАННЯ 2. Підготовка системи")
    C_new, d_new, q, tol = prepare(C, d, EPS)

    header("ЗАВДАННЯ 2. Метод простої ітерації (Якобі)")
    x_j, k_j = jacobi(C_new, d_new, tol)

    header("ЗАВДАННЯ 2. Метод Зейделя")
    x_s, k_s = seidel(C_new, d_new, tol)

    header("ПОРІВНЯЛЬНІ ТАБЛИЦІ")
    print("Завдання 1 (точні методи):")
    print(f"{'Метод':<14}{'x1':>11}{'x2':>11}{'x3':>11}{'x4':>11}")
    for name, x in exact.items():
        print(f"{name:<14}{fmt_x(x)}")

    print("\nЗавдання 2 (наближені методи, eps = 1e-4):")
    print(f"{'Метод':<18}{'x1':>11}{'x2':>11}{'x3':>11}{'x4':>11}{'Ітерацій':>10}")
    print(f"{'Простої ітерації':<18}{fmt_x(x_j)}{k_j:>10}")
    print(f"{'Зейделя':<18}{fmt_x(x_s)}{k_s:>10}")

    print("\nВисновок: метод Зейделя досяг заданої точності за меншу кількість ітерацій,"
          f" ніж МПІ ({k_s} проти {k_j}).")


if __name__ == "__main__":
    main()