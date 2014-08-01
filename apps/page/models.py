# -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField
from django.conf import settings
from helper.models import *

class Page(EntityBaseFields, MainImageField):
    '''
    Любая статическая страница сайта.
    '''
    # title = models.CharField(
    #     max_length   = 254,
    #     verbose_name = u'Заголовок',
    # )

    # slug  = AutoSlugField(
    #     populate_from = 'title',
    #     always_update = True,
    #     editable      = True,
    #     null          = True,
    #     blank         = True,
    #     verbose_name  = u'Идентификатор для url',
    #     help_text     = u'Если оставить пустым, то сгенерируется автоматически.',
    # )

    body  = models.TextField(
        verbose_name = u'Содержимое',
    )

    # main_img = models.ImageField(
    #     upload_to    = settings.IMAGES_UPLOAD_FOLDER,
    #     blank        = True,
    #     null         = True,
    #     verbose_name = u'Главная картинка',
    # )

    images = models.ManyToManyField(
        Image,
        verbose_name = u'Картинки',
        blank        = True,
        null         = True,
        related_name = 'page__images',
    )

    class Meta():
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'

    # def __unicode__(self):
    #     return self.title

    # def get_absolute_url(self):
    #     return self.slug
