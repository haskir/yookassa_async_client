from pydantic import BaseModel


class AuthorizationDetails(BaseModel):
    rrn: str | None  # Retrieval Reference Number — уникальный идентификатор транзакции в системе эмитента.
    auth_code: str | None  # Код авторизации. Выдается эмитентом и подтверждает проведение авторизации.
    three_d_secure: bool  # Отображение пользователю формы для прохождения аутентификации по 3‑D Secure.
    # true — ЮKassa отобразила пользователю форму, чтобы он мог пройти аутентификацию по 3‑D Secure;
    # false — платеж проходил без аутентификации по 3‑D Secure.


__all__ = [
    "AuthorizationDetails",
]
