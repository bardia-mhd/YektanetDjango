from django.urls import path

from . import views
from .views import AdDetailRedirectView

app_name = "advertiser_management"
urlpatterns = [
    path('', views.HomePageView.as_view(), name='homePage'),
    path('<int:pk>/', AdDetailRedirectView.as_view(), name='detail'),
    path('createAd/', views.AdFromView.as_view(), name='createAd'),
    path('<int:pk>/details/', views.AdDetails.as_view(), name='adDetails'),
    path('searchAd/', views.SearchAdForm.as_view(), name='searchAd'),
]
