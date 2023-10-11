import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Результат задачи 1"

async def task2():
    await asyncio.sleep(1)
    return "Результат задачи 2"

def process_results(results):
    for result in results:
        print(f"Получен результат: {result}")

async def main():
    results = await asyncio.gather(task1(), task2())
    process_results(results)

if __name__ == "__main__":
    asyncio.run(main())
