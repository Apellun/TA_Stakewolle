import random
import string
import smtplib
from datetime import datetime
from email.message import EmailMessage
from config import (EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD)
from core.celery import mailing


def generate_code(length=20):
    characters = string.ascii_letters + string.digits
    referral_code = ''.join(random.choice(characters) for _ in range(length))
    return referral_code


def check_code_expired(code):
    if code.expiry_date < datetime.now():
            return True
    return False


@mailing.task(name='codes.utils.send_email')
def send_email(email: str, code: str):
    msg = EmailMessage()
    msg['Subject'] = "Ваш реферальный код в API Stakewolle"
    msg['From'] = "Stakewolle API"
    msg['To'] = email
    msg.set_content(f"Привет, ваш реферальный код: {code}")

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.send_message(msg)
