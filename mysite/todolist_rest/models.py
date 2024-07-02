from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField()

    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f'Task(title={self.title}, description={self.description}, is_done={self.is_done}, todolist={self.todolist})'
