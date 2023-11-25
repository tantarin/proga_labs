# Улучшите асинхронный веб-скрапер из предыдущей задачи. Преобразуйте его в класс асинхронного менеджера контекста
# и используйте вместе с async with изнутри асинхронной функции main, которая
# вызывается через asyncio.run(main()).

import aiohttp
import asyncio
from bs4 import BeautifulSoup

class AsyncWebScraper:
    def __init__(self, urls_file):
        self.urls_file = urls_file
        self.urls = self.load_urls()

    def load_urls(self):
        with open(self.urls_file, 'r') as file:
            return [line.strip() for line in file]

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def scrape_page(self, session, url):
        html = await self.fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string
        print(f"Title from {url}: {title}")

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def scrape_all(self):
        tasks = [self.scrape_page(self.session, url) for url in self.urls]
        await asyncio.gather(*tasks)

async def main():
    async with AsyncWebScraper("urls.txt") as scraper:
        await scraper.scrape_all()

if __name__ == "__main__":
    asyncio.run(main())
