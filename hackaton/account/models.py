from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser


class CustomUser(AbstractUser, AbstractBaseUser):
    username = models.CharField(blank=True, null=True, max_length=100, default="user")

    email = models.EmailField(unique=True)

    middle_name = models.CharField(max_length=100)
    birthday = models.DateTimeField(null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email