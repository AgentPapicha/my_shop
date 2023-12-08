from django.http import Http404
from rest_framework import generics

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer


class LatestArticles(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()[0:3]
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticlesPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 100


class ArticlesList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticlesList3(generics.ListAPIView):
    pagination_class = ArticlesPagination

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetail(APIView):
    def get_object(self, article_slug):
        try:
            return Article.objects.get(slug=article_slug)
        except Article.DoesNotExist:
            return Http404

    def get(self, request, article_slug, format=None):
        article = self.get_object(article_slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
