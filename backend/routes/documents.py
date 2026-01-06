from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os
import shutil

from backend.services.damage_detection import analyze_damage
from backend.db_session import get_db
from backend.models.claim_document import ClaimDocument
from backend.models.claim import Claim

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = "uploads/claims"

@router.post("/upload/{claim_id}")
def upload_document(
    claim_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1️⃣ Ensure upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # 2️⃣ Save file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 3️⃣ Run damage analysis (AI simulation)
    damage_result = analyze_damage(file_path)


    # 4️⃣ Save document record
    doc = ClaimDocument(
        claim_id=claim_id,
        file_name=file.filename,
        file_type=file.content_type
    )
    db.add(doc)

    # 5️⃣ Update claim with AI damage info (if claim exists)
    claim = db.query(Claim).filter(Claim.claim_id == claim_id).first()
    if claim:
        claim.damage_type = damage_result["damage_type"]
        claim.damage_severity = damage_result["severity"]

    db.commit()

    # 6️⃣ Return response with AI output
    return {
        "message": "Document uploaded successfully",
        "file_name": file.filename,
        "ai_damage_type": damage_result["damage_type"],
        "ai_severity": damage_result["severity"]
    }
