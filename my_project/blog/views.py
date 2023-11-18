from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


class LatestArticles(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()[0:3]
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
