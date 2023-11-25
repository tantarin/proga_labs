# Сделайте два потока, представляющие сервер и клиент, где клиентский поток будет ждать готовности сервера, прежде чем отправлять
# ему какой­либо запрос. Используйте threading.Barrier

import threading
import time

class ServerClientCommunication:
    def __init__(self):
        self.barrier = threading.Barrier(2)  # Устанавливаем барьер для двух потоков

    def server_function(self):
        print("Server is waiting...")
        self.barrier.wait()  # Ожидаем, пока клиент не приготовится
        print("Server received request")

    def client_function(self):
        print("Client is preparing...")
        time.sleep(2)  # Представим, что клиент выполняет какую-то подготовительную работу
        print("Client is ready!")
        self.barrier.wait()  # Сообщаем серверу, что клиент готов

if __name__ == "__main__":
    communication = ServerClientCommunication()
    server_thread = threading.Thread(target=communication.server_function)
    client_thread = threading.Thread(target=communication.client_function)
    server_thread.start()
    client_thread.start()
    server_thread.join()
    client_thread.join()
