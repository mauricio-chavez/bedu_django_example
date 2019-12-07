"""Accounts URL's config"""

from django.urls import path

from rest_framework import routers

from . import views


app_name = 'accounts'

urlpatterns = [
    path('<int:id>/', views.nombre, name='nombre'),
    path('login/', views.signin, name='login'),
    path('login-class/', views.LoginView.as_view(), name='login_class'),
    path('profile/', views.perfil, name='profile'),
    path('logout/', views.signoff, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup-class/', views.SignupView.as_view(), name='signup_class'),
]
