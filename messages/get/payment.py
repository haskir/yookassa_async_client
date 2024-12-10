from datetime import datetime
from pprint import pprint

from pydantic import BaseModel, field_validator

from ..validators import check_metadata, check_transfers
from ..components import *
from ..components.bank_card import BankCardPaymentMethod
from ..payment_methods import *
from .confirmation import *


class _PaymentRequired(BaseModel):
    id: str  # Идентификатор способа оплаты.
    status: PaymentStatus
    amount: Amount
    recipient: Recipient


class Payment(_PaymentRequired):
    income_amount: Amount | None = None
    description: str | None = None
    payment_method: PaymentMethod | None = None
    captured_at: datetime | None = None  # Время подтверждения платежа. Указывается по UTC и передается в формате ISO 8601.
    created_at: datetime  # Время создания способа оплаты. UTC ISO 8601 (2017-11-03T11:52:31.827Z).
    expires_at: datetime | None = None  # Время, до которого вы можете бесплатно отменить или подтвердить платеж. В указанное время платеж в статусе waiting_for_capture будет автоматически отменен. Указывается по UTC и передается в формате ISO 8601. Пример: 2017-11-03T11:52:31.827Z
    confirmation: Confirmation | None = None
    test: bool  # Признак тестового способа оплаты.
    refunded_amount: Amount | None = None  # Сумма возврата.
    paid: bool  # Признак оплаты.
    refundable: bool  # Возможность провести возврат по API.
    receipt_registration: PaymentStatus | None = None
    metadata: dict | None = None
    cancellation_details: CancellationDetails | None = None
    authorization_details: AuthorizationDetails | None = None
    # Данные о распределении денег — сколько и в какой магазин нужно перевести. Присутствует, если вы используете cплитование платежей.
    transfers: list[Transfer] | None = None
    deal: Deal | None = None  # Данные о сделке, в составе которой проходит платеж. Присутствует, если вы проводите Безопасную сделку
    merchant_customer_id: str | None = None  # Идентификатор покупателя в вашей системе, например электронная почта или номер телефона.
    invoice_details: InvoiceDetails | None = None

    @field_validator('metadata')
    def _check_metadata(cls, value: dict) -> dict:
        return check_metadata(value)

    @field_validator('description')
    def check_description(cls, value: str) -> str:
        if len(value) > 128:
            raise ValueError("Description must be less than 128 characters")
        return value

    @field_validator('merchant_customer_id')
    def check_merchant_customer_id(cls, value: str) -> str:
        if len(value) > 200:
            raise ValueError("Merchant customer ID must be less than 200  characters")
        return value

    @field_validator('transfers')
    def _check_transfers(cls, value: list[Transfer]) -> list[Transfer]:
        return check_transfers(value)

    @classmethod
    def fabric(cls, data: dict) -> 'Payment':
        pprint(data)
        conf_type = {
            "embedded": EmbeddedConfirmation,
            "external": External,
            "mobile_application": MobileApplication,
            "qr": QR,
            "redirect": Redirect,
        }
        payment_method = {
            "bank_card": BankCardPaymentMethod,
            "qiwi": QiwiPaymentMethod,
            "sber_pay": SberPayPaymentMethod,
            "sbp": SBPPaymentMethod,
            "installments": SplitPaymentMethod,
            "t_pay": TPaymentMethod,
            "yoo_money": YooMoneyPaymentMethod,
        }
        additional = {
            "payment_method": payment_method.get(data.get('payment_method').get('type'))(
                **data.get('payment_method')) if data.get('payment_method') else None,
            "confirmation": conf_type.get(data.get('confirmation', {}).get('type'))(
                **data.get('confirmation')) if data.get('confirmation') else None,
        }
        return cls(**(data | additional))


__all__ = [
    'Payment',
]
