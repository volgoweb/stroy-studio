from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import BuildingsListPage

urlpatterns = patterns('',
    # url(r'^$', 'building.views.buildings_page', name='building__residences_page'),
    url(r'^$', BuildingsListPage.as_view(), name='building__buildings_list_page'),
    url(r'^(?P<pk>\d+)/$', 'main.building.views.building_detail_page', name='building__building_detail_page'),

    url(r'^residences/', include('main.building.residence.urls')),
)
