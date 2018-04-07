import asyncio
import os
from aiohttp import ClientSession
from config import *

async def download_image(url, id):
    if os.path.isfile(os.path.join(DATA_DIR, id + '.jpg')):
        return
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            with open(os.path.join(DATA_DIR, id + '.jpg'), 'wb') as f:
                f.write(response)
