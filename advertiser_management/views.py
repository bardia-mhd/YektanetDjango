from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.views.generic import RedirectView

from .models import Advertiser, Ad


class AdDetailRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'detail'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        ad.incClicks()
        self.url = ad.link
        return ad.link


def show_home_page(request):
    advertisers_list = Advertiser.objects.all()
    context = {"advertisers_list": advertisers_list}
    ad_lists = Ad.objects.all()
    for ad in ad_lists:
        ad.incViews()
    return render(request, 'advertiser_management/home_page.html', context)


def create_ad(request):
    pass
