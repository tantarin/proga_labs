import asyncio

import aiohttp
import json

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            message = input("Введите сообщение (или 'exit' для завершения): ")
            if message == 'exit':
                break

            data = {"message": message}
            async with session.post('http://localhost:8080/echo', json=data) as response:
                response_data = await response.json()
                print("Получен ответ:", response_data["message"])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
