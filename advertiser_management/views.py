from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def show_home_page(request):
    return HttpResponse("hello")


def detail(request, question_id):
    pass


def create_ad(request):
    pass
