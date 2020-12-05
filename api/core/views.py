from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]