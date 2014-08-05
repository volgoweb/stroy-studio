# -*- coding:utf-8 -*-
from .models import *
from main.helper.utils import add_pagingation
from .models import Residence
from .forms import ResidenceFilters
from main.building.views import BuildingsList

def block_residences_list(request):
    filters_form = ResidenceFiltersForm(prefix = 'residences_filters')
    if request.GET.get('residences_filters'):
        filters_form = ResidenceFiltersForm(request.GET, prefix = 'residences_filters')

    residences = Residence.objects.all()
    # добавляем пагинацию
    page = request.GET.get('page', 1)
    residences = add_pagingation(models = residences, page = page)

    return render_to_response('block_residences_list.html', {
        'residences'           : residences,
        'labels'        : InfoReason.get_verbose_names(),
    }, context_instance = RequestContext(request))

class ResidencesList(BuildingsList):
    model                = Residence
    template_name        = "building/residence/residences_page.html"
    # paginate_by          = 10
    # default_filter_param = 'all'
    filters_form         = ResidenceFilters

    def define_filters(self):
        '''
        Генерация словаря с фильтрами для queryset согласно полученным GET-параметрам.
        '''
        super(ResidencesList, self).define_filters()

        filters = self.dk['filters']
        if self.request.GET.get('floors_count'):
            filters['floors_count'] = self.request.GET.get('floors_count')
        if self.request.GET.get('total_area_gt'):
            filters['living_area__lt'] = self.request.GET.get('living_area_gt')
        if self.request.GET.get('living_area_lt'):
            filters['living_area__gt'] = self.request.GET.get('living_area_lt')

        self.dk['filters'] = filters
