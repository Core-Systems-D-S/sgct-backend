from django.contrib.auth.models import AbstractUser
from django.db import models
from sgtc.choices import roles
# Create your models here.

class User(AbstractUser):
    company_rol = models.CharField(max_length=30, choices=roles)