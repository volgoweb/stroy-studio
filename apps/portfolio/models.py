# -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField
from django.conf import settings
from main.helper.models import *

class WorkType(Dictionary):
    '''
    Тип работы.
    '''
    pass

class Portfolio(EntityBaseFields, TitleAndSlugFields, MainImageField, DescField, DateField):
    '''
    Описание выполненной работы.
    '''

    class Meta():
        verbose_name        = u'Работа из портфолио'
        verbose_name_plural = u'Работа из портфолио'

    work_type = models.ForeignKey(
        WorkType,
        blank        = True,
        null         = True,
        verbose_name = u'Тип работ',
        related_name = 'portfolio--work_type',
    )

    images = models.ManyToManyField(
        Image,
        verbose_name = u'Картинки',
        blank        = True,
        null         = True,
        related_name = 'portfolio--images',
    )

    project_link = models.URLField(
        max_length   = 254,
        verbose_name = u'Ссылка на проект',
        help_text    = u'Полный веб-адрес страницы описания проекта здания (например, "http://www.stroyka.ru/projects/44")',
        blank        = True,
        null         = True,
    )

    address = models.TextField(
        verbose_name = u'Адрес',
        help_text    = u'Адрес выполнения работ',
        blank        = True,
        null         = True,
    )

    def get_absolute_url(self):
        return 'portfolio/{0}'.format(self.slug)
