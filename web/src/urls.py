from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import include, url
from .yasg import urlpatterns as swagger_url
from django.views.generic import TemplateView

admin_url = settings.ADMIN_URL

urlpatterns = [
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('registrations/', include('registrations.urls')),
    path('articles/', include('articles.urls')),
    path(f'{admin_url}/', admin.site.urls),
    path(f'{admin_url}/defender/', include('defender.urls')),
    path('api/', include('rest_framework.urls')),
    path('registration/', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    path('email-verification/',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),

]

urlpatterns += swagger_url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if settings.ENABLE_SILK:
        urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
