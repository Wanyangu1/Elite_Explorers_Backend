# flights/models.py

from django.db import models

class FlightSearch(models.Model):
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    depart_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origin} to {self.destination}"
