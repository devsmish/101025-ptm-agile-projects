from rest_framework import serializers
from projects.models import Task
from projects.serializers.tags import TagSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "status", "priority"]


"""Подробная информация о задаче
Напишите сериализатор TaskInfoSerializer для получения подробной информации о задаче.
Поле для тегов должно быть вложенным объектом, которым является уже готовый сериализатор TagsSerializer."""
class TaskInfoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
