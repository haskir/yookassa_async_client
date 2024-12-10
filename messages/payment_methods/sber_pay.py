from .method import PaymentMethod
from ..components.card import Card


class SberPayPaymentMethod(PaymentMethod):
    type: str = "sberbank"
    card: Card
    phone: str | None


__all__ = [
    "SberPayPaymentMethod",
]
