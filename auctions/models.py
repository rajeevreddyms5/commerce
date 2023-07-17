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
    time = models.DateTimeField(auto_now_add=True)
    listedby = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="listed_by")
    status = models.BooleanField(default=False)
    wathlist = models.ManyToManyField(User, blank=True)
    winner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="won") 
    


class Bids(models.Model):
    bid = models.ManyToManyField(Listings)
    bidby = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="bid_by")
    bidprice = models.IntegerField(null=True, blank=False)


class Comments(models.Model):
    commentsby = models.ManyToManyField(User)
    comments = models.TextField(null=True, blank=False)
