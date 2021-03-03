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
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect

from . import services
from . import serializers
from . import swagger_schemas as schemas

from users.models import User
from users.serializers import UserSerializer

# class UserRetrieve(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserRetrieve(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')

#     def put(self, request, pk, format=None):
#         ...
#
#     def patch(self, request, pk, format=None):
#         ...
#
#     def delete(self, request, pk, format=None):


class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'profiles': queryset})
