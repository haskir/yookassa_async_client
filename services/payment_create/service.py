from client import YooKassaClient
from messages.yookassa import CreatePayment


class CreatePaymentService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def create(self, payment: CreatePayment, idempotency_key: str) -> dict:
        response = await self._client.post_request("payments", idempotency_key, payment)
        if response.status_code == 200:
            return response.json()
        raise Exception(response.json())
