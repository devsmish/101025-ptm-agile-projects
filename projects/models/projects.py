from django.db import models
from django.utils import timezone
from .project_file import ProjectFile

"""Создайте модель Project со следующими полями:
Название проекта: строковое, уникальное
Описание проекта: строковое, большое поле, обязательно к заполнению
Дата создания проекта: должна проставляться автоматически при создании"""

class Project(models.Model):
    pr_title = models.CharField(max_length=160, null=False)
    pr_description = models.TextField(null=False)
    pr_date_create = models.DateField(default=timezone.now) # models.DateField(auto_now_add=True)

    files = models.ManyToManyField(ProjectFile, related_name='projects', blank=True)

    class Meta:
        ordering = ['-pr_title']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'projects'
        unique_together = ['pr_title', 'pr_description']

    @property
    def file_count(self):
        return self.files.count()

    def __str__(self):
        return self.pr_title
