from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")

def data_view(request):
    return HttpResponse('<h1>Data Page</h1><p>Это страница с данными.</p>')

def test_view(request):
    return HttpResponse('<h1>Test Page</h1><p>Это страница с тестовым содержимым.</p>')

