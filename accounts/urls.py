"""Accounts URL's config"""

from django.urls import path

from .views import sign_in, perfil, signoff, signup, nombre


app_name = 'accounts'
urlpatterns = [
    path('<int:id>/', nombre, name='nombre'),
    path('login/', sign_in, name='login'),
    path('profile/', perfil, name='profile'),
    path('logout/', signoff, name='logout'),
    path('signup/', signup, name='signup'),
]
