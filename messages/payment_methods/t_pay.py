from messages.payment_methods import Card, PaymentMethod


class TPaymentMethod(PaymentMethod):
    type = "tinkoff_bank"
    card: Card