from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    path("", include(router.urls))
]