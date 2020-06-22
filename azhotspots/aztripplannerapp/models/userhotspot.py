from django.db import models
from .hotspot import HotSpot
from .itinerary import Itinerary
from django.urls import reverse


class UserHotSpot(models.Model):

    notes = models.CharField(max_length=501)
    visited = models.BooleanField(default=False)
    hotspot = models.ForeignKey(HotSpot, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("userhotspot")
        verbose_name_plural = ("userhotspots")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("userhotspot_detail", kwargs={"pk": self.pk})
