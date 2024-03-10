from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    has_verified_email = models.BooleanField(default=False)
    
class Subscription(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    tier = models.CharField(max_length=100, default='Free')

    def __str__ (self):
        return self.email.username