import asyncio
from pprint import pprint

# from env import YOOKASSA_SHOP_ID, YOOKASSA_API_KEY
# from services import CreatePaymentService
# from messages import *
# from client import YooKassaClient

from test import *


async def main():
    # pprint(await test_create())
    pprint(await test_get_payments())
    pprint(await test_cancel("2eea1a52-000f-5000-b000-142bc08f6229"))


asyncio.run(main())
