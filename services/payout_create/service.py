from client import YooKassaClient
from messages.yookassa import CreatePayout, Payout


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
            return Payout.model_validate(response)
        raise Exception(response.json())