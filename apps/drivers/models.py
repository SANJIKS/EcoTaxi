from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_latitude = models.FloatField()
    current_longitude = models.FloatField()
    last_update = models.DateTimeField(auto_now=True)
