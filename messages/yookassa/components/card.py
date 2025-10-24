from enum import StrEnum

from pydantic import BaseModel, Field, field_validator


class CardProduct(BaseModel):
    code: str  # Код продукта карты.
    name: str | None  # Название продукта карты.


class CardType(StrEnum):
    MASTER_CARD = "MasterCard"
    VISA = "Visa"
    MIR = "Mir"
    UNION_PAY = "UnionPay"


class Card(BaseModel):
    """
    :param last4: Последние 4 цифры номера карты.
    :param expiry_year: Год истечения срока действия карты.
    :param expiry_month: Месяц истечения срока действия карты.
    :param card_type: Тип банковской карты. Возможные значения: Mastercard, Visa, Mir, UnionPay
    :param card_product: Карточный продукт платежной системы, с которым ассоциирована банковская карта.
    :param first6: Первые 6 цифр номера карты.
    :param issuer_country: Код страны, в которой выпущена карта. Передается в формате ISO-3166 alpha-2. Пример: RU.
    :param issuer_name: Название организации, которая выпустила карту
    :param source: Источник данных банковской карты.
    """

    last4: str
    expiry_year: str
    expiry_month: str
    card_type: CardType
    card_product: CardProduct | None = None
    first6: str = Field(default="")
    issuer_country: str = Field(default="")
    issuer_name: str = Field(default="")
    source: str = Field(default="")

    @field_validator("first6")
    def check_first6(cls, value: str) -> str:
        if len(value) != 6:
            raise ValueError("First 6 digits must be 6 characters long")
        return value

    @field_validator("last4")
    def check_last4(cls, value: str) -> str:
        if len(value) != 4:
            raise ValueError("Last 4 digits must be 4 characters long")
        return value

    @field_validator("expiry_year")
    def check_expiry_year(cls, value: str) -> str:
        if len(value) != 4:
            raise ValueError("Expiry year must be 4 characters long")
        return value

    @field_validator("expiry_month")
    def check_expiry_month(cls, value: str) -> str:
        if len(value) != 2:
            raise ValueError("Expiry month must be 2 characters long")
        return value
