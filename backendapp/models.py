from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
# https://app.getpostman.com/join-team?invite_code=f7cb4d2aa2b3e7e6587102b6766518f9


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    bio = models.TextField(null=True, max_length=500)
    # profile_img = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    username = models.CharField(max_length=50, null=False)
    phone = models.CharField(null=True, blank=True, max_length=22)
    location = models.CharField(max_length=100, null=True, blank=True)
    is_mover = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

