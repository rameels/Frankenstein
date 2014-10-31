from django.conf.urls import patterns, include, url

from frankapp import views

urlpatterns = patterns('',
    url(r'^index/$', views.index),
    url(r'^results/$', views.results),
)
