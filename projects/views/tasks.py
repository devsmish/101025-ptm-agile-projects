from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from projects.models import Task
from projects.serializers.tasks import TaskSerializer, TaskInfoSerializer


"""Напишите сериализатор для модели Task с полями id, name, status, priority для получения общей информации о задачах.
Импортируйте написанный ранее сериализатор AllTasksSerializer
Напишите отображение, которое будет выводить JSON данные о всех задачах из базы данных:
"""

@api_view(["GET"])
def get_list_tasks(request: Request):
    task = Task.objects.all()
    task_list = TaskSerializer(task, many=True)
    return Response(
        data=task_list.data,
        status=status.HTTP_200_OK
    )


"""Детальная информация о задаче
Импортируйте сериализатор TaskInfoSerializer.
Напишите функцию с аргументом task_id для получения детальной информации о задаче:
Проверьте существование задачи по её id. Если задачи нет - выведите соответствующее сообщение, если задача есть - 
выведите её содержимое."""


@api_view(["GET"])
def get_task_detail(request: Request, task_id: int):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(
            data={"message": f"Task with id {task_id} not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    serialized_data = TaskInfoSerializer(task)

    return Response(
        data=serialized_data.data,
        status=status.HTTP_200_OK
    )
