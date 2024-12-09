from messages.payment_methods import PaymentMethod


class YooMoneyPaymentMethod(PaymentMethod):
    type: str = "yoo_money"