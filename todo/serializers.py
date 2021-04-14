from rest_framework import serializers

from todo.models.todo_list import Todo
from todo.models.todo_tag import Tag


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "context", "deadline", "created_at", "tag"]


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name", "registered_date"]
        read_only_fields = ["registered_date"]
