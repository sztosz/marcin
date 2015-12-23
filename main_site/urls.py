from django.conf.urls import patterns, include, url
from django.contrib import admin

from main_site.views import *

urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^onas/$', AboutPageView.as_view(), name='about'),
    url(r'^kancelaria/$', OfficePageView.as_view(), name='office'),
    url(r'^cennik/$', PricingPageView.as_view(), name='pricing'),
    url(r'^eporady/$', AdvicesPageView.as_view(), name='advices'),
    url(r'^publikacje/$', PublicationsPageView.as_view(), name='publications'),
    url(r'^dodatki/$', ExtrasPageView.as_view(), name='extras'),
    url(r'^kontakt/$', ContactPageView.as_view(), name='contact'),

    # url(r'^uslugi/$', ServicesPageView.as_view(), name='services'),
    url(r'uslugi/', include('main_site.services_urls', namespace='services')),

)
