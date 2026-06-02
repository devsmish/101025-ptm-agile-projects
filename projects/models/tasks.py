from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from projects.enums import statuses, priorities
from projects.models.tags import Tag
from django.contrib.auth.models import User


"""Создайте модель Task со следующими полями:
Название задачи: строковое поле, уникальное, минимальная длина названия - 10 символов
Описание: большое строковое поле, может быть пустым
Статус: строковое поле максимальной длины в 15 символов, должно быть полем выбора разных статусов. По умолчанию все задачи новые
Приоритет: строковое поле максимальной длины в 15 символов, должно быть полем выбора разных приоритетов
Проект: связь с моделью Project, при удалении проекта все задачи должны удаляться
Дата создания задачи: поле, поддерживающее и дату, и время, заполняется автоматически только при создании
Дата обновления: поле, поддерживающее и дату, и время, заполняется автоматически всегда
Дата удаления: поле, в котором может ничего не быть"""
class Task(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=statuses, default='1')
    priority = models.CharField(max_length=15, choices=priorities)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')

    due_date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='tasks')

    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-due_date', 'assignee']
        unique_together = ['title', 'project']

    def __str__(self):
        return self.title
