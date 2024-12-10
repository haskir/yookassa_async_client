from pydantic import BaseModel

from .method import PaymentMethod


class PayerBankDetails(BaseModel):
    bank_id: str
    bic: str


class SBPPaymentMethod(PaymentMethod):
    type: str = "sbp"
    payer_bank_details: PayerBankDetails | None
    sbp_operation_id: str | None


__all__ = [
    "PayerBankDetails",
    "SBPPaymentMethod",
]
