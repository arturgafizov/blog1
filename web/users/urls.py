from django.urls import path

from . import views


from users.views import UserRetrieve, UserList

urlpatterns = [
    path('<int:pk>/', UserRetrieve.as_view(), name='profile-detail'),
    path('', UserList.as_view(), name='user-list'),
]
