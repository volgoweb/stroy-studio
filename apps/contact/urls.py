from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = patterns('',
    #url(r'^$', PortfoliosList.as_view(), name='portfolio__portfolios_list_page'),
    url(r'^call-me-save-ajax/$', 'main.contact.views.call_me_save_ajax', name='contact__call_me_save_ajax'),
)
