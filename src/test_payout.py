from datetime import UTC, datetime

from src.messages import CreatePayout
from src.services import PayoutService
from src.settings import Settings

__all__ = ["TestPayout"]


class TestPayout:
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self._service: PayoutService = PayoutService(settings)

    async def create_payout(self, payout: CreatePayout = None, idempotency_key: str = None):
        idempotency_key = idempotency_key or datetime.now(UTC).isoformat()
        return await self._service.create(payout, idempotency_key)

    async def get_payout(self, _id: str):
        return await self._service.get(_id)