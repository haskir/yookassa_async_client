from pydantic import BaseModel

from .card import Card


class PayoutDestination(BaseModel):
    type: str

    @classmethod
    def factory(cls, data: dict) -> 'PayoutDestination':
        return {
            "bank_card": CardDestination,
            "sbp": SBPDestination,
            "yoo_money": YooMoneyDestination
        }.get(data.get('type'))(**data)


class CardDestination(PayoutDestination):
    type: str = "bank_card"
    card: Card


class SBPDestination(PayoutDestination):
    type: str = "sbp"
    bank_id: str
    phone: str
    recipient_checked: bool


class YooMoneyDestination(PayoutDestination):
    type: str = "yoo_money"
    account_number: str


class PersonalData(BaseModel):
    id: str


__all__ = [
    'PayoutDestination',
    'CardDestination',
    'SBPDestination',
    'YooMoneyDestination',
    'PersonalData'
]
