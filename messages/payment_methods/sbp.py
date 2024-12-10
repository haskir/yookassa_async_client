from datetime import datetime

from pydantic import BaseModel

from ..payment_methods import PaymentMethod


class PayerBankDetails(BaseModel):
    bank_id: str
    bic: str


class SBPPaymentMethod(PaymentMethod):
    type: str = "sbp"
    payer_bank_details: PayerBankDetails | None
    sbp_operation_id: str | None
