import asyncio
from pprint import pprint

from loguru import logger

from src.settings import Settings
from src.test_payment import TestPayment
from src.test_payout import TestPayout


async def main_payment(settings: Settings):
    test: TestPayment = TestPayment(settings)
    created = await test.test_create_payment()
    print(f"{created['id'] = }")
    ID: str = "2eea3451-000f-5000-a000-123f486dd482"
    pprint(dict(await test.test_get_single_payment(ID)))
    # pprint(await test_capture(ID))
    # pprint(await test_cancel(ID))
    ...


async def main_payout(settings: Settings):
    test: TestPayout = TestPayout(settings)  # noqa


if __name__ == "__main__":
    _settings: Settings = Settings.load(".env", "logs", logger)
    asyncio.run(main_payment(_settings))
