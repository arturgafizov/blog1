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
    author = serializers.EmailField(required=False)

    class Meta:
        model = Comment

        fields = (
            'id', 'author', 'content', 'parent', 'updated', 'article',
        )

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        if not user.is_authenticated and not attrs.get('author'):
            raise serializers.ValidationError('Введите емаил')
        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            validated_data['author'] = user.email
            validated_data['user'] = user
        return Comment.objects.create(**validated_data)
        # return Comment.objects.create(
        #     author=validated_data['author'],
        #     content=validated_data['content'],
        #     article=validated_data['article'],
        #     parent=validated_data.get('parent'),
        #     user=validated_data.get('user'),
        # )


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



