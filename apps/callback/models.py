# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from main.helper.models import *
from django.conf import settings

class Callback(EntityBaseFields):
    author_user = models.ForeignKey(
        User,
        blank        = True,
        null         = True,
        editable     = False,
        verbose_name = u'Автор, зарегистрированный на сайте',
    )

    author = models.CharField(
        max_length   = 254,
        verbose_name = u'Клиент',
    )

    ip = models.CharField(
        max_length   = 20,
        blank        = True,
        null         = True,
        editable     = False,
        verbose_name = u'IP адрес',
    )

    email = models.EmailField(
        blank        = True,
        null         = True,
        verbose_name = u'Электронный адрес',
    )

    text = models.TextField(
        verbose_name = u'Отзыв',
    )

    rate = models.IntegerField(
        blank        = True,
        null         = True,
        verbose_name = u'Оценка',
    )

    class Meta():
        verbose_name        = u'Отзыв'
        verbose_name_plural = u'Отзывы'
