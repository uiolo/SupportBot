import sys
import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Json, ValidationError


class Settings(BaseSettings):
    main_chat_id: int
    bot_token: SecretStr
    admins: Json

    db_host: str
    db_user: str
    db_password: SecretStr
    db_name: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

try:
    config = Settings()
except ValidationError as _ex:
    for err in _ex.errors():
        err_place = err['loc'][0]
        logging.error(f'{err_place} is not provided or just wrong. It must be string!')
    sys.exit()