from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from ..components import Amount, PayoutStatus, Deal, SelfEmployed, CancellationDetails
from ..components.payout_destination import PayoutDestination
from ..receipt import Receipt
from ..validators import check_metadata


class _PayoutRequired(BaseModel):
    id: str
    amount: Amount
    status: PayoutStatus
    payout_destination: PayoutDestination
    created_at: datetime
    test: bool


class Payout(_PayoutRequired):
    description: str = Field(default="", max_length=128)
    deal: Deal | None = None
    self_employed: SelfEmployed | None = None
    receipt: Receipt | None = None
    cancellation_details: CancellationDetails | None = None
    metadata: dict = Field(default_factory=dict)

    @classmethod
    def fabric(cls, data: dict) -> 'Payout':
        data["payout_destination"] = PayoutDestination.factory(data['payout_destination'])
        return cls(**data)

    @field_validator("metadata")
    def _check_metadata(cls, value: dict) -> dict:
        return check_metadata(value)


__all__ = [
    "Payout",
]
