from django.contrib import admin

# Register your models here.
from appointments.models import AppointmentRequest

admin.site.register(AppointmentRequest)