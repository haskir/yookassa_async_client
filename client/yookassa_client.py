from httpx import AsyncClient, BasicAuth


class YooKassaClient:
    api: str = "https://api.yookassa.ru/v3/"

    def __init__(self, settings):
        self._settings = settings
        self._id = settings.YOOKASSA_SHOP_ID
        self._api_key = settings.YOOKASSA_API_KEY
        self._auth = BasicAuth(self._id, self._api_key)

    async def get(self, path: str, query: dict = None):
        async with AsyncClient() as client:
            return await client.get(self.api + path, params=query, auth=self._auth)

    async def post(self, path: str, data: dict = None):
        async with AsyncClient() as client:
            return await client.post(self.api + path, json=data, auth=self._auth)
