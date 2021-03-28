import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from account.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    uid = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='Public identifier'
    )

    email = models.EmailField(
        unique=True,
        max_length=128,
    )

    first_name = models.CharField(
        blank=False,
        max_length=128
    )

    last_name = models.CharField(
        blank=False,
        max_length=128
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_admin = models.BooleanField(
        default=False
    )

    refresh_token = models.TextField(
        null=True,
        default=None,
    )

    EMAIL_FIELDS = 'email'
    USERNAME_FIELD = 'email'
