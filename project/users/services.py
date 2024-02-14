from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from users.schemas import UserCreate
from codes.services import get_code_by_code_str
from codes.utils import check_code_expired
from core.exceptions import CodeExpiredException, UserDoesntExistException


async def register_with_code(code_str: str, new_user_data: UserCreate , db: AsyncSession, user_manager):
    code = await get_code_by_code_str(code_str, db)
    if check_code_expired(code):
        raise CodeExpiredException
    new_user_data.referrer_id = code.user_id
    new_refferal = await user_manager.create(new_user_data)
    return new_refferal


async def get_referrals_list(user_id: int, db: AsyncSession):
    try:
        user = await db.execute(
            select(User)
            .options(joinedload(User.referrals))
            .where(User.id == user_id)
        )
        user = user.scalars().unique().one()
        return user.referrals
    except NoResultFound:
        raise UserDoesntExistException