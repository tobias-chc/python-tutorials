from pydantic import HttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Case insensitive
class AppConfig(BaseSettings):
    database_host: HttpUrl
    database_user: str = Field(min_length=5)
    database_password: str = Field(min_length=10)
    api_key: str = Field(min_length=20)


# Further config behavior of BaseSettings with SettingsConfigDict
## Check: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
## 1. Read them from a .env file
## 2. Case sensitivity should be enforced
## 3. Extra environment variables are forbidden within the .env file
class AppConfig2(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="forbid",
    )
    database_host: HttpUrl
    database_user: str = Field(min_length=5)
    database_password: str = Field(min_length=10)
    api_key: str = Field(min_length=20)
