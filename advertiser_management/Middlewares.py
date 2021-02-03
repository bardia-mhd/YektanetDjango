from django.utils import timezone

from advertiser_management.models import Ad
from django.utils.datetime_safe import datetime


class ViewAdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.META.get('PATH_INFO') == '/home/':
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            ad_lists = Ad.objects.all()
            for ad in ad_lists:
                ad.inc_views(ip)
        response = self.get_response(request)
        return response
