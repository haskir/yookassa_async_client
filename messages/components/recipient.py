from pydantic import BaseModel


class Recipient(BaseModel):
    # Получатель платежа.
    account_id: str  # Идентификатор магазина в ЮKassa.
    gateway_id: str  # Идентификатор субаккаунта. Используется для разделения потоков платежей в рамках одного аккаунта.


__all__ = [
    "Recipient",
]
