import aiohttp
from flask import Flask
from aio_executor import run_with_asyncio

app = Flask(__name__)


async def get_random_quote():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.quotable.io/random') as response:
            quote = await response.json()
    return f'{quote["content"]} ({quote["author"]})'


@app.route('/')
@run_with_asyncio
async def index():
    return await get_random_quote()


if __name__ == '__main__':
    app.run()
