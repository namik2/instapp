from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True, blank=True)


    USERNAME_FIELD = 'email' #because Account.username' must be unique because it is named as the 'USERNAME_FIELD'
    REQUIRED_FIELDS = ['username']