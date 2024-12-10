from pydantic import BaseModel

from .status import CancellationStatus


class CancellationDetails(BaseModel):
    party: CancellationStatus  # Участник процесса платежа, который принял решение об отмене транзакции. Может принимать значения yoo_money, payment_network и merchant.
    reason: str  # Причина отмены платежа


__all__ = [
    'CancellationDetails',
]