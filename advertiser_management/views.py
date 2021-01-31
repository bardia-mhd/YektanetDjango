from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Advertiser, Ad


def show_home_page(request):
    advertisers_list = Advertiser.objects.all()
    context = {"advertisers_list": advertisers_list}
    ad_lists = Ad.objects.all()
    for ad in ad_lists:
        ad.incViews()
    return render(request, 'advertiser_management/home_page.html', context)


def detail(request, question_id):
    pass


def create_ad(request):
    pass
