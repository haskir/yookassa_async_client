from client import YooKassaClient
from .get_classes import PaymentList, PaymentListRequest
from messages.payment_get import Payment


class GetPaymentService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def get(self, ID: str) -> Payment:
        response = await self._client.get_request(path=f'payments/{ID}')
        if response.status_code == 200:
            return Payment.fabric(response.json())
        raise Exception(response.json())

    async def get_payments(self, r: PaymentListRequest = None) -> PaymentList:
        q = r.to_dict() if r else None
        response = await self._client.get_request(path="payments", query=q)
        if response.status_code == 200:
            return PaymentList(**response.json())
        raise Exception(response.json())
