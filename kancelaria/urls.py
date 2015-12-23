from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from main_site import views as main_site

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', main_site.HomePageView.as_view(), name='home'),
    url(r'^', include('main_site.urls', namespace='main_site')),

)
