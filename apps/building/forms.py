# -*- coding: utf-8 -*-
from django import forms
from .models import Building, Foundation, ConstructionType, RoofCovering
from constance import config

class BuildingFilters(forms.Form):
    foundation = forms.ModelChoiceField(
        queryset    = Foundation.objects.all(),
        empty_label = config.SELECT_EMPTY_LABEL,
        required    = False,
        label       = Building._meta.get_field_by_name('foundation')[0].verbose_name,
    )

    construction_type = forms.ModelChoiceField(
        queryset    = ConstructionType.objects.all(),
        empty_label = config.SELECT_EMPTY_LABEL,
        required    = False,
        label       = Building._meta.get_field_by_name('construction_type')[0].verbose_name,
    )

    roof_covering = forms.ModelChoiceField(
        queryset    = RoofCovering.objects.all(),
        empty_label = config.SELECT_EMPTY_LABEL,
        required    = False,
        label       = Building._meta.get_field_by_name('roof_covering')[0].verbose_name,
    )

    total_area_lt = forms.IntegerField(
        required = False,
        label    = u'от',
    )

    total_area_gt = forms.IntegerField(
        required = False,
        label    = u'до',
    )

    length_lt = forms.IntegerField(
        required = False,
        label    = u'от',
    )

    length_gt = forms.IntegerField(
        required = False,
        label    = u'до',
    )

    width_lt = forms.IntegerField(
        required = False,
        label    = u'от',
    )

    width_gt = forms.IntegerField(
        required = False,
        label    = u'до',
    )

    price_lt = forms.IntegerField(
        required = False,
        label    = u'от',
    )

    price_gt = forms.IntegerField(
        required = False,
        label    = u'до',
    )

    def __init__(self, *args, **kwargs):
        super(BuildingFilters, self).__init__(*args, **kwargs)
        # Добавляет в объект формы словарь, содержащий подписи полей модели.
        self.set_verbose_names_dict(Building)

    def set_verbose_names_dict(self, model):
        '''
        Добавляет в объект формы словарь, содержащий подписи полей модели.
        '''
        fields = model._meta.fields
        self.model_fields_verbose_names = {}
        for f in model._meta.fields:
            self.model_fields_verbose_names[f.name] = f.verbose_name

    def get_base_queryset(self):
        return Building.objects.all()

    def get_filtered_queryset(self):
        '''
        Возвращает queryset моделей, отфильтрованных согласно выставленным в форме полям.
        '''
        values = getattr(self, 'cleaned_data', {})
        queryset = base_queryset = self.get_base_queryset()

        if values:
            not_empty_values = {}
            for f, v in values.iteritems():
                if v:
                    not_empty_values[f] = v
            queryset = base_queryset.filter(**not_empty_values)

        return queryset
