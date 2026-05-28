"""Напишите сериализатор для получения всех тегов.
Импортируйте модель Tag.
Импортируйте сериализатор AllTagsSerializer.
Напишите функцию, которая будет отображать список всех тегов в формате JSON."""
from rest_framework import serializers
from projects.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
