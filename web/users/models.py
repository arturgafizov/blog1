from django.db import models

from . import managers

from main.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profiles')
    phone = models.CharField(null=True, max_length=15)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, max_length=255)

