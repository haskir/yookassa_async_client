from pydantic import BaseModel

from .components import Deal, Transfer, Amount
from .receipt import Receipt


class CapturePayment(BaseModel):
    """
    Подтверждает вашу готовность принять платеж. После подтверждения платеж перейдет в статус succeeded.
    Это значит, что вы можете выдать товар или оказать услугу пользователю.
    Подтвердить можно только платеж в статусе waiting_for_capture и только в течение определенного времени (зависит от способа оплаты).
    Если вы не подтвердите платеж в отведенное время, он автоматически перейдет в статус canceled, и деньги вернутся пользователю.

    В ответ на запрос придет объект платежа в актуальном статусе.
    """
    amount: Amount
    receipt: Receipt
    airline: None
    transfers: list[Transfer]
    deal: Deal


__all__ = [
    "CapturePayment",
]
