"""
Example API endpoint with Swagger documentation:

    class ExampleViewSet(viewsets.ViewSet):

        @swagger_auto_schema(responses=schemas.response_schema_dict)
        def list(self, request):
            '''
            Example API for retrieving users list.

                Access for all.

                Example enum description:
                    IN_PROGRESS = 1
                    REJECTED = 2
                    CLOSED = 3
            '''
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
"""
from rest_framework import views
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from drf_yasg.utils import swagger_auto_schema

from . import services
from . import serializers
from . import swagger_schemas as schemas

from users.models import User
from users.serializers import UserSerializer

class UserRetrieve(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



