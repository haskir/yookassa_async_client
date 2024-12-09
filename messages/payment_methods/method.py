from pydantic import BaseModel


class PaymentMethod(BaseModel):
    id: str
    saved: bool  # С помощью сохраненного способа оплаты можно проводить безакцептные списания.
    title: str  # Название способа оплаты.
    type: str