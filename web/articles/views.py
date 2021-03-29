from rest_framework import views
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import mixins
from drf_yasg.utils import swagger_auto_schema

from .models import Article, Category
from . import serializers
from . import swagger_schemas as schemas


class ArticleViewSet(ModelViewSet):
    serializer_class = serializers.ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()

