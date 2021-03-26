from django.urls import path
from django.views.generic import TemplateView

from . import views

from registrations.views import ChangeUserPasswordView, PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path('change-password/', ChangeUserPasswordView.as_view(), name='change_password'),
    path('signup/', views.SignUpView.as_view()),
    path('confirm-email/', views.VerifyEmailView.as_view()),
    path('signin/', views.SignInView.as_view()),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view()),
    ]

urlpatterns += [
    path('password/recovery/<uidb64>/<token>/', TemplateView.as_view(), name='password_reset_confirm')
]

urlpatterns += [
    path('verify/<token>/', TemplateView.as_view(), name='account_confirm_email'),
    path('verify/', TemplateView.as_view(), name='account_email_verification_sent'),
]
