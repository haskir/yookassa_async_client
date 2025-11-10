from datetime import datetime, timedelta

from src.client import YooKassaClient
from src.messages import Amount, CreatePayment, Redirect
from src.messages.yookassa import Currency
from src.services import DatetimeCriteria, PaymentListRequest, PaymentService
from src.settings import Settings

__all__ = ["TestPayment"]


class TestPayment:
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self._client: YooKassaClient = YooKassaClient(shop_id=self.settings.shop_id, api_key=self.settings.api_key)
        self._service: PaymentService = PaymentService(self._client)

    async def test_get_single_payment(self, ID: str):
        return await self._service.get(ID)

    async def test_get_payments(self):
        return await self._service.get_payments(
            r=PaymentListRequest(
                created_at=DatetimeCriteria(gte=datetime.now() - timedelta(days=1)),
            )
        )

    async def test_create_payment(self):
        p = CreatePayment(
            amount=Amount(value=100, currency=Currency.RUB),
            description="Тестовая оплата на 100 зябликов",
            confirmation=Redirect(return_url="https://discord.ru/"),
        )
        return await self._service.create(p,idempotency_key= "123")

    async def test_capture_payment(self, ID: str):
        return await self._service.capture(ID, value=80, currency=Currency.RUB)

    async def test_cancel_payment(self, ID: str):
        return await self._service.cancel(ID)
