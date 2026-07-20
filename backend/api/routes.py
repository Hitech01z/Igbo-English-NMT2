from fastapi import APIRouter
from pydantic import BaseModel

from api.translator import translator_service

router = APIRouter()


class TranslationRequest(BaseModel):
    text: str
    source: str | None = None
    target: str | None = None


@router.get("/")
def root():
    return {
        "message": "Igbo-English NMT API is running."
    }


@router.post("/translate")
def translate(request: TranslationRequest):

    return translator_service.translate(
        request.text
    )