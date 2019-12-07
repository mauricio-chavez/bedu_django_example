"""Bedu Django URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from cats import views as cats_views
from accounts import views as accounts_views

router = routers.DefaultRouter()
router.register('cats', cats_views.CatViewSet)
router.register('api/accounts', accounts_views.UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
] + router.urls
