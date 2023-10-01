import math
import timeit
import threading


# Функция для численного интегрирования
def integrate(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x_i = a + i * h
        result += f(x_i)

    result *= h
    return result


# Функция для интегрирования на подинтервале
def integrate_subinterval(f, a, b, n, result, lock):
    partial_result = integrate(f, a, b, n)
    with lock:
        result.value += partial_result


# Основная функция
def main():
    a = 0
    b = 1
    n = 1000  # Количество интервалов
    num_threads = 4  # Количество потоков
    lock = threading.Lock()
    threads = []
    # Общая переменная для хранения интегральной суммы
    result = threading.Value('d', 0.0)

    # Запуск потоков
    for i in range(num_threads):
        thread = threading.Thread(target=integrate_subinterval, args=(
        math.sin, a + i * (b - a) / num_threads, a + (i + 1) * (b - a) / num_threads, n // num_threads, result, lock))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Итоговый результат
    final_result = result.value
    print("Интеграл:", final_result)


if __name__ == "__main__":
    # Замер времени выполнения
    execution_time = timeit.timeit(main, number=1)
    print("Время выполнения:", execution_time, "секунд")
