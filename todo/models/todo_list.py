from django.db import models

from todo.models.todo_tag import Tag


class Todo(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
    )

    context = models.TextField()

    deadline = models.DateTimeField(
        null=True,
        auto_now_add=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    tag = models.ManyToManyField(
        Tag,
        verbose_name="태그"
    )

    class Meta:
        db_table = "todo.L"
