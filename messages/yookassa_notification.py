from pydantic import BaseModel

from .yookassa import Payment, PaymentStatus


class YooKassaNotification(BaseModel):
    type: str = "notification"
    event: PaymentStatus
    object: Payment