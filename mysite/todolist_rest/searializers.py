from rest_framework import serializers

from todolist_rest.models import TodoList, Task


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["name"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["todolist", "title", "description", "is_done"]
