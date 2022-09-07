import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True)
    email = models.EmailField(verbose_name='Email Address', unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Active', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def unique_id(self):
        return str(self.id)

    def has_email(self):
        return str(self.email)
