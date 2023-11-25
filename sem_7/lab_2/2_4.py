# Создайте два потока, один из которых будет записывать данные в
# файл, а другой ­ считывать данные с файла. Используйте объекты типа Future, чтобы синхронизировать потоки и избежать гонки потоков.

import concurrent.futures


data_to_write = "Hello, World!"
file_name = "example.txt"

def write_to_file(data, file_name):
    with open(file_name, 'w') as file:
        file.write(data)

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_write = executor.submit(write_to_file, data_to_write, file_name)
        future_read = executor.submit(read_from_file, file_name)
        concurrent.futures.wait([future_write, future_read], return_when=concurrent.futures.ALL_COMPLETED)
        result_write = future_write.result()
        result_read = future_read.result()

        print(f"Data written to file: {result_write}")
        print(f"Data read from file: {result_read}")
