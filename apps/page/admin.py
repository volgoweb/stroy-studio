# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)

admin.site.register(Page, PageAdmin);

