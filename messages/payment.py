from datetime import datetime
from pydantic import BaseModel, field_validator

from messages.validators import check_metadata, check_transfers
from .components import *
from .payment_methods import PaymentMethod


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


__all__ = [
    'Payment',
]
