from rest_framework import serializers

from users.models import User
# Create your serializers here.


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','phone', 'mobile', 'email', 'password')
