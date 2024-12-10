from client import YooKassaClient


class CancelPaymentService:
    def __init__(self, client: YooKassaClient):
        self._client = client

    async def cancel(self, ID: str):
        idem_key = f"cancel_{ID}"
        response = await self._client.post_request(path=f'payments/{ID}/cancel', idempotency_key=idem_key)
        if response.status_code == 200:
            return response.json()
        raise Exception(response.json())