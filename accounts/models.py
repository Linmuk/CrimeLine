from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('citizen', 'Citizen'),
        ('admin', 'Administrator'),
    ]
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='citizen')

    def __str__(self):
        return self.username