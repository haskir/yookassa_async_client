from client import YooKassaClient
from .get_classes import PaymentList, PaymentListRequest
from messages import Payment


class GetService:
    def __init__(self, client: YooKassaClient) -> None:
        self._client = client

    async def get(self, payment_id: str) -> Payment:
        response = await self._client.get_request(path=f'payments/{payment_id}')
        if response.status_code == 200:
            return Payment(**response.json())
        raise Exception(response.json())

    async def get_payments(self, request: PaymentListRequest) -> PaymentList:
        response = await self._client.get_request(path="payments", query=request.to_dict())
        if response.status_code == 200:
            return PaymentList(**response.json())
        raise Exception(response.json())
