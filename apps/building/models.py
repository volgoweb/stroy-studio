# -*- coding: utf-8 -*-
from django.db import models
from main.helper.models import *
from django.conf import settings

class ConstructionType(Dictionary):
    '''
    Тип конструкции жилых домов
    '''
    pass

class Foundation(Dictionary):
    '''
    Тип фундамента
    '''
    pass

class RoofCovering(Dictionary):
    '''
    Кровельное покрытие
    '''
    pass

class Building(EntityBaseFields, TitleAndSlugFields, MainImageField, DescField):
    '''
    Строение.
    Это может быть либо уже готовый дом, гараж, баня,
    либо проект.
    '''

    images = models.ManyToManyField(
        Image,
        verbose_name = u'Картинки',
        blank        = True,
        null         = True,
        related_name = 'building--images',
    )

    planning_schemes = models.ManyToManyField(
        Image,
        verbose_name = u'Схемы планировки',
        blank        = True,
        null         = True,
        related_name = 'building--planning_schemes',
    )

    construction_type = models.ForeignKey(
        ConstructionType,
        verbose_name = u'Тип конструкции',
        related_name = 'building--construction_type',
    )

    total_area = models.IntegerField(
        verbose_name = u'Общая площадь',
    )

    length = models.FloatField(
        verbose_name = u'Длина',
    )

    width = models.FloatField(
        verbose_name = u'Ширина',
    )

    foundation = models.ForeignKey(
        Foundation,
        verbose_name = u'Тип фундамента',
        related_name = 'building--foundation',
        blank        = True,
        null         = True,
    )

    external_wall = models.CharField(
        max_length   = 254,
        verbose_name = u'Внешние стены',
        blank        = True,
        null         = True,
    )

    roof_covering = models.ForeignKey(
        RoofCovering,
        verbose_name = u'Кровельное покрытие',
        related_name = 'building--roof_covering',
        blank        = True,
        null         = True,
    )

    price = models.IntegerField(
        verbose_name = u'Цена',
        blank        = True,
        null         = True,
    )

    old_price = models.IntegerField(
        verbose_name = u'Старая цена',
        blank        = True,
        null         = True,
    )

    sale = models.IntegerField(
        verbose_name = u'Скидка',
        blank        = True,
        null         = True,
    )

    view_count = models.IntegerField(
        verbose_name = u'Количество просмотров',
        blank        = True,
        null         = True,
    )

    buy_count = models.IntegerField(
        verbose_name = u'Количество купленных',
        blank        = True,
        null         = True,
    )

    def get_dimensions(self):
        return '{0}x{1} м'.format(self.length, self.width)

    def get_total_area_with_measure(self):
        return '{0} кв.м.'.format(self.total_area)

    def get_price_with_measure(self):
        return '{0} руб.'.format(self.price)

    def get_old_price_with_measure(self):
        return '{0} руб.'.format(self.old_price)

    def get_metr_price(self):
        return round(self.price / self.total_area)

    def get_metr_price_with_measure(self):
        return '{0} руб. за кв.м.'.format(self.get_metr_price())
