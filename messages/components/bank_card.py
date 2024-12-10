from ..components.card import Card
from ..payment_methods import PaymentMethod


class BankCardPaymentMethod(PaymentMethod):
    type: str = "bank_card"
    card: Card  # Данные банковской карты.


__all__ = [
    "BankCardPaymentMethod",
]
