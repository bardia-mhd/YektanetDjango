from django.db import models

from .models import *


class table_view_hour(models.Model):
    ad = models.CharField(max_length=300)
    view = models.PositiveIntegerField(default=0)


class table_click_hour(models.Model):
    ad = models.CharField(max_length=300)
    click = models.PositiveIntegerField(default=0)


class table_view_day(models.Model):
    ad = models.CharField(max_length=300)
    view = models.PositiveIntegerField(default=0)


class table_click_day(models.Model):
    ad = models.CharField(max_length=300)
    click = models.PositiveIntegerField(default=0)
