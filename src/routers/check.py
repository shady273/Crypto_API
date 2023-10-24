from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
def health_check():
    return JSONResponse({
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }, status_code=200)
