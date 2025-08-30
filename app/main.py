import logging.config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api.v1.routes import api_v1_router

logging.config.dictConfig(settings.logging_config)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

app.include_router(api_v1_router)

@app.get("/")
def root():
    return {
        "message": "Hello, World!"
    }

# To run the FastAPI app in development mode, use the following command:
# uvicorn app.main:app --reload --reload-dir app