# Stakewolle API

<p>Технологии: Fast API, SQLAlchemy, Alembic, Postgres(asyncpg), Celery, Redis

## Как запустить:
1. Скачайте репозиторий
2. Заполните файл .env
3. Из корня проекта создайте виртуальное окружение и активируйте его
    `python3 -m venv venv` <br>
    `source/venv/bin/activate`
4. Запустите команду для установки зависимостей
    `pip install -r requirements.txt`
5. Перейдите в директорию project и запустите команду для стартовой миграции в базу
   `project/alembic upgrade head`
6. Запустите Celery
    `celery -A core.celery:mailing worker`
7. Запустите файл main.py или введите команду в терминале:
    `uvicorn main:app`

## Эндпоинты
### Автодокументация API доступна по адресу /docs

### /auth/
Стандартные эндпоинты fastapi-users <p>
<b>register</b> (POST) — зарегистрироваться: обязательные поля username, email, password. <p>
<b>jwt/login</b> (POST) — получить токен: нужно передать form-data с username (тут нужно ввести email) и password пользователя. <p>
<b>jwt/logout</b> (POST) - логаут для аутентифицированного пользователя. <p>

### /codes/
Доступны для аутентифицированных пользователей <p> 
<b>get_by_email</b> (GET) — получить реферальный код на электронную почту. <p>
<b>create_code</b> (POST) — создать реферальный код. <p>
<b>delete_code</b> (DELETE) — удалить реферальный код. <p>

### /users/
<b>referrals/{user_id}</b> (GET) — получить список рефералов по id реферера. <p>
<b>register/{code_str}</b> (POST) — зарегистрироваться по коду в качестве реферала. <p>

## Как тестировать:

Запустите из корневого каталога команду: <p>
`pytest` <p>
Или потестируйте на странице автодокументации. <p>
