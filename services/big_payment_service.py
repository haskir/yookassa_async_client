from .payment_create.service import CreatePaymentService
from .payment_get.service import GetPaymentService
from .payment_cancel.service import CancelPaymentService
from .payment_capture.service import CapturePaymentService


class PaymentService(CreatePaymentService, GetPaymentService, CancelPaymentService, CapturePaymentService):
    ...
