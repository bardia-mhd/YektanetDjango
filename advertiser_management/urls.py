
from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_home_page, name='homePage'),
    path('<int:pk>/', AdDetailRedirectView.as_view(), name='detail'),
    path('create_ad/', views.create_ad(), name='createAd'),
]
