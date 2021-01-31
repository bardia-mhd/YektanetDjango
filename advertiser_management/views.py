from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import RedirectView, FormView

from .forms import AdForm
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


class AdFromView(FormView):
    form_class = AdForm
    template_name = 'advertiser_management/create_ad.html'


    def form_valid(self, form):
        title1 = form.cleaned_data.get("title")
        advertiser_id1 = form.cleaned_data.get("advertiser_id")
        link1 = form.cleaned_data.get("link")
        img1 = form.cleaned_data.get("img")
        obj1 = Ad.objects.create(
            title=title1,
            img=img1,
            link=link1,
            clicks=0,
            views=0,
            advertiser=Advertiser.objects.get(pk=advertiser_id1)
        )
        obj1.save()
        return HttpResponseRedirect(reverse('advertiser_management:homePage'))
