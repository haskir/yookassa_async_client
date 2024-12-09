from pydantic import BaseModel, field_validator

from validators import check_metadata
from .status import PaymentStatus
from .amount import Amount


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


__all__ = [
    "Settlement",
    "Deal",
    "InvoiceDetails",
    "Transfer",
]