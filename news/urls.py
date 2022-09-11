from rest_framework.routers import DefaultRouter
from django.urls import path

from news.views import ArticleViewSet, AuthorViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = router.urls
