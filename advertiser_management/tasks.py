from celery import shared_task, task
from advertiser_management.models import *


@shared_task
def task_view(ad_id):
    a = Ad.objects.get(id={ad_id})
    return a.get_views()


@shared_task
def task_clicks(ad_id):
    a = Ad.objects.get(id={ad_id})
    return a.get_clicks()
