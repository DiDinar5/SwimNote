from django.urls import path

from athletes import views

urlpatterns = [
    path('', views.index, name='index'),
]