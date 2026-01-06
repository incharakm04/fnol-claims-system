from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from backend.db_session import get_db
from backend.models.claim import Claim
from backend.schemas.claim_schema import ClaimCreate

router = APIRouter(prefix="/claim", tags=["Claims"])

@router.post("/start")
def start_claim(
    claim: ClaimCreate,
    db: Session = Depends(get_db)
):
    claim_id = f"FNOL-{uuid.uuid4().hex[:8]}"

    new_claim = Claim(
        claim_id=claim_id,
        policy_number=claim.policy_number,
        claim_type=claim.claim_type,
        incident_date=claim.incident_date,
        incident_location=claim.incident_location,
        description=claim.description,
        status="Submitted"
    )

    db.add(new_claim)
    db.commit()
    db.refresh(new_claim)

    return {
        "message": "Claim started successfully",
        "claim_id": claim_id
    }
