# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.admin import site
from django.template import RequestContext
from django.http import Http404

def front_page(request):
    return render_to_response('index.html', {}, context_instance = RequestContext(request))
