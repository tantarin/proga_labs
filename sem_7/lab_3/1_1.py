import asyncio
import time

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
