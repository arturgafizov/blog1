from django.contrib import admin

from .models import Category, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
