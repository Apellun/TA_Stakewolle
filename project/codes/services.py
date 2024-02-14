from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select
from users.models import User
from codes.models import ReferralCode
from codes.utils import check_code_expired, generate_code, send_email
from core.exceptions import (
    CodeExistsException,
    CodeDoesntExistException,
    CodeExpiredException
)


async def get_code_by_user_id(user_id: int, db: AsyncSession):
    try:
        code = await db.execute(
            select(ReferralCode)
            .where(ReferralCode.user_id == user_id)
        )
        code = code.scalars().unique().one()
        return code
    except NoResultFound:
        raise CodeDoesntExistException


async def get_code_by_code_str(code_str: str, db: AsyncSession):
    try:
        code = await db.execute(
            select(ReferralCode)
            .where(ReferralCode.code == code_str)
        )
        code = code.scalars().unique().one()
        return code
    except NoResultFound:
        raise CodeDoesntExistException


async def create_code(user_id: int, db: AsyncSession):
    try:
        code = await get_code_by_user_id(user_id, db)
    except CodeDoesntExistException:
        code = ReferralCode(
            code = generate_code(),
            expiry_date = datetime.now() + relativedelta(months=1),
            user_id = user_id
        )
        db.add(code)
        await db.flush()
        await db.commit()
        await db.refresh(code)
        return code
    
    if check_code_expired(code):
            await db.delete(code)
            code = ReferralCode(
            code = generate_code(),
            expiry_date = datetime.now() + relativedelta(months=1),
            user_id = user_id
            )
            db.add(code)
            await db.flush()
            await db.commit()
            await db.refresh(code)
            return code
    else:
        raise CodeExistsException
    

async def delete_code(user_id: int, db: AsyncSession):
    code = await get_code_by_user_id(user_id, db)
    await db.delete(code)
    await db.commit()
    

async def send_code_to_email(user: User, db: AsyncSession):
    code = await get_code_by_user_id(user.id, db)
    if check_code_expired(code):
        raise CodeExpiredException
    else:
        send_email.delay(user.email, code.code)