import asyncio
import time
from termcolor import colored
from pynput import keyboard

async def display_time():
    try:
        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            colored_time = colored(current_time, "blue")
            print(f"\rТекущая дата и время: {colored_time}", end="")
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass

def on_key_release(key):
    if key == keyboard.Key.esc:
        print("\nВыход из программы.")
        return False

async def main():
    asyncio.create_task(display_time())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        with keyboard.Listener(on_release=on_key_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

