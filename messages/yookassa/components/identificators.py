from pydantic import BaseModel, field_validator

__all__ = [
    "SelfEmployed",
    "RecipientOnCreate",
    "Recipient",
    "Customer",
]


class SelfEmployed(BaseModel):
    """
    Идентификатор самозанятого в ЮKassa.
    """

    id: str


class RecipientOnCreate(BaseModel):
    """Идентификатор субаккаунта. Используется для разделения потоков платежей в рамках одного аккаунта."""

    gateway_id: str


class Recipient(RecipientOnCreate):
    """Получатель платежа"""

    account_id: str  # Идентификатор магазина в ЮKassa.


class Customer(BaseModel):
    """
    :param inn: ИНН пользователя (10 или 12 цифр).
    Если у физического лица отсутствует ИНН, необходимо передать паспортные данные в параметре full_name.

    """

    full_name: str | None
    inn: str | None
    email: str | None
    phone: str | None

    @field_validator("full_name")
    def check_full_name(cls, value: str) -> str:
        if len(value) > 200:
            raise ValueError("Full name must be less than 200 characters")
        return value

    @field_validator("inn")
    def check_inn(cls, value: str) -> str:
        if len(value) not in [10, 12]:
            raise ValueError("INN must be 10 or 12 characters")
        return value
