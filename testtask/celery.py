from datetime import timedelta
from celery import Celery
import os
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testtask.settings')


app = Celery('testtask')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'run-every-10-minutes': {
        'task': 'accounts.tasks.update_user_intagram_statistics',
        'schedule': timedelta(minutes=1),
    },
}

