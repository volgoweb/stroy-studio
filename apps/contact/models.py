# -*- coding: utf-8 -*-
from django.db import models
from main.helper.models import *

class Claim(EntityBaseFields):
    '''
    Абстрактный класс.
    Заявка.
    От этого класса наследуются "заявка на обратный звонок", "запись на встречу" и т.п.
    '''

    ip = models.CharField(
        max_length   = 25,
        blank        = True,
        null         = True,
        verbose_name = u'IP адрес',
        help_text    = u'IP адрес компьютера, с которого подается заявка.',
    )

    name = models.CharField(
        max_length   = 150,
        verbose_name = u'Ваше имя',
    )

    # TODO добавить captcha

    class Meta():
        abstract = True

class CallMeClaim(Claim):
    '''
    Заявка на обратный звонок.
    '''
    phone = models.CharField(
        max_length   = 40,
        verbose_name = u'Телефон',
    )

    time = models.CharField(
        max_length   = 254,
        verbose_name = u'Удобное время',
    )



    class Meta():
        verbose_name        = u'Заявка на обратный звонок'
        verbose_name_plural = u'Заявки на обратный звонок'

class ConsultationClaim(Claim):
    '''
    Заявка на консультацию.
    Посетитель сайта указывает свои вопросы или тему, которую хотел бы детально обсудить,
    а также свой телефон. Специалист компании подготавливает все необходимые данные,
    перезванивает песетителю сайта и отвечает на все вопросы.
    '''

    phone = models.CharField(
        max_length   = 40,
        blank        = True,
        null         = True,
        verbose_name = u'Телефон',
    )

    email = models.EmailField(
        verbose_name = u'Email',
    )

    question = models.TextField(
        verbose_name = u'Вопросы',
    )

    class Meta():
        verbose_name        = u'Заявка на консультацию'
        verbose_name_plural = u'Заявки на консультацию'

class MeetingClaim(Claim):
    '''
    Заявка для записи на встречу.
    '''

    phone = models.CharField(
        max_length   = 40,
        verbose_name = u'Телефон',
    )

    comment = models.TextField(
        verbose_name = u'Дата и цель встречи',
        help_text = u'Укажите удобные для вас день и время, а также темы, которые хотите обсудить на встрече.',
    )

    class Meta():
        verbose_name        = u'Заявка на встречу'
        verbose_name_plural = u'Заявки на встречу'

class Office(EntityBaseFields, TitleAndSlugFields):
    '''
    Описание офиса компании.
    '''

    is_main = models.BooleanField(
        default      = False,
        verbose_name = u'Главный офис',
        help_text    = u'Обычно на всех страницах сайта указывается адрес и телефон главного офиса.',
    )

    city = models.CharField(
        max_length = 50,
        null = True,
        blank = True,
        verbose_name = u'Город',
    )

    address = models.TextField(
        verbose_name = u'Адрес',
    )

    # TODO написать свое поле и виджет для удобного введения дней и часов работы и при этом возможность выводить эти данные в разных шаблонах по-разному.
    working_hours = models.TextField(
        verbose_name = u'Часы работы',
    )

    # TODO создать свое поле для хранения сериализованного массива телефонов
    phones = models.TextField(
        verbose_name = u'Телефоны',
    )
