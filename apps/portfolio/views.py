# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.admin import site
from django.template import RequestContext
from django.http import Http404
from django.views.generic import ListView
from .models import Portfolio
from .forms import PortfolioFilters

def portfolio_detail_page(request, slug):
    model = Portfolio.objects.get(slug = slug)
    return render_to_response('page/page.html', {'page': model,}, context_instance = RequestContext(request))

class PortfoliosListPage(ListView):
    model                = Portfolio
    template_name        = "portfolio/portfolios_list_page.html"
    context_object_name  = 'models'
    paginate_by          = 10
    default_filter_param = 'all'
    filters_form         = PortfolioFilters

    def __init__(self, *args, **kwargs):
        super(PortfoliosListPage, self).__init__(*args, **kwargs)
        self.dk = {}

    def get_queryset(self):
        qs = self.model.entity_base_manager.active_objects()
        # Генерация словаря с фильтрами для queryset согласно полученным GET-параметрам.
        self.define_filters()
        # Фильтрация queryset, сгенерированного ранее методом define_filters().
        qs = self.filter_queryset(qs)

        qs = qs.filter(**self.dk['filters'])
        return qs

    def define_filters(self):
        '''
        Генерация словаря с фильтрами для queryset согласно полученным GET-параметрам.
        '''
        filters = {}
        if self.request.GET.get('foundation'):
            filters['foundation__id'] = self.request.GET.get('foundation')
        if self.request.GET.get('construction_type'):
            filters['construction_type__id'] = self.request.GET.get('construction_type')
        if self.request.GET.get('roof_covering'):
            filters['roof_covering__id'] = self.request.GET.get('roof_covering')
        if self.request.GET.get('total_area_gt'):
            filters['total_area__lt'] = self.request.GET.get('total_area_gt')
        if self.request.GET.get('total_area_lt'):
            filters['total_area__gt'] = self.request.GET.get('total_area_lt')

        self.dk['filters'] = filters

    def filter_queryset(self, queryset):
        '''
        Фильтрация queryset, сгенерированного ранее методом define_filters().
        '''
        queryset = queryset.filter(**self.dk['filters'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PortfoliosListPage, self).get_context_data(**kwargs)
        context['filters_form'] = self.filters_form(getattr(self.request, 'GET', None))

        context['request'] = self.request
        return context

class PortfoliosWithoutFilters(ListView):
    model                = Portfolio
    template_name        = "portfolio/portfolios_list_page.html"
    context_object_name  = 'models'
    paginate_by          = 10
    default_filter_param = 'all'

