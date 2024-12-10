from client import YooKassaClient
from .get_classes import PaymentList, PaymentListRequest
from messages import Payment


class GetPaymentService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def get(self, payment_id: str) -> Payment:
        response = await self._client.get_request(path=f'payments/{payment_id}')
        if response.status_code == 200:
            return Payment(**response.json())
        raise Exception(response.json())

    async def get_payments(self, r: PaymentListRequest | None = None) -> PaymentList:
        q = r.to_dict() if r else None
        print(f'{q = }')
        response = await self._client.get_request(path="payments", query=q)
        if response.status_code == 200:
            return PaymentList(**response.json())
        raise Exception(response.json())
