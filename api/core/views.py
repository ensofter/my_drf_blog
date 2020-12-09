from rest_framework import viewsets
from .serializers import PostSerializer, TagSerializer
from .models import Post
from taggit.models import Tag
from rest_framework import permissions
from rest_framework import pagination


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    ordering = 'created'


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
