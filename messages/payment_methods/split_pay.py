from messages.payment_methods import PaymentMethod


class SplitPaymentMethod(PaymentMethod):
    type: str = "installments"