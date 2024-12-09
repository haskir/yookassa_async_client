from messages.payment_methods import PaymentMethod


class QiwiPaymentMethod(PaymentMethod):
    type: str = "qiwi"