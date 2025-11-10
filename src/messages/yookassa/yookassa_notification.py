from enum import StrEnum

from pydantic import BaseModel

from .payment import Payment

__all__ = ["YooKassaEvent", "YooKassaNotification"]


class YooKassaEvent(StrEnum):
    waiting_for_capture = "waiting_for_capture"
    succeeded = "succeeded"
    canceled = "canceled"


class YooKassaNotification(BaseModel):
    type: str = "notification"
    event: YooKassaEvent
    object: Payment
