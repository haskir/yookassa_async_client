from pprint import pprint

from httpx import AsyncClient, BasicAuth, Response
from pydantic import BaseModel

__all__ = ["YooKassaClient"]

from src.settings import Settings


class YooKassaClient:
    api: str = "https://api.yookassa.ru/v3/"

    def __init__(self, settings: Settings):
        self._id: int = settings.shop_id
        self._api_key: str = settings.api_key
        self._auth: BasicAuth = BasicAuth(str(self._id), self._api_key)
        self._debug: bool = settings.DEBUG

    async def get_request(self, path: str, query: dict = None) -> Response:
        self.repr_query(path, query)
        async with AsyncClient(base_url=self.api, auth=self._auth) as client:
            return await client.get(path, params=query)

    async def post_request(self, path: str, idempotency_key: str, data: BaseModel | dict = None) -> Response:
        self.repr_data(path, data)
        async with AsyncClient(base_url=self.api, auth=self._auth) as client:
            return await client.post(
                path,
                json=data.model_dump() if isinstance(data, BaseModel) else data,
                headers={"Idempotence-Key": idempotency_key},
            )

    def repr_query(self, path: str, query: dict):
        if not self._debug:
            return
        print(f"{path = }", end="\t")
        if query is None:
            print("query = None")
        else:
            pprint(query)

    def repr_data(self, path: str, data: BaseModel | dict):
        if not self._debug:
            return
        print(f"{path = }", end="\t")
        if data is None:
            print("data=None")

        if isinstance(data, dict):
            pprint(data)
        elif isinstance(data, BaseModel):
            print(data.model_dump_json(indent=4))
