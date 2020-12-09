from rest_framework import serializers
from .models import Post
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ("id", "h1", "title", "slug", "description", "content", "image", "created_at", "author", "tags")
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("id", "slug", "name")
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


