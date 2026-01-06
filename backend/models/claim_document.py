from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from backend.models.base import Base

class ClaimDocument(Base):
    __tablename__ = "claim_documents"

    id = Column(Integer, primary_key=True, index=True)
    claim_id = Column(String(30), ForeignKey("claims.claim_id"))
    file_name = Column(String(255), nullable=False)
    file_type = Column(String(50))
    uploaded_at = Column(TIMESTAMP)
