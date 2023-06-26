from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class ActiveListing(models.Model):

    title = models.CharField(max_length=64, blank=False, default=None)
    discription = models.TextField(blank=False, default=None)
    url = models.URLField(default=None)
    startbid = models.IntegerField(default=0
                                   )
    category = models.CharField(max_length=64, blank=False, default=None)
    Listingowner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listings", default=None)
    maxbid = models.IntegerField(default=0
                                 )
    maxbidonwer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bidss", default=None)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} : {self.discription} to {self.Listingowner}"


class Comment(models.Model):

    comment = models.TextField(blank=False)
    commentlist = models.IntegerField(default=0
                                      )
    commentowner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="usercomments", default=None)


class Bid(models.Model):

    currentbid = models.IntegerField(default=0
                                     )
    biddedlist = models.IntegerField(default=0
                                     )
    bidowner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userbid", default=None)


class Watchlist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userwatch", default=None)
    list = models.IntegerField(default=0
                               )
