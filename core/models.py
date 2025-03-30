from django.db import models
from django.contrib.auth.models import AbstractUser
from core.manager import UserManager

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []