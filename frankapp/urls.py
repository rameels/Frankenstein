from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from frankapp import views

urlpatterns = patterns('',
	(r'^$', RedirectView.as_view(url='/index/')),
	url(r'^index/$', views.index),
    url(r'^search/people/$', views.searchpeople),
    url(r'^search/events/$', views.searchevents),
)
