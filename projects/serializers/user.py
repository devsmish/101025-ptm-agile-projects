import re

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.password_validation import validate_password
from django.db.models import CharField
from django.core.exceptions import ValidationError
from rest_framework import serializers
from projects.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'role', 'email', 'phone', 'last_login')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("id", "date_joined", "last_login", "is_active")
        exclude = ("password", "is_superuser", "is_staff", "user_permissions", "groups")

"""Создайте новый сериализатор RegisterUserSerializer для регистрации нового пользователя. Сериализатор будет обрабатывать поля:
username
first_name
last_name
email
position
password
re_password
Поле re_password - искусственно созданное поле для проверки совпадения паролей, содержит настройки:
Максимальная длина - 128 символов
Только для записи
В параметре extra_kwargs указать, что поле password строго только для записи."""



class RegisterUserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, required=True, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'password', 're_password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    """Создайте в этом сериализаторе метод validate. Этот метод должен проверять:
username (Любые буквы из латиницы, символ нижнего подчёркивания, цифры от 0 до 9)
first_name (Строго буквы из латиницы, любым регистром)
last_name (Строго буквы из латиницы, любым регистром)
password (пароль и его повторный ввод должны совпадать, так же вызов базовых проверок пароля от системы Django)
Переопределите метод create для хеширования пароля и его установке для пользователя перед созданием.
Напишите классовое отображение, которое будет принимать данные из запроса и создавать пользователя.
Зарегистрируйте новый эндпоинт, протестируйте его, чтобы убедиться, что он работает.
Закомментируйте все изменения, создайте запрос на слияние."""


    def validate(self, data):
        if not re.match(r'[a-zA-Z0-9_]+', data['username']):
            raise serializers.ValidationError("username must exist 'a-z', '0-9' and '_'")
        if not data['first_name'].isalpha():
            raise serializers.ValidationError("first_name must exist 'a-Z'")
        if not data['last_name'].isalpha():
            raise serializers.ValidationError("last_name must exist 'a-Z'")
        if not data['password']:
            raise serializers.ValidationError("password must be enter")
        if data['password'] != data['re_password']:
            raise serializers.ValidationError("passwords didn't match")
        try:
            validate_password(data['password'])
        except ValidationError as error:
            raise serializers.ValidationError(error.messages)

        return data

    def create(self, validated_data):
        validated_data.pop('re_password')
        password = validated_data.pop('password')
        # user = User.objects.create(**validated_data)
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user