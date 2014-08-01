# -*- coding: utf-8 -*-
from django.db import models
from page.models import Page
from helper.models import *

class News(Page, DateField):
    class Meta():
        verbose_name        = u'Новость'
        verbose_name_plural = u'Новости'

