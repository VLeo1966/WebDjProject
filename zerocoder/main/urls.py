from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Ссылка на приложение main
    path('new/', views.new),  # Ссылка на приложение weather
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
]