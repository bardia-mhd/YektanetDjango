from django.db import models

# Create your models here.
from django.db.models import Sum


class Advertiser(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    name = models.CharField(max_length=150)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @staticmethod
    def get_total_clicks():
        return Advertiser.objects.aggregate(Sum('clicks'))

    def describe_me(self):
        return "this class is made for advertisers!"

    @staticmethod
    def help():
        return "this class has name,clicks,id,views\n" + "and it has setter/getter methods" + "and it extends BaseAdvertising class"

    def get_clicks(self):
        return self.clicks

    def inc_clicks(self):
        self.clicks += 1

    def inc_views(self):
        self.views += 1

    def get_views(self):
        return self.views


class Ad(models.Model):
    title = models.CharField(max_length=150)
    imgUrl = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_imgUrl(self):
        return self.imgUrl

    def set_imgUrl(self, imgUrl):
        self.imgUrl = imgUrl

    def get_link(self):
        return self.link

    def set_link(self, link):
        self.link = link

    def set_advertiser(self, advertiser):
        self.advertiser = advertiser

    def get_clicks(self):
        return self.clicks

    def inc_clicks(self):
        self.advertiser.inc_clicks()
        self.clicks += 1

    def inc_views(self):
        self.advertiser.inc_views()
        self.views += 1

    def get_views(self):
        return self.views
