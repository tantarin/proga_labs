# Напишите программу, используя объекты типа Future, чтобы асинхронно скачать несколько изображений с Интернета. Каждое изображение должно быть загружено в отдельный поток и сохранено на
# диск. Используйте семафор, чтобы ограничить количество одновременно выполняющихся потоков загрузки, чтобы избежать блокировки по IP от сервера или серверов.

import concurrent.futures
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import BoundedSemaphore

# URL-ы изображений, которые вы хотите загрузить
image_urls = [
    'url1',
    'url2',
    'url3',
    # Добавьте здесь остальные URL-ы
]

# Папка для сохранения изображений
output_folder = 'downloaded_images'

# Создаем папку, если ее нет
os.makedirs(output_folder, exist_ok=True)

# Семафор для ограничения количества одновременно выполняющихся потоков
semaphore = BoundedSemaphore(value=2)  # Установите значение семафора в желаемое количество потоков

def download_image(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

def download_image_async(url, filename):
    with semaphore:
        download_image(url, filename)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=len(image_urls)) as executor:
        futures = {executor.submit(download_image_async, url, os.path.join(output_folder, f"image_{i}.jpg")): url for i, url in enumerate(image_urls)}

        for future in as_completed(futures):
            url = futures[future]
            try:
                future.result()
                print(f"Downloaded: {url}")
            except Exception as e:
                print(f"Failed to download {url}. Error: {e}")
