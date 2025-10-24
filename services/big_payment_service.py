from .payment_cancel.service import CancelPaymentService
from .payment_capture.service import CapturePaymentService
from .payment_create.service import CreatePaymentService
from .payment_get.service import GetPaymentService


class PaymentService(CreatePaymentService, GetPaymentService, CancelPaymentService, CapturePaymentService):
    ...
