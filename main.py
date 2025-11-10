import asyncio

from loguru import logger

from src.messages import Amount, Currency, Payment, Payout
from src.settings import Settings


async def main_payment(settings: Settings) -> None:
    from src.test_models import test_payment
    from src.test_payment import TestPayment

    exist_id: str = ""  # noqa: F841

    async def create() -> str:
        created: Payment = await test.create_payment(test_payment)
        return created.id

    async def get(_id: str) -> str:  # noqa: F841
        return (await test.get_payment(_id)).id

    async def cancel(_id: str) -> None:  # noqa: F841
        await test.cancel_payment(_id)

    async def capture(_id: str) -> Payment:  # noqa: F841
        return await test.capture_payment(_id, amount=Amount(value=80, currency=Currency.RUB))

    test: TestPayment = TestPayment(settings)
    exist_id = await create()
    await get(exist_id)
    # await cancel(exist_id)
    input("Жду оплаты")
    await capture(exist_id)


async def main_payout(settings: Settings) -> None:
    from src.test_models import get_test_payout
    from src.test_payout import TestPayout

    exist_id: str = ""  # noqa: F841

    async def create() -> str:
        created: Payout = await test.create_payout(get_test_payout(settings))
        return created.id

    async def get(_id: str) -> Payout:
        return await test.get_payout(_id)

    test: TestPayout = TestPayout(settings)  # noqa
    exist_id = await create()
    await get(exist_id)


def test_models():
    from src.test_models import test_payment

    print(test_payment.model_dump_json(indent=4))


if __name__ == "__main__":
    _settings: Settings = Settings.load(".env", "logs", logger)
    # asyncio.run(main_payment(_settings))
    asyncio.run(main_payout(_settings))
