from src.client import YooKassaClient
from src.messages import Amount, CreatePayout, PersonalData, YooMoneyDestination
from src.messages.yookassa import Currency
from src.services import PayoutService
from src.settings import Settings

__all__ = ["TestPayout"]


def _test_payout(settings: Settings) -> CreatePayout:
    return CreatePayout(
        amount=Amount(value=100, currency=Currency.RUB),
        description="Тестовая выплата 100 зябликов квоуну",
        payout_destination_data=YooMoneyDestination(account_number=settings.my_kassa_id),
        personal_data=[PersonalData(id="123")],
    )


class TestPayout:
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self._client: YooKassaClient = YooKassaClient(settings)
        self._service: PayoutService = PayoutService(settings)

    async def create_payout(self, payout: CreatePayout = None, idempotency_key: str = "create_1"):
        if payout is None:
            payout = _test_payout(self.settings)
        return await self._service.create(payout, idempotency_key)

    async def get_payout(self, _id: str):
        return await self._service.get(_id)