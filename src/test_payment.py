from datetime import UTC, datetime, timedelta

from src.messages import Amount, CreatePayment
from src.services import DatetimeCriteria, PaymentListRequest, PaymentService
from src.settings import Settings

__all__ = ["TestPayment"]


class TestPayment:
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self._service: PaymentService = PaymentService(settings)

    async def get_payment(self, ID: str):
        return await self._service.get(ID)

    async def get_payments(self, params: PaymentListRequest = None):
        query: PaymentListRequest = params or PaymentListRequest(
            created_at=DatetimeCriteria(gte=datetime.now(UTC) - timedelta(days=1)),
        )
        return await self._service.get_payments(query)

    async def create_payment(self, payment: CreatePayment, key: str = None):
        idempotency_key: str = key or datetime.now(UTC).isoformat()
        return await self._service.create(payment, idempotency_key)

    async def capture_payment(self, ID: str, amount: Amount, key: str = None):
        idempotency_key: str = key or f"capture_{ID}"
        return await self._service.capture(ID, amount, idempotency_key)

    async def cancel_payment(self, ID: str, key: str = None):
        idempotency_key: str = key or f"cancel_{ID}"
        return await self._service.cancel(ID, idempotency_key)
