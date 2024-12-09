from pydantic import BaseModel, field_validator

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


class Payment(BaseModel):
    type: str  # Значение — bank_card. Код способа оплаты.
    id: str  # Идентификатор способа оплаты.
    saved: bool  # С помощью сохраненного способа оплаты можно проводить безакцептные списания.
    title: str  # Название способа оплаты.
    card: PaymentMethod  # Данные банковской карты.
    captured_at: str | None  # Время подтверждения платежа. Указывается по UTC и передается в формате ISO 8601.
    created_at: str  # Время создания способа оплаты. UTC ISO 8601 (2017-11-03T11:52:31.827Z).
    expires_at: str | None  # Время, до которого вы можете бесплатно отменить или подтвердить платеж. В указанное время платеж в статусе waiting_for_capture будет автоматически отменен. Указывается по UTC и передается в формате ISO 8601. Пример: 2017-11-03T11:52:31.827Z
    confirmation: Confirmation | None
    test: bool  # Признак тестового способа оплаты.
    refunded_amount: Amount | None  # Сумма возврата.
    paid: bool  # Признак оплаты.
    refundable: bool  # Возможность провести возврат по API.
    receipt_registration: PaymentStatus | None  # Статус регистрации чека. Возможные значения:
    metadata: dict | None
    cancellation_details: CancellationDetails | None
    authorization_details: AuthorizationDetails | None
    transfers: list | None  # Данные о распределении денег — сколько и в какой магазин нужно перевести. Присутствует, если вы используете cплитование платежей.
    deal: Deal | None  # Данные о сделке, в составе которой проходит платеж. Присутствует, если вы проводите Безопасную сделку
    merchant_customer_id: str | None  # Идентификатор покупателя в вашей системе, например электронная почта или номер телефона.
    invoice_details: InvoiceDetails | None

    @field_validator('metadata')
    def check_metadata(cls, value: dict) -> dict:
        if value is None:
            return {}
        if len(value) > 16:
            raise ValueError("Metadata must be less than 16 items")
        for key, value in value.items():
            if not isinstance(key, str):
                raise ValueError(f"Metadata key '{key}' must be a string")
            if len(key) > 32:
                raise ValueError(f"Metadata key '{key}' must be less than 32 characters")
            if len(str(value)) > 512:
                raise ValueError(f"Metadata value '{value}' must be less than 512 characters")
        return value

    @field_validator('merchant_customer_id')
    def check_merchant_customer_id(cls, value: str) -> str:
        if len(value) > 200:
            raise ValueError("Merchant customer ID must be less than 200  characters")
        return value
