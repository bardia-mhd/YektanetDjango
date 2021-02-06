from celery import shared_task, task
from advertiser_management.models import *

import datetime

start_time = datetime.datetime.now().replace(hour=00, minute=00)
certain_hour = 24
end_time = start_time.replace(hour=certain_hour)


@shared_task
def task_view_hour():
    for i in Ad.objects.all().count():
        return View.objects.filter(created_at__hour__gte=datetime.now().hour - 1, ad=i,
                                   created_at__lte=datetime.now()).count()


@shared_task
def task_clicks_hour():
    for i in Ad.objects.all().count():
        return Click.objects.filter(created_at__hour__gte=datetime.now().hour - 1, ad=i,
                                    created_at__lte=datetime.now()).count()


@shared_task
def task_view_day():
    for i in Ad.objects.all().count():
        return Click.objects.filter(created_at__range=(start_time, end_time), ad=i,
                                    created_at__lte=datetime.now()).count()


@shared_task
def task_view_day():
    for i in Ad.objects.all().count():
        return View.objects.filter(created_at__range=(start_time, end_time), ad=i,
                                   created_at__lte=datetime.now()).count()
