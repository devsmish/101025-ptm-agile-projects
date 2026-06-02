from django.contrib import admin

from projects.models import Task, Project

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'assignee', 'created_at', 'due_date',]
    list_filter = ['status', 'priority', 'project', 'created_at', 'due_date', 'assignee']
    search_fields = ['title']

    actions = ['set_status_done', 'set_priority_low', 'set_priority_middle', 'set_priority_high',
               'set_priority_critical']

    @admin.action(description='Закрыто')
    def set_status_done(self, request, queryset):
        queryset.update(status='5')  # '5' соответствует 'Done' в enums.py
        self.message_user(request, "Статус выбранных задач изменен на 'Выполнено'.")

    @admin.action(description='Низкий')
    def set_priority_low(self, request, queryset):
        queryset.update(priority='1')
        self.message_user(request, "Приоритет выбранных задач изменен на 'Низкий'.")

    @admin.action(description='Средний')
    def set_priority_middle(self, request, queryset):
        queryset.update(priority='2')
        self.message_user(request, "Приоритет выбранных задач изменен на 'Средний'.")

    @admin.action(description='Высокий')
    def set_priority_high(self, request, queryset):
        queryset.update(priority='3')
        self.message_user(request, "Приоритет выбранных задач изменен на 'Высокий'.")

    @admin.action(description='Очень высокий')
    def set_priority_critical(self, request, queryset):
        queryset.update(priority='4')  # '4' соответствует 'Critical' в enums.py
        self.message_user(request, "Приоритет выбранных задач изменен на 'Очень высокий'.")

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['pr_title', 'pr_date_create', 'count_of_files']
    list_filter = ['pr_date_create']
    search_fields = ['pr_title']
    actions = ['replace_simbols']

    @admin.display(description='count of Files')
    def count_of_files(self, obj):
        return obj.file_count

    @admin.action(description='replace_spaces_on_underscores')
    def replace_simbols(self, request, query_set):
        for project in query_set:
            project.pr_title = project.pr_title.strip().replace(' ', '_')
            project.save()
        return query_set
