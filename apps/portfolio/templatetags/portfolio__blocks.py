# -*- coding: utf-8 -*-
# from django.template.defaultfilters import stringfilter
from django import template
from django.template.loader import get_template
from django.template import Context
from constance import config
from portfolio.models import Portfolio

register = template.Library()

@register.simple_tag
def last_portfolios_block(**kwargs) :
    count_models = 3
    # models = Portfolio.objects.order_by('-update_date')[:count_models]
    models = Portfolio.objects.order_by('title')[:count_models]

    c = {
        'request'            : kwargs.get('request'),
        'items'              : models,
        'list_class'         : 'last-portfolios portfolios-block',
        'cols'               : 12,
        'item_class'         : 'portfolios-block__item',
        'item_template'      : 'theme_framework_dk/detail/all_centered__img_top.html',
        'item_head_template' : 'theme_framework_dk/detail/item__head.html',
        'item_body_template' : 'theme_framework_dk/detail/item__body.html',
    }
    t = get_template('theme_framework_dk/list/grid/simple.html')
    output = t.render(Context(c))
    return output
