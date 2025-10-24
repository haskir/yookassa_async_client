from client import YooKassaClient
from messages.yookassa import Payment


class CapturePaymentService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def capture(self, ID: str, value: float, currency: str) -> Payment:
        idem_key = f"capture_{ID}"
        response = await self._client.post_request(
            path=f'payments/{ID}/capture', idempotency_key=idem_key,
            data={"amount": {"value": value, "currency": currency}}
        )
        if response.status_code == 200:
            return Payment(**response.json())
        raise Exception(response.json())
