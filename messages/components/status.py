from enum import Enum


class PaymentStatus(Enum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"
    WAITING_FOR_CAPTURE = "waiting_for_capture"


class CancellationStatus(Enum):
    # yoo_money, payment_network и merchant.
    YOO_MONEY = "yoo_money"
    PAYMENT_NETWORK = "payment_network"
    MERCHANT = "merchant"


__all__ = [
    'PaymentStatus',
    'CancellationStatus',
]