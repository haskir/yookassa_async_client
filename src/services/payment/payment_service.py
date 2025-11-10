from httpx import Response

from src.client import YooKassaClient
from src.messages import Amount, CreatePayment, Payment, PaymentList, PaymentListRequest

__all__ = ["PaymentService"]

from src.settings import Settings


class PaymentService:
    def __init__(self, settings: Settings, exception_type: type[Exception] = Exception) -> None:
        self._client: YooKassaClient = YooKassaClient(settings)
        self._settings: Settings = settings
        self._exception: type[Exception] = exception_type

    async def get(self, ID: str) -> Payment:
        response: Response = await self._client.get_request(path=f"payments/{ID}")
        if response.status_code == 200:
            self._repr_response(response)
            return Payment.model_validate(response.json())
        raise self._exception(response.json())

    async def get_payments(self, params: PaymentListRequest = None) -> PaymentList:
        query = params.to_dict() if params else None
        response: Response = await self._client.get_request(path="payments", query=query)
        if response.status_code == 200:
            self._repr_response(response)
            return PaymentList(**response.json())
        raise self._exception(response.json())

    async def create(self, payment: CreatePayment, idempotency_key: str) -> Payment:
        response: Response = await self._client.post_request("payments", idempotency_key, payment)
        if response.status_code == 200:
            self._repr_response(response)
            return Payment.model_validate(response.json())
        raise self._exception(response.json())

    async def capture(self, ID: str, amount: Amount, idempotency_key: str) -> Payment:
        response: Response = await self._client.post_request(
            path=f"payments/{ID}/capture",
            idempotency_key=idempotency_key,
            data={"amount": amount.model_dump()},
        )
        if response.status_code == 200:
            self._repr_response(response)
            return Payment.model_validate(response.json())
        raise self._exception(response.json())

    async def cancel(self, ID: str, idempotency_key: str) -> Payment:
        response: Response = await self._client.post_request(
            path=f"payments/{ID}/cancel",
            idempotency_key=idempotency_key,
        )
        if response.status_code == 200:
            self._repr_response(response)
            return Payment.model_validate(response.json())
        raise self._exception(response.json())

    def _repr_response(self, response: Response) -> None:
        if not self._settings.DEBUG:
            return
        print(f"{response.status_code}: {response.json()}")