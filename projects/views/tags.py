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

