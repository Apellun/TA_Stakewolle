from datetime import datetime
from core.schemas import BaseAPISchemaModel
  
    
class ReferralCode(BaseAPISchemaModel):
    code: str
    expiry_date: datetime