from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class FastAPIConfig(BaseSettings):
    app_host: str = os.environ.get("APP_HOST")
    app_port: int = os.environ.get("APP_PORT")
    reload: bool = True


config = FastAPIConfig()


class DBConfig(BaseSettings):
    db_host: str = os.environ.get("DB_HOST")
    db_port: str = os.environ.get("DB_PORT")
    db_name: str = os.environ.get("DB_NAME")
    db_user: str = os.environ.get("DB_USER")
    db_pass: str = os.environ.get("DB_PASS")


db_config = DBConfig()
