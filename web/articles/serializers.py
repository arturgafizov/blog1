from rest_framework import serializers

from .models import Article, Category, Comment
from main.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SlugField(source='get_absolute_url', allow_unicode=True)

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'parent', 'url',
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment

        fields = (
            'id', 'author', 'content', 'parent', 'updated',
        )


class ShortArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    url = serializers.SlugField(source='get_absolute_url', allow_unicode=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'category', 'created', 'updated', 'image', 'author', 'url', 'comment_count',
        )


class ArticleSerializer(ShortArticleSerializer):
    comments = CommentSerializer(many=True, source='comment_set')

    class Meta(ShortArticleSerializer.Meta):
        fields = ShortArticleSerializer.Meta.fields + ('comments', 'content', )
