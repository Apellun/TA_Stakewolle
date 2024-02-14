from celery import Celery
from config import REDIS_URL


mailing = Celery('mailing', broker=REDIS_URL, include=["codes.utils"])
mailing.conf.update(broker_connection_retry_on_startup=True,)