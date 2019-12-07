"""Cats app models"""

from django.contrib.auth.models import User
from django.db import models


class Cat(models.Model):
    """Cat model"""
    name = models.CharField(max_length=15)
    breed = models.CharField(max_length=15)
    birthday = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' (' + self.breed + ')'