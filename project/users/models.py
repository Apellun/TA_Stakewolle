from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTable
from core.db import Base


class User(SQLAlchemyBaseUserTable, Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    is_superuser = Column(Boolean, nullable=False, default=False)
    is_verified = Column(Boolean, nullable=False, default=True)
    
    user_code = Column(Integer, ForeignKey('referral_code.id'), nullable=True)
    user_code = relationship('ReferralCode', back_populates='user', uselist=False, cascade="all, delete, delete-orphan")
    
    referrer_id = Column(Integer, ForeignKey('user.id'))
    referrer = relationship('User', remote_side=[id])
    
    referrals = relationship('User', back_populates='referrer', lazy="joined")
    