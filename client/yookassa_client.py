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
        async with AsyncClient() as client:
            return await client.get(self.api + path, params=query, auth=self._auth)

    async def post_request(self, path: str, idempotency_key: str, data: dict | BaseModel):
        data = self._deep_serialize(data)
        pprint(data)
        async with AsyncClient() as client:
            return await client.post(
                self.api + path,
                json=data,
                headers={"Idempotence-Key": idempotency_key},
                auth=self._auth
            )

    @classmethod
    def _deep_serialize(cls, obj):
        if isinstance(obj, BaseModel):
            # Рекурсивно обрабатываем каждое поле BaseModel
            return {key: cls._deep_serialize(value) for key, value in dict(obj).items()}
        elif isinstance(obj, list):
            # Рекурсивно обрабатываем элементы списка
            return [cls._deep_serialize(item) for item in obj]
        elif isinstance(obj, dict):
            # Рекурсивно обрабатываем ключи и значения словаря
            return {key: cls._deep_serialize(value) for key, value in obj.items()}
        else:
            # Оставляем неизменными значения простых типов
            return obj
