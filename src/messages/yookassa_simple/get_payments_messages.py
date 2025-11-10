from dataclasses import dataclass
from datetime import datetime

from src.messages.yookassa.components import PaymentStatus, Transfer


@dataclass(slots=True)
class PaymentList:
    items: list[Transfer]
    next_cursor: str = ""
    type: str = "list"

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)


@dataclass(slots=True)
class DatetimeCriteria:
    gte: datetime | None = None
    gt: datetime | None = None
    lte: datetime | None = None
    lt: datetime | None = None

    def __post_init__(self):
        if self.gte is None and self.gt is None and self.lte is None and self.lt is None:
            raise ValueError("At least one of the datetime criteria must be specified")

    def to_dict(self) -> dict:
        result = dict()
        if gte := self.gte:
            result["gte"] = gte.isoformat()
        if gt := self.gt:
            result["gt"] = gt.isoformat()
        if lte := self.lte:
            result["lte"] = lte.isoformat()
        if lt := self.lt:
            result["lt"] = lt.isoformat()
        return result


@dataclass(slots=True)
class PaymentListRequest:
    created_at: DatetimeCriteria | None = None
    captured_at: DatetimeCriteria | None = None
    status: PaymentStatus | None = None
    limit: int | None = None
    cursor: str = ""

    def to_dict(self) -> dict:
        result = dict()
        if created_at := self.created_at:
            arg, value = created_at.to_dict().popitem()
            result[f"created_at.{arg}"] = value
        if captured_at := self.captured_at:
            arg, value = captured_at.to_dict().popitem()
            result[f"captured_at.{arg}"] = value
        if status := self.status:
            result["status"] = status.value
        if limit := self.limit:
            result["limit"] = limit
        return result


__all__ = ["PaymentListRequest", "PaymentList", "DatetimeCriteria"]
