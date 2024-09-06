from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=256)
    birthday = models.DateField()
    livesPlace = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, blank=True, default="")
    