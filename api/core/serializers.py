from rest_framework import serializers
from .models import Post
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    tag = TagListSerializerField()

    class Meta:
        model = Post
        fields = ("id", "h1", "title", "url", "description", "content", "image", "created_at", "author", "tag")