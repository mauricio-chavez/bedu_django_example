"""Cat app serializers"""

# Nativas

# Django

# Third Party
from rest_framework import serializers

# Locales
from .models import Cat


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'