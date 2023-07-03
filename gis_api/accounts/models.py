from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username =  models.CharField(max_length=255, blank=True,null=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
