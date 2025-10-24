from datetime import date

from pydantic import BaseModel, Field

from .identificators import Customer

__all__ = [
    "IndustryDetails",
    "MarkQuantity",
    "Item",
    "OperationalDetails",
    "Receipt",
]


class IndustryDetails(BaseModel):
    federal_id: str
    document_date: date
    document_number: str
    value: str


class MarkQuantity(BaseModel):
    numerator: int
    denominator: int


class Item(BaseModel):
    description: str = Field(max_length=128)  # Наименование
    vat_code: str  # НДС
    quantity: int  # Количество
    measure: str | None
    mark_quantity: MarkQuantity | None
    payment_subject: str | None
    payment_mode: str | None
    country_of_origin_code: str | None = Field(max_length=3)
    customs_declaration_number: str | None
    excise: str | None  # Сумма акциза товара с учетом копеек. Десятичное число с точностью до 2 знаков после точки.
    product_code: str | None
    mark_code_info: object | None
    mark_mode: str | None = "0"
    payment_subject_industry_details: list[IndustryDetails] = Field(default_factory=list, max_length=100)


class OperationalDetails(BaseModel):
    operation_id: int
    value: str
    created_at: date


class Receipt(BaseModel):
    customer: Customer
    items: list[Item]
    phone: str | None
    email: str | None
    tax_system_code: str | None
    receipt_industry_details: list[IndustryDetails] = Field(default_factory=list, max_length=100)
    receipt_operational_details: OperationalDetails | None
