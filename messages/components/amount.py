from pydantic import field_validator, BaseModel


class Amount(BaseModel):
    # Сумма платежа.
    # Иногда партнеры ЮKassa берут с пользователя дополнительную комиссию, которая не входит в эту сумму.
    value: float  # Сумма в выбранной валюте. Всегда дробное значение. Разделитель дробной части — точка, разделитель тысяч отсутствует. Количество знаков после точки зависит от выбранной валюты. Пример: 1000.00.
    currency: str  # Трехбуквенный код валюты в формате ISO-4217. Пример: RUB. Должен соответствовать валюте субаккаунта (recipient.gateway_id), если вы разделяете потоки платежей, и валюте аккаунта (shopId в личном кабинете), если не разделяете.

    @field_validator('value')
    def check_value(cls, value: float) -> float:
        return float(f'{value:.2f}')

    @field_validator('currency')
    def check_currency(cls, value: str) -> str:
        if len(value) != 3:
            raise ValueError("Currency must be 3 characters long")
        return value.upper()


__all__ = [
    'Amount',
]
