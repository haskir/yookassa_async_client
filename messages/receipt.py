from datetime import date

from pydantic import BaseModel, field_validator

from .components import Customer


class IndustryDetails(BaseModel):
    federal_id: str
    document_date: date
    document_number: str
    value: str


class MarkQuantity(BaseModel):
    numerator: int
    denominator: int


class Item(BaseModel):
    description: str  # Наименование
    vat_code: str  # НДС
    quantity: int  # Количество
    measure: str | None
    mark_quantity: MarkQuantity | None
    payment_subject: str | None
    payment_mode: str | None
    country_of_origin_code: str | None
    customs_declaration_number: str | None
    excise: str | None  # Сумма акциза товара с учетом копеек (тег в 54 ФЗ — 1229). Десятичное число с точностью до 2 знаков после точки.
    product_code: str | None
    mark_code_info: object | None
    mark_mode: str | None = "0"
    payment_subject_industry_details: list[IndustryDetails]

    @field_validator('country_of_origin_code')
    def check_country_of_origin_code(cls, value: str) -> str:
        if len(value) > 3:
            raise ValueError("Country of origin code must be less than 3 characters")
        return value

    @field_validator('payment_subject_industry_details')
    def check_payment_subject_industry_details(cls, value: list[IndustryDetails]) -> list[IndustryDetails]:
        if len(value) > 100:
            raise ValueError("Payment subject industry details must be less than 100 items")
        return value

    @field_validator('description')
    def check_description(cls, value: str) -> str:
        if len(value) > 128:
            raise ValueError("Description must be less than 128 characters")
        return value


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
    receipt_industry_details: list[IndustryDetails]
    receipt_operational_details: OperationalDetails | None

    @field_validator('items')
    def check_items(cls, value: list[Item]) -> list[Item]:
        if len(value) > 100:
            raise ValueError("Items must be less than 100 items")
        return value
