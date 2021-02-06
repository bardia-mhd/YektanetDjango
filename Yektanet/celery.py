import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advertiser_management.settings')

app = Celery('advertiser_management')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'last_hour_views': {
        'tasks': 'advertiser_management.tasks.task_view',
        'schedule': crontab(hour='*/1'),
        'args': 2
    },

    'last_hour_clicks': {
        'tasks': 'advertiser_management.tasks.task_clicks',
        'schedule': crontab(hour='*/1'),
        'args': 2
    },

    'last_day_views': {
        'tasks': 'advertiser_management.tasks.task_view',
        'schedule': crontab(hour='*/24'),
        'args': 2
    },

    'last_day_clicks': {
        'tasks': 'advertiser_management.tasks.task_clicks',
        'schedule': crontab(hour='*/24'),
        'args': 2
    },

}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
