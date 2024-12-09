from pydantic import BaseModel, field_validator




class CreateYookassaPaymentRequest(BaseModel):
    amount: Amount
    confirmation: Confirmation
    description: str
    capture: bool

    @field_validator('description')
    def check_description(cls, value: str) -> str:
        if len(value) > 128:
            raise ValueError("Description must be less than 128 characters")
        return value


__all__ = ['Amount', 'Confirmation', 'CreateYookassaPaymentRequest']