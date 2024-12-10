import os

from dotenv import load_dotenv

load_dotenv(".env")

YOOKASSA_SHOP_ID: str = os.getenv("YOOKASSA_SHOP_ID")
YOOKASSA_API_KEY: str = os.getenv("YOOKASSA_API_KEY")