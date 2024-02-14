from datetime import datetime
from sqlalchemy import insert, select
from tests.conftest import client, async_session_maker
from codes.models import ReferralCode


def test_register():
    response = client.post("/auth/register",
                           json={
                            "email": "user1@example.com",
                            "password": "string1",
                            "username": "string1"
                            })

    assert response.status_code == 201
 
    
async def test_add_code():
    test_datetime = datetime.strptime("2025-02-14 19:09:37", "%Y-%m-%d %H:%M:%S")
    async with async_session_maker() as session:
        query = insert(ReferralCode).values(code="test", expiry_date=test_datetime, user_id=1)
        await session.execute(query)
        await session.commit()

        query = select(ReferralCode)
        result = await session.execute(query)
        result = result.first()
        assert result[0].code == 'test'
        assert result[0].expiry_date == test_datetime
 
            
def test_register_with_code():
    response = client.post("/users/code_register/test", json={
    "email": "user2@example.com",
    "password": "string2",
    "username": "string2"
    })
    
    assert response.status_code == 201


def test_get_referrals_list():
    response = client.post("/users/referrals/1")
    
    assert len(response.json()) == 1