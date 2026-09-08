import aiohttp
from config import API_URL, API_KEY

HEADERS = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json",
}


class APIClient:

    def __init__(self):
        self.base = API_URL

    async def get(self, path, params=None):

        async with aiohttp.ClientSession(headers=HEADERS) as session:

            async with session.get(
                f"{self.base}{path}",
                params=params,
                timeout=15
            ) as resp:

                resp.raise_for_status()

                return await resp.json()

    async def post(self, path, json=None):

        async with aiohttp.ClientSession(headers=HEADERS) as session:

            async with session.post(
                f"{self.base}{path}",
                json=json,
                timeout=15
            ) as resp:

                resp.raise_for_status()

                return await resp.json()

    async def patch(self, path, json=None):

        async with aiohttp.ClientSession(headers=HEADERS) as session:

            async with session.patch(
                f"{self.base}{path}",
                json=json,
                timeout=15
            ) as resp:

                resp.raise_for_status()

                return await resp.json()


api = APIClient()