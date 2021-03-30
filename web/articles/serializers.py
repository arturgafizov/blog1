from rest_framework import serializers

from .models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'title', 'content', 'category', 'created', 'updated',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name', 'parent',
        )
