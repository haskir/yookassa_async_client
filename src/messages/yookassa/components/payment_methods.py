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


class BasePaymentMethod(BaseModel):
    id: str
    saved: bool  # С помощью сохраненного способа оплаты можно проводить безакцептные списания.
    title: str = Field(default="")  # Название способа оплаты.


class QiwiPaymentMethod(BasePaymentMethod):
    type: PaymentType = PaymentType.QIWI


class SberPayPaymentMethod(BasePaymentMethod):  # noqa
    type: PaymentType = PaymentType.SBERBANK
    card: Card
    phone: str | None


class PayerBankDetails(BaseModel):
    bank_id: str
    bic: str


class SBPPaymentMethod(BasePaymentMethod):
    type: PaymentType = PaymentType.SBP
    payer_bank_details: PayerBankDetails | None
    sbp_operation_id: str | None


class SplitPaymentMethod(BasePaymentMethod):
    type: PaymentType = PaymentType.SPLIT


class TPaymentMethod(BasePaymentMethod):
    type: PaymentType = PaymentType.TINKOFF_BANK
    card: Card


class YooMoneyPaymentMethod(BasePaymentMethod):
    type: PaymentType = PaymentType.YOO_MONEY


class BankCardPaymentMethod(BasePaymentMethod):
    type: PaymentType = PaymentType.BANK_CARD
    card: Card | None = None


PaymentMethod = (
    QiwiPaymentMethod
    | SberPayPaymentMethod
    | PayerBankDetails
    | SBPPaymentMethod
    | SplitPaymentMethod
    | TPaymentMethod
    | YooMoneyPaymentMethod
    | BankCardPaymentMethod
    | None
)