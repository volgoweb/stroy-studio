# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category',)

admin.site.register(Article, ArticleAdmin);

class ArticleCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ArticleCategory, ArticleCategoryAdmin);

