from django.contrib import admin

from todolist_rest.models import TodoList, Task

# Register your models here.

admin.register(TodoList)
admin.register(Task)
