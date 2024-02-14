from fastapi import Depends, APIRouter
from fastapi_pagination import Page, paginate
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from users.manager import get_user_manager
from users import services
from users.schemas import UserRead, UserCreate

users_router = APIRouter()


@users_router.get('/referrals/{user_id}', status_code=200, response_model=Page[UserRead])
async def get_referrals_list(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Получение информации о рефералах по id реферера
    """
    results = await services.get_referrals_list(user_id, db)
    return paginate(results)


@users_router.post('/code_register/{code_str}', status_code=201, response_model=UserRead)
async def register_with_code(code_str: str, new_user_data: UserCreate, db: AsyncSession = Depends(get_db), user_manager = Depends(get_user_manager)):
    """
    Регистрация по реферальному коду в качестве реферала.
    """
    result = await services.register_with_code(code_str, new_user_data, db, user_manager)
    return result