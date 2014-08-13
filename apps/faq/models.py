# -*- coding: utf-8 -*-
from django.db import models
from main.helper.models import *

class Faq(EntityBaseFields):
    question = models.TextField(
        verbose_name = u'Вопрос',
    )

    answer = models.TextField(
        null         = True,
        blank        = True,
        verbose_name = u'Ответ',
    )

    class Meta():
        verbose_name        = u'Вопрос-ответ'
        verbose_name_plural = u'Вопросы-ответы'

