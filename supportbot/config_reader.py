from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Json

class Settings(BaseSettings):
    bot_token: SecretStr
    admins: Json
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()