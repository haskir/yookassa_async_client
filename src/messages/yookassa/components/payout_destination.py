from enum import StrEnum

from pydantic import BaseModel

from .card import Card

__all__ = [
    "Destination",
    "PayoutDestination",
    "CardDestination",
    "SBPDestination",
    "YooMoneyDestination",
    "PersonalData",
]


class Destination(StrEnum):
    BANK_CARD = "bank_card"
    SBP = "sbp"
    YOO_MONEY = "yoo_money"


class CardDestination(BaseModel):
    type: Destination = Destination.BANK_CARD
    card: Card


class SBPDestination(BaseModel):
    type: Destination = Destination.SBP
    bank_id: str
    phone: str
    recipient_checked: bool


class YooMoneyDestination(BaseModel):
    type: Destination = Destination.YOO_MONEY
    account_number: int


class PersonalData(BaseModel):
    id: str


PayoutDestination = CardDestination | SBPDestination | YooMoneyDestination