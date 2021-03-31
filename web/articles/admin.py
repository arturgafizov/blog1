from django.contrib import admin

from .models import Category, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'get_category')
    search_fields = ['category__name', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', )
    search_fields = ['parent', ]
