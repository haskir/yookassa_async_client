from .method import PaymentMethod
from ..components.bank_card import Card


class TPaymentMethod(PaymentMethod):
    type: str = "tinkoff_bank"
    card: Card


__all__ = [
    "TPaymentMethod",
]
