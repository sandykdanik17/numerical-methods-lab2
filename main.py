
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
    return "".join(f"{(0.0 if abs(v) < 1e-12 else v):>11.{digits}f}" for v in x)


def main():
    # Завдання 1
    exact = {}
    for name, who, func in [("Крамера", "Степан", cramer), ("Гаусса", "Тарас", gauss),
                            ("Матричний", "Степан", matrix_method), ("LU-розкладу", "Саша", lu)]:
        header(f"ЗАВДАННЯ 1. Метод {name} ({who})")
        try:
            x = func(A, b)
            check_solution(A, b, x)
            exact[name] = x
        except NotImplementedError:
            print("ще не готово\n")
            exact[name] = None

    # Завдання 2
    iterative = {"Простої ітерації": None, "Зейделя": None}
    try:
        header("ЗАВДАННЯ 2. Підготовка системи (Данік)")
        C_new, d_new, q, tol = prepare(C, d, EPS)
        for name, func in [("Простої ітерації", jacobi), ("Зейделя", seidel)]:
            header(f"ЗАВДАННЯ 2. Метод {name} (Данік)")
            try:
                iterative[name] = func(C_new, d_new, tol)
            except NotImplementedError:
                print("ще не готово\n")
    except NotImplementedError:
        print("normal_form ще не готово\n")

    # Таблиці
    header("ПОРІВНЯЛЬНІ ТАБЛИЦІ")
    print("Завдання 1:")
    print(f"{'Метод':<14}{'x1':>11}{'x2':>11}{'x3':>11}{'x4':>11}")
    for name, x in exact.items():
        print(f"{name:<14}" + ("ще не готово" if x is None else fmt_x(x)))

    print("\nЗавдання 2 (eps = 1e-4):")
    print(f"{'Метод':<18}{'x1':>11}{'x2':>11}{'x3':>11}{'x4':>11}{'Ітерацій':>10}")
    for name, res in iterative.items():
        if res is None:
            print(f"{name:<18}ще не готово")
        else:
            x, k = res
            print(f"{name:<18}{fmt_x(x)}{k:>10}")


if __name__ == "__main__":
    main()
