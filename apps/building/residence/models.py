# -*- coding: utf-8 -*-
from django.db import models
from main.building.models import *

class Residence(Building):
    '''
    Жилой дом с указанием всех его параметров.
    Это может быть либо уже готовый дом,
    либо проект дома.
    '''

    living_area = models.IntegerField(
        verbose_name = u'Жилая площадь',
    )

    floors_count = models.IntegerField(
        verbose_name = u'Количество этажей',
    )

    interior_wall = models.CharField(
        max_length   = 254,
        verbose_name = u'Внутренние стены',
        blank        = True,
        null         = True,
    )

    floor_desk = models.CharField(
        max_length   = 254,
        verbose_name = u'Межэтажное перекрытие',
        blank        = True,
        null         = True,
    )

    class Meta():
        verbose_name        = u'Дом'
        verbose_name_plural = u'Дома'

    def get_absolute_url(self):
        return '/residences/%d/' % self.pk
