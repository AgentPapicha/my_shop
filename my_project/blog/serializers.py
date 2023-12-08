from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):  # FIXME: better to use HyperLinkedModelSerializer
    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "article_text",
            "created_at",
            "author_name",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )
