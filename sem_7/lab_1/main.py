import math


# а и b - диапазон интегрирования
# f - функция (например, sin, cos, tan, ...) # может быть любая функция из библиотеки math
# n_iter - число разбиений
def integrate(f, a, b, n_iter=1000):
    dx = (b - a) / n_iter
    area = 0
    x = a
    for i in range(n_iter):
        area += dx * (f(x) + f(x + dx)) / 2
        x += dx
    return area


if __name__ == '__main__':
    print(integrate(math.sin, 0, 1, n_iter=100))
