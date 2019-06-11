from django.db import models
from django.contrib.auth.models import User

class Beer(models.Model):
    """ A Beer with some basic properties
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    abv = models.FloatField()

    def __str__(self):
        return self.name


class Review(models.Model):
    """ A review for a Beer. If a Beer is removed we should removed associated reviews 
    """
    STARS_CHOICES = [(x, f"{x} Star") for x in range(1,6)]
    beer = models.ForeignKey(to=Beer, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING) # keep reviews from deleted users
    stars = models.IntegerField(choices=STARS_CHOICES)
    comment = models.CharField(max_length=500)