from fastapi import APIRouter
from endpoints import transcribe

router = APIRouter()
router.include_router(transcribe.router)
