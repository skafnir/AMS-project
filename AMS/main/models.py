from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

