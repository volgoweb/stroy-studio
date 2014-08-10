# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

from django.views.generic import ListView

class CallbacksListPage(ListView):
    model                = Callback
    template_name        = "callback/callbacks_list_page.html"
    context_object_name  = 'models'
    queryset = Callback.entity_base_manager.active_objects()
    paginate_by          = 10

    def get_context_data(self, **kwargs):
        context = super(CallbacksListPage, self).get_context_data(**kwargs)
        # форма добавления отзыва
        # TODO не работает captcha
        context['add_callback_form'] = CallbackForm()
        return context

def add_callback(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST, request = request)
        if form.is_valid():
            form.save()
            HttpResponseRedirect('callback')

