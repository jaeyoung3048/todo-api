from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from account.manager import UserManager

import uuid


class User(AbstractBaseUser, PermissionsMixin):

    object = UserManager()

    uid = models.UUIDField(
        unique=True,
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

    EMAIL_FIELDS = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']