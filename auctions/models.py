from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass # Do nothing for now



class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField
    category = models.CharField(max_length=64)
    startingbid = models.IntegerField
    link = models.URLField(blank=True)
    watchlist = models.ForeignKey(User, blank=True)    
    


class Bids(models.Model):
    price = models.IntegerField


class Comments(models.Model):
    comments = models.TextField


class Activelistings(models.Model):
