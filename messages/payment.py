from datetime import datetime
from enum import Enum

from pydantic import BaseModel, field_validator

from validators import check_metadata
from .components import *
from .payment_methods import PaymentMethod


class Settlement(BaseModel):
    type: str = "payout"  # Тип операции. Фиксированное значение: payout — выплата продавцу.
    amount: Amount  # Данные о сумме распределения денег.


class Deal(BaseModel):
    id: str  # Идентификатор сделки.
    settlements: list[Settlement]  # Данные о распределении денег.


class InvoiceDetails(BaseModel):
    id: str | None = None  # Идентификатор счета в ЮКасса.


class Transfer(BaseModel):
    account_id: str
    amount: Amount
    status: PaymentStatus
    platform_fee_amount: Amount
    description: str | None
    metadata: dict | None

    @field_validator('metadata')
    def _check_metadata(cls, value: dict) -> dict:
        return check_metadata(value)


class ReceiptRegistration(Enum):
    pending = "pending"
    succeeded = "succeeded"
    canceled = "canceled"


class Payment(BaseModel):
    id: str  # Идентификатор способа оплаты.
    status: PaymentStatus
    amount: Amount
    income_amount: Amount
    description: str | None
    recipient: Recipient
    payment_method: PaymentMethod | None
    captured_at: str | None  # Время подтверждения платежа. Указывается по UTC и передается в формате ISO 8601.
    created_at: str  # Время создания способа оплаты. UTC ISO 8601 (2017-11-03T11:52:31.827Z).
    expires_at: str | None  # Время, до которого вы можете бесплатно отменить или подтвердить платеж. В указанное время платеж в статусе waiting_for_capture будет автоматически отменен. Указывается по UTC и передается в формате ISO 8601. Пример: 2017-11-03T11:52:31.827Z
    confirmation: Confirmation | None
    test: bool  # Признак тестового способа оплаты.
    refunded_amount: Amount | None  # Сумма возврата.
    paid: bool  # Признак оплаты.
    refundable: bool  # Возможность провести возврат по API.
    receipt_registration: PaymentStatus | None
    metadata: dict | None
    cancellation_details: CancellationDetails | None
    authorization_details: AuthorizationDetails | None
    transfers: list[Transfer]  # Данные о распределении денег — сколько и в какой магазин нужно перевести. Присутствует, если вы используете cплитование платежей.
    deal: Deal | None  # Данные о сделке, в составе которой проходит платеж. Присутствует, если вы проводите Безопасную сделку
    merchant_customer_id: str | None  # Идентификатор покупателя в вашей системе, например электронная почта или номер телефона.
    invoice_details: InvoiceDetails | None

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
