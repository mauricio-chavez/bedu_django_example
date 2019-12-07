"""Cats app views"""

# Nativas

# Django
from django.http import JsonResponse

# Third-party
from rest_framework import viewsets

# Locales
from .models import Cat
from .serializers import CatSerializer


def index(request):
    return JsonResponse({
        'message': 'Hola mundo'
    })



class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer