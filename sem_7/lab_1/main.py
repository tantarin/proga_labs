import math


def rectangle_method(f, a, b, n, mode='left'):
    h = (b - a) / n
    points = [a + i * h for i in range(n + 1)]
    if mode == 'left':
        values = [f(points[i]) for i in range(n)]
    else:
        values = [f(points[i + 1]) for i in range(n)]
    return h * sum(values)


# метод трапеций
# а и b - диапазон интегрирования
# f - функция (например, sin, cos, tan, ...) # может быть любая функция из библиотеки math
# n_iter - число разбиений
def integrate_trapezoidal(f, a, b, n):
    h = (b - a) / n  # Шаг интегрирования
    result = 0.5 * (f(a) + f(b))  # Первое и последнее значение функции

    for i in range(1, n):
        x_i = a + i * h
        result += f(x_i)

    result *= h  # Умножаем на шаг интегрирования
    return result


if __name__ == '__main__':
    print(integrate_trapezoidal(math.sin, 0, 1, n=100))
    print(rectangle_method(math.sin, 0, 1, 100, mode='left'))
