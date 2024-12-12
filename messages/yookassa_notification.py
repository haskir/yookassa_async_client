from typing import Annotated, Literal

from pydantic import BaseModel

from .payment_get import Payment


class YooKassaNotification(BaseModel):
    type: str = "notification"
    event: Annotated[str, Literal["waiting_for_capture", "succeeded", "canceled"]]
    object: Payment