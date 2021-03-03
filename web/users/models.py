from django.contrib.auth import get_user_model
from django.db import models

from . import managers

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_set')
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, blank=True, max_length=255)
    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.user} {self.id}'
