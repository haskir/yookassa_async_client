from pydantic import BaseModel, field_validator

from ..components import CancellationStatus


class Confirmation(BaseModel):
    type: str  # Значение — confirmation. Код способа оплаты.


class EmbeddedConfirmation(Confirmation):
    type: str = "embedded"
    confirmation_token: str  # Токен для инициализации платежного виджета ЮKassa.


class ExternalConfirmation(Confirmation):
    type: str = "external"


class MobileApplicationConfirmation(Confirmation):
    type: str = "mobile_application"
    confirmation_url: str  # Диплинк на мобильное приложение, в котором пользователь подтверждает платеж.


class QRConfirmation(Confirmation):
    type: str = "qr"
    confirmation_data: str  # Данные для генерации QR-кода.


class RedirectConfirmation(Confirmation):
    """
        URL, на который необходимо перенаправить пользователя после проведения платежа.
    """
    type: str = "redirect"
    # URL, на который необходимо перенаправить пользователя для подтверждения оплаты.
    # confirmation_url: str
    # Запрос на проведение платежа с аутентификацией по 3-D Secure.
    # Будет работать, если оплату банковской картой вы по умолчанию принимаете без подтверждения платежа пользователем.
    # В остальных случаях аутентификацией по 3-D Secure будет управлять ЮKassa.
    enforce: bool | None = None

    return_url: str

    @field_validator('return_url')
    def check_return_url(cls, value: str) -> str:
        if len(value) > 2048:
            raise ValueError("Return URL must be less than 2048  characters")
        return value


class CancellationDetails(BaseModel):
    party: CancellationStatus  # Участник процесса платежа, который принял решение об отмене транзакции. Может принимать значения yoo_money, payment_network и merchant.
    reason: str  # Причина отмены платежа


__all__ = [
    'Confirmation',
    'EmbeddedConfirmation',
    'ExternalConfirmation',
    'MobileApplicationConfirmation',
    'QRConfirmation',
    'RedirectConfirmation',
    'CancellationDetails',
]
