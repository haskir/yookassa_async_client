from pydantic import BaseModel, field_validator
from .components import Confirmation, Amount, Transfer, Deal
from .payment_methods import PaymentMethod
from .receipt import Receipt


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


class CreateYookassaPayment(BaseModel):
    # Данные для формирования чека (receipt) необходимо передавать в этих случаях:
    # - вы компания или ИП и для оплаты с соблюдением требований 54-ФЗ используете Чеки от ЮKassa;
    # - вы компания или ИП, для оплаты с соблюдением требований 54-ФЗ используете стороннюю онлайн-кассу и отправляете данные для чеков по одному из сценариев: Платеж и чек одновременно  или Сначала чек, потом платеж ;
    # - вы самозанятый и используете решение ЮKassa для автоотправки чеков.
    amount: Amount
    description: str | None
    receipt: Receipt
    recipient: NotImplemented
    payment_token: str | None
    payment_method_id: str | None
    payment_method_data: PaymentMethod | None
    confirmation: Confirmation
    save_payment_method: bool | None
    capture: bool | None
    client_ip: str | None
    metadata: dict | None
    airline: None
    transfers: list[Transfer] | None
    deal: Deal | None
    merchant_customer_id: str | None
    receiver: Receiver | None

    @field_validator('description')
    def check_description(cls, value: str) -> str:
        if len(value) > 128:
            raise ValueError("Description must be less than 128 characters")
        return value


__all__ = [
    'Receiver',
    'CreateYookassaPayment',
]
