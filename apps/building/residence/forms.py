# -*- coding: utf-8 -*-
from django import forms
from .models import Residence
from constance import config
from building.forms import BuildingFilters

class ResidenceFilters(BuildingFilters):
    floors_count = forms.IntegerField(
        required = False,
        label    = Residence._meta.get_field_by_name('floors_count')[0].verbose_name,
    )

    living_area_lt = forms.IntegerField(
        required = False,
        label    = u'от',
    )

    living_area_gt = forms.IntegerField(
        required = False,
        label    = u'до',
    )

    def __init__(self, *args, **kwargs):
        super(ResidenceFilters, self).__init__(*args, **kwargs)
        # Добавляет в объект формы словарь, содержащий подписи полей модели.
        self.set_verbose_names_dict(Residence)
