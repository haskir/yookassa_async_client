from pydantic import BaseModel


class SelfEmployed(BaseModel):
    """
    Идентификатор самозанятого в ЮKassa.
    """
    id: str


__all__ = ["SelfEmployed"]
