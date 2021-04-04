from django.db.models import Count
from rest_framework import views
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import mixins
from drf_yasg.utils import swagger_auto_schema

from .models import Article, Category
from . import serializers
from . import swagger_schemas as schemas


class ArticleViewSet(ModelViewSet):
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ShortArticleSerializer
        return serializers.ArticleSerializer

    def get_queryset(self):
        # user = self.request.user
        # return Article.objects.filter(author=user)
        return Article.objects.all().annotate(comment_count=Count('comment_set'))


class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Category.objects.all()
