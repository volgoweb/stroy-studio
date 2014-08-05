from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import PortfoliosList

urlpatterns = patterns('',
    url(r'^$', PortfoliosList.as_view(), name='portfolio__portfolios_list_page'),
    url(r'^(?P<slug>[^/]+)/$', 'main.portfolio.views.portfolio_detail_page', name='portfolio__portfolio_detail_page'),
)
