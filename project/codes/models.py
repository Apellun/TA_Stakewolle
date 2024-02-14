from sqlalchemy import (
    Column, Integer,
    String, ForeignKey, DateTime
)
from sqlalchemy.orm import relationship
from core.db import Base
    

class ReferralCode(Base):
    __tablename__ = "referral_code"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    user = relationship('User', back_populates='user_code', single_parent=True)