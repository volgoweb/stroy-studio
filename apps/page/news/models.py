# -*- coding: utf-8 -*-
from django.db import models
from main.page.models import Page
from main.helper.models import *

class News(Page, DateField):
    class Meta():
        verbose_name        = u'Новость'
        verbose_name_plural = u'Новости'

