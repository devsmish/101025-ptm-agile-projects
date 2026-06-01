from django.http import HttpResponse
from django.urls import path

from projects.views.projects import get_list_projects
from projects.views.tasks import get_list_tasks
from projects.views.tags import get_list_tags, get_tag_by_id, update_tag, create_tag, delete_tag

urlpatterns = [
    path('', lambda request: HttpResponse('hello')),
    path('projects/',get_list_projects),
    path('tasks/', get_list_tasks),
    path('tags/', get_list_tags),
    path('tags/<int:tag_id>/', get_tag_by_id),
    path('tags/<int:tag_id>/update/', update_tag),
    path('tags/tag-create/', create_tag),
    path('tags/<int:tag_id>/delete/', delete_tag),
]
