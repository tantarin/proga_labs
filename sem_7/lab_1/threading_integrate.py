import math
import timeit
import threading


def integrate(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x_i = a + i * h
        result += f(x_i)

    result *= h
    return result


class Integrator:
    def __init__(self):
        self.lock = threading.Lock()
        self.result = 0.0

    def integrate_subinterval(self, f, a, b, n):
        self.lock.acquire()
        try:
            partial_result = integrate(f, a, b, n)
            self.result += partial_result
        finally:
            self.lock.release()


def main():
    a = 0
    b = 1
    n = 1000
    num_threads = 4
    threads = []

    integrator = Integrator()

    for i in range(num_threads):
        start = a + i * (b - a) / num_threads
        end = a + (i + 1) * (b - a) / num_threads
        thread = threading.Thread(target=integrator.integrate_subinterval,
                                  args=(math.sin, start, end, n // num_threads))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    final_result = integrator.result
    print("Интеграл:", final_result)


if __name__ == "__main__":
    execution_time = timeit.timeit(main, number=1)
    print("Время выполнения:", execution_time, "секунд")
