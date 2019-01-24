from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


DURATION_TIME_CHOICES = (

    (timedelta(minutes=15), "15 min"),
    (timedelta(minutes=30), "30 min"),
    (timedelta(minutes=45), "45 min"),
    (timedelta(hours=1), "1 hour"),
    (timedelta(hours=1, minutes=15), "1 hour 15 minutes"),
    (timedelta(hours=1, minutes=30), "1 hour 30 minutes"),
    (timedelta(hours=1, minutes=45), "1 hour 30 minutes"),
    (timedelta(hours=2), "2 hours"),
)


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    type_of = models.CharField(max_length=255, verbose_name="Type")
    duration = models.DurationField(choices=DURATION_TIME_CHOICES, blank=True, verbose_name="Duration")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")

