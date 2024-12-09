from pydantic import BaseModel, field_validator


class Customer(BaseModel):
    # ИНН пользователя (10 или 12 цифр). Если у физического лица отсутствует ИНН, необходимо передать паспортные данные в параметре full_name.
    # Можно передавать, если используете Чеки от ЮKassa или онлайн-кассу Orange Data, Атол Онлайн.
    full_name: str | None
    inn: str | None
    email: str | None
    phone: str | None

    @field_validator('full_name')
    def check_full_name(cls, value: str) -> str:
        if len(value) > 200:
            raise ValueError("Full name must be less than 200 characters")
        return value

    @field_validator('inn')
    def check_inn(cls, value: str) -> str:
        if len(value) not in [10, 12]:
            raise ValueError("INN must be 10 or 12 characters")
        return value


__all__ = [
    "Customer",
]
