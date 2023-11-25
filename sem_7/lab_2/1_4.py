import concurrent.futures

# Напишите программу для вычисления факториала числа с использованием нескольких потоков.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    n = int(input("Введите число для вычисления факториала: "))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(factorial, n)
        print("Вычисление факториала...")
        result = future.result()

    print(f"Факториал {n} равен {result}")

if __name__ == "__main__":
    main()
