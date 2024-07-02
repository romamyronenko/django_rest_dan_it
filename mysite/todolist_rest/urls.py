from django.urls import path, include
from rest_framework import routers

from todolist_rest.views import TodoListViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register('todolists', TodoListViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
