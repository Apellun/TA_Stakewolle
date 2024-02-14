from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from users.utils import user
from codes.schemas import ReferralCode
from core.db import get_db
from codes import services

codes_router = APIRouter()


@codes_router.get('/get_by_email/', status_code=200)
async def get_code_by_email(user = Depends(user), db: AsyncSession = Depends(get_db)):
    """
    Получение реферального кода по email адресу для аутентифицированного пользователя.
    """
    await services.send_code_to_email(user, db)


@codes_router.post('/create_code/', status_code=201, response_model=ReferralCode)
async def create_code(user = Depends(user), db: AsyncSession = Depends(get_db)):
    """
    Создание кода для аутентифицированного пользователя.
    """
    result = await services.create_code(user.id, db)
    return result


@codes_router.delete('/delete_code/', status_code=204)
async def delete_code(user = Depends(user), db: AsyncSession = Depends(get_db)):
    """
    Удаление кода для аутентифицированного пользователя.
    """
    await services.delete_code(user.id, db)