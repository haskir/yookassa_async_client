from datetime import datetime, timedelta

from src.messages import Amount, CreatePayment, Redirect
from src.messages.yookassa import Currency
from src.services import DatetimeCriteria, PaymentListRequest, PaymentService
from src.settings import Settings

__all__ = ["TestPayment"]


class TestPayment:
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self._service: PaymentService = PaymentService(settings)

    async def get_payment(self, ID: str):
        return await self._service.get(ID)

    async def test_get_payments(self):
        return await self._service.get_payments(
            params=PaymentListRequest(
                created_at=DatetimeCriteria(gte=datetime.now() - timedelta(days=1)),
            )
        )

    async def create_payment(self, key: str = None):
        payment: CreatePayment = CreatePayment(
            amount=Amount(value=100, currency=Currency.RUB),
            description="Тестовая оплата на 100 зябликов",
            confirmation=Redirect(return_url="https://discord.ru/"),
        )
        idempotency_key: str = key or datetime.now().isoformat()
        return await self._service.create(payment, idempotency_key)

    async def capture_payment(self, ID: str, amount: Amount, key: str = None):
        idempotency_key: str = key or f"capture_{ID}"
        return await self._service.capture(ID, amount, idempotency_key)

    async def cancel_payment(self, ID: str, key: str = None):
        idempotency_key: str = key or f"cancel_{ID}"
        return await self._service.cancel(ID, idempotency_key)
