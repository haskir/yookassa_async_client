from messages.payment_methods import Card, PaymentMethod


class TPaymentMethod(PaymentMethod):
    type: str = "tinkoff_bank"
    card: Card