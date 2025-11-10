from pydantic import BaseModel, Field

from src.messages.yookassa import Currency

__all__ = "CreatePaymentDTO", "CapturePaymentDTO"


class _Amount(BaseModel):
    value: float
    currency: Currency


class CreatePaymentDTO(BaseModel):
    amount: _Amount
    description: str = Field(default="", max_length=128)
    confirmation: dict  # {"type": "redirect", "return_url": "http://localhost:8000"}

    @classmethod
    def fabric(cls, value: float, currency: Currency, url: str, description: str = "") -> "CreatePaymentDTO":
        return cls(
            amount=_Amount(value=value, currency=currency),
            description=description,
            confirmation={"type": "redirect", "return_url": url},
        )


class CapturePaymentDTO(BaseModel):
    amount: _Amount
