
from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_home_page, name='homePage'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('create_ad/', views.create_ad(), name='createAd'),
]
