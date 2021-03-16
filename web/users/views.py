from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from dj_rest_auth.views import PasswordChangeView
from . import serializers
from . import swagger_schemas as schemas

from users.models import Profile
from users.serializers import ProfileSerializer,  UploadAvatarSerializer, UploadAvatarUserSerializer
# class UserRetrieve(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UploadAvatarView(GenericAPIView):
    # serializer_class = UploadAvatarSerializer
    serializer_class = UploadAvatarUserSerializer
    parser_classes = [FileUploadParser, ]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user).select_related('user')

    def post(self, request):
        # print(request.data)
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserRetrieveView(GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/profile_detail.html'
    serializer_class = ProfileSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user).select_related('user')

    def get(self, request):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        if serializer.is_valid():
            serializer.save()
            return Response({'profile': serializer.data}, status=status.HTTP_200_OK)
        return Response({'profile': serializer.data}, status=status.HTTP_404_NOT_FOUND)

        # return redirect('profile-detail')


class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/profile.html'

    def get(self, request):
        queryset = Profile.objects.all()
        return Response({'profiles': queryset})


class ChangeUserPasswordView(PasswordChangeView):
    pass
