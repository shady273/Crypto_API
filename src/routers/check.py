from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.core.dependencies import crypto_service
from src.services.crypto import CryptoServices

router = APIRouter()


@router.get("/")
def health_check():
    return JSONResponse({
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }, status_code=200)


@router.get("/data")
async def health_check(crypto_service: Annotated[CryptoServices, Depends(crypto_service)]):
    await crypto_service.update_crypto()
    return JSONResponse({
        "status_code": 200,
        "detail": "ok",
        "result": "update"
    }, status_code=200)