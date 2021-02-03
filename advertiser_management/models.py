from django.db import models
import operator
from datetime import timedelta

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

    def get_last_2_hour_clicks(self):
        clicks_list_temp = []
        for i in range(2):
            time_threshold = timezone.now() - timedelta(hours=(i + 1))
            results = self.click_set.filter(time__gt=time_threshold).count()
            if i > 0:
                clicks_sum = 0
                for j in range(i):
                    clicks_sum += clicks_list_temp[j]
                results -= clicks_sum
            clicks_list_temp.append(results)
        return clicks_list_temp

    def get_last_2_hour_views(self):
        views_list_temp = []
        for i in range(2):
            time_threshold = timezone.now() - timedelta(hours=(i + 1))
            results = self.view_set.filter(time__gt=time_threshold).count()
            if i > 0:
                views_sum = 0
                for j in range(i):
                    views_sum += views_list_temp[j]
                results -= views_sum
            views_list_temp.append(results)
        return views_list_temp

    def get_clicks_with_views(self):
        list_clicks = self.get_last_2_hour_clicks()
        list_views = self.get_last_2_hour_views()
        temp_dict = {}
        for i in range(5):
            if list_views[i] != 0:
                x = list_clicks[i]/list_views[i]
                x = round(x, 3)
            else:
                x = 0
            time_threshold = timezone.now() - timedelta(hours=(i+1))
            temp_dict ['hour ' + str(time_threshold)] = x
        sorted_dict = sorted(temp_dict.items(), key=operator.itemgetter(1))
        sorted_dict.reverse()
        return sorted_dict

    def get_average_between_view_and_clicks(self):
        temp_sum = 0
        for click in self.click_set.all():
            for view in self.view_set.all():
                if view.get_ip() == click.get_ip() and view.get_time() < click.get_time():
                    selected_view = view
            time = click.get_time - selected_view.get_time()
            temp_sum += time.seconds
            avg = round(temp_sum / self.click_set.count(), 3)
            print('average second : ' + str(avg))
            average_time = str(timedelta(seconds=avg))
            return average_time

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
