from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='page2'),
    path('news/', include('news.urls'))
]