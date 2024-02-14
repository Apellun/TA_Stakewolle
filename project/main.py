import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from users.base_config import fastapi_users, auth_backend
from users.schemas import UserCreate, UserRead
from users.routers import users_router
from codes.routers import codes_router


app = FastAPI(
    title="Stakewolle API"
)
add_pagination(app)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Аутентификация"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Аутентификация"],
)
app.include_router(users_router, prefix="/users", tags=["Пользователи"])
app.include_router(codes_router, prefix="/codes", tags=["Коды"])


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, workers=3)