from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from ..components import Amount, CancellationDetails, Deal, PayoutStatus, Receipt, SelfEmployed
from ..components.payout_destination import PayoutDestination
from ..validators import check_metadata

__all__ = ["Payout"]


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

    @field_validator("metadata")
    def _check_metadata(cls, value: dict) -> dict:
        return check_metadata(value)
