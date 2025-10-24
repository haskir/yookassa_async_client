from pprint import pprint

from httpx import AsyncClient, BasicAuth
from pydantic import BaseModel


class YooKassaClient:
    api: str = "https://api.yookassa.ru/v3/"

    def __init__(self, shop_id: str, api_key: str):
        self._id = shop_id
        self._api_key = api_key
        self._auth = BasicAuth(self._id, self._api_key)

    async def get_request(self, path: str, query: dict = None):
        async with AsyncClient(auth=self._auth) as client:
            return await client.get(self.api + path, params=query)

    async def post_request(self, path: str, idempotency_key: str, data: BaseModel = None):
        pprint(data)
        async with AsyncClient(auth=self._auth) as client:
            return await client.post(
                self.api + path,
                json=data.model_dump(),
                headers={"Idempotence-Key": idempotency_key},
            )