from client import YooKassaClient
from messages.payout_create import CreatePayout
from messages.payout_get import Payout


class CreatePayoutService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def create(self, payout: CreatePayout, idempotency_key: str) -> Payout:
        response = await self._client.post_request(
            path="payouts",
            idempotency_key=idempotency_key,
            data=payout
        )
        if response.status_code == 200:
            return Payout.fabric(response)
        raise Exception(response.json())