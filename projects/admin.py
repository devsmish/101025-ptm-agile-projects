from django.contrib import admin

from projects.models import Task, Project

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'assignee', 'created_at', 'due_date',]
    list_filter = ['status', 'priority', 'assignee',]
    search_fields = ['title']

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['pr_title', 'pr_date_create']
    list_filter = ['pr_date_create']
    actions = ['replace_simbols']

    @admin.action(description='replace_spaces_on_underscores')
    def replace_simbols(self, request, query_set):
        for project in query_set:
            project.pr_title = project.pr_title.strip().replace(' ', '_')
            project.save()
        return query_set
