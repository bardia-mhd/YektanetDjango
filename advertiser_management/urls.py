
from django.urls import path

from . import views
from .views import AdDetailRedirectView

app_name = "advertiser_management"
urlpatterns = [
    path('', views.show_home_page, name='homePage'),
    path('<int:pk>/', AdDetailRedirectView.as_view(), name='detail'),
    path('createAd/', views.AdFromView.as_view(), name='createAd'),
]
