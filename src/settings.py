import os
from typing import Literal, Self

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["Settings"]


ex = Literal["forbid", "ignore"]


class AppSettingsWithFactory(BaseSettings):
    DEBUG: bool = Field(default=False, validation_alias="DEBUG")
    LOG_DIR: str = Field()

    @property
    def mode(self):
        return "DEBUG" if self.DEBUG else "PRODUCTION"

    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    @classmethod
    def load(cls, env_path: str, log_dir: str, logger) -> Self:
        USE_FILE = os.path.exists(env_path)
        if not USE_FILE:
            logger.warning(f"File {env_path} not found")
        return cls(
            _env_file=env_path if USE_FILE else "",  # type: ignore
            LOG_DIR=log_dir,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.DEBUG:
            print(f"Log dir: {self.LOG_DIR}")


class Settings(AppSettingsWithFactory):
    shop_id: int = Field(validation_alias="YOOKASSA_SHOP_ID")
    api_key: str = Field(validation_alias="YOOKASSA_API_KEY")
    my_kassa_id: int = Field(validation_alias="MY_YOO_KASSA_ID")