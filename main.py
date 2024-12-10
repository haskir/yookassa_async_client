import asyncio
from datetime import datetime, timedelta
from pprint import pprint

from env import YOOKASSA_SHOP_ID, YOOKASSA_API_KEY
from service import GetService
from client import YooKassaClient
from service.get import PaymentListRequest, DatetimeCriteria


async def main():
    client = YooKassaClient(shop_id=YOOKASSA_SHOP_ID, api_key=YOOKASSA_API_KEY)
    get_service = GetService(client)

    test_id = "2ee90369-000f-5000-a000-14e6bfdd63bc"
    res = await get_service.get_payments(
        r=PaymentListRequest(created_at=DatetimeCriteria(gte=datetime.now() - timedelta(days=1)))
    )
    print(res)
    pprint(res)

asyncio.run(main())
