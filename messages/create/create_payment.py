from pydantic import BaseModel, field_validator

from ..validators import check_transfers
from ..components import Amount, Transfer, Deal, RecipientOnCreate
from .confirmation import *
from ..payment_methods import PaymentMethod
from ..receipt import Receipt


class Receiver(BaseModel):
    type: str = "bank_account"
    account_number: str
    bic: str

    @field_validator('account_number')
    def check_account_number(cls, value: str) -> str:
        if len(value) != 20:
            raise ValueError("Account number must be 20 characters")
        return value

    @field_validator('bic')
    def check_bic(cls, value: str) -> str:
        if len(value) != 9:
            raise ValueError("BIC must be 9 characters")
        return value


class _CreatePaymentRequired(BaseModel):
    amount: Amount


class CreatePayment(_CreatePaymentRequired):
    # Данные для формирования чека (receipt) необходимо передавать в этих случаях:
    # - вы компания или ИП и для оплаты с соблюдением требований 54-ФЗ используете Чеки от ЮKassa;
    # - вы компания или ИП, для оплаты с соблюдением требований 54-ФЗ используете стороннюю онлайн-кассу и отправляете данные для чеков по одному из сценариев: Платеж и чек одновременно  или Сначала чек, потом платеж ;
    # - вы самозанятый и используете решение ЮKassa для авто отправки чеков.
    description: str | None = ""
    receipt: Receipt | None = None
    confirmation: Confirmation | None = None
    recipient: RecipientOnCreate | None = None
    payment_token: str | None = None
    payment_method_id: str | None = None
    payment_method_data: PaymentMethod | None = None
    save_payment_method: bool | None = None
    capture: bool | None = None
    client_ip: str | None = None
    metadata: dict | None = None
    airline: None = None
    transfers: list[Transfer] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = None
    receiver: Receiver | None = None

    @field_validator('description')
    def check_description(cls, value: str) -> str:
        if len(value) > 128:
            raise ValueError("Description must be less than 128 characters")
        return value

    @field_validator('transfers')
    def _check_transfers(cls, value: list[Transfer]) -> list[Transfer]:
        return check_transfers(value)


__all__ = [
    'Receiver',
    'CreatePayment',
]
