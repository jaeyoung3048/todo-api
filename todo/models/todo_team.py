import uuid

from django.db import models

from account.models.user import User


class Team(models.Model):

    uid = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='Public identifier'
    )

    name = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False
    )

    leader = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    @property
    def get_id(self):
        return self.id

    class Meta:
        db_table = "todo.T"
