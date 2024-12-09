from httpx import AsyncClient, BasicAuth


class YooKassaClient:
    api: str = "https://api.yookassa.ru/v3/"

    def __init__(self, settings):
        self._settings = settings
        self._id = settings.YOOKASSA_SHOP_ID
        self._api_key = settings.YOOKASSA_API_KEY
        self._auth = BasicAuth(self._id, self._api_key)
