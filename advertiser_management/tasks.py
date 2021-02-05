from celery import shared_task, task
from advertiser_management.models import *


@task(name='viewPerHour')
def views_per_hour(ad_id):
    a = Advertiser.objects.get(id=ad_id)
    return a.get_views()
