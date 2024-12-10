from .method import PaymentMethod


class YooMoneyPaymentMethod(PaymentMethod):
    type: str = "yoo_money"


__all__ = [
    "YooMoneyPaymentMethod",
]
