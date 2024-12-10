from datetime import datetime, timedelta
from pprint import pprint

from env import YOOKASSA_SHOP_ID, YOOKASSA_API_KEY
from messages import Amount, CreatePayment, RedirectConfirmation
from services import GetPaymentService, CreatePaymentService
from client import YooKassaClient
from services.get import PaymentListRequest, DatetimeCriteria


async def test_get_single_payment(ID: str = "2ee90369-000f-5000-a000-14e6bfdd63bc"):
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    get_service = GetPaymentService(client)

    single_payment = await get_service.get(payment_id=ID)
    return await get_service.get(payment_id=ID)


async def test_get_payments():
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    get_service = GetPaymentService(client)
    return await get_service.get_payments(
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
