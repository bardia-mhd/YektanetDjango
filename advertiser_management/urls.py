from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import AdDetailRedirectView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ads', views.AdViewSet)
router.register(r'advertisers', views.AdvertiserViewSet)
router.register(r'view', views.ViewViewSet)
router.register(r'clicks', views.ClickViewSet)

app_name = "advertiser_management"
urlpatterns = [
    path('', include(router.urls)),
    path('api/login', views.login),
    # path('', views.HomePageView.as_view(), name='homePage'),
    # path('<int:pk>/', AdDetailRedirectView.as_view(), name='detail'),
    # path('createAd/', views.AdFromView.as_view(), name='createAd'),
    # path('<int:pk>/details/', views.AdDetails.as_view(), name='adDetails'),
    # path('searchAd/', views.SearchAdForm.as_view(), name='searchAd'),
]
