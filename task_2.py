import random
import scipy.integrate as spi


def f(x):
    """
    Функція, інтеграл якої будемо обчислювати.
    """
    return x ** 2


def monte_carlo_integral(a, b, num_points):
    """
    Обчислює визначений інтеграл методом Монте-Карло.
    """
    max_y = f(b)
    points_under_curve = 0

    for _ in range(num_points):
        # Випадкова координата x у межах інтегрування
        x = random.uniform(a, b)

        # Випадкова координата y у межах прямокутника
        y = random.uniform(0, max_y)

        # Якщо точка знаходиться під графіком функції
        if y <= f(x):
            points_under_curve += 1

    # Площа прямокутника
    rectangle_area = (b - a) * max_y

    # Частка точок під графіком * площа прямокутника
    integral_value = (points_under_curve / num_points) * rectangle_area

    return integral_value


if __name__ == "__main__":
    a = 0
    b = 2
    num_points = 100_000

    monte_carlo_result = monte_carlo_integral(a, b, num_points)

    quad_result, quad_error = spi.quad(f, a, b)

    print(f"Метод Монте-Карло: {monte_carlo_result}")
    print(f"Функція quad: {quad_result}")
    print(f"Оцінка похибки quad: {quad_error}")
    print(f"Різниця між Monte Carlo та quad: {abs(monte_carlo_result - quad_result)}")