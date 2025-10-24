from enum import StrEnum

__all__ = [
    "PaymentStatus",
    "CancellationStatus",
    "ReceiptRegistration",
    "PayoutStatus",
]


class PayoutStatus(StrEnum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"


class PaymentStatus(StrEnum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"
    WAITING_FOR_CAPTURE = "waiting_for_capture"


class CancellationStatus(StrEnum):
    # yoo_money, payment_network и merchant.
    YOO_MONEY = "yoo_money"
    PAYMENT_NETWORK = "payment_network"
    MERCHANT = "merchant"


class ReceiptRegistration(StrEnum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"
