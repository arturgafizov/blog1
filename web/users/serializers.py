from rest_framework import serializers

from users.models import Profile
# Create your serializers here.


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','phone', 'mobile', 'email', 'password')
