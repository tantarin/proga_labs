import asyncio
import aiohttp
import asyncpg
import json

WEB_SERVER_URL = "https://rnacentral.org/api/v1/rna/"
DB_CONNECTION_STRING = "postgres://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs"

async def fetch_web_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(WEB_SERVER_URL) as response:
            data = await response.text()
            json_data = json.loads(data)
            return json_data

async def fetch_db_data():
    conn = await asyncpg.connect(DB_CONNECTION_STRING)
    query = "SELECT * FROM rnc_database"
    result = await conn.fetch(query)
    await conn.close()
    return result

async def main():
    web_data = await fetch_web_data()
    db_data = await fetch_db_data()

    print("Web Data:")
    print(json.dumps(web_data, indent=4))
    print("\nDatabase Data:")
    for row in db_data:
        print(row)

if __name__ == "__main__":
    asyncio.run(main())
