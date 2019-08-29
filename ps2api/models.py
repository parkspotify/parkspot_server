from django.db import models
from django.contrib.auth.backends import get_user_model

# Create your models here.
USER = get_user_model()


class Raspberry(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitute = models.FloatField()
    parkspots = models.IntegerField()

    def detected_parkspot(self):
        self.parkspots = self.parkspots + 1

    def set_location(self, longitude, latitude):
        self.longitude = longitude
        self.latitute = latitude
