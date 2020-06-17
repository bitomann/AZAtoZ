from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Itinerary (models.Model):

    name = models.CharField(max_length=51)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("itinerary")
        verbose_name_plural = ("itineraries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("itinerary_detail", kwargs={"pk": self.pk})
