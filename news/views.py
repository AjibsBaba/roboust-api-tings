from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from news.models import Article, Author
from news.serializers import ArticleSerializer, AuthorSerializer


class ArticleViewSet(viewsets.ViewSet):
    """
    An article viewser for news articles
    """

    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ViewSet):
    """
    Views to access authors
    """

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
