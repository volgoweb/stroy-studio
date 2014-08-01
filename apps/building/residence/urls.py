from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import ResidencesList

from views import BuildingsList

urlpatterns = patterns('',
    url(r'^$', ResidencesList.as_view(), name='residence__residences_list_page'),
)

