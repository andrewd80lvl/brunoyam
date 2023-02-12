import asyncio
import aiohttp
import requests
from datetime import datetime


async def get_html(url):
    print(f'Start: {url}')
    async with aiohttp.ClientSession() as session:
        async with requests.get(url) as response:
            data = await response.text()
            print(len(data))


async def get_data(url):
    print(f'Start: {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(len(data))

urls = ['http://meduza.io', 'https://google.ru', 'https://dzen.ru', 'https://ya.ru', 'http://lib.ru']

t1 = datetime.now()
jobs = [get_html(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(jobs))

print('time', (datetime.now() - t1).microseconds)
