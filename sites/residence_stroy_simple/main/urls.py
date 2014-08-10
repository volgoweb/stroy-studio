from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'main.views.front_page', name='main__front_page'),
    url(r'^buildings/', include('main.building.urls')),
    url(r'^page/', include('main.page.urls')),
    url(r'^portfolio/', include('main.portfolio.urls')),
    url(r'^callback/', include('main.callback.urls')),

    url(r'^captcha/', include('captcha.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
