from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=64)
    startingbid = models.IntegerField(null=True, blank=False)
    link = models.URLField(blank=True)
    time = models.DateTimeField(auto_now=True)
    watchlist = models.BooleanField(default=False)    
    


class Bids(models.Model):
    price = models.IntegerField(null=True, blank=False)


class Comments(models.Model):
    comments = models.TextField(null=True, blank=False)
