from django.contrib.auth.models import User
from django.db import models

from main.models import Service

APPOINTMENT_STATUS =(
    (1, "WAITING"),
    (2, "VERIFIED"),
    (3, "REJECTED"),
)


class AppointmentRequest(models.Model):
    status = models.IntegerField(choices=APPOINTMENT_STATUS, default=1, verbose_name="Status")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    services = models.ManyToManyField(Service, verbose_name="Services")
    duration_total = models.DurationField(verbose_name="Duration")
    price_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    date_from = models.DateTimeField(verbose_name="Best date for me")
    date_to = models.DateTimeField()
    extra_info = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    def __str__(self):
        return f'User: {self.user}, status: {self.status}, duration: {self.duration_total}, ' \
            f'date: {self.date_from}, created: {self.created}'

