import requests
import concurrent.futures

# Напишите программу на Python, которая выполняет одновременные HTTP запросы с использованием потоков.
# Используйте библиотеку requests.

def make_request(url):
    response = requests.get(url)
    return response.text

def main():
    urls = [
        "https://docs.python.org/3/",
        "https://habr.com",
        "https://tproger.ru"
    ]

    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(make_request, url): url for url in urls}

        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                response = future.result()
                print(f"Запрос к {url} завершен.")
                results.append(response)
            except Exception as e:
                print(f"Запрос к {url} завершился с ошибкой: {str(e)}")


if __name__ == "__main__":
    main()
