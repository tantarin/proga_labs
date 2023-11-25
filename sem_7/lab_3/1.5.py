#Создайте асинхронный веб-скрапер, используя aiohttp и asyncio, который собирает информацию из нескольких веб-страниц одновременно.
# Вынесите код скрапера в отдельный класс. Загружайте список URLs из отдельного файла.

import aiohttp
import asyncio

class WebScraper:
    def __init__(self, urls_file):
        self.urls_file = urls_file

    async def fetch_url(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def scrape(self, url):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch_url(session, url)
            print(html)

    async def scrape_all(self):
        tasks = []
        with open(self.urls_file, 'r') as file:
            urls = file.read().splitlines()

        for url in urls:
            task = asyncio.create_task(self.scrape(url))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls_file = "urls.txt"
    scraper = WebScraper(urls_file)

    asyncio.run(scraper.scrape_all())
