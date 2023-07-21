from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Listings(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=False)
    category = models.CharField(max_length=64, blank=True)
    bidprice = models.DecimalField(null=True, blank=False, decimal_places=2, max_digits=10)
    link = models.URLField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    listedby = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="created_by")
    status = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watch")
    winner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="won") 


class Bids(models.Model):
    bid = models.ManyToManyField(Listings)
    bidby = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="bid_by")


class Comments(models.Model):
    commentsby = models.ManyToManyField(User)
    comments = models.TextField(null=True, blank=False)
