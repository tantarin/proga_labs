# Дополните решение из лабораторной работы № 1 с кодом функции integrate.
# Проведите замеры времени вычисления для разного числа потоков и процессов.

import math
import concurrent.futures as ftres
from functools import partial


def integrate(f, a, b, *, n=1000):
    h = (b - a) / n  # Шаг интегрирования
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x_i = a + i * h
        result += f(x_i)

    result *= h
    return result


def foo():
    n_jobs = 4
    a = 0
    b = 1
    f = lambda x: x
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    # future_result = executor.submit(identity,10)
    # ai, bi = 0, 0
    step = (b - a) / n_jobs

    fs = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    print(step, fs)

    spawn_lst = []
    for i in fs:
        spawn = partial(executor.submit, integrate, f, i[0], i[1])
        spawn_lst.append(spawn)

    res = []
    for f in spawn_lst:
        res.append(f())

    print(res)

    s = [r.result() for r in ftres.as_completed(res)]

    print(sum(s))
    return res