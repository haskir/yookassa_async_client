import asyncio
from pprint import pprint

from test import *


async def main():
    # created = await test_create()
    # print(f'{created['id'] = }')
    ID = "2eea3451-000f-5000-a000-123f486dd482"
    pprint(dict(await test_get_single_payment(ID)))
    # pprint(await test_capture(ID))
    # pprint(await test_cancel("2eea1a52-000f-5000-b000-142bc08f6229"))


asyncio.run(main())
