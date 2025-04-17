# backend/app/api.py
from fastapi import APIRouter, HTTPException
from app.services.OCR import OCR

router = APIRouter(prefix="/text-ai-assistance")

@router.post("/", tags=["text"])
async def doc_to_text(text: str = "") -> dict:
    try:
        converter = OCR()
        result = converter.Query(text)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Assistance failed: {str(e)}")