from django.db import models
from django.urls import reverse
from .user import User

class Itinerary (models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("itinerary")
        verbose_name_plural = ("itineraries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("itinerary_detail", kwargs={"pk": self.pk})
