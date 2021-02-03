from django.db import models

# Create your models here.
from django.db.models import Sum
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Advertiser(models.Model):
    name = models.CharField(max_length=150)

    @staticmethod
    def get_total_clicks():
        return Advertiser.objects.aggregate(Sum('clicks')).get('clicks__sum')

    def inc_views(self):
        sum = 0
        for ad in self.ad_set.all():
            sum += ad.get_clicks()
        return sum

    def get_views(self):
        sum = 0
        for ad in self.ad_set.all():
            sum += ad.get_views()
        return sum


class Ad(models.Model):
    title = models.CharField(max_length=150)
    imgUrl = models.CharField(max_length=300)
    img = models.ImageField(upload_to='images', default='default.jpg')
    link = models.URLField(max_length=300)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    def get_clicks(self):
        return self.click_set.count()

    def inc_clicks(self, ip):
        obj1 = Click.objects.create(
            ad=self,
            time=timezone.now(),
            user_ip=ip
        )
        obj1.save()

    def inc_views(self, ip):
        obj1 = Click.objects.create(
            ad=self,
            time=timezone.now(),
            user_ip=ip
        )
        obj1.save()

    def get_views(self):
        return self.view_set.count()

    def is_approve(self):
        return self.approve


class View(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    user_ip = models.GenericIPAddressField()

    def get_ip(self):
        return self.user_ip

    def get_time(self):
        return self.time

    def set_ip(self, ip):
        self.user_ip = ip


class Click(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    user_ip = models.GenericIPAddressField()

    def get_ip(self):
        return self.user_ip

    def get_time(self):
        return self.time

    def set_ip(self, ip):
        self.user_ip = ip
