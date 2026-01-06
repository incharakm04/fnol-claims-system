from pydantic import BaseModel
from datetime import date

class ClaimCreate(BaseModel):
    policy_number: str
    claim_type: str
    incident_date: date
    incident_location: str
    description: str
