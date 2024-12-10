from client import YooKassaClient
from messages.payment_get import Payment
from messages.capture_payment import CapturePayment


class CapturePaymentService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def capture(self, ID: str, capture: CapturePayment) -> Payment:
        idem_key = f"capture_{ID}"
        response = await self._client.post_request(path=f'payments/{ID}/capture', idempotency_key=idem_key)
        if response.status_code == 200:
            return Payment(**response.json())
        raise Exception(response.json())