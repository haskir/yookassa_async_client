from pydantic import BaseModel, field_validator

from ..components import CancellationStatus


class Confirmation(BaseModel):
    type: str  # Значение — confirmation. Код способа оплаты.


class Embedded(Confirmation):
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
    type: str = "redirect"
    confirmation_url: str  # URL, на который необходимо перенаправить пользователя для подтверждения оплаты.
    enforce: bool | None  # Запрос на проведение платежа с аутентификацией по 3-D Secure. Будет работать, если оплату банковской картой вы по умолчанию принимаете без подтверждения платежа пользователем. В остальных случаях аутентификацией по 3-D Secure будет управлять ЮKassa. Если хотите принимать платежи без дополнительного подтверждения пользователем, напишите вашему менеджеру ЮKassa.
    return_url: str | None  # URL, на который необходимо перенаправить пользователя после проведения платежа.

    @field_validator('return_url')
    def check_return_url(cls, value: str) -> str:
        if len(value) > 2048:
            raise ValueError("Return URL must be less than 2048  characters")
        return value


class CancellationDetails(BaseModel):
    party: CancellationStatus  # Участник процесса платежа, который принял решение об отмене транзакции. Может принимать значения yoo_money, payment_network и merchant.
    reason: str  # Причина отмены платежа


