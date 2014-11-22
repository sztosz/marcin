from django.conf.urls import patterns, include, url
from django.contrib import admin

from main_site.services_views import *


urlpatterns = patterns(
    '',
    url(r'^$', ServicesPageView.as_view(), name='services'),
    url(r'^sprawykarne/$', CriminalPageView.as_view(), name='criminal'),
    url(r'^przedsiebiorcy/$', EntrepreneursPageView.as_view(), name='entrepreneurs'),
    url(r'^klienciindywidulani/$', IndividualPageView.as_view(), name='individual'),
    url(r'^instytucjepubliczne/$', PublicPageView.as_view(), name='public'),
    url(r'^sprawyrodzinne/$', FamilyPageView.as_view(), name='family'),
    url(r'^upadlosc/$', BankruptPageView.as_view(), name='bankrupt'),
    url(r'^podatki/$', AdministrationPageView.as_view(), name='administration'),
    url(r'^prawopracy/$', WorkPageView.as_view(), name='work'),
)
