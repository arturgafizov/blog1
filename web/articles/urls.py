from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')

urlpatterns = [

]
urlpatterns += router.urls
