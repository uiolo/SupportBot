from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Json, JsonValue


class Settings(BaseSettings):
    bot_token: SecretStr
    admins: Json

    db_host: str
    db_user: str
    db_password: SecretStr
    db_name: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()