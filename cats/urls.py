"""Cats app URLs config"""

from django.urls import path

from rest_framework import routers

from . import views


app_name = 'cats'

urlpatterns = [
    path('hola-mundo/', views.index, name='index'),
] + router.urls

