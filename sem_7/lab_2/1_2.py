import requests
import threading

# Напишите программу для одновременной загрузки нескольких файлов (например картинок) с использованием потоков.
# Используйте для скачивания одну из библиотек urllib, requests или wget.


file_urls = [
    "https://source.unsplash.com/user/c_v_r/1900x800",
    "https://source.unsplash.com/user/c_v_r/100x100",
]


def download_file(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Загружен файл: {file_name}")
    else:
        print(f"Не удалось загрузить файл: {url}")


def main():
    threads = []

    for url in file_urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
