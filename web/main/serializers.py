from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class FullUserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ('id', 'get_full_name', 'email', 'first_name', 'last_name',)


class UserSerializer(FullUserSerializer):
    class Meta:
        model = User
        fields = ('id', 'get_full_name')
