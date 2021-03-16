from django.urls import path

from . import views


from users.views import UserRetrieveView, UploadAvatarView, ChangeUserPasswordView

urlpatterns = [
    path('', UserRetrieveView.as_view(), name='profile-detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),
    path('change-password/', ChangeUserPasswordView.as_view(), name='change_password'),
    # path('', UserList.as_view(), name='user-list'),
]
