from django.urls import path, include
from . import views
from core.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home, name='home')
]