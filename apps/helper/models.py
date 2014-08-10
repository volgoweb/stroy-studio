# -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField
from django.conf import settings

class FieldsLabelsMixin(object):
    '''
    Добавляет метод получения словаря подписей (verbose_name) всех полей модели.
    '''
    def get_field_labels(self):
        return dict([(f.name, f.verbose_name) for f in self._meta.fields])

class Dictionary(models.Model):
    '''
    Абстрактная модель для всех моделей-словарей.
    '''
    class Meta():
        abstract = True

    id = models.CharField(
        max_length   = 254,
        primary_key  = True,
        verbose_name = 'id',
    )
    title = models.CharField(
        max_length   = 254,
        verbose_name = u'Название',
    )

    def __unicode__(self):
        return self.title

class Image(models.Model):
    '''
    Модель для хранения картинок.
    '''
    image = models.ImageField(
        upload_to    = 'images',
        verbose_name = u'Картинка',
    )

    def __unicode__(self):
        return self.image.url

class EntityBaseManager(models.Manager):
    def active_objects(self):
        '''
        Возвращает активные (опубликованные) модели.
        '''
        return self.get_queryset().filter(active = True)

class EntityBaseFields(models.Model, FieldsLabelsMixin):
    '''
    Абстрактная модель, содержащая все базовые поля и методы
    для типвоых сущностей сайта (страница, новость, статья, здание и т.д.).
    '''

    class Meta():
        abstract = True

    create_date = models.DateTimeField(
        auto_now_add = True,
        editable     = False,
        verbose_name = u'Дата создания',
    )

    update_date = models.DateTimeField(
        auto_now     = True,
        editable     = False,
        verbose_name = u'Дата создания',
    )

    active = models.BooleanField(
        default      = True,
        verbose_name = u'Активно',
        help_text    = u'Если не активно, то не будет отображаться на сайте.',
    )

    objects             = models.Manager()
    entity_base_manager = EntityBaseManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

class TitleAndSlugFields(models.Model):
    '''
    Абстрактная модель для добавления распространенного поля "Заголовка"
    '''

    class Meta():
        abstract = True

    title = models.CharField(
        max_length   = 254,
        null         = True,
        blank        = True,
        verbose_name = u'Заголовок',
    )

    slug  = AutoSlugField(
        populate_from = 'title',
        unique_with   = ('id', 'title'),
        always_update = True,
        editable      = True,
        null          = True,
        blank         = True,
        verbose_name  = u'Идентификатор для url',
        help_text     = u'Если оставить пустым, то сгенерируется автоматически.',
    )

class MainImageField(models.Model):
    '''
    Абстрактная модель для добавления распространенного поля "главная картинка"
    '''

    class Meta():
        abstract = True

    main_img = models.ImageField(
        upload_to    = settings.IMAGES_UPLOAD_FOLDER,
        default      = 'images/no_photo.png',
        blank        = True,
        null         = True,
        verbose_name = u'Главная картинка',
    )

    def get_main_image(self):
        return self.main_img

class DescField(models.Model):
    '''
    Абстрактная модель для добавления распространенного поля "описание"
    '''

    class Meta():
        abstract = True

    desc  = models.TextField(
        verbose_name = u'Описание',
        null          = True,
        blank         = True,
    )

class DateField(models.Model):
    '''
    Абстрактная модель для добавления распространенного поля "дата".
    Например, для сущности "новость" данное поле является датой, к которой привязана новость.
    '''

    class Meta():
        abstract = True

    date = models.DateTimeField(
        blank        = True,
        null         = True,
        verbose_name = u'Дата',
    )
