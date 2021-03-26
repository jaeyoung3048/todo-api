from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.manager import UserManager

import uuid, os
from random import randint


def upload_image(instance, filename):
  filename_base, filename_ext = os.path.splitext(filename)

  return '%s' % (
      now().strftime('%Y%m%d')+'_'+str(randint(10000000, 99999999))
  )


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

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

    refresh_token = models.TextField(
        null=True,
        default=None,
    )

    EMAIL_FIELDS = 'email'
    USERNAME_FIELD = 'email'


class Profile(models.Model):
    email = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        blank=False,
        max_length=128
    )

    last_name = models.CharField(
        blank=False,
        max_length=128
    )

    photo = models.ImageField(
        upload_to=upload_image,
        editable=True,
        null=True
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(email=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
