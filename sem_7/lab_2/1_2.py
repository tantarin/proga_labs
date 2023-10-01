import requests
import threading

# Список URL-адресов файлов, которые вы хотите загрузить
file_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg",
    # Добавьте другие URL-адреса здесь
]

def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split("/")[-1]  # Имя файла из URL
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
