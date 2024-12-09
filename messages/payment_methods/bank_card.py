from enum import Enum

from pydantic import BaseModel, field_validator

from .method import PaymentMethod


class CardProduct(BaseModel):
    code: str  # Код продукта карты.
    name: str | None  # Название продукта карты.


class CardType(Enum):
    MasterCard = "MasterCard"
    Visa = "Visa"
    Mir = "Mir"
    UnionPay = "UnionPay"


class Card(PaymentMethod):
    first6: str | None  # Первые 6 цифр номера карты.
    last4: str  # Последние 4 цифры номера карты.
    expiry_year: str  # Год истечения срока действия карты.
    expiry_month: str  # Месяц истечения срока действия карты.
    card_type: CardType  # Тип банковской карты. Возможные значения:  (для карт Mastercard и Maestro), Visa (для карт Visa и Visa Electron), Mir, UnionPay
    card_product: CardProduct | None  # Карточный продукт платежной системы, с которым ассоциирована банковская карта.
    issuer_country: str | None  # Код страны, в которой выпущена карта. Передается в формате ISO-3166 alpha-2. Пример: RU.
    issuer_name: str | None  # Название организации, которая выпустила карту.
    source: str | None  # Источник данных банковской карты. Возможные значения: mir_pay, apple_pay, google_pay. Присутствует, если пользователь при оплате выбрал карту, сохраненную в Mir Pay, Apple Pay или Google Pay.

    @field_validator('first6')
    def check_first6(cls, value: str) -> str:
        if len(value) != 6:
            raise ValueError("First 6 digits must be 6 characters long")
        return value

    @field_validator('last4')
    def check_last4(cls, value: str) -> str:
        if len(value) != 4:
            raise ValueError("Last 4 digits must be 4 characters long")
        return value
