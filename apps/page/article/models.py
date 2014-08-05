# -*- coding: utf-8 -*-
from django.db import models
from main.page.models import Page
from main.helper.models import *

class ArticleCategory(Dictionary):
    pass

    class Meta():
        verbose_name        = u'Категория'
        verbose_name_plural = u'Категории'

class Article(Page):
    category = models.ForeignKey(ArticleCategory, verbose_name = u'Категория', related_name = 'article--category')

    class Meta():
        verbose_name        = u'Статья'
        verbose_name_plural = u'Статьи'

    def get_absolute_url(self):
        return 'article/{0}'.format(self.slug)
