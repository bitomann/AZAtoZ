from django.db import models
from .itinerary import Itinerary
from .user import User
from django.urls import reverse


class HotSpot (models.Model):

    name = models.CharField(max_length=50)
    image = models.CharField
    description = models.CharField(max_length=200)
    activities = models.CharField
    websiteurl = models.CharField

    class Meta:
        verbose_name = ("hotspot")
        verbose_name_plural = ("hotspots")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hotspot_detail", kwargs={"pk": self.pk})
