# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
from django.template import Context
from constance import config
from .forms import CallMeClaimForm

register = template.Library()

@register.inclusion_tag('contact/call_me_button_with_popup.html')
def call_me_button_with_popup() :
    context = {
        'form': CallMeClaimForm(),
    }
    return context
