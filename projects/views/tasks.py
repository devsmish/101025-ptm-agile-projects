from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from projects.models import Task
from projects.serializers.tasks import TaskSerializer


"""Напишите сериализатор для модели Task с полями id, name, status, priority для получения общей информации о задачах.
Импортируйте написанный ранее сериализатор AllTasksSerializer
Напишите отображение, которое будет выводить JSON данные о всех задачах из базы данных:
"""

@api_view(["GET"])
def get_list_tasks(request):
    task = Task.objects.all()
    task_list = TaskSerializer(task, many=True)
    return Response(task_list.data)
