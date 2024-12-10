from client import YooKassaClient


class GetPayoutService:
    def __init__(self, client: YooKassaClient):
        self._client = client

    async def get(self, ID: str):
        return await self._client.get_request(f"/payouts/{ID}")
