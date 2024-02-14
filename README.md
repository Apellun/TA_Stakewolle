# Stakewolle API

<p>Технологии: Fast API, aiosqlite, SQLAlchemy, Alembic, fastapi-users, fastapi-mail

## Как запустить:
<p>1. Скачайте репозиторий
<p>2. Заполните файл .env
<p>3. Из корня проекта создайте виртуальное окружение и включите его
<p>`python3 -m venv venv`
<p>`source/venv/bin/activate`
<p>4. Из корня проекта запустите команду для установки зависимостей
<p>`pip install -r requirements.txt`
<p>5. Перейдите в директорию project и запустите команду для стартовой миграции в базу
<p>`project/alembic upgrade head`
<p>6. Запустите файл main.py или введите команду в терминале:
<p>`uvicorn main:app`

## Эндпоинты
### Автодокументация API доступна по адресу /docs

### /auth/
Стандартные эндпоинты fastapi-users
<b>register<b> POST — Зарегистрироваться: обязательные поля username, email, password.
<b>jwt/login<b> POST — Получить токен: нужно передать form-data с username (тут нужно ввести email) и password юзера.
<b>jwt/logout<b> POST - Логаут для аутентифицированного юзера.

### /codes/
Доступны для аутентифицированных пользователей
<b>get_by_email<b> GET — получить реферальный код на электронную почту.
<b>create_code<b> POST — создать реферальный код.
<b>delete_code<b> DELETE — удалить реферальный код.

### /users/
<b>referrals/{user_id}<b> GET — получить список рефералов по id реферера.
<b>register/{code_str}<b> POST — зарегистрироваться по коду в качестве реферала.

## Как тестировать:

Запустите из корневого каталога команду:
`pytest`
Или потестируйте на странице автодокументации.
