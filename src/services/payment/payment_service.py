from src.client import YooKassaClient
from src.messages import Amount, CreatePayment, Currency, Payment, PaymentList, PaymentListRequest

__all__ = ["PaymentService"]


class PaymentService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def get(self, ID: str) -> Payment:
        response = await self._client.get_request(path=f"payments/{ID}")
        if response.status_code == 200:
            return Payment.model_validate(response.json())
        raise Exception(response.json())

    async def get_payments(self, r: PaymentListRequest = None) -> PaymentList:
        q = r.to_dict() if r else None
        response = await self._client.get_request(path="payments", query=q)
        if response.status_code == 200:
            return PaymentList(**response.json())
        raise Exception(response.json())

    async def create(self, payment: CreatePayment, idempotency_key: str) -> Payment:
        response = await self._client.post_request("payments", idempotency_key, payment)
        if response.status_code == 200:
            return Payment.model_validate(response.json())
        raise Exception(response.json())

    async def capture(self, ID: str, value: float, currency: Currency) -> Payment:
        idem_key = f"capture_{ID}"
        response = await self._client.post_request(
            path=f"payments/{ID}/capture",
            idempotency_key=idem_key,
            data=Amount(value=value, currency=currency),
        )
        if response.status_code == 200:
            return Payment.model_validate(response.json())
        raise Exception(response.json())

    async def cancel(self, ID: str) -> Payment:
        idem_key = f"cancel_{ID}"
        response = await self._client.post_request(
            path=f"payments/{ID}/cancel",
            idempotency_key=idem_key,
        )
        if response.status_code == 200:
            return Payment.model_validate(response.json())
        raise Exception(response.json())