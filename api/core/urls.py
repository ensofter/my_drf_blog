from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagDetailView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),
]