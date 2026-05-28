'''Напишите функцию, которая будет обрабатывать GET запросы для получения списка всех проектов из Базы данных.
Зарегистрировать эту функцию в списке эндпоинтов в файле urls.py'''
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from projects.models import Project
from projects.serializers.projects import ProjectSerializer


@api_view(['GET'])
def get_list_projects(request):
    projects = Project.objects.all()
    pr_list = ProjectSerializer(projects,many=True)
    return Response(pr_list.data)
