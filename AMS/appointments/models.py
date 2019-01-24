from django.contrib.auth.models import User
from django.db import models

from main.models import Service

APPOINTMENT_STATUS =(
    (1, "waiting"),
    (2, "verified"),
    (3, "rejected"),
)


class AppointmentRequest(models.Model):
    status = models.IntegerField(choices=APPOINTMENT_STATUS, default=1, verbose_name="Status")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    services = models.ManyToManyField(Service, verbose_name="Services")
    duration_total = models.DurationField(verbose_name="Duration")
    date = models.DateTimeField(verbose_name="Best date for me")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    def __str__(self):
        return f'User: {self.user}, status: {self.status}, services: {self.services}, duration: {self.duration_total}'

