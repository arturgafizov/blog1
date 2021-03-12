from django.urls import path

from . import views


from users.views import UserRetrieveView, UploadAvatarView

urlpatterns = [
    path('', UserRetrieveView.as_view(), name='profile-detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),
    # path('', UserList.as_view(), name='user-list'),
]
