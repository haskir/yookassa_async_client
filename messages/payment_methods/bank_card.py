from pydantic import BaseModel, field_validator

from ..components import Confirmation, Amount, PaymentStatus, CancellationDetails, AuthorizationDetails


class CardProduct(BaseModel):
    code: str  # Код продукта карты.
    name: str | None  # Название продукта карты.


class Card(BaseModel):
    first6: str | None  # Первые 6 цифр номера карты.
    last4: str  # Последние 4 цифры номера карты.
    expiry_year: str  # Год истечения срока действия карты.
    expiry_month: str  # Месяц истечения срока действия карты.
    card_type: str  # Тип банковской карты. Возможные значения: MasterCard (для карт Mastercard и Maestro), Visa (для карт Visa и Visa Electron), Mir, UnionPay, JCB, AmericanExpress, DinersClub, DiscoverCard, InstaPayment, InstaPaymentTM, Laser, Dankort, Solo, Switch и Unknown.
    card_product: CardProduct | None  # Карточный продукт платежной системы, с которым ассоциирована банковская карта.
    issuer_country: str | None  # Код страны, в которой выпущена карта. Передается в формате ISO-3166 alpha-2. Пример: RU.
    issuer_name: str | None  # Название организации, которая выпустила карту.
    source: str | None  # Источник данных банковской карты. Возможные значения: mir_pay, apple_pay, google_pay. Присутствует, если пользователь при оплате выбрал карту, сохраненную в Mir Pay, Apple Pay или Google Pay.


class Settlement(BaseModel):
    type: str = "payout"  # Тип операции. Фиксированное значение: payout — выплата продавцу.
    amount: Amount  # Данные о сумме распределения денег.


class Deal(BaseModel):
    id: str  # Идентификатор сделки.
    settlements: list[Settlement]  # Данные о распределении денег.


class InvoiceDetails(BaseModel):
    id: str | None = None  # Идентификатор счета в ЮКасса.


class BankCard(BaseModel):
    type: str  # Значение — bank_card. Код способа оплаты.
    id: str  # Идентификатор способа оплаты.
    saved: bool  # С помощью сохраненного способа оплаты можно проводить безакцептные списания.
    title: str  # Название способа оплаты.
    card: Card  # Данные банковской карты.
    captured_at: str | None  # Время подтверждения платежа. Указывается по UTC и передается в формате ISO 8601.
    created_at: str  # Время создания способа оплаты. UTC ISO 8601 (2017-11-03T11:52:31.827Z).
    expires_at: str | None  # Время, до которого вы можете бесплатно отменить или подтвердить платеж. В указанное время платеж в статусе waiting_for_capture будет автоматически отменен. Указывается по UTC и передается в формате ISO 8601. Пример: 2017-11-03T11:52:31.827Z
    confirmation: Confirmation | None
    test: bool  # Признак тестового способа оплаты.
    refunded_amount: Amount | None  # Сумма возврата.
    paid: bool  # Признак оплаты.
    refundable: bool  # Возможность провести возврат по API.
    receipt_registration: PaymentStatus | None  # Статус регистрации чека. Возможные значения:
    metadata: dict | None
    cancellation_details: CancellationDetails | None
    authorization_details: AuthorizationDetails | None
    transfers: list | None  # Данные о распределении денег — сколько и в какой магазин нужно перевести. Присутствует, если вы используете cплитование платежей.
    deal: Deal | None  # Данные о сделке, в составе которой проходит платеж. Присутствует, если вы проводите Безопасную сделку
    merchant_customer_id: str | None  # Идентификатор покупателя в вашей системе, например электронная почта или номер телефона.
    invoice_details: InvoiceDetails | None

    @field_validator('metadata')
    def check_metadata(cls, value: dict) -> dict:
        if value is None:
            return {}
        if len(value) > 16:
            raise ValueError("Metadata must be less than 16 items")
        for key, value in value.items():
            if not isinstance(key, str):
                raise ValueError(f"Metadata key '{key}' must be a string")
            if len(key) > 32:
                raise ValueError(f"Metadata key '{key}' must be less than 32 characters")
            if len(str(value)) > 512:
                raise ValueError(f"Metadata value '{value}' must be less than 512 characters")
        return value

    @field_validator('merchant_customer_id')
    def check_merchant_customer_id(cls, value: str) -> str:
        if len(value) > 200:
            raise ValueError("Merchant customer ID must be less than 200  characters")
        return value