# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class CallbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'update_date', 'text')

admin.site.register(Callback, CallbackAdmin);

