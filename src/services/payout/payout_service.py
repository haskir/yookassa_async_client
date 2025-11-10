from httpx import Response

from src.client import YooKassaClient
from src.messages import CreatePayout, Payout

__all__ = ["PayoutService"]

from src.settings import Settings


class PayoutService:
    def __init__(self, settings: Settings, exception_type: type[Exception] = Exception):
        self._client: YooKassaClient = YooKassaClient(settings)
        self._settings: Settings = settings
        self._exception: type[Exception] = exception_type

    async def get(self, ID: str) -> Payout:
        response: Response = await self._client.get_request(path=f"payouts/{ID}")
        if response.status_code == 200:
            self._repr_response(response)
            return Payout.model_validate(response)
        raise self._exception(response.json())

    async def create(self, payout: CreatePayout, idempotency_key: str) -> Payout:
        response: Response = await self._client.post_request(
            path="payouts",
            idempotency_key=idempotency_key,
            data=payout,
        )
        if response.status_code == 200:
            self._repr_response(response)
            return Payout.model_validate(response)
        raise self._exception(response.json())

    def _repr_response(self, response: Response) -> None:
        if not self._settings.DEBUG:
            return
        print(f"{response.status_code}: {response.json()}")