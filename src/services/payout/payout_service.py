from src.client import YooKassaClient
from src.messages import CreatePayout, Payout

__all__ = ["PayoutService"]


class PayoutService:
    def __init__(self, client: YooKassaClient):
        self._client = client

    async def get(self, ID: str) -> Payout:
        return await self._client.get_request(f"/payouts/{ID}")

    async def create(self, payout: CreatePayout, idempotency_key: str) -> Payout:
        response = await self._client.post_request(path="payouts", idempotency_key=idempotency_key, data=payout)
        if response.status_code == 200:
            return Payout.model_validate(response)
        raise Exception(response.json())