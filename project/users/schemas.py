from pydantic import EmailStr
from typing import Optional
from fastapi_users import schemas
from core.schemas import BaseAPISchemaModel
    
    
class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    referrer_id: Optional[int] = None
    
    
class UserRead(BaseAPISchemaModel):
    username: str
    email: str