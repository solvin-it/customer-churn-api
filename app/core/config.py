from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    """
    Application settings for the FastAPI template project.
    This class uses Pydantic's BaseSettings to load configuration from environment variables
    and provides default values for various application settings.
    It includes configurations for the application name, version, description, database connection,
    JWT settings, CORS, logging, and OAuth.
    """
    
    # Use SettingsConfigDict to define how settings are loaded
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    # Core app configurations
    app_name: str = os.getenv('APP_NAME', 'Customer Churn API')
    app_version: str = os.getenv('APP_VERSION', '0.1.0')
    app_description: str = os.getenv('APP_DESCRIPTION', 'API for predicting customer churn using machine learning.')
    app_url: str = os.getenv('APP_URL', 'http://localhost:8000')
    debug: bool = os.getenv('DEBUG', 'True') == 'True'

    # Database configurations
    # db_host: str
    # db_port: int = 3306
    # db_user: str
    # db_password: str
    # db_name: str

    # JWT
    # jwt_secret_key: str
    # jwt_algorithm: str = 'HS256'
    # jwt_expiration_minutes: int = 30
    # jwt_refresh_expiration_days: int = 7

    # CORS settings
    cors_origins: list[str] = ['*']  # Allow all origins by default
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    cors_allow_headers: list[str] = ['*']  # Allow all headers by default
    
    # Logging settings
    log_level: str = 'INFO'
    log_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # log_file: str | None = None
    logging_config: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": log_format,
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": log_level.upper(),
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["console"],
                "level": log_level.upper(),
                "propagate": False,
            },
            "uvicorn.error": {
                "handlers": ["console"],
                "level": log_level.upper(),
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["console"],
                "level": log_level.upper(),
                "propagate": False,
            },
        },
    }

    # OAuth
    # google_client_id: str | None = None
    # google_client_secret: str | None = None

    # @property
    # def database_url(self) -> str:
    #     """Construct the database URL from the individual components."""
    #     return f'mysql+asyncmy://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
    
settings = Settings()