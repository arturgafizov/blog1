from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from allauth.account.models import EmailAddress

class User(AbstractUser):

    username = None
    email = models.EmailField('Email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def full_name(self):
        return self.get_full_name()

    def email_verified(self):
        email = self.emailaddress_set.filter(primary=True).first()
        return email.verified if email else False

    email_verified.boolean = True


    def __str__(self):
        return self.email
