from django.db import models

from .choices import ArticleStatus

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='parent_set', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    objects = models.Manager()


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='article_set')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    hidden = models.SmallIntegerField(choices=ArticleStatus.choices, default=ArticleStatus.ACTIVE)

    objects = models.Manager()

    def get_category(self):
        return ",".join([str(p.name) for p in self.category.all()])

