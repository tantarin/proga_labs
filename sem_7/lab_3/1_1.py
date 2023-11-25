import asyncio
import time

# Создайте простую асинхронную функцию, которая в бесконечном цикле отображает текущее время с интервалом 1 секунда, и запустите ее с помощью asyncio.
# Завершать программу можно через комбинацию клавиш типа Ctrl + C или Ctrl + Break.

async def display_time():
    try:
        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Текущее время: {current_time}")
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass

async def main():
    await display_time()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
