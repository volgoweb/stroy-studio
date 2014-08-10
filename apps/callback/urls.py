# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import CallbacksListPage

urlpatterns = patterns('',
    url(r'^$', CallbacksListPage.as_view(), name='callback__callbacks_list_page'),
    url(r'^add-callback/$', 'main.callback.views.add_callback', name='callback__add_callback'),
)

