from celery import shared_task, task
from advertiser_management.models import *

import datetime

start_time = datetime.datetime.now().replace(hour=00, minute=00)
certain_hour = 24
end_time = start_time.replace(hour=certain_hour)


@shared_task
def task_view_hour():
    ads = Ad.objects.all()
    for ad in ads:
        time = datetime.now() - timedelta(hours=1)
        status = hour_status.objects.create(ad=ad, time=time)
        return View.objects.filter(ad=ad, time=time).count()


@shared_task
def task_click_hour():
    ads = Ad.objects.all()
    for ad in ads:
        time = datetime.now() - timedelta(hours=1)
        status = daily_status.objects.create(ad=ad, time=time)
        return Click.objects.filter(ad=ad, time=time).count()


@shared_task
def task_view_hour():
    ads = Ad.objects.all()
    for ad in ads:
        time = start_time - end_time
        status = hour_status.objects.create(ad=ad, time=time)
        return View.objects.filter(ad=ad, created_at__range=time).count()


@shared_task
def task_click_hour():
    ads = Ad.objects.all()
    for ad in ads:
        time = start_time - end_time
        status = daily_status.objects.create(ad=ad, time=time)
        return Click.objects.filter(ad=ad, create_ad__range=time).count()
