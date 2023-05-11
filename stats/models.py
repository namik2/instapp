from django.db import models
from accounts.models import Account
# Create your models here.


class IntagramStats(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    following = models.IntegerField(default=0)
    follower = models.IntegerField(default=0)


