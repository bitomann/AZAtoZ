from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .itinerary import Itinerary


class User(models.Model):

    username = models.CharField
    password = models.CharField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(
        Itinerary, related_name="itineraries",
        null=True, # Makes column nullable in DB
        blank=True, # Allows blank value on objects
        on_delete=models.CASCADE)


# These receiver hooks allow you to continue to
# work with the `User` class in your Python code.


# Every time a `User` is created, a matching `Itinerary`
# object will be created and attached as a one-to-one
# property
@receiver(post_save, sender=User)
def create_itinerary(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)

# Every time a `User` is saved, its matching `Itinerary`
# object will be saved.
@receiver(post_save, sender=User)
def save_itinerary(sender, instance, **kwargs):
    instance.itinerary.save()
