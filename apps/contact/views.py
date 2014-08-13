# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from main.helper.constants import constants

def call_me_save_ajax(request):
    if request.method != "POST" or not request.is_ajax():
        return HttpResponse(constants.BAD_AJAX_RESPONSE)

