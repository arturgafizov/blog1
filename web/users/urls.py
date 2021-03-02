from django.urls import path

from . import views


from users.views import UserRetrieve

urlpatterns = [
    path('<int:pk>/', UserRetrieve.as_view(), name='user-detail')
]
