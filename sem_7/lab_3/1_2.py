import asyncio
import time
from termcolor import colored
from pynput import keyboard

# Улучшите предыдущую программу. Распечатывайте текущие дату и время в одной и той же строке (используйте символ возврата каретки '\r') разными цветами с помощью библиотеки termcolor.
# Добавьте обработку события нажатия клавиши Esc с помощью библиотеки pynput, чтобы можно было выйти из программы.

async def display_time():
    try:
        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            colored_time = colored(current_time, "blue")
            print(f"\rТекущая дата и время: {colored_time}", end="")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass

async def main():
    task = asyncio.create_task(display_time())

    try:
        await task
    except KeyboardInterrupt:
        pass
    finally:
        task.cancel()

def on_key_release(key):
    if key == keyboard.Key.esc:
        print("\nВыход из программы.")
        loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(main())
        with keyboard.Listener(on_release=on_key_release) as listener:
            loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()