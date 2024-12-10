from pydantic import BaseModel


class RecipientOnCreate(BaseModel):
    gateway_id: str  # Идентификатор субаккаунта. Используется для разделения потоков платежей в рамках одного аккаунта.


class Recipient(RecipientOnCreate):
    '''
     Получатель платежа
    '''
    account_id: str  # Идентификатор магазина в ЮKassa.


__all__ = [
    "RecipientOnCreate",
    "Recipient",
]
