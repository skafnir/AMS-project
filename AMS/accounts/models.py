from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=64, blank=True)
    street = models.CharField(max_length=64, blank=True)
    postal_code = models.CharField(max_length=5, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return f'{self.user}, {self.phone_number}'

