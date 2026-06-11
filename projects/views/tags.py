from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from projects.models import Tag
from projects.serializers.tags import TagSerializer

@api_view(["GET"])
def get_list_tags(request):
    tag = Tag.objects.all()
    tag_list = TagSerializer(tag, many=True)
    return Response(tag_list.data)

"""Задача 17: Отображение для обновления информации о теге
Поставьте в декоратор api_view() метод для чтения ‘GET’.
Отображение для получения тега по id
Напишите отображение с принимаемым аргументом tag_id.
Проверьте существование такого тега и если он есть - вернуть информацию о нём."""

@api_view(['GET'])
def get_tag_by_id(request: Request, tag_id: int):
    try:
        tag = Tag.objects.get(id=tag_id)
    except Tag.DoesNotExist:
        return JsonResponse(
            data={'message': "wrong tag id"},
            status=status.HTTP_404_NOT_FOUND
        )

    serialized_data = TagSerializer(tag)

    return JsonResponse(
        data=serialized_data.data,
        status=status.HTTP_200_OK
    )

# variant 2
    tag = get_object_or_404(Tag, id=tag_id)
    serialized_data = TagSerializer(tag)

    return JsonResponse(
        data=serialized_data.data,
        status=status.HTTP_200_OK
    )

"""Отображение для обновления информации о теге
Поставьте в декоратор api_view() метод для обновления ‘PUT’.
Напишите запрос, который будет получать конкретный тег по id:
Реализуйте проверку на получение объекта тега. Если объекта нет - выведите соответствующее сообщение.
Напишите отображение, которое будет принимать из тела запроса новые данные:
Реализуйте проверку валидации полученных данных.
Обновите полученный объект тега новыми данными и сохраните его."""
@api_view(['PUT'])
def update_tag(request: Request, tag_id: int):
    tag = get_object_or_404(Tag, id=tag_id)
    serialized_data = TagSerializer(tag, request.data)
    if serialized_data.is_valid(raise_exception=True):
        serialized_data.save()
        return JsonResponse(
            data=serialized_data.data,
            status=status.HTTP_200_OK
        )
    return JsonResponse(
        data=serialized_data.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

"""Представление для создания тега
Поставьте в декоратор api_view() метод для обновления ‘POST’.
Напишите отображение, которое будет создавать новый объект тега.
Реализуйте проверку валидации полученных данных.
Сохраните новый объект в базе данных."""
@api_view(['POST'])
def create_tag(request: Request):
    serialized_tag = TagSerializer(data=request.data)
    if serialized_tag.is_valid(raise_exception=True):
        serialized_tag.save()
        return JsonResponse(
            data=serialized_tag.data,
            status=status.HTTP_201_CREATED
        )
    return JsonResponse(
        data=serialized_tag.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

"""Представление для удаления тега
Поставьте в декоратор api_view() метод для обновления ‘DELETE’.
Напишите запрос, который будет получать конкретный тег по id.
Напишите отображение, которое будет удалять полученный объект тега и выводить сообщение об успешном удалении."""
@api_view(['DELETE'])
def delete_tag(request: Request, tag_id: int):
    tag = get_object_or_404(Tag, id=tag_id)
    serialized_data = TagSerializer(tag)
    tag.delete()

    return JsonResponse(
        data=serialized_data.data,
        status=status.HTTP_200_OK
    )
