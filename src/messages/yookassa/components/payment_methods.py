from enum import StrEnum

from pydantic import BaseModel, Field

from .card import Card

__all__ = [
    "PaymentMethod",
    "PaymentType",
    "QiwiPaymentMethod",
    "SberPayPaymentMethod",
    "SBPPaymentMethod",
    "SplitPaymentMethod",
    "TPaymentMethod",
    "YooMoneyPaymentMethod",
    "BankCardPaymentMethod",
]


class PaymentType(StrEnum):
    QIWI = "qiwi"
    SBERBANK = "sberbank"
    SBP = "sbp"
    SPLIT = "installments"
    TINKOFF_BANK = "tinkoff_bank"
    YOO_MONEY = "yoo_money"
    BANK_CARD = "bank_card"


class PaymentMethod(BaseModel):
    id: str
    saved: bool  # С помощью сохраненного способа оплаты можно проводить безакцептные списания.
    title: str = Field(default="")  # Название способа оплаты.
    type: str


class QiwiPaymentMethod(PaymentMethod):
    type: PaymentType = PaymentType.QIWI


class SberPayPaymentMethod(PaymentMethod):
    type: PaymentType = PaymentType.SBERBANK
    card: Card
    phone: str | None


class PayerBankDetails(BaseModel):
    bank_id: str
    bic: str


class SBPPaymentMethod(PaymentMethod):
    type: PaymentType = PaymentType.SBP
    payer_bank_details: PayerBankDetails | None
    sbp_operation_id: str | None


class SplitPaymentMethod(PaymentMethod):
    type: PaymentType = PaymentType.SPLIT


class TPaymentMethod(PaymentMethod):
    type: PaymentType = PaymentType.TINKOFF_BANK
    card: Card


class YooMoneyPaymentMethod(PaymentMethod):
    type: PaymentType = PaymentType.YOO_MONEY


class BankCardPaymentMethod(PaymentMethod):
    type: PaymentType = PaymentType.BANK_CARD
    card: Card | None = None
