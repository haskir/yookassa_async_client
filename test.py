from datetime import datetime, timedelta

from client import YooKassaClient
from env import *
from messages import Amount, CreatePayment, CreatePayout, PersonalData, Redirect, YooMoneyDestination
from messages.yookassa.components.currency import Currency
from services import (
    CancelPaymentService,
    CapturePaymentService,
    CreatePaymentService,
    CreatePayoutService,
    DatetimeCriteria,
    GetPaymentService,
    PaymentListRequest,
)
from services.payout_get.service import GetPayoutService


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


async def test_create_payment():
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = CreatePaymentService(client)
    p = CreatePayment(
        amount=Amount(value=100, currency=Currency.RUB),
        description='Тестовая оплата на 100 зябликов',
        confirmation=Redirect(return_url="https://discord.ru/")
    )
    return await service.create(p, "123")


async def test_capture_payment(ID: str):
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = CapturePaymentService(client)
    return await service.capture(ID, value=80, currency=Currency.RUB)


async def test_cancel_payment(ID: str):
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = CancelPaymentService(client)
    return await service.cancel(ID)


async def test_create_payout():
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = CreatePayoutService(client)
    p = CreatePayout(
        amount=Amount(value=100, currency=Currency.RUB),
        description='Тестовая выплата 100 зябликов квоуну',
        payout_destination_data=YooMoneyDestination(account_number=MY_YOO_KASSA_ID),
        personal_data=[PersonalData(id=MY_YOO_KASSA_ID)],
    )
    return await service.create(p, "create_1")


async def test_get_payout(ID: str):
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    service = GetPayoutService(client)
    return await service.get(ID)