import re

from django.shortcuts import get_object_or_404
from django.utils import timezone

from advertiser_management.models import Ad
from django.utils.datetime_safe import datetime


class ViewAdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.META.get('PATH_INFO') == '/advertiser_management/':
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            ad_lists = Ad.objects.all()
            for ad in ad_lists:
                ad.inc_views(ip)
            print('view of add')
        response = self.get_response(request)
        return response


class ClicksAdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url1 = request.META.get('PATH_INFO')
        if re.search('/advertiser_management/\d+', url1):
            x = re.split('/', request.META.get('PATH_INFO'))
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            ad = get_object_or_404(Ad, pk=x[2])
            ad.inc_clicks(ip)
            print('clicked on ad with id ' + x[2])
        response = self.get_response(request)
        return response
