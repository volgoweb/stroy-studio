from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from .views import PortfoliosListPage

urlpatterns = patterns('',
    url(r'^$', PortfoliosListPage.as_view(), name='portfolio__portfolios_list_page'),
)
