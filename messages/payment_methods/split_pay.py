from .method import PaymentMethod


class SplitPaymentMethod(PaymentMethod):
    type: str = "installments"


__all__ = [
    "SplitPaymentMethod",
]
