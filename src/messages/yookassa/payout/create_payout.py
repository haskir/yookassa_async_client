from pydantic import BaseModel, Field, field_validator

from ..components import Amount, Deal, PayoutDestination, PersonalData, Receipt, SelfEmployed
from ..validators import check_metadata

__all__ = ["CreatePayout"]


class _CreatePayoutRequired(BaseModel):
    amount: Amount


class CreatePayout(_CreatePayoutRequired):
    payout_destination_data: PayoutDestination | None = None
    payout_token: str = Field(default="")
    payment_method_id: str = Field(default="")
    description: str = Field(default="", max_length=128)
    deal: Deal | None = None
    self_employed: SelfEmployed | None = None
    receipt_data: Receipt | None = None
    personal_data: list[PersonalData] = Field(default_factory=list)
    metadata: dict | None = None

    @field_validator("metadata")
    def _check_metadata(cls, value: dict) -> dict:
        return check_metadata(value)
