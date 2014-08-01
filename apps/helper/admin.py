from django.contrib import admin
from .models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    pass
    # list_display = ['__all__']

admin.site.register(Image, ImageAdmin);

