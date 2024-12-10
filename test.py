from datetime import datetime, timedelta
from pprint import pprint

from env import YOOKASSA_SHOP_ID, YOOKASSA_API_KEY
from messages import Amount, CreatePayment, RedirectConfirmation, CapturePayment
from services import GetPaymentService, CreatePaymentService
from client import YooKassaClient
from services import CancelPaymentService, CapturePaymentService, PaymentListRequest, DatetimeCriteria


async def test_get_single_payment(ID: str = "2ee90369-000f-5000-a000-14e6bfdd63bc"):
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = GetPaymentService(client)
    return await service.get(ID)


async def test_get_payments():
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = GetPaymentService(client)
    return await service.get_payments(
        r=PaymentListRequest(
            created_at=DatetimeCriteria(
                gte=datetime.now() - timedelta(days=1)
            )
        )
    )


async def test_create():
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = CreatePaymentService(client)
    p = CreatePayment(
        amount=Amount(value=100, currency='RUB'),
        description='Тестовая оплата на 100 зябликов',
        confirmation=RedirectConfirmation(return_url="https://discord.ru/")
    )
    return await service.create(p)


async def test_capture(ID: str):
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = CapturePaymentService(client)
    capture = CapturePayment(amount=Amount(value=80, currency='RUB'))
    return await service.capture(ID, capture)


async def test_cancel(ID: str):
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = CancelPaymentService(client)
    return await service.cancel(ID)