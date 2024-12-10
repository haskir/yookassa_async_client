from .method import PaymentMethod


class QiwiPaymentMethod(PaymentMethod):
    type: str = "qiwi"


__all__ = [
    "QiwiPaymentMethod",
]
