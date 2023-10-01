import asyncio

# Асинхронная функция 1
async def task1():
    await asyncio.sleep(2)
    return "Результат задачи 1"

# Асинхронная функция 2
async def task2():
    await asyncio.sleep(1)
    return "Результат задачи 2"

# Функция для обработки результатов
def process_results(results):
    for result in results:
        print(f"Получен результат: {result}")

async def main():
    # Запуск двух задач параллельно
    results = await asyncio.gather(task1(), task2())

    # Обработка результатов
    process_results(results)

if __name__ == "__main__":
    asyncio.run(main())
