from enum import StrEnum

from pydantic import BaseModel, field_validator

__all__ = [
    "Confirmation",
    "ConfirmationType",
    "EmbeddedConfirmation",
    "External",
    "MobileApplication",
    "QR",
    "Redirect",
]


class ConfirmationType(StrEnum):
    EMBEDDED = "embedded"
    EXTERNAL = "external"
    MOBILE_APPLICATION = "mobile_application"
    QR = "qr"
    REDIRECT = "redirect"


class EmbeddedConfirmation(BaseModel):
    """Токен для инициализации платежного виджета ЮKassa."""

    type: ConfirmationType = ConfirmationType.EMBEDDED
    confirmation_token: str


class External(BaseModel):
    type: ConfirmationType = ConfirmationType.EXTERNAL


class MobileApplication(BaseModel):
    """Ссылка на мобильное приложение, в котором пользователь подтверждает платеж."""

    type: ConfirmationType = ConfirmationType.MOBILE_APPLICATION
    confirmation_url: str


class QR(BaseModel):
    type: ConfirmationType = ConfirmationType.QR
    confirmation_data: str  # Данные для генерации QR-кода.


class Redirect(BaseModel):
    """
    confirmation_url: URL, на который необходимо перенаправить пользователя после проведения платежа
    enforce: Запрос на проведение платежа с аутентификацией по 3-D Secure.
        Будет работать, если оплату банковской картой вы по умолчанию
        принимаете без подтверждения платежа пользователем. В остальных случаях аутентификацией
        по 3-D Secure будет управлять ЮKassa;
    return_url: URL, на который будет произведен возврат пользователя после оплаты.
    """

    type: ConfirmationType = ConfirmationType.REDIRECT
    confirmation_url: str = ""
    return_url: str = ""
    enforce: bool | None = None

    @field_validator("return_url", check_fields=False)
    def check_return_url(cls, value: str) -> str:
        if len(value) > 2048:
            raise ValueError("Return URL must be less than 2048 characters")
        return value


Confirmation = EmbeddedConfirmation | External | MobileApplication | QR | Redirect
