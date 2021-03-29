import os

from random import randint

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from account.models.user import User


def upload_image(instance, filename):
  filename_base, filename_ext = os.path.splitext(filename)

  return '%s' % (
      now().strftime('%Y%m%d')+'_'+str(randint(10000000, 99999999))
  )


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

    class Meta:
        db_table = "Account.P"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(email=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
