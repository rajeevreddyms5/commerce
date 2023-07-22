from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Listings(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=False)
    category = models.CharField(max_length=64, blank=True)
    startingprice = models.DecimalField(null=True, blank=False, decimal_places=2, max_digits=10)
    link = models.URLField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    listedby = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="created_by")
    status = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watch")
    winner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="won") 


class Bids(models.Model):
    bidby = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="bid_by")
    bidlisting = models.ForeignKey(Listings, null=True, on_delete=models.CASCADE, related_name="bidslist")
    bidplaced = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    


class Comments(models.Model):
    comments = models.TextField(null=True, blank=False)
    commentsby = models.ManyToManyField(User, related_name="commented_by")
    commentlist = models.ManyToManyField(Listings, related_name="commented_on")
    
