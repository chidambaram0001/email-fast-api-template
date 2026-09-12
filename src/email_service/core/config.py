from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    port:int = 9000
    email_id:str = ''
    password:str = ''
    db_connection_str:str=''
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()