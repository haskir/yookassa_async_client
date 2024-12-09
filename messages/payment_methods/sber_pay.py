from messages.payment_methods import PaymentMethod, Card


class SberPayPaymentMethod(PaymentMethod):
    type: str = "sberbank"
    card: Card
    phone: str | None