from pydantic import BaseModel, Field

from ..components import Amount, PaymentStatus, Recipient, Redirect

__all__ = ["Payment"]


class _PaymentRequired(BaseModel):
    id: str  # Идентификатор способа оплаты.
    status: PaymentStatus
    amount: Amount
    recipient: Recipient


class Payment(_PaymentRequired):
    description: str = Field(default="", max_length=128)
    confirmation: Redirect | None = None
    test: bool  # Признак тестового способа оплаты.
    paid: bool  # Признак оплаты.
