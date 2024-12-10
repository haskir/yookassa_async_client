from pydantic import BaseModel, field_validator

from messages.components import CancellationStatus


class Confirmation(BaseModel):
    type: str  # Значение — confirmation. Код способа оплаты.


class EmbeddedConfirmation(Confirmation):
    type: str = "embedded"
    confirmation_token: str  # Токен для инициализации платежного виджета ЮKassa.


class External(Confirmation):
    type: str = "external"


class MobileApplication(Confirmation):
    type: str = "mobile_application"
    confirmation_url: str  # Диплинк на мобильное приложение, в котором пользователь подтверждает платеж.


class QR(Confirmation):
    type: str = "qr"
    confirmation_data: str  # Данные для генерации QR-кода.


class Redirect(Confirmation):
    """
        URL, на который необходимо перенаправить пользователя после проведения платежа.
    """
    type: str = "redirect"
    # URL, на который необходимо перенаправить пользователя для подтверждения оплаты.
    return_url: str
    # Запрос на проведение платежа с аутентификацией по 3-D Secure.
    # Будет работать, если оплату банковской картой вы по умолчанию принимаете без подтверждения платежа пользователем.
    # В остальных случаях аутентификацией по 3-D Secure будет управлять ЮKassa.
    locale: str | None = ""
    enforce: bool | None = None

    @field_validator('return_url')
    def check_return_url(cls, value: str) -> str:
        if len(value) > 2048:
            raise ValueError("Return URL must be less than 2048 characters")
        return value


__all__ = [
    'Confirmation',
    'EmbeddedConfirmation',
    'External',
    'MobileApplication',
    'QR',
    'Redirect',
]
