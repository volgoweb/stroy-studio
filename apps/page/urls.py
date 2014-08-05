from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^(?P<slug>[^/]+)/$', 'main.page.views.page', name='page__page'),
)
