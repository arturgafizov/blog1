from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import mixins
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers

from .models import Article, Category, Comment
from . import serializers
from . import swagger_schemas as schemas
from .permissions import EditCommentPermission


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


class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = ()

    def get_queryset(self):
        # return Comment.objects.filter(user=self.request.user).select_related('user')
        return Comment.objects.all()

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(EditCommentPermission)
        return Response(serializer.data, status=HTTP_201_CREATED)

    # def update(self, request, **kwargs):
    #     instance = self.get_queryset()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data)
