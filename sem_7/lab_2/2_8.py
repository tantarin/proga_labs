# Написать программу для параллельного поиска файла в директории.
# Каждый поток должен обрабатывать свой фрагмент файлов директории и синхронизироваться с другими потоками, чтобы убедиться, что
# файл найден только один раз. Как только первый файл по его шаблону
# найден ­ все потоки поиска завершаются.

import os
import threading

class FileSearchThread(threading.Thread):
    def __init__(self, directory, file_pattern):
        super(FileSearchThread, self).__init__()
        self.directory = directory
        self.file_pattern = file_pattern
        self.found_file = None
        self.lock = threading.Lock()

    def run(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if self.file_pattern in file:
                    with self.lock:
                        if self.found_file is None:
                            self.found_file = os.path.join(root, file)
                            print(f"File found by thread {threading.current_thread().name}: {self.found_file}")
                            return

if __name__ == "__main__":
    target_directory = "/path/to/search"  # Укажите путь к директории, в которой нужно искать файл
    file_pattern = "target_file.txt"  # Укажите имя или шаблон файла, который нужно найти

    threads = []
    for i in range(5):  # Выберите количество потоков по вашему усмотрению
        thread = FileSearchThread(target_directory, file_pattern)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Дополнительная обработка после завершения поиска, если необходимо
    found_files = [thread.found_file for thread in threads if thread.found_file is not None]

    if found_files:
        print("All threads completed. First file found:", found_files[0])
    else:
        print("File not found.")
