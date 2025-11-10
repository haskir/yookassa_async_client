from pydantic import BaseModel

from .status import CancellationStatus

__all__ = ["CancellationDetails"]


class CancellationDetails(BaseModel):
    """
    Участник процесса платежа, который принял решение об отмене транзакции.
    Может принимать значения yoo_money, payment_network и merchant.
    """

    party: CancellationStatus
    reason: str  # Причина отмены платежа
