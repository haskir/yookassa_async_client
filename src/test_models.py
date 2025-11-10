from src.messages import Amount, CreatePayment, Currency, Redirect

__all__ = ["payment"]


payment: CreatePayment = CreatePayment(
    amount=Amount(value=100, currency=Currency.RUB),
    description="Тестовая оплата на 100 зябликов",
    confirmation=Redirect(confirmation_url="https://discord.ru/"),
)