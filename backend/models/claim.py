from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP
from backend.models.base import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_id = Column(String(30), unique=True, nullable=False)
    policy_number = Column(String(50), nullable=False)
    claim_type = Column(String(20), nullable=False)
    incident_date = Column(Date, nullable=False)
    incident_location = Column(String(255), nullable=False)
    description = Column(Text)
    damage_type = Column(String(50))
    damage_severity = Column(String(20))
    status = Column(String(20))
    created_at = Column(TIMESTAMP)
