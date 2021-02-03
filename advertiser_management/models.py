from django.db import models

# Create your models here.
from django.db.models import Sum


class Advertiser(models.Model):
    clicks = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=150)

    @staticmethod
    def get_total_clicks():
        return Advertiser.objects.aggregate(Sum('clicks'))

    def inc_clicks(self):
        self.clicks += 1
        self.save()

    def inc_views(self):
        self.views += 1


class Ad(models.Model):
    title = models.CharField(max_length=150)
    imgUrl = models.CharField(max_length=300)
    img = models.ImageField(upload_to='images', default='default.jpg')
    link = models.CharField(max_length=300)
    clicks = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def inc_clicks(self):
        self.advertiser.inc_clicks()
        self.clicks += 1
        self.save()
        self.advertiser.save()

    def inc_views(self):
        self.advertiser.inc_views()
        self.views += 1
        self.save()
        self.advertiser.save()

