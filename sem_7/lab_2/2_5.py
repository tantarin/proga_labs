# : Напишите программу, которая создает 3 потока. Первый поток должен устанавливать состояние объекта типа Event каждую секунду.
# Второй поток должен ждать наступления события и выводить сообщение "Event occurred". Третий поток должен выводить сообщение
# "Event did not occur" каждую секунду, до тех пор, пока не наступит событие. Как только событие происходит, третий поток должен
# остановиться.

import threading
import time

def event_setter(event):
    while True:
        time.sleep(1)
        event.set()

def event_waiter(event):
    print("Waiting for the event to occur...")
    event.wait()
    print("Event occurred")

def event_checker(event):
    while not event.is_set():
        print("Event did not occur")
        time.sleep(1)

if __name__ == "__main__":
    event = threading.Event()
    setter_thread = threading.Thread(target=event_setter, args=(event,))
    waiter_thread = threading.Thread(target=event_waiter, args=(event,))
    checker_thread = threading.Thread(target=event_checker, args=(event,))

    setter_thread.start()
    waiter_thread.start()
    checker_thread.start()

    waiter_thread.join()
    checker_thread.join()

    print("All threads have finished.")
