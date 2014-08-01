# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.admin import site
from django.template import RequestContext
from django.http import Http404
from .models import Page

def page(request, slug):
    model = Page.objects.get(slug = slug)
    return render_to_response('page/page.html', {'page': model,}, context_instance = RequestContext(request))
