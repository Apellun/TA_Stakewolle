from sqlalchemy import select
from tests.conftest import client, async_session_maker
from codes.models import ReferralCode


def test_register():
    response = client.post("/auth/register", json={
                        "email": "user@example.com",
                        "password": "string",
                        "username": "string"
                        })

    assert response.status_code == 201
    

def test_login():
    response = client.post("/auth/jwt/login", data={
    "username": "user@example.com",
    "password": "string"
    })
    
    token = response.json()["access_token"]
    assert token
    return token


def test_create_code():
    token = test_login()
    response = client.post("/codes/create_code/", headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 201
    assert response.json()["code"]


def test_get_code_by_email():
    token = test_login()
    response = client.get("/codes/get_by_email/", headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200


def test_delete_code():
    token = test_login()
    response = client.delete("/codes/delete_code/", headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 204
    
    
async def test_code_deleted():
    async with async_session_maker() as session:
        query = select(ReferralCode)
        result = await session.execute(query)
        assert len(result.all()) == 0