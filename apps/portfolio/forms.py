# -*- coding: utf-8 -*-
from django import forms
from .models import *
from constance import config

class PortfolioFilters(forms.Form):
    work_type = forms.ModelChoiceField(
        queryset    = WorkType.objects.all(),
        empty_label = config.SELECT_EMPTY_LABEL,
        required    = False,
        label       = Portfolio._meta.get_field_by_name('work_type')[0].verbose_name,
    )


