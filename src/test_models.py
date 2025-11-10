from src.messages import Amount, CreatePayment, CreatePayout, Currency, PersonalData, Redirect, YooMoneyDestination

__all__ = ["test_payment", "get_test_payout"]

from src.settings import Settings

test_payment: CreatePayment = CreatePayment(
    amount=Amount(value=100, currency=Currency.RUB),
    description="Тестовая оплата на 100 зябликов",
    confirmation=Redirect(confirmation_url="https://discord.ru/"),
)


def get_test_payout(settings: Settings) -> CreatePayout:
    return CreatePayout(
        amount=Amount(value=100, currency=Currency.RUB),
        description="Тестовая выплата 100 зябликов квоуну",
        payout_destination_data=YooMoneyDestination(account_number=settings.my_kassa_id),
        personal_data=[PersonalData(id="123")],
    )