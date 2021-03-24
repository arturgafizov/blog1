from django.urls import path
from django.views.generic import TemplateView

from . import views


from users.views import UserRetrieveView, UploadAvatarView


urlpatterns = [
    path('', UserRetrieveView.as_view(), name='profile-detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),

]

urlpatterns += [
    path('verify/<token>/', TemplateView.as_view(), name='account_confirm_email'),
    path('verify/', TemplateView.as_view(), name='account_email_verification_sent'),
]
