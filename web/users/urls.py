from django.urls import path

from . import views


from users.views import UserRetrieve, UserList

urlpatterns = [
    path('<int:bk>/', UserRetrieve.as_view(), name='user-detail'),
    path('', UserList.as_view(), name='user-list'),
]
